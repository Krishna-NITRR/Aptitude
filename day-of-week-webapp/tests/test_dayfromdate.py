def test_day_from_date_odd_days():
    from src.dayfromdate import day_from_date_odd_days

    # Test cases
    test_cases = {
        "12-01-1979": "Friday",
        "01-01-2000": "Saturday",
        "29-02-2020": "Saturday",  # Leap year
        "31-12-1999": "Friday",
        "01-01-1900": "Monday",
        "15-08-1947": "Friday",
        "22-10-2025": "Wednesday",
        "01-01-2023": "Sunday",
        "31-12-2023": "Sunday",
        "29-02-2024": "Thursday"  # Leap year
    }

    for date_str, expected_day in test_cases.items():
        assert day_from_date_odd_days(date_str) == expected_day, f"Failed for {date_str}"