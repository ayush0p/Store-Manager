import tempfile
import unittest
from pathlib import Path

from inventory import Inventory


class InventoryTests(unittest.TestCase):
    def test_add_product_is_saved_and_reloaded(self):
        with tempfile.TemporaryDirectory() as directory:
            storage_path = Path(directory) / "inventory.json"
            inventory = Inventory(storage_path)
            inventory.add("p100", "Pear", 12.5, 10)

            reloaded_inventory = Inventory(storage_path)
            product = reloaded_inventory.get("P100")

            self.assertEqual(product.name, "Pear")
            self.assertEqual(product.quantity, 10)
