# Mass Spectrometry Analysis Project

## 📌 Overview
This repository contains Python scripts for analyzing mass spectrometry (MS) proteomics data. The project is divided into two main analysis modules:

1.  **Ribosomal Protein Coverage**: Identifying ribosomal proteins and analyzing their detection quality.
2.  **Virtual 2D Gel**: Visualizing the global physical properties of the proteome (Sample F6).

---

## 📂 1. Ribosomal Protein Coverage (`data_from_excel.py`)

<img width="1200" height="750" alt="coverage_histogram" src="https://github.com/user-attachments/assets/4d8ab658-63c0-4ebd-87d4-0f55641de3d0" />

### 🧪 Overview
The goal of this script is to identify ribosomal proteins based on their annotation and to examine their **coverage [%]**, which reflects how well each protein was detected in the MS experiment.

### 🔬 Analysis Steps
1.  **Load Data**: Reads the Excel file into a pandas DataFrame.
2.  **Filter**: Selects rows where the **Description** column contains:
    * `"ribosomal"` or
    * `"ribosome-binding"` (case-insensitive).
3.  **Clean**: Extracts numeric values from the **Coverage [%]** column.
4.  **Statistics**: Generates summary statistics (count, mean, median, standard deviation).
5.  **Visualize**: Creates a histogram of the coverage distribution.

### 📊 Output Plot
* **Histogram**: Shows the distribution of coverage percentage across all identified ribosomal proteins.
    * **X-axis**: Coverage [%]
    * **Y-axis**: Number of Proteins

### 🧠 Biological Interpretation
Ribosomal proteins are typically abundant and well-detected in mass spectrometry experiments. Their coverage distribution provides insight into protein abundance, peptide detectability, and the overall quality of the MS experiment.

---

## 📂 2. Proteome Distribution – Virtual 2D Gel (`graph_from_excel.py`)

<img width="1878" height="846" alt="image" src="https://github.com/user-attachments/assets/47245471-22a9-4e09-8718-c0bc330c09fd" />

### 🧪 Overview
This script creates a "Virtual 2D Gel" visualization for **Sample F6**. It plots proteins based on their molecular weight and isoelectric point, mimicking a physical 2-DE gel separation.

### 🔬 Analysis Steps
1.  **Smart Loading**: Automatically scans the Excel file to find the correct header row (handling metadata rows common in Proteome Discoverer output).
2.  **Data Cleaning**: 
    * Coerces numeric data for molecular weight and pI.
    * Removes proteins with missing abundance values.
3.  **Visualization**: Uses **Plotly** to generate an interactive scatter plot.

### 📊 Output Plot
* **File**: Saves an interactive HTML file named `virtual_2d_gel.html`.
* **Plot Details**:
    * **X-axis**: Isoelectric Point (calc. pI).
    * **Y-axis**: Molecular Weight (MW [kDa]) on a **Log scale**.
    * **Color**: Mapped to **Abundance: F6: Sample** (Viridis scale).
    * **Interactivity**: Hovering over a dot reveals the Gene Symbol, Accession ID, and Description.

### 🧠 Biological Interpretation
By plotting MW vs. pI, we observe the global distribution of the proteome:
* **Vertical Spread**: Shows the dynamic range of protein sizes.
* **Horizontal Spread**: Shows the charge distribution (acidic vs. basic proteins).
* **Color Intensity**: Highlights which proteins are most abundant in the sample.

---

## 🚀 How to Run

### Requirements
Ensure you have the following Python libraries installed. Note that `openpyxl` is required for reading Excel files and `plotly` is required for the interactive graph.

```bash
python -m pip install pandas numpy matplotlib plotly openpyxl


## 🤖 Use of AI Assistance

GitHub Copilot was used as a coding assistant during this assignment to support code writing and structuring. The tool was used in an assistive manner, similar to documentation or autocomplete, while all design decisions, logic, and final code review were performed by me.

Prompt for Script 1 (Ribosomal Analysis):

"Hi! Please help me write a Python program using pandas and NumPy. Read an Excel (.xlsx) file located in a folder called "data". Filter the DataFrame to keep only rows where the "Description" column contains either the word "ribosomal" or "Ribosome-binding". Create a histogram showing the distribution of the proteins (X-axis: proteins name, Y-axis: Coverage values)."

Prompt for Script 2 (Virtual 2D Gel):

"I have a mass spectrometry dataset... The columns include: "Accession", "Gene Symbol", "MW [kDa]", "calc. pI", and "Abundance: F6: Sample". Please write a Python script using pandas and plotly.express to create an interactive "Virtual 2D Gel" scatter plot... X-axis: "calc. pI", Y-axis: "MW [kDa]" (Log calculation), Color: "Abundance"."



