from store.shop import place_order


def run_shop():
    print("Witaj w sklepie!")
    name = input("Jaki towar cię interesuje?: ")
    quantity = int(input("Ile sztuk/kg chcesz kupić?: "))

    result = place_order(name, quantity)
    if result is not None:
        total_price = result["total_price"]
        print(f"Łączny koszt zamówienia to: {total_price} zł")


if __name__ == "__main__":
    run_shop()
