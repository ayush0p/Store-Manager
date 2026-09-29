def normalize_product_id(product_id):
    return product_id.strip().upper()


def validate_price(price):
    price = float(price)
    if price < 0:
        raise ValueError("Price cannot be negative.")
    return price


def validate_quantity(quantity):
    quantity = int(quantity)
    if quantity < 0:
        raise ValueError("Quantity cannot be negative.")
    return quantity


def validate_cart_quantity(quantity):
    quantity = validate_quantity(quantity)
    if quantity == 0:
        raise ValueError("Quantity must be greater than zero.")
    return quantity
