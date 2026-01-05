#!/usr/bin/env python3
"""analyze_submissions.py

Usage: python analyze_submissions.py [subjects.txt] [README.md]

Generates a report with:
 1) Students that have not submitted certain assignments.
 2) Students who submitted after the dead-line.
 3) Submissions currently marked OPEN.

Assumes every student is expected to submit all assignments listed in the README (Day01..Day09 and Final Project proposal).
"""
from __future__ import annotations
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from typing import Dict, List, Optional, Tuple


def parse_readme_deadlines(path: str) -> Dict[str, datetime]:
    """Return mapping from assignment name to deadline (UTC-aware datetime).

    Normalizes day names to `DayNN` (zero-padded) format.
    """
    deadlines: Dict[str, datetime] = {}
    day_re = re.compile(r"Day\s*0?(\d{1,2})\s*Dead-?line:\s*([0-9]{4}\.[0-9]{2}\.[0-9]{2}\s*[0-9]{2}:[0-9]{2})", re.I)
    final_re = re.compile(r"Final Project proposal\s*dead-?line:\s*([0-9]{4}\.[0-9]{2}\.[0-9]{2}\s*[0-9]{2}:[0-9]{2})", re.I)
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            m = day_re.search(line)
            if m:
                num = int(m.group(1))
                key = f"Day{num:02d}"
                dt = datetime.strptime(m.group(2), "%Y.%m.%d %H:%M")
                dt = dt.replace(tzinfo=timezone.utc)
                deadlines[key] = dt
                continue
            m = final_re.search(line)
            if m:
                key = "Final Project proposal"
                dt = datetime.strptime(m.group(1), "%Y.%m.%d %H:%M")
                dt = dt.replace(tzinfo=timezone.utc)
                deadlines[key] = dt
    return deadlines


def parse_subjects(path: str) -> List[Dict]:
    """Parse subjects.txt; returns list of dicts with keys: id, status, title, assignments (list), student, timestamp (datetime or None).

    This normalizes assignments to `DayNN` and attempts to robustly extract multi-day entries and student names in common formats.
    """
    rows = []
    final_re = re.compile(r"Final Project proposal", re.I)

    with open(path, encoding="utf-8") as fh:
        for raw in fh:
            line = raw.strip()
            if not line:
                continue
            parts = line.split("\t")
            # expected parts: id, status, title, maybe blank, timestamp
            _id = parts[0] if len(parts) > 0 else ""
            status = parts[1] if len(parts) > 1 else ""
            title = parts[2] if len(parts) > 2 else ""
            timestamp = None
            if len(parts) >= 5 and parts[4].strip():
                ts = parts[4].strip()
                timestamp = _parse_iso_z(ts)
            elif len(parts) == 4 and parts[3].strip():
                # sometimes timestamp is the 4th column
                ts = parts[3].strip()
                # if ts looks like ISO
                if re.match(r"\d{4}-\d{2}-\d{2}T", ts):
                    timestamp = _parse_iso_z(ts)

            # find day numbers: 'Day 05', 'Day5' etc.
            assignment_nums = set()
            for n in re.findall(r"Day\s*0?(\d{1,2})", title, re.I):
                assignment_nums.add(int(n))
            # also catch 'and 06' style when second day doesn't include 'Day'
            for n in re.findall(r"\band\s*0?(\d{1,2})\b", title, re.I):
                assignment_nums.add(int(n))
            assignments = [f"Day{num:02d}" for num in sorted(assignment_nums)]
            if final_re.search(title):
                assignments.append("Final Project proposal")

            # student extraction: try several heuristics
            student = _extract_student_from_title(title)
            rows.append({
                "id": _id,
                "status": status,
                "title": title,
                "assignments": assignments,
                "student": student,
                "timestamp": timestamp,
            })
    return rows


def _parse_iso_z(s: str) -> datetime:
    s = s.strip()
    # convert trailing Z to +00:00 for fromisoformat
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(s)
    except Exception:
        # fallback: try common formats
        try:
            dt = datetime.strptime(s, "%Y-%m-%dT%H:%M:%S%z")
        except Exception:
            dt = None
    return dt


