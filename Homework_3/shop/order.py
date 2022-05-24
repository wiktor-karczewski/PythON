import random
from .product import Product, print_product


class Order:
    def __init__(self, first_name, last_name, order_list=None):
        self.first_name = first_name
        self.last_name = last_name
        if order_list is None:
            order_list = []
        self.order_list = order_list

        total_price = 0
        for product in order_list:
            total_price += product.price
        self.total_price = total_price
        pass


def print_order(order):
    print("=" * 20)
    print(f"Zamawiający: {order.first_name} {order.last_name}")
    print("Lista zakupów:")
    for product in order.order_list:
        print_product(product)
    print(f"Łączna kwota: {order.total_price}")
    print("=" * 20)

def create_random_order():
    random_number = random.randint(1, 20)
    order = []
    for i in range(random_number):
        order.append(Product("Produkt" + str(i), "random", random.randint(1, 15)))
    random_order = Order("Janusz", "Kowalski", order)
    print_order(random_order)