def convert_temperature(value: float, unit: str):
    # Bug 1 fixed: Incorrect formula for Celsius to Fahrenheit
    # Correct formula is (C * 9 / 5) + 32

    # Bug 2 fixed: Incorrect formula for Fahrenheit to Celsius
    # Correct formula is (F - 32) * 5 / 9

    # Bug 3 fixed: Missing validation for invalid unit input

    if unit == 'C':
        return round((value * 9 / 5) + 32, 1)
    elif unit == 'F':
        return round((value - 32) * 5 / 9, 1)
    else:
        return "Invalid Unit"
