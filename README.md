# Inventory Management System
## Overview
This Inventory Management System is a Python application designed to manage products in an inventory. It allows users to add, update, and remove products, track low stock items, record sales, and generate reports on the current inventory and total revenue.

## Features
- **Add Product**: Add new products to the inventory with a unique identifier, name, price, and quantity.
- **Update Product**: Update details of existing products, including name, price, and quantity.
- **Remove Product**: Remove products from the inventory.
- **Track Inventory**: Identify products with low stock based on a user-defined threshold quantity.
- **Record Sale**: Record the sale of products and update inventory quantities and total revenue.
- **Generate Report**: Generate a report of the current inventory and total revenue from sales.


## Classes and Methods
### `Product` Class
The `Product` class stores product details.

**Attributes**
- `product_id` (int): Unique identifier for the product.
- `name` (str): Name of the product.
- `price` (float): Price of the product.
- `quantity` (int): Quantity of the product in stock.

### `InventoryManagementSystem` Class
The `InventoryManagementSystem` class manages the inventory of products.

**Attributes**
- `inventory` (dict): A dictionary to store product_id and Product objects.
- `total_revenue` (float): Total revenue from sales.

**Methods**
* `add_product(product_id, name, price, quantity)`: Add a new product to the inventory.
* `update_product(product_id, name=None, price=None, quantity=None)`: Update an existing product in the inventory.
* `remove_product(product_id)`: Remove a product from the inventory.
* `track_inventory(threshold)`: Track products with low stock based on a threshold quantity.
* `record_sale(product_id, quantity_sold)`: Record a sale of a product and update the inventory.
* `generate_report()`: Generate a report of the current inventory and total revenue.
  
## User Input Functions
* `add_product_input()`: Take user input for adding a new product to the inventory.
* `update_product_input(product_id)`: Take user input for updating an existing product in the inventory.
* `record_sale_input()`: Take user input for recording a sale of a product.
* `track_inventory_input()`: Take user input for tracking low stock products based on a threshold quantity.

## Main Program Loop
The main program loop provides a menu-driven interface for users to interact with the system. Users can choose to add a product, update a product, record a sale, track low stock products, generate a report, or exit the program.

### Usage
1. **Run the Program**: Start the program to display the menu options.
2. **Choose an Option**: Enter the number corresponding to the desired action:

   `1` : Add a product

   `2` : Update a product

   `3` : Record a sale

   `4` : Track low stock products

   `5` : Generate a report

   `6` : Exit the program
3. **Follow Prompts**: Follow the prompts to enter the necessary details for the chosen action.
4.  **View Results**: View the results of the action, such as updated inventory, sales records, low stock products, or a generated report.

## Example
Here is an example of how the program might be used:

```
=== Inventory Management System ===
1. Add Product
2. Update Product
3. Record Sale
4. Track Low Stock Products
5. Generate Report
6. Exit
Enter your choice (1-6): 1
Enter Product ID: 101
Enter Product Name: Laptop
Enter Product Price: 50000
Enter Product Quantity: 10
Product added successfully.

=== Inventory Management System ===
1. Add Product
2. Update Product
3. Record Sale
4. Track Low Stock Products
5. Generate Report
6. Exit
Enter your choice (1-6): 5
Current Inventory:
Product: Laptop, Price: 50000.0, Quantity: 10
Total Revenue from Sales: Rs.0

=== Inventory Management System ===
1. Add Product
2. Update Product
3. Record Sale
4. Track Low Stock Products
5. Generate Report
6. Exit
Enter your choice (1-6): 6
Exiting...
```

## Author
Developed by Vaanmathi R.