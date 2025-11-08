# 🧮 Age Calculator (Interactive Input Version)

This program calculates the user's exact age in **years, months, and days** based on their date of birth.  
It uses **Interactive Input**.

---

## 📋 Description

The program asks the user to enter their birth date in the format `DD-MM-YYYY` using the command line.  
It then calculates the difference between the current date and the user's birth date and displays their exact age in years, months, and days.

---

## ⚙️ How It Works

1. The program prompts the user to type their date of birth (e.g. `24/02/1999`).
2. It reads the input from the command line using the built-in `input()` function.
3. It uses Python's `datetime` module to calculate the exact time difference between today and the entered birth date.
4. Finally, it prints the result in a readable format such as: '26 years, 8 months and 15 days.'

---

## 🤖 How I Used Copilot

This program was written with the assistance of the **GitHub Copilot** tool in **Visual Studio Code (VS Code)**.

### 🧾 Prompt I Gave to Copilot:
> I need you to write me a program that uses Interactive Input.  
> The program should calculate the age of the user in years, months, and days.  
> Ask the user to input their date of birth and then output the age.  
> For example, my input is `24/02/1999` and the output will be:  
> `26 years, 8 months, and 15 days.`

Copilot generated the initial version of the code based on this description, and I reviewed and tested the final implementation to ensure it works correctly.
