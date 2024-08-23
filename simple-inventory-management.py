import csv 

def load_inventory(filename):
    inventory = []
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                #converting quantity ans price to integers for further operations
                row['quantity'] = int(row['quantity'])
                row['price'] = float(row['price'])
                inventory.append(row)
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty inventory.")
    return inventory

def save_inventory(filename, inventory):
    """Saving inventory to a CSV file"""
    with open(filename, 'w', newline='') as file:
        fieldnames = ['id','name', 'quantity', 'price']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(inventory)

def add_product(inventory, product):
    """Adding a product to the inventory"""
    inventory.append(product)
    print(f"Added product: {product['name']}")

def remove_product(inventory, product_id):
    """Removing a product from the inventory"""
    for i,product in enumerate(inventory):
        if product['id'] == product_id:
            del inventory[i]
            print(f"Removed product with id: {product_id}")
            return
    print(f"No product with id: {product_id} found in the inventory.")


def main():
    filename = "product-inventory.csv"
    #loading the inventory file (csv) into dictionaries in a list
    inventory = load_inventory(filename)

    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Remove Product")
        print("6. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            id = input("Enter product ID: ")
            name = input("Enter product name: ")
            quantity = int(input("Enter product quantity: "))
            price = float(input("Enter product price: "))
            product = {'id': id, 'name': name, 'quantity': quantity, 'price': price}
            add_product(inventory, product)
        elif choice == '2':
            product_id = input("Enter product ID to remove: ")
            remove_product(inventory, product_id)
        elif choice == '6':
            save_inventory(filename, inventory)
            print("Inventory Saved. Exiting...")
            break
        else: 
            print("Invalid choice. Please choose again.")




if __name__ == "__main__":
    main()