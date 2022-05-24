import math


def calculate_c(a_len, b_len):
    return math.sqrt(pow(a_len, 2) + pow(b_len, 2))


a = int(input("Wpisz długość pierwszej przyprostokątnej: "))
b = int(input("Wpisz długość drugiej przyprostokątnej: "))

print(calculate_c(a, b))
