products = {
    "chleb": {
        "quantity": 100,
        "price": 3.5
    },
    "jajka": {
        "quantity": 150,
        "price": 1
    },
    "mleko": {
        "quantity": 12,
        "price": 3,
    }
}

def update_quantity(product_name, ordered_quantity):
    products[product_name]["quantity"] -= ordered_quantity
