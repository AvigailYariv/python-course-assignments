# Mass Spectrometry Analysis – Ribosomal Protein Coverage

## 📌 Overview
This assignment analyzes mass spectrometry (MS) results stored in an Excel file.  
The goal is to identify ribosomal proteins based on their annotation and to examine
their **coverage [%]**, which reflects how well each protein was detected in the MS experiment.

The analysis is implemented in Python using **pandas**, **NumPy**, and **matplotlib**.


---

## 🧪 Input Data
The input is an Excel (`.xlsx`) file containing mass spectrometry results.

Expected columns:
- **First column**: Protein or sample identifier
- **Description**: Textual annotation of the protein
- **Coverage [%]**: Percentage of the protein sequence covered by detected peptides

---

## 🔬 Analysis Steps
1. Load the Excel file into a pandas DataFrame
2. Filter rows where the **Description** column contains:
   - `"ribosomal"` or
   - `"ribosome-binding"`  
   (case-insensitive)
3. Extract and clean numeric values from the **Coverage [%]** column
4. Generate summary statistics (count, mean, median, standard deviation)
5. Create visualizations of ribosomal protein coverage

---

## 📊 Output Plot

### 2️⃣ Histogram – Coverage Distribution
- **X-axis**: Coverage [%]
- **Y-axis**: Number of ribosomal proteins
- Shows the overall distribution of coverage values

## 🚀 How to Run

### Requirements
Install dependencies:
```bash
python -m pip install pandas numpy matplotlib openpyxl
```

---

## 🧠 Biological Interpretation

Ribosomal proteins are typically abundant and well-detected in mass spectrometry experiments.
Their coverage distribution provides insight into:

* Protein abundance

* Peptide detectability

* Overall quality of the MS experiment

Variability in coverage may arise from differences in protein size, structure,
and amino acid composition.

---

## 🤖 Use of AI Assistance

GitHub Copilot was used as a coding assistant during this assignment to support code writing and structuring.
The tool was used in an assistive manner, similar to documentation or autocomplete, while all design
decisions, logic, and final code review were performed by me.

"Hi! Please help me write a Python program using pandas and NumPy.

The program should do the following:

Read an Excel (.xlsx) file located in a folder called "data", which is in the same directory as this Python file.
The Excel file contains mass spectrometry results.
The first column contains sample identifiers.
One of the columns is called "Description".
One of the columns is called "Coverage [%]".
There is only one sheet.
Load the Excel file into a pandas DataFrame.
Filter the DataFrame to keep only rows where the "Description" column contains
either the word "ribosomal" or "Ribosome-binding" (case-insensitive).
From the filtered rows, analyze the "Coverage [%]" values.
Create a histogram showing the distribution of the proteins.
X-axis: proteins name.
Y-axis: Coverage values.
Please use pandas for data handling and NumPy where appropriate."