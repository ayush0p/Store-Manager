inventory = {
    "P001": {"name": "Apple", "price": 10, "quantity": 100},
    "P002": {"name": "Banana", "price": 5, "quantity": 200},
    "P003": {"name": "Orange", "price": 8, "quantity": 150},
    "P004": {"name": "Grapes", "price": 12, "quantity": 80},
    "P005": {"name": "Mango", "price": 15, "quantity": 50},
    "P006": {"name": "Pineapple", "price": 20, "quantity": 30},
    "P007": {"name": "Strawberry", "price": 25, "quantity": 40},
    "P008": {"name": "Bread", "price": 40, "quantity": 60},
    "P009": {"name": "Milk", "price": 30, "quantity": 70},
    "P010": {"name": "Eggs", "price": 15, "quantity": 90},
    "P011": {"name": "Cheese", "price": 50, "quantity": 20},
}

def npd(product_id): #normalize product id
    return product_id.strip().upper()

def add_product(product_id, name, price, quantity):
    product_id = npd(product_id)
    if not product_id:
        print("Product ID cannot be empty.")
    elif price < 0 or quantity < 0:
        print("Price and quantity cannot be negative.")
    elif product_id in inventory:
        print(f"Product ID {product_id} already exists. Use update_product to modify it.")
    else:
        inventory[product_id] = {"name": name, "price": price, "quantity": quantity}
        print(f"Product {name} added successfully.")

def update_product(product_id, name=None, price=None, quantity=None):
    product_id = npd(product_id)
    if product_id in inventory:
        if price is not None and price < 0:
            print("Price cannot be negative.")
            return
        if quantity is not None and quantity < 0:
            print("Quantity cannot be negative.")
            return
        if name is not None:
            inventory[product_id]["name"] = name
        if price is not None:
            inventory[product_id]["price"] = price
        if quantity is not None:
            inventory[product_id]["quantity"] = quantity
        print(f"Product ID {product_id} updated successfully.")
    else:
        print(f"Product ID {product_id} does not exist. Use add_product to add it.")

def delete_product(product_id):
    product_id = npd(product_id)
    if product_id in inventory:
        del inventory[product_id]
        print(f"Product ID {product_id} deleted successfully.")
    else:
        print(f"Product ID {product_id} does not exist.")

def display_inventory():
    print("\nCurrent Inventory:")
    if not inventory:
        print("Inventory is empty.")
        return
    print(f"{'ID':<8}{'Name':<15}{'Price':<10}{'Quantity':<10}")
    print("-" * 43)
    for product_id, details in inventory.items():
        print(f"{product_id:<8}{details['name']:<15}{details['price']:<10.2f}{details['quantity']:<10}")

def cart_total(cart):
    total = 0
    for product_id, quantity in cart.items():
        total += inventory[product_id]["price"] * quantity
    return total

def checkout(cart):
    normalized_cart = {}
    for product_id, quantity in cart.items():
        product_id = npd(product_id)
        normalized_cart[product_id] = normalized_cart.get(product_id, 0) + quantity
    cart = normalized_cart

    for product_id, quantity in cart.items():
        if product_id not in inventory:
            print(f"Product ID {product_id} does not exist.")
            return
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return
        if quantity > inventory[product_id]["quantity"]:
            print(f"Not enough stock for {inventory[product_id]['name']}. Available: {inventory[product_id]['quantity']}")
            return

    total = cart_total(cart)
    print("\n========== BILL ==========")
    print(f"{'Product':<15}{'Qty':<8}{'Price':<10}{'Amount':<10}")
    print("-" * 43)
    for product_id, quantity in cart.items():
        product = inventory[product_id]
        amount = product["price"] * quantity
        print(f"{product['name']:<15}{quantity:<8}{product['price']:<10.2f}{amount:<10.2f}")
    print("-" * 43)
    print(f"Total amount to pay: {total:.2f}")
    for product_id, quantity in cart.items():
        inventory[product_id]["quantity"] -= quantity
    print("Checkout complete. Inventory updated.")
    print("Thank you for shopping!")
    return True

def menu():
    print("Welcome to the Store Manager")
    print("1. Add Product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. Display Inventory")
    print("5. Checkout")
    print("6. Exit")
    return input("Enter your choice: ")

while True:
    try:
        choice = int(menu())
    except ValueError:
        print("Please enter a number from 1 to 6.")
        continue

    if choice == 1:
        product_id = input("Enter Product ID: ")
        name = input("Enter Product Name: ")
        try:
            price = float(input("Enter Product Price: "))
            quantity = int(input("Enter Product Quantity: "))
            add_product(product_id, name, price, quantity)
        except ValueError:
            print("Price must be a number and quantity must be a whole number.")
    elif choice == 2:
        product_id = input("Enter Product ID to update: ")
        name = input("Enter new Product Name (leave blank to keep unchanged): ")
        price_input = input("Enter new Product Price (leave blank to keep unchanged): ")
        quantity_input = input("Enter new Product Quantity (leave blank to keep unchanged): ")
        try:
            price = float(price_input) if price_input else None
            quantity = int(quantity_input) if quantity_input else None
            update_product(product_id, name if name else None, price, quantity)
        except ValueError:
            print("Price must be a number and quantity must be a whole number.")
    elif choice == 3:
        product_id = input("Enter Product ID to delete: ")
        delete_product(product_id)
    elif choice == 4:
        display_inventory()
        input("\nPress Enter to return to the menu...")
    elif choice == 5:
        cart = {}
        while True:
            product_id = input("Enter Product ID to add to cart (or 'done' to finish): ")
            if product_id.lower() == "done":
                break
            product_id = npd(product_id)
            if product_id not in inventory:
                print("Product ID does not exist.")
                continue
            try:
                quantity = int(input("Enter quantity: "))
            except ValueError:
                print("Quantity must be a whole number.")
                continue
            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue
            if cart.get(product_id, 0) + quantity > inventory[product_id]["quantity"]:
                print(f"Not enough stock. Available: {inventory[product_id]['quantity']}")
                continue
            cart[product_id] = cart.get(product_id, 0) + quantity
        if cart:
            if checkout(cart):
                break
        else:
            print("Cart is empty.")
    elif choice == 6:
        print("Exiting the Store Manager. Goodbye!")
        break
    else:
        print("Please enter a number from 1 to 6.")
