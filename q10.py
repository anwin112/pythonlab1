#(10) Declare a list/tuple containing all the twelve months. Write a Python program
#that converts a month name entered via the Python console to the number
#of days in that month (Consider leap year as well the code):

def get_days_in_month(month):
    # List of months with corresponding days, considering leap years for February
    months_days = {
        "January": 31,
        "February": 29 if is_leap_year() else 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }
    return months_days.get(month.capitalize(), "Invalid month name")

def is_leap_year():
    # Check if the current year is a leap year
    year = int(input("Enter a year: "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def main():
    month = input("Enter the month name: ")
    days = get_days_in_month(month)
    if days == "Invalid month name":
        print(days)
    else:
        print(f"{month.capitalize()} has {days} days.")

if __name__ == "__main__":
    main()
