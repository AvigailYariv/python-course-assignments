# Program to calculate age in years, months, and days from birth date
from datetime import datetime

def calculate_age(birth_date, today):
	years = today.year - birth_date.year
	months = today.month - birth_date.month
	days = today.day - birth_date.day

	if days < 0:
		months -= 1
		# Get days in previous month
		prev_month = today.month - 1 or 12
		prev_year = today.year if today.month != 1 else today.year - 1
		days_in_prev_month = (datetime(prev_year, prev_month % 12 + 1, 1) - datetime(prev_year, prev_month, 1)).days
		days += days_in_prev_month
	if months < 0:
		years -= 1
		months += 12
	return years, months, days

def main():
	birth_str = input("Enter your date of birth (DD/MM/YYYY): ")
	try:
		birth_date = datetime.strptime(birth_str, "%d/%m/%Y")
	except ValueError:
		print("Invalid date format. Please use DD/MM/YYYY.")
		return
	today = datetime.today()
	years, months, days = calculate_age(birth_date, today)
	print(f"{years} years, {months} months and {days} days.")

if __name__ == "__main__":
	main()
