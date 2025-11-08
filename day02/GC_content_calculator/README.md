# 🧬 GC Content Calculator
---
## 📖 Overview

This Python program calculates the GC content (the percentage of guanine and cytosine bases) in a DNA sequence provided in a FASTA file.
It uses command-line arguments (sys.argv) to receive the input filename directly from the user, reads the file, extracts the DNA sequence, and prints the GC content as a percentage with two decimal places.

The program also automatically ignores FASTA header lines that begin with >.

💡 What Is GC Content?

GC content refers to the proportion of G (guanine) and C (cytosine) bases in a DNA molecule.
GC content is biologically important because DNA regions with high GC content are more thermally stable (due to 3 hydrogen bonds between G–C vs. 2 between A–T).
It can give insights into genome composition, evolutionary differences, and gene expression properties.

---

## ⚙️ Program Description
/ Functionality - Receives a FASTA file as a command-line argument.
/ Reads the DNA sequence from the file.
/ Ignores header lines starting with >.
/ Calculates GC content.
/ Prints the GC content with two decimal precision.

## 🧩 Command to Run the Program
To run the program from the command line:
* python GC_content_calculator.py path/to/your_file.fasta

Example:
python GC_content_calculator.py test_sequence.fasta

🧪 Example Output
Attempting to read file: test_sequence.fasta

File opened successfully

Read 2 lines

Read sequence length: 120

GC content: 48.33%

---

## 🧠 Original Prompt to GitHub Copilot

This program was generated with the following instruction to Copilot:
> I need you to write me a Python program that:
> Receives a FASTA file containing a DNA sequence.
> Uses command-line input (sys.argv) to get the filename from the user.
> Reads the DNA sequence from the file.
> Calculates and prints the GC content as a percentage with two decimal points.
> Ignores any FASTA header lines that start with '>'.
