import calculations.lokata

initial = int(input("Wprowadź kapitał początkowy: "))
percentage = int(input("Wprowadź procent: "))
years = int(input("Wprowadź liczbę lat: "))

final_value = calculations.lokata.calculate_deposit(initial, percentage, years)

print(f"Po {years} latach twoja lokata jest warta {final_value:.2f}")