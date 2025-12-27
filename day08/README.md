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

Run the script

From the day08 directory:

python data_from_excel.py

---

## 🧠 Biological Interpretation

Ribosomal proteins are typically abundant and well-detected in mass spectrometry experiments.
Their coverage distribution provides insight into:

* Protein abundance

* Peptide detectability

* Overall quality of the MS experiment

Variability in coverage may arise from differences in protein size, structure,
and amino acid composition.

