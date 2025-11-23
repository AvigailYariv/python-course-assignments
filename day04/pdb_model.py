import tkinter as tk
from tkinter import ttk, messagebox
import requests
from io import BytesIO
from PIL import Image, ImageTk

# ---------------- BUSINESS LOGIC ---------------- #

def fetch_pdb_data(query):
    """
    Search PDB for a protein name or sequence using RCSB search API.
    Returns JSON metadata and an image URL (if available).
    """
    search_url = "https://search.rcsb.org/rcsbsearch/v2/query?json="

    query_json = {
        "query": {
            "type": "terminal",
            "service": "text",
            "parameters": {
                "attribute": "rcsb_text",
                "operator": "contains_phrase",
                "value": query
            }
        },
        "return_type": "entry",
        "request_options": {
            "results_content_type": ["experimental"]
        }
    }

    try:
        response = requests.get(search_url + requests.utils.quote(str(query_json)))
        response.raise_for_status()
        data = response.json()

        if not data.get("result_set"):
            return None, None

        pdb_id = data["result_set"][0]["identifier"]
        metadata_url = f"https://data.rcsb.org/rest/v1/core/entry/{pdb_id}"
        metadata = requests.get(metadata_url).json()

        image_url = f"https://cdn.rcsb.org/images/structures/{pdb_id.lower()}_assembly-1.jpeg"

        return metadata, image_url

    except Exception:
        return None, None

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
