def day_from_date_odd_days(date_str):
    """
    Calculate the day of the week from a given date using the odd days concept.
    Input: date_str in 'dd-mm-yyyy' format.
    Output: Day of the week as a string (e.g., 'Monday').
    """
python3 day-of-week-webapp/src/app.py$BROWSER http://127.0.0.1:5000
    days_in_month_normal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_in_month_leap   = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    day, month, year = map(int, date_str.split('-'))
    original_year = year

    years = year - 1
    years_odd = (years % 400)

    centuries = years_odd // 100
    leap_years = (years_odd % 100) // 4
    ordinary_years = (years_odd % 100) - leap_years

    odd_days = [0, 5, 3, 1]
    total_odd_days = odd_days[centuries]

    total_odd_days += (leap_years * 2)
    total_odd_days += (ordinary_years * 1)

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        months_days = days_in_month_leap
    else:
        months_days = days_in_month_normal

    total_odd_days += sum(months_days[:month - 1])
    total_odd_days += day

    result = total_odd_days % 7
    return week_days[result]