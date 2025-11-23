🚀 ***PDB Model Viewer**

A clean and intuitive Python GUI tool for searching, downloading, and visualizing protein structures from the RCSB PDB database.

🔬 *Overview*

The PDB Model Viewer lets you:

✨ Search proteins by PDB ID
📥 Automatically download PDB files
🧬 Parse and visualize basic protein structure data
🖼 Display a 2D image in a Tkinter GUI
⌨️ Accept command-line arguments using sys.argv

🧰 *Technologies Used*

🐍 Python 3.8
🪟 Tkinter
🌐 Requests
🖼 Pillow (PIL)

🔍 *How the Protein Search Works*

When you type a PDB ID (e.g., 1ABC):

🌐 The app downloads:
https://files.rcsb.org/download/<PDB_ID>.pdb

💾 Saves it locally to:
./pdb_files/

🧬 Parses the structure

🖼 Renders a simple visualization

📟 Displays it in the GUI

If the ID does not exist → ❌ “No result found”

AI instructions for ChatGTP:
PDB is a website that contains structural data for proteins whose structures have been experimentally determined.
In the day04 folder, write a Python program that downloads specific data (details provided at the end) from the PDB website and saves it locally, either in a single file or in multiple files.

Make sure to separate the business logic from the user interface (UI).
The UI must be implemented as a GUI.

On the PDB website, we normally search by a protein name or by an amino-acid sequence, and then the website returns details about the protein structure.
I want the GUI to ask the user for either a protein name or a sequence. The program should then search the PDB website, retrieve the structure information, and display all relevant data, for example:

Classification: Biotin-binding protein

Organism(s): Shewanella denitrificans OS217

Expression System: Escherichia coli

Mutation(s): No

Deposited: 2011-07-19

Released: 2012-04-11

Deposition Author(s): Livnah, O., Meir, A.

Experimental Data Snapshot

Method: X-RAY DIFFRACTION

Resolution: 1.07 Å

R-Value Free: 0.185 (Depositor), 0.185 (DCC)

R-Value Work: 0.158 (Depositor), 0.158 (DCC)

R-Value Observed: 0.160 (Depositor)

In addition to the text data, the program should also display a picture of the protein structure.

PDB website: https://www.rcsb.org/
