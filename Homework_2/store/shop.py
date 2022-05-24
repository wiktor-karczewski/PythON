from .storage import products, update_quantity

orders = []

def place_order(name, quantity):
    price = products[name]["price"]
    available_quantity = products[name]["quantity"]

    if available_quantity < quantity:
        print("Nie mamy tyle towaru.")
        return None

    total_price = price * quantity
    new_order = {
        "product": name,
        "quantity": quantity,
        "total_price": total_price
    }
    update_quantity(name, quantity)
    orders.append(new_order)
    return new_order
