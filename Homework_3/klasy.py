from shop.apple import Apple
from shop.potato import Potato
from shop.order import Order, create_random_order
from shop.product import Product


def start_example():
    empty_order = Order("Jan", "Kowalski", order_list=[])
    wiktor_order = Order("Wiktor", "Karczewski", order_list=[])
    empty_order.print_self()
    wiktor_order.print_self()
    create_random_order()
    some_apples = Apple("Red", "Big", 4, 5)
    some_potatoes = Potato("Młode", "small", 2, 5)
    some_apples.print_self()
    some_potatoes.print_self()


if __name__ == "__main__":
    print("Start")
    start_example()

