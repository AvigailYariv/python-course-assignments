"""
Amino Acid Structure Learning Game

This game helps students learn to identify amino acids from their structural formulas.
Place amino acid structure images in the 'images' folder with filenames matching the amino acid names.
"""

import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import os
import random
from amino_acid_game_model import AminoAcidModel

class AminoAcidGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Amino Acid Structure Game")
        
        # Use the game model to hold state and logic
        self.model = AminoAcidModel()
        self.current_amino_acid = None
        
        self.setup_gui()
        self.load_new_question()

    def setup_gui(self):
        
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Score display (just a single number: correct guesses, can go negative)
        self.score_var = tk.StringVar(value="Score: 0")
        score_label = ttk.Label(main_frame, textvariable=self.score_var, font=('Arial', 12))
        score_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))
        
        # Image display (placeholder until images are added)
        self.image_label = ttk.Label(main_frame)
        self.image_label.grid(row=1, column=0, columnspan=2, pady=(0, 10))
        
        # Answer entry
        self.answer_var = tk.StringVar()
        answer_label = ttk.Label(main_frame, text="Enter amino acid name:", font=('Arial', 11))
        answer_label.grid(row=2, column=0, columnspan=2, pady=(0, 5))
        
        self.answer_entry = ttk.Entry(main_frame, textvariable=self.answer_var, width=30)
        self.answer_entry.grid(row=3, column=0, columnspan=2, pady=(0, 10))
        
        # Buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=4, column=0, columnspan=2, pady=(0, 10))
        
        submit_btn = ttk.Button(button_frame, text="Submit", command=self.check_answer)
        submit_btn.grid(row=0, column=0, padx=5)
        
        next_btn = ttk.Button(button_frame, text="Next", command=self.load_new_question)
        next_btn.grid(row=0, column=1, padx=5)
        
        quit_btn = ttk.Button(button_frame, text="Quit", command=self.quit_game)
        quit_btn.grid(row=0, column=2, padx=5)
        
        # Bind Enter key to submit
        self.answer_entry.bind('<Return>', lambda e: self.check_answer())
        
        # Center window on screen
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'+{x}+{y}')

    def load_image(self, amino_acid_name):
        """Load and display the amino acid structure image"""
        try:
            # Resolve the images directory relative to this script file so the
            # game works even if the current working directory is different.
            script_dir = os.path.dirname(os.path.abspath(__file__))
            images_dir = os.path.join(script_dir, 'images')

            # Try common image extensions
            candidates = [f'{amino_acid_name}.png', f'{amino_acid_name}.jpg', f'{amino_acid_name}.jpeg']
            image_path = None
            for c in candidates:
                p = os.path.join(images_dir, c)
                if os.path.exists(p):
                    image_path = p
                    break

            if image_path is None:
                # Provide helpful debug information about files in the images dir
                try:
                    files = os.listdir(images_dir)
                except Exception:
                    files = []
                raise FileNotFoundError(f"No image found for '{amino_acid_name}'. Tried {candidates}. Files in images/: {files}")

            image = Image.open(image_path)

            # Resize image if needed (adjust size as needed)
            max_size = (400, 400)
            image.thumbnail(max_size, Image.Resampling.LANCZOS)

            photo = ImageTk.PhotoImage(image)
            self.image_label.configure(image=photo, text='')
            self.image_label.image = photo  # Keep a reference!
            return True
        except Exception as e:
            print(f"Error loading image for {amino_acid_name}: {e}")
            # Show a helpful message in the GUI so the user can fix filenames
            self.image_label.configure(text=f"[Image not found: {amino_acid_name}]")
            return False

    def load_new_question(self):
        """Load a new random amino acid question"""
        self.answer_var.set("")  # Clear previous answer
        # Ask model for next question
        amino_acid = self.model.next_question()
        self.current_amino_acid = amino_acid
        
        # Try to load the image
        if self.load_image(amino_acid):
            self.answer_entry.focus()  # Focus on entry field
        else:
            messagebox.showerror("Error", "Failed to load amino acid image. Please ensure images are in the 'images' folder.")

    def check_answer(self):
        """Check if the given answer is correct"""
        if not self.current_amino_acid:
            return
        user_answer = self.answer_var.get()
        correct, msg = self.model.check_answer(user_answer)
        # Update score shown in GUI
        self.score_var.set(f"Score: {self.model.get_score()}")

        if correct:
            # Show success and move to next question
            messagebox.showinfo("Correct!", msg)
            self.load_new_question()
        else:
            # Show retry message and keep the same question
            messagebox.showinfo("Try again", msg)
            self.answer_entry.focus()

    def quit_game(self):
        """Exit the game with a final score"""
        if messagebox.askyesno("Quit Game", f"Final Score: {self.model.get_score()}\nDo you want to quit?"):
            self.root.destroy()

def main():
    root = tk.Tk()
    game = AminoAcidGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()