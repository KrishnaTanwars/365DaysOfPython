# Question: Given a year, write a function that returns `True` if it is a leap year and `False` otherwise. A year is a leap year if it is divisible by 4, except for end-of-century years, which must be divisible by 400.

def is_leap(year):
    """
    Determines if a given year is a leap year.
    - Divisible by 400 -> Leap
    - Divisible by 100 but not 400 -> Not Leap
    - Divisible by 4 but not 100 -> Leap
    - Not divisible by 4 -> Not Leap
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year_to_check = 2024
if is_leap(year_to_check):
    print(f"{year_to_check} is a leap year.")
else:
    print(f"{year_to_check} is not a leap year.")

year_to_check = 1990
if is_leap(year_to_check):
    print(f"{year_to_check} is a leap year.")
else:
    print(f"{year_to_check} is not a leap year.") 
