# Store-Manager

Simple Python-based store management software with inventory and checkout features.

## Features

1. Add, update, delete, and display products.
2. Input validation prevents negative prices/quantities and invalid product IDs.
3. Cart supports multiple products and combined quantities.
4. Stock availability is checked before items enter the cart.
5. Checkout reduces stock, saves the changed inventory, thanks the customer, and exits.
6. Inventory persists in `inventory.json` after restarting the program.
7. Automated tests verify inventory persistence, cart validation and stock limits, and billing calculations.

## Technology Used

1. Python 3
2. Microsoft Visual Studio Code
3. Python Standard Library:
   - `pathlib` — handles inventory file paths safely.
   - `json` — saves and reloads inventory data.
   - `dataclasses` — defines the product data model.
   - `tempfile` — creates isolated temporary files during tests.

## How to Use

1. Download or clone the repository.
2. Open the project folder in an IDE of your choice.
3. Run `main.py`.

Alternatively, open a terminal in the project directory and run:

```bash
python3 main.py
