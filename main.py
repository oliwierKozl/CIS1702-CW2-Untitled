# CIS 1702 - CW2 - Inventory Management System
"""
TODO:
- Add a directory tree to see what submenu you are in etc. - DONE
- add actual data handling (json read/write) - oliver
- input validation - luca
- testing
"""

# Python.
import sys, uuid
import datahandler

# Path always includes "Inventory management system" and "Main Menu".
current_path = ["Inventory Management System", "Main Menu"]
persistent_logs = []

def clear_screen():
    if sys.stdout.isatty():
        print("\033[2J\033[H", end="", flush=True)
    else:
        print("\n" * 100, end="", flush=True)

# Persistence for relevant things (e.g. view stock, search results).
def log(msg: str):
    persistent_logs.append(msg)
    print(msg)
    
# Current path and location.
def push_location(name: str):
    current_path.append(name)

#Removes the last path, used when we go back to the menu
def pop_location():
    if len(current_path) > 1:
        current_path.pop()

# String formatting for the directory tree.
def show_location():
    clear_screen()
    app_name = current_path[0]
    parts = current_path[1:]
    if parts:
        location = (
            " > ".join(parts[:-1] + [f"«{parts[-1]}»"]) 
            if len(parts) > 1 
            else f"«{parts[0]}»"
        )
    else:
        location = f"«{app_name}»"
    print(f"{app_name} - {location}")
    if persistent_logs:
        print("\n")  # Space between header and logs.
        for msg in persistent_logs:
            print(msg)

def main():
    while True:
        show_location()
        choice = input(
            "1. Add Item\n"
            "2. View Stock\n"
            "3. Update Item\n"
            "4. Search\n"
            "q. Quit\n"
            "Select: "
            ).strip().lower()
        if choice == "1":
            add_item()
        elif choice == "2":
            view_stock()
        elif choice == "3":
            update_item()
        elif choice == "4":
            search()
        elif choice == "q":
            break

def add_item():
    push_location("Add Item")
    show_location()
    name = input("Enter item name: ").strip()
    price = input("Enter item price: ").strip()
    quantity = input("Enter item quantity: ").strip()
    result = datahandler.add_item(name, price, quantity) # Add item
    log(result)
    pop_location()

# Dysfunctional - awaiting full implementation.
def view_stock():
    push_location("View Stock (placeholder)")
    show_location()
    stock = datahandler.view_all()
    if len(stock) == 0:
        log("Nothing is in stock")
    else:
        for item in stock:
            log(item)

    pop_location()

# Includes delete item function.
def update_item():
    push_location("Update Item")
    while True:
        show_location()
        update_search = input(
            "1. Edit Item\n"
            "2. Delete Item\n"
            "b. Back\n"
            "Select: "
        ).strip().lower()
        if update_search == "1":
            edit_item()
        elif update_search == "2":
            delete_item()
        elif update_search == "b":
            break
    pop_location()

# Dysfunctional - awaiting full implementation.
def edit_item():
    push_location("Edit Item")
    show_location()
    new_name = input("New name (leave blank to keep): ")
    log(f"Edited {'item_id'} -> Name={new_name or '(unchanged)'}")
    pop_location()


def delete_item():
    push_location("Delete Item")
    show_location()
    #Displays the stock
    stock = datahandler.view_all()

    if len(stock) == 0:
        log("No items in stock")
    else:
        log(stock)
        item = input("Which item would you like to delete: ").capitalize()
        deleted_item = datahandler.delete_item(item)
        #Logs the deleted item's id
        log(f"Deleted ({deleted_item[1]}) ")
    pop_location()


#Dysfunctional - awaiting full implementation.
def search():
    push_location("Search")
    while True:
        show_location()
        search_choice = input(
            "1. By Name\n"
            "2. By Price\n"
            "3. By Quantity\n"
            "b. back\n"
            "Select: "
        ).strip().lower()
        if search_choice == "1":
            search_by_name()
        elif search_choice == "2":
            search_by_price()
        elif search_choice == "3":
            search_by_quantity()
        elif search_choice == "b":
            break
    pop_location()

# Dysfunctional - awating full implementation.
def search_by_name():
    push_location("Search by Name")
    show_location()
    q = input("Name: ") 
    item = datahandler.view_item(q)
    if type(item) == str:
        log(item)
    else:
        log(f"Results for item {q}")
        log(f"ID: {item['item_id']}")
        log(f"Price: {item['price']}")
        log(f"Quantity: {item['quantity']}")
    pop_location()

# Dysfunctional - awating full implementation.
def search_by_price():
    push_location("Search by Price")
    show_location()
    q = input("Price: ")
    results = datahandler.search_by_price(q)

    # Check if there are any results
    if len(results) < 1:
        log("No items found")
    else:
        for item, value in results.items():
            log(f"Item name: {item}")
            log(f"Item ID: {value['item_id']}")
            log(f"Price: {value['price']}")
            log(f"Quantity: {value['quantity']}")
            log("\n--------\n")

    pop_location()

# Dysfunctional - awating full implementation.
def search_by_quantity():
    push_location("Search by Quantity")
    show_location()
    q = input("Quantity: ")
    results = datahandler.search_by_quantity(q)

    # Check if there are any results
    if len(results) < 1:
        log("No items found")
    else:
        for item, value in results.items():
            log(f"Item name: {item}")
            log(f"Item ID: {value['item_id']}")
            log(f"Price: {value['price']}")
            log(f"Quantity: {value['quantity']}")
            
            log("\n--------\n")
    pop_location()

if __name__ == "__main__":
    main()
