def cart_total(cart, inventory):
    return sum(inventory.get(product_id).price * quantity for product_id, quantity in cart.items.items())


def create_bill(cart, inventory):
    lines = [
        "\n========== BILL ==========",
        f"{'Product':<15}{'Qty':<8}{'Price':<10}{'Amount':<10}",
        "-" * 43,
    ]
    for product_id, quantity in cart.items.items():
        product = inventory.get(product_id)
        amount = product.price * quantity
        lines.append(f"{product.name:<15}{quantity:<8}{product.price:<10.2f}{amount:<10.2f}")
    lines.extend(["-" * 43, f"Total amount to pay: {cart_total(cart, inventory):.2f}"])
    return "\n".join(lines)
