import os
from day09.analyze_submissions import parse_readme_deadlines, parse_subjects, analyze


def test_basic_run():
    root = os.path.dirname(__file__)
    readme = os.path.join(root, 'README.md')
    subjects = os.path.join(root, 'subjects.txt')
    deadlines = parse_readme_deadlines(readme)
    rows = parse_subjects(subjects)
    missing, late, open_subs = analyze(deadlines, rows)
    assert isinstance(missing, dict)
    assert isinstance(late, list)
    assert isinstance(open_subs, list)
    # Basic sanity checks: some open submissions should exist
    assert len(open_subs) > 0
    # all late entries should correspond to an OPEN submission
    for item in late:
        matches = [r for r in rows if r['status'].upper() == 'OPEN' and r['student'] == item['student'] and item['assignment'] in r['assignments']]
        assert matches, f"late entry not found in open rows: {item}"
