import pandas as pd
import plotly.express as px
import os

# 1. Setup the file path
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'data', 'sample_6.xlsx')

print(f"Looking for file at: {file_path}")

# 2. Smart Load: Find the header row automatically
try:
    # Read the file without a header first to see the raw layout
    df_raw = pd.read_excel(file_path, engine='openpyxl', header=None)
    
    # Search the first 10 rows for our target columns
    header_row_idx = None
    target_col = "MW [kDa]"
    
    for i, row in df_raw.head(10).iterrows():
        # Convert row to string to search for the column name
        row_values = [str(val).strip() for val in row.values]
        if target_col in row_values:
            header_row_idx = i
            print(f"Found header on Row {i} (Index {i})")
            break
            
    if header_row_idx is None:
        print(f"CRITICAL ERROR: Could not find the column '{target_col}' in the first 10 rows.")
        print("Please check if the Excel file is encrypted or has a different format.")
        exit()

    # Reload the dataframe using the found header row
    df = pd.read_excel(file_path, engine='openpyxl', header=header_row_idx)

except Exception as e:
    print(f"Error loading file: {e}")
    exit()

# 3. Clean and Prepare the Data
numeric_cols = ['MW [kDa]', 'calc. pI', 'Abundance: F6: Sample']

# Strip whitespace from column names just in case (e.g. " MW [kDa] ")
df.columns = df.columns.str.strip()

# Check for missing columns one last time
missing = [c for c in numeric_cols if c not in df.columns]
if missing:
    print(f"Error: We found the header, but are still missing these columns: {missing}")
    print(f"Columns found: {df.columns.tolist()}")
    exit()

# Convert columns to numeric
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop empty rows
df_clean = df.dropna(subset=['Abundance: F6: Sample'])

print(f"Successfully loaded {len(df_clean)} proteins.")

# 4. Create the Plot
fig = px.scatter(
    df_clean,
    x='calc. pI',
    y='MW [kDa]',
    color='Abundance: F6: Sample',
    log_y=True, 
    hover_data=['Gene Symbol', 'Accession', 'Description'], 
    title='Virtual 2D Gel: Proteome Distribution (Sample F6)',
    labels={'calc. pI': 'Isoelectric Point (pI)', 'MW [kDa]': 'Molecular Weight (kDa)'},
    color_continuous_scale='Viridis',
    template='plotly_white'
)

# 5. Save
output_path = os.path.join(current_dir, 'virtual_2d_gel.html')
fig.write_html(output_path)
print(f"Graph saved successfully to: {output_path}")
# fig.show() # Uncomment this if you want it to open in the browser immediately