import tkinter as tk
from tkinter import ttk, messagebox
import requests
from io import BytesIO
from PIL import Image, ImageTk

# ---------------- BUSINESS LOGIC ---------------- #

import requests

def fetch_pdb_data(query):
    search_url = "https://search.rcsb.org/rcsbsearch/v2/query"

    # Build the query payload
    query_json = {
        "query": {
            "type": "terminal",
            "service": "full_text",   # more general search
            "parameters": {
                "value": query
            }
        },
        "return_type": "entry",
        "request_options": {
            "return_all_hits": True,
            "results_content_type": ["experimental"]  # or ["experimental", "computational"]
        }
    }

    headers = {
        "Content-Type": "application/json"
    }

    resp = requests.post(search_url, json=query_json, headers=headers)
    resp.raise_for_status()

    data = resp.json()
    print("DEBUG: Search response:", data)  # debug

    results = data.get("result_set")
    if not results:
        return None, None

    # Collect first few PDB IDs (or choose how you want to manage)
    pdb_ids = [hit["identifier"] for hit in results]
    print("DEBUG: Found PDB IDs:", pdb_ids)

    # For now, just use the first
    pdb_id = pdb_ids[0]

    # Fetch metadata
    metadata_url = f"https://data.rcsb.org/rest/v1/core/entry/{pdb_id}"
    metadata_resp = requests.get(metadata_url)
    metadata_resp.raise_for_status()
    metadata = metadata_resp.json()

    # Image URL (assembly-1 is common but not guaranteed)
    image_url = f"https://cdn.rcsb.org/images/structures/{pdb_id.lower()}_assembly-1.jpeg"

    return metadata, image_url


# ---------------- GUI ---------------- #

class PDBApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDB Protein Search")

        main = ttk.Frame(root, padding=10)
        main.grid(row=0, column=0)

        ttk.Label(main, text="Enter protein name or sequence:").grid(row=0, column=0, sticky="w")
        self.query_entry = ttk.Entry(main, width=50)
        self.query_entry.grid(row=1, column=0, pady=5)

        search_btn = ttk.Button(main, text="Search", command=self.search)
        search_btn.grid(row=1, column=1, padx=10)

        self.result_text = tk.Text(main, width=70, height=20)
        self.result_text.grid(row=2, column=0, columnspan=2, pady=10)

        self.image_label = ttk.Label(main)
        self.image_label.grid(row=3, column=0, columnspan=2)

    def search(self):
        query = self.query_entry.get().strip()
        if not query:
            messagebox.showerror("Error", "Please enter a query.")
            return

        metadata, image_url = fetch_pdb_data(query)
        if metadata is None:
            messagebox.showerror("Error", "No results found.")
            return

        self.display_metadata(metadata)
        self.display_image(image_url)

    def display_metadata(self, metadata):
        self.result_text.delete("1.0", tk.END)
        for key, value in metadata.items():
            self.result_text.insert(tk.END, f"{key}: {value}\n")

    def display_image(self, url):
        try:
            img_data = requests.get(url).content
            img = Image.open(BytesIO(img_data))
            img = img.resize((300, 300))
            self.photo = ImageTk.PhotoImage(img)
            self.image_label.configure(image=self.photo)
        except Exception:
            self.image_label.configure(text="Image unavailable")


if __name__ == "__main__":
    root = tk.Tk()
    PDBApp(root)
    root.mainloop()
