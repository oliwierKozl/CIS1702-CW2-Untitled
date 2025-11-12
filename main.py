# CIS 1702 - CW2 - Inventory Management System
'''
TODO:
- Add a directory tree to see what submenu you are in etc.
- add actual data handling (json read/write) - oliver
- input validation - luca
- testing
-
'''

# Basic main functionality
def Main():
    while True:
        print("\n=== Inventory Management System ===")
        print("1. Add Item")
        print("2. View Stock")
        print("3. Update Item")
        print("4. Search")
        print("q. Quit")

        choice = input("Select an option: ").strip().lower()

        if choice == '1':
            AddItem()
        elif choice == '2':
            ViewStock()
        elif choice == '3':
            UpdateItem()
        elif choice == '4':
            Search()
        elif choice == 'q':
            print("Quitting program.")
            break
        else:
            print("Invalid choice, please try again.")

# guessing what we might store - can remove/change or add options later.
def AddItem():
    print("\n--- Add New Item ---")
    item_id = input("Enter item ID: (id system not figured out yet, enter anything) ")
    name = input("Enter item name: ")
    price = input("Enter item price: ")
    quantity = input("Enter item quantity: ")

    # placeholder for adding logic later - whatever oliver does with the json stuff will change this.
    print(f"\nItem Added (preview): ID={item_id}, Name={name}, Price={price}, Quantity={quantity}")

def ViewStock():
    print("\n--- View Stock ---")
    # placeholder for later json data display
    print("(This would display all inventory items in a table format. (needs json stuff tho)")

def UpdateItem():
    while True:
        print("\n--- Update Item ---")
        print("1. Edit Item")
        print("2. Delete Item")
        print("b. Back to Main Menu")

        sub_choice = input("Select an option: ").strip().lower()

        if sub_choice == '1':
            EditItem()
        elif sub_choice == '2':
            DeleteItem()
        elif sub_choice == 'b':
            break
        else:
            print("Invalid choice, please try again.")

def EditItem():
    print("\n--- Edit Item ---")
    item_id = input("Enter the ID of the item to edit: ")
    print("Enter new values (leave blank to keep current):")
    new_name = input("New name: ")
    new_price = input("New price: ")
    new_quantity = input("New quantity: ")
    print(f"\nEditing item {item_id} with changes -> Name: {new_name}, Price: {new_price}, Quantity: {new_quantity}")

def DeleteItem():
    print("\n--- Delete Item ---")
    item_id = input("Enter the ID of the item to delete: ")
    print(f"Item with ID {item_id} would be deleted (placeholder).")

def Search():
    while True:
        print("\n--- Search ---")
        print("1. Search by Name")
        print("2. Search by Price")
        print("3. Search by Quantity")
        print("b. Back to Main Menu")

        search_choice = input("Select an option: ").strip().lower()

        if search_choice == '1':
            SearchByName()
        elif search_choice == '2':
            SearchByPrice()
        elif search_choice == '3':
            SearchByQuantity()
        elif search_choice == 'b':
            break
        else:
            print("Invalid choice, please try again.")

def SearchByName():
    print("\n--- Search by Name ---")
    name = input("Enter item name to search: ")
    print(f"Searching for items with name '{name}' (placeholder).")

def SearchByPrice():
    print("\n--- Search by Price ---")
    price = input("Enter price to search: ")
    print(f"Searching for items with price '{price}' (placeholder).")

def SearchByQuantity():
    print("\n--- Search by Quantity ---")
    quantity = input("Enter quantity to search: ")
    print(f"Searching for items with quantity '{quantity}' (placeholder).")

if __name__ == "__main__":
    Main()
