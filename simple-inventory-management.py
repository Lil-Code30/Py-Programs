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

def add_product(inventory, product):
    """Add a product to the inventory."""


def main():
    filename = "product-inventory.csv"
    inventory = load_inventory(filename)
    print(inventory)




if __name__ == "__main__":
    main()