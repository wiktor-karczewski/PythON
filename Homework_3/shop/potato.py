class Potato:
    def __init__(self, sort, size, price, quantity):
        self.quantity = quantity
        self.sort = sort
        self.size = size
        self.price = price

    def calculate_final_amount(self):
        final_amount = self.quantity * self.price
        return final_amount

    def print_self(self):
        print("=" * 20)
        print(f"Ziemniaki typu {self.sort} w ilości {self.quantity} kg")
        print(f"Łączna kwota to {self.calculate_final_amount()} zł")
        print("=" * 20)
