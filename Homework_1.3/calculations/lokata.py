def calculate_deposit(initial_value, percentage, years):
    value = initial_value * (1 + percentage / 100) ** years
    return value