def _extract_student_from_title(title: str) -> str:
    # first try ' by NAME'
    m = re.search(r"\bby\s+(.+)$", title, re.I)
    if m:
        student = m.group(1).strip()
        return student.title()
    # then try trailing -NAME (e.g., '-Name')
    m = re.search(r"[-–]\s*(.+)$", title)
    if m:
        student = m.group(1).strip()
        return student.title()
    # else try to take the remainder after the last 'Day..' occurrence
    day_matches = list(re.finditer(r"Day\s*0?(\d{1,2})", title, re.I))
    if day_matches:
        last = day_matches[-1]
        remainder = title[last.end():].strip()
        # remove leading connectors and common words
        remainder = remainder.lstrip(" -:,")
        # if there's still a hyphen-separated name, take last segment
        if "-" in remainder:
            remainder = remainder.split("-")[-1].strip()
        # remove common filler words
        remainder = re.sub(r"(?i)\b(and|proposal|for|final project)\b", "", remainder)
        remainder = " ".join(remainder.split()).strip()
        if remainder:
            return remainder.title()
    # fallback to last token
    parts = title.split()
    if parts:
        return parts[-1].title()
    return ""


def analyze(deadlines: Dict[str, datetime], rows: List[Dict]) -> Tuple[Dict[str, List[str]], List[Dict], List[Dict]]:
    """Returns: (missing_submissions: {student: [assignments]}, late_submissions: [dicts], open_submissions: [dicts])"""
    expected_assignments = sorted([k for k in deadlines.keys()], key=lambda k: k)
    # build set of students
    students = set()
    # map student->assignment->list of timestamps
    subs = defaultdict(lambda: defaultdict(list))
    open_subs = []

    for r in rows:
        student = r["student"]
        students.add(student)
        if r["status"].upper() == "OPEN":
            open_subs.append(r)
        for assignment in r["assignments"]:
            subs[student][assignment].append(r)

    missing: Dict[str, List[str]] = {}
    late: List[Dict] = []

    for student in sorted(students):
        missing_list = []
        for assignment in expected_assignments:
            recs = subs[student].get(assignment, [])
            if not recs:
                missing_list.append(assignment)
            else:
                # find earliest timestamp among recs that have timestamp AND are still OPEN
                ts_list = [r["timestamp"] for r in recs if r["timestamp"] and r.get("status", "").upper() == "OPEN"]
                if not ts_list:
                    # either no timestamp or no OPEN record -> do not mark as late
                    continue
                earliest = min(ts_list)
                deadline = deadlines.get(assignment)
                if deadline and earliest > deadline:
                    late.append({
                        "student": student,
                        "assignment": assignment,
                        "submitted": earliest,
                        "deadline": deadline,
                    })
        if missing_list:
            missing[student] = missing_list
    return missing, late, open_subs


def format_report(missing: Dict[str, List[str]], late: List[Dict], open_subs: List[Dict]) -> str:
    lines = []
    lines.append("REPORT\n" + "=" * 40)
    lines.append("\n1) Students missing submissions:\n")
    if not missing:
        lines.append("All students submitted every expected assignment.\n")
    else:
        for student, assigns in sorted(missing.items()):
            lines.append(f"- {student}: {', '.join(assigns)}")
    lines.append("\n2) Students who submitted after the deadline:\n")
    if not late:
        lines.append("No late submissions detected.\n")
    else:
        for item in sorted(late, key=lambda x: (x['student'], x['assignment'])):
            lines.append(f"- {item['student']} - {item['assignment']}: submitted {item['submitted'].isoformat()} (deadline {item['deadline'].isoformat()})")
    lines.append("\n3) Submissions currently OPEN:\n")
    if not open_subs:
        lines.append("No OPEN submissions.\n")
    else:
        for r in open_subs:
            ts = r['timestamp'].isoformat() if r['timestamp'] else 'no timestamp'
            lines.append(f"- id {r['id']} - {', '.join(r['assignments'])} - {r['student']} - {ts}")
    return "\n".join(lines)


def main(argv=sys.argv[1:]):
    subjects_path = argv[0] if len(argv) >= 1 else "subjects.txt"
    readme_path = argv[1] if len(argv) >= 2 else "README.md"
    deadlines = parse_readme_deadlines(readme_path)
    if not deadlines:
        print("No deadlines parsed from README.md. Exiting.")
        return 1
    rows = parse_subjects(subjects_path)
    missing, late, open_subs = analyze(deadlines, rows)
    report = format_report(missing, late, open_subs)
    print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
