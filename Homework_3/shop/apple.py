class Apple:
    def __init__(self, sort, size, price, quantity):
        self.sort = sort
        self.size = size
        self.price = price
        self.quantity = quantity

    def calculate_final_amount(self):
        final_amount = self.quantity * self.price
        return final_amount

    def print_self(self):
        print("=" * 20)
        print(f"Jabłka typu {self.sort} w ilości {self.quantity} kg")
        print(f"Łączna kwota to {self.calculate_final_amount()} zł")
        print("=" * 20)