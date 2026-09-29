# Store-Manager
Simple python based store management software, with inventory and checkout features 
..................

#Features 
1- Add, update, delete, and display products.
2- Add, update, delete, and display products.
3- Input validation prevents negative prices/quantities and invalid product IDs
4- Cart supports multiple products and combined quantities
5- Stock availability is checked before items enter the cart
6- Checkout reduces stock, saves the changed inventory, thanks the customer, and exits
7- Inventory persists in inventory.json after restarting the program.

#Technology used 
1- Python 3
2- Microsoft Visual Studio Code 
3- Python standard library
  3.1- pathlib to handle inventory file path safely 
  3.2- json saves and reloads inventory
  3.3- dataclasses defines product data model 
  3.4- tempfile created isolated temp files during tests

#How to use 
1- Download the script files
2- Open main.py in IDE of Choice 
3- Alternately open terminal in the same directory as the file and run "python3 main.py"
4- A welcome menu opens up, perform operations as needed 

