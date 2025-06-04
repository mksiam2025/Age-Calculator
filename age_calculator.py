from datetime import datetime

def calculate_age(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")
    today = datetime.today()
    age_years = today.year - birthdate.year
    age_months = today.month - birthdate.month
    age_days = today.day - birthdate.day

    if age_days < 0:
        age_months -= 1
        age_days += 30  # Approximate days in month
    if age_months < 0:
        age_years -= 1
        age_months += 12

    return age_years, age_months, age_days

dob = input("Enter your birthdate (DD/MM/YYYY): ")
years, months, days = calculate_age(dob)
print(f"Your age is: {years} years, {months} months, and {days} days.")
