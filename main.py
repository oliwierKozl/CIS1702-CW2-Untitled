# CIS 1702 - CW2 - Inventory Management System
'''
TODO:
- Add a directory tree to see what submenu you are in etc. - DONE
- add actual data handling (json read/write) - oliver
- input validation - luca
- testing
-
'''
# python
import sys

# Default path variable
current_path = ["Inventory Management System", "Main Menu"]
persistent_logs = []

# Clears screen when going to a new menu.
def clear_screen():
    if sys.stdout.isatty():
        print("\033[2J\033[H", end="", flush=True)
    else:
        print("\n" * 100, end="", flush=True)

# Keeps persistance for important stuff like search results or view stock etc..
def log(msg: str):
    persistent_logs.append(msg)
    print(msg)
# current path and location
def push_location(name: str):
    current_path.append(name)

def pop_location():
    if len(current_path) > 1:
        current_path.pop()

# actual string formatting for the directory tree
def show_location():
    clear_screen()
    app = current_path[0]
    parts = current_path[1:]
    if parts:
        location = " > ".join(parts[:-1] + [f"«{parts[-1]}»"]) if len(parts) > 1 else f"«{parts[0]}»"
    else:
        location = f"«{app}»"
    print(f"{app} - {location}")
    if persistent_logs:
        print()  # space between header and logs
        for msg in persistent_logs:
            print(msg)

# main and submenu function
def Main():
    while True:
        show_location()
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
            break

def AddItem():
    push_location("Add Item")
    show_location()
    item_id = input("Enter item ID: ")
    name = input("Enter item name: ")
    price = input("Enter item price: ")
    quantity = input("Enter item quantity: ")
    log(f"Added: ID={item_id}, Name={name}, Price={price}, Qty={quantity}")
    pop_location()

def ViewStock():
    push_location("View Stock (placeholder)")
    show_location()
    log("(no items yet)")
    pop_location()

def UpdateItem():
    push_location("Update Item")
    while True:
        show_location()
        print("1. Edit Item")
        print("2. Delete Item")
        print("b. Back")
        sub = input("Select: ").strip().lower()
        if sub == '1':
            EditItem()
        elif sub == '2':
            DeleteItem()
        elif sub == 'b':
            break
    pop_location()

def EditItem():
    push_location("Edit Item")
    show_location()
    item_id = input("ID to edit: ")
    new_name = input("New name (leave blank to keep): ")
    log(f"Edited {item_id} -> Name={new_name or '(unchanged)'}")
    pop_location()

def DeleteItem():
    push_location("Delete Item")
    show_location()
    item_id = input("ID to delete: ")
    log(f"Deleted (placeholder) {item_id}")
    pop_location()

def Search():
    push_location("Search")
    while True:
        show_location()
        print("1. By Name")
        print("2. By Price")
        print("3. By Quantity")
        print("b. Back")
        s = input("Select: ").strip().lower()
        if s == '1':
            SearchByName()
        elif s == '2':
            SearchByPrice()
        elif s == '3':
            SearchByQuantity()
        elif s == 'b':
            break
    pop_location()

# this is kinda fucked rn but we ball
def SearchByName():
    push_location("Search by Name")
    show_location()
    q = input("Name: ")
    log(f"Searching for '{q}' (placeholder)")
    pop_location()

def SearchByPrice():
    push_location("Search by Price")
    show_location()
    q = input("Price: ")
    log(f"Searching for '{q}' (placeholder)")
    pop_location()

def SearchByQuantity():
    push_location("Search by Quantity")
    show_location()
    q = input("Quantity: ")
    log(f"Searching for '{q}' (placeholder)")
    pop_location()

if __name__ == "__main__":
    Main()
