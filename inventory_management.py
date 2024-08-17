from pymongo import MongoClient

def get_database():
    client = MongoClient("mongodb://localhost:27017/")
    return client["inventory_db"]

db = get_database()
inventory_collection = db["Inventory"]

def add_item():
    item_id = input("Enter item ID: ")
    name = input("Enter item name: ")
    quantity = int(input("Enter item quantity: "))
    price = float(input("Enter item price: "))
    category = input("Enter item category: ")

    item = {
        "item_id": item_id,
        "name": name,
        "quantity": quantity,
        "price": price,
        "category": category,
    }
    inventory_collection.insert_one(item)
    print(f"Item '{name}' added to inventory.\n")

def view_items():
    items = inventory_collection.find()
    for item in items:
        print(item)
    print()

def update_item():
    item_id = input("Enter the item ID to update: ")
    update_fields = {}

    name = input("Enter new name (leave blank to skip): ")
    if name:
        update_fields["name"] = name

    quantity = input("Enter new quantity (leave blank to skip): ")
    if quantity:
        update_fields["quantity"] = int(quantity)

    price = input("Enter new price (leave blank to skip): ")
    if price:
        update_fields["price"] = float(price)

    category = input("Enter new category (leave blank to skip): ")
    if category:
        update_fields["category"] = category

    if update_fields:
        inventory_collection.update_one(
            {"item_id": item_id},
            {"$set": update_fields}
        )
        print(f"Item '{item_id}' updated.\n")
    else:
        print("No updates made.\n")

def delete_item():
    item_id = input("Enter the item ID to delete: ")
    inventory_collection.delete_one({"item_id": item_id})
    print(f"Item '{item_id}' deleted from inventory.\n")

def search_item():
    name = input("Enter item name to search (leave blank to skip): ")
    category = input("Enter item category to search (leave blank to skip): ")

    query = {}
    if name:
        query["name"] = name
    if category:
        query["category"] = category

    results = inventory_collection.find(query)
    for item in results:
        print(item)
    print()

def main():
    while True:
        print("Inventory Management System")
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Search Item")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_item()
        elif choice == '2':
            view_items()
        elif choice == '3':
            update_item()
        elif choice == '4':
            delete_item()
        elif choice == '5':
            search_item()
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()