Day01 Dead-line: 2025.11.02 22:00
Day02 Dead-line: 2025.11.09 22:00
Day03 Dead-line: 2025.11.16 22:00
Day04 Dead-line: 2025.11.23 22:00
Day05 Dead-line: 2025.11.29 22:00
Day06 Dead-line: 2025.12.06 22:00
Day07 
Day08 Dead-line: 2025.12.30 22:00
Day09 Dead-line: 2026.01.10 22:00 
Final Project proposal dead-line: 2026.01.11 22:00
Final Project submission dead-line: 2026.01.25 22:00

---

Usage
-----

This program prints a report from the "subjects.txt" and "README.md" as follow:

You can generate the report by running:

python analyze_submissions.py subjects.txt README.md

The script prints three sections:
1) Students missing submissions (per expected assignment listed in this README).
2) Students who submitted after the deadline (with timestamps).
3) Submissions currently marked OPEN (subject id, assignment, student, timestamp).

Notes: The script assumes deadlines in this README are UTC and parses submission timestamps in `subjects.txt` as UTC (ISO format with Z).
 

# AI prompt:
---
using Copilot of VScode this is what I have wrote:

"I have a file of data called "subjects.txt" which I need to analyse. In the README.md file there is dates of dead-lines of submition. I need you to write a program that will create a report with the following details:

Students that have not submitted certain assignments. (on what assignments)
Students who submitted after the dead-line. (and on what assignments)
what submmisions are still open."