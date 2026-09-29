from validation import normalize_product_id, validate_cart_quantity


class Cart:
    def __init__(self):
        self.items = {}

    def add(self, product_id, quantity, inventory):
        product_id = normalize_product_id(product_id)
        quantity = validate_cart_quantity(quantity)
        product = inventory.get(product_id)
        if product is None:
            raise ValueError("Product ID does not exist.")
        new_quantity = self.items.get(product_id, 0) + quantity
        if new_quantity > product.quantity:
            raise ValueError(f"Not enough stock. Available: {product.quantity}")
        self.items[product_id] = new_quantity

    def is_empty(self):
        return not self.items
