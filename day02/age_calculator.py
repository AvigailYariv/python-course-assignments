# ...existing code...
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, date
from age_model import calculate_age_from_string, AgeCalculator

def calculate_age(s: str):
    """
    Compatibility wrapper. Returns (years, months) for birthday string "DD/MM/YYYY".
    """
    return calculate_age_from_string(s)

__all__ = ["calculate_age", "AgeCalculator"]

def on_calculate():
    s = entry.get()
    try:
        years, months = calculate_age(s)
        result_var.set(f"{years} years and {months} months")
    except ValueError as e:
        messagebox.showerror("Invalid input", str(e))
        result_var.set("")

# GUI
root = tk.Tk()
root.title("Age Calculator")
root.configure(bg="light pink")  # light pink background

frame = tk.Frame(root, bg="light pink", padx=12, pady=12)
frame.pack()

label = tk.Label(frame, text="Enter birthday (DD/MM/YYYY):", bg="light pink")
label.grid(row=0, column=0, sticky="w")

entry = tk.Entry(frame, width=20)
entry.grid(row=1, column=0, pady=(6, 6), sticky="w")
entry.insert(0, "24/02/1999")  # example

btn = tk.Button(frame, text="Calculate Age", command=on_calculate)
btn.grid(row=1, column=1, padx=(8,0))

result_var = tk.StringVar()
result_label = tk.Label(frame, textvariable=result_var, bg="light pink", fg="black")
result_label.grid(row=2, column=0, columnspan=2, pady=(10,0), sticky="w")

# allow Enter key to calculate
root.bind('<Return>', lambda event: on_calculate())

root.resizable(False, False)
root.mainloop()