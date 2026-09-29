import tempfile
import unittest
from pathlib import Path

from billing import cart_total, create_bill
from cart import Cart
from inventory import Inventory


class BillingTests(unittest.TestCase):
    def test_bill_contains_total_and_product(self):
        with tempfile.TemporaryDirectory() as directory:
            inventory = Inventory(Path(directory) / "inventory.json")
            cart = Cart()
            cart.add("P001", 2, inventory)

            bill = create_bill(cart, inventory)

            self.assertEqual(cart_total(cart, inventory), 20)
            self.assertIn("Apple", bill)
            self.assertIn("Total amount to pay: 20.00", bill)
