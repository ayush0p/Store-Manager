# Store-Manager

Simple Python-based store management software with inventory and checkout features.

## Features

1. Add, update, delete, and display products.
2. Input validation prevents negative prices/quantities and invalid product IDs.
3. Cart supports multiple products and combined quantities.
4. Stock availability is checked before items enter the cart.
5. Checkout reduces stock, saves the changed inventory, thanks the customer, and exits.
6. Inventory persists in `inventory.json` after restarting the program.

## Technology Used

1. Python 3
2. Microsoft Visual Studio Code
3. Python standard library:
   - `pathlib` — handles inventory file paths safely
   - `json` — saves and reloads inventory
   - `dataclasses` — defines the product data model
   - `tempfile` — creates isolated temporary files during tests

## How to Use

1. Download the script files.
2. Open `main.py` in an IDE of your choice.
3. Alternatively, open a terminal in the same directory and run:

   ```bash
   python3 main.py
