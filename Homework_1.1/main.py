import speed

print("Zmierzmy predkosc biegu.")
ask_distance = int(input("Wpisz dystans: "))
ask_time = int(input("Wpisz czas: "))

print("Prędkość to: ", speed.calculate_speed(ask_distance, ask_time), "km/h")
