import json
from pathlib import Path

from models import Product
from validation import normalize_product_id, validate_price, validate_quantity


DEFAULT_INVENTORY = {
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


class Inventory:
    def __init__(self, storage_path=None):
        self.storage_path = Path(storage_path or Path(__file__).with_name("inventory.json"))
        self.products = self._load()

    def _load(self):
        if self.storage_path.exists():
            with self.storage_path.open() as file:
                data = json.load(file)
        else:
            data = DEFAULT_INVENTORY
        return {product_id: Product.from_dict(product) for product_id, product in data.items()}

    def save(self):
        data = {product_id: product.to_dict() for product_id, product in self.products.items()}
        with self.storage_path.open("w") as file:
            json.dump(data, file, indent=4)

    def get(self, product_id):
        return self.products.get(normalize_product_id(product_id))

    def add(self, product_id, name, price, quantity):
        product_id = normalize_product_id(product_id)
        if not product_id:
            raise ValueError("Product ID cannot be empty.")
        if product_id in self.products:
            raise ValueError(f"Product ID {product_id} already exists.")
        self.products[product_id] = Product(name, validate_price(price), validate_quantity(quantity))
        self.save()

    def update(self, product_id, name=None, price=None, quantity=None):
        product_id = normalize_product_id(product_id)
        product = self.get(product_id)
        if product is None:
            raise ValueError(f"Product ID {product_id} does not exist.")
        if name:
            product.name = name
        if price is not None:
            product.price = validate_price(price)
        if quantity is not None:
            product.quantity = validate_quantity(quantity)
        self.save()

    def delete(self, product_id):
        product_id = normalize_product_id(product_id)
        if product_id not in self.products:
            raise ValueError(f"Product ID {product_id} does not exist.")
        del self.products[product_id]
        self.save()

    def reduce_stock(self, cart_items):
        for product_id, quantity in cart_items.items():
            product = self.get(product_id)
            if product is None:
                raise ValueError(f"Product ID {product_id} does not exist.")
            if quantity > product.quantity:
                raise ValueError(f"Not enough stock for {product.name}. Available: {product.quantity}")
        for product_id, quantity in cart_items.items():
            self.products[normalize_product_id(product_id)].quantity -= quantity
        self.save()

    def display(self):
        print("\nCurrent Inventory:")
        if not self.products:
            print("Inventory is empty.")
            return
        print(f"{'ID':<8}{'Name':<15}{'Price':<10}{'Quantity':<10}")
        print("-" * 43)
        for product_id, product in self.products.items():
            print(f"{product_id:<8}{product.name:<15}{product.price:<10.2f}{product.quantity:<10}")
