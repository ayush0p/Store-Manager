from billing import create_bill
from cart import Cart
from inventory import Inventory


def menu():
    print("\nWelcome to the Store Manager")
    print("1. Add Product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. Display Inventory")
    print("5. Checkout")
    print("6. Exit")
    return input("Enter your choice: ")


def checkout(inventory):
    cart = Cart()
    while True:
        product_id = input("Enter Product ID to add to cart (or 'done' to finish): ")
        if product_id.lower() == "done":
            break
        try:
            cart.add(product_id, input("Enter quantity: "), inventory)
        except ValueError as error:
            print(error)

    if cart.is_empty():
        print("Cart is empty.")
        return False

    print(create_bill(cart, inventory))
    inventory.reduce_stock(cart.items)
    print("Checkout complete. Inventory updated.")
    print("Thank you for shopping!")
    return True


def main():
    inventory = Inventory()
    while True:
        choice = menu()
        try:
            if choice == "1":
                inventory.add(
                    input("Enter Product ID: "),
                    input("Enter Product Name: "),
                    input("Enter Product Price: "),
                    input("Enter Product Quantity: "),
                )
                print("Product added successfully.")
            elif choice == "2":
                product_id = input("Enter Product ID to update: ")
                name = input("Enter new Product Name (leave blank to keep unchanged): ") or None
                price = input("Enter new Product Price (leave blank to keep unchanged): ") or None
                quantity = input("Enter new Product Quantity (leave blank to keep unchanged): ") or None
                inventory.update(product_id, name, price, quantity)
                print("Product updated successfully.")
            elif choice == "3":
                inventory.delete(input("Enter Product ID to delete: "))
                print("Product deleted successfully.")
            elif choice == "4":
                inventory.display()
                input("\nPress Enter to return to the menu...")
            elif choice == "5":
                if checkout(inventory):
                    break
            elif choice == "6":
                print("Exiting the Store Manager. Goodbye!")
                break
            else:
                print("Please enter a number from 1 to 6.")
        except ValueError as error:
            print(error)


if __name__ == "__main__":
    main()
