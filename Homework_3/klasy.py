from shop.apple import Apple
from shop.potato import Potato
from shop.order import Order, print_order, create_random_order
from shop.product import Product, print_product

if __name__ == "__main__":
    print("Start")

    green_apple = Apple("red", "small", 5)
    red_apple = Apple("green", "big", 3)
    big_potato = Potato("Batat", "big", 8)
    small_potato = Potato("Kartofel", "small", 2)
    cookies = Product("Ciastka", "słodycze", 10)

    empty_order = Order("Jan", "Kowalski", order_list=[cookies])
    wiktor_order = Order("Wiktor", "Karczewski", order_list=[cookies, cookies])

    print_order(empty_order)
    print_order(wiktor_order)
    create_random_order()
