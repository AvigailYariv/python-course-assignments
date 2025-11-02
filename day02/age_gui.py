import tkinter as tk
from tkinter import messagebox
from age_model import AgeCalculator

def on_calculate():
    s = entry.get().strip()
    try:
        years, months = AgeCalculator.from_string(s).calculate()
        result_var.set(f"{years} years and {months} months")
    except ValueError as e:
        messagebox.showerror("Invalid input", str(e))
        result_var.set("")

root = tk.Tk()
root.title("Age Calculator")
root.configure(bg="light pink")

frame = tk.Frame(root, bg="light pink", padx=12, pady=12)
frame.pack()

label = tk.Label(frame, text="Enter birthday (DD/MM/YYYY):", bg="light pink")
label.grid(row=0, column=0, sticky="w")

entry = tk.Entry(frame, width=20)
entry.grid(row=1, column=0, pady=(6, 6), sticky="w")
entry.insert(0, "24/02/1999")

btn = tk.Button(frame, text="Calculate Age", command=on_calculate)
btn.grid(row=1, column=1, padx=(8,0))

result_var = tk.StringVar()
result_label = tk.Label(frame, textvariable=result_var, bg="light pink", fg="black")
result_label.grid(row=2, column=0, columnspan=2, pady=(10,0), sticky="w")

root.bind('<Return>', lambda event: on_calculate())
root.resizable(False, False)

if __name__ == '__main__':
    root.mainloop()