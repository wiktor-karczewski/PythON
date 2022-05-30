import random
from shop.product import Product
from shop.order_element import OrderElement


class Order:
    def __init__(self, first_name, last_name, order_list=None):
        self.first_name = first_name
        self.last_name = last_name
        if order_list is None:
            order_list = []
        self.order_list = order_list
        self.total_price = self.calculate_total_price()

    def calculate_total_price(self):
        total_price = 0
        for element in self.order_list:
            total_price += element.calculate_price()
        return total_price

    def print_self(self):
        print("=" * 20)
        print(f"Zamawiający: {self.first_name} {self.last_name}")
        print("Lista zakupów:")
        for product in self.order_list:
            product.print_self()
        print(f"Łączna kwota: {self.total_price}")
        print("=" * 20)


def create_random_order():
    random_number = random.randint(1, 20)
    order = []
    for i in range(random_number):
        order.append(OrderElement(Product("Produkt" + str(i), "inne", random.randint(1, 15)), random.randint(1, 8)))
    random_order = Order("Janusz", "Kowalski", order)
    random_order.print_self()
