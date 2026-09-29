import tempfile
import unittest
from pathlib import Path

from cart import Cart
from inventory import Inventory


class CartTests(unittest.TestCase):
    def test_lowercase_product_code_is_normalized(self):
        with tempfile.TemporaryDirectory() as directory:
            inventory = Inventory(Path(directory) / "inventory.json")
            cart = Cart()
            cart.add("p001", 2, inventory)

            self.assertEqual(cart.items, {"P001": 2})

    def test_cannot_add_more_than_available_stock(self):
        with tempfile.TemporaryDirectory() as directory:
            inventory = Inventory(Path(directory) / "inventory.json")
            cart = Cart()

            with self.assertRaises(ValueError):
                cart.add("P001", 101, inventory)
