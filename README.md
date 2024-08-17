# Inventory Management System

## Overview

This Inventory Management System is a Python-based application that allows users to perform CRUD (Create, Read, Update, Delete) operations on inventory items stored in a MongoDB database. The system is designed to be simple yet effective for managing inventory data such as item ID, name, quantity, price, and category.

## Features

- **Add Item**: Add new items to the inventory with unique IDs.
- **View Items**: Display all items currently in the inventory.
- **Update Item**: Update the details (e.g., quantity, price) of an existing item.
- **Delete Item**: Remove an item from the inventory using its ID.
- **Search Item**: Search for items by name or category.

## Prerequisites

- **Python 3.x**: Make sure Python is installed on your system. You can download it from [here](https://www.python.org/downloads/).
- **MongoDB**: Install and run MongoDB on your system. You can download it from [here](https://www.mongodb.com/try/download/community).

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/ddevilz/chef-master.git
cd inventory_management
```

### 2. Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 3. MongoDB Setup

Ensure that MongoDB is installed and running on your system. By default, the application connects to a MongoDB instance running locally on the default port `27017`.

- **Database Name**: `inventory_db`
- **Collection Name**: `Inventory`

You can modify the database connection settings in the `inventory_management.py` script if necessary.

### 4. Running the Application

Run the application using the following command:

```bash
python inventory_management.py
```

### 5. Using the Application

Follow the on-screen prompts to perform the following actions:

- **1. Add Item**: Add a new item to the inventory by providing the item ID, name, quantity, price, and category.
- **2. View Items**: View all items stored in the inventory.
- **3. Update Item**: Update the details of an existing item by providing the item ID and the fields you wish to update.
- **4. Delete Item**: Remove an item from the inventory using its item ID.
- **5. Search Item**: Search for items in the inventory by name or category.
- **6. Exit**: Exit the application.

### 6. Example Usage

#### Adding an Item

```
Enter item ID: 101
Enter item name: Laptop
Enter item quantity: 5
Enter item price: 999.99
Enter item category: Electronics
Item 'Laptop' added to inventory.
```

#### Viewing Items

```
{'_id': ObjectId('...'), 'item_id': '101', 'name': 'Laptop', 'quantity': 5, 'price': 999.99, 'category': 'Electronics'}
```

## Project Structure

- `inventory_management.py`: Main script containing the logic for CRUD operations and user interaction.
- `README.md`: Documentation file explaining the project setup and usage.
- `requirements.txt`: List of Python dependencies required to run the application.
