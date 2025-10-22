def day_from_date_odd_days(date_str):
    """
    Calculate the day of the week from a given date using the odd days concept.
    Input: date_str in 'dd-mm-yyyy' format.
    Output: Day of the week as a string (e.g., 'Monday').
    """

    # Number of odd days in 400 years = 0, so we only need the year mod 400
    days_in_month_normal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_in_month_leap   = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    # Parse the input date
    day, month, year = map(int, date_str.split('-'))
    original_year = year

    # Years contribution
    years = year - 1  # Exclude the given year
    years_odd = (years % 400)

    # Odd days in 400, 100, 4 years
    centuries = years_odd // 100
    leap_years = (years_odd % 100) // 4
    ordinary_years = (years_odd % 100) - leap_years

    # Odd days from centuries
    odd_days = [0, 5, 3, 1]  # Odd days for 0th, 1st, 2nd, 3rd century in a 400-year cycle
    total_odd_days = odd_days[centuries]

    # Odd days from remaining years
    total_odd_days += (leap_years * 2)
    total_odd_days += (ordinary_years * 1)

    # Odd days from months of current year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        months_days = days_in_month_leap
    else:
        months_days = days_in_month_normal

    total_odd_days += sum(months_days[:month - 1])

    # Odd days from days of the current month
    total_odd_days += day

    # Day of the week
    result = total_odd_days % 7
    return week_days[result]

# Example usage:
date_string = "12-01-1979"  # 22 October 2025
print(day_from_date_odd_days(date_string))  # Output: 'Wednesday'
