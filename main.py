# python
# CIS 1702 - CW2 - Inventory Management System
"""
TODO:
- Add a directory tree to see what submenu you are in etc. - DONE
- add actual data handling (json read/write) - oliver
- input validation - luca
- testing
"""

import uuid
import datahandler

# Path always includes "Inventory management system" and "Main Menu".
current_path = ["Inventory Management System", "Main Menu"]


# Current path and location.
def push_location(name: str):
    current_path.append(name)


# Removes the last path, used when we go back to the menu
def pop_location():
    if len(current_path) > 1:
        current_path.pop()


# String formatting for the directory tree.
def show_location():
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


def valid_choice(num: str, min: float, max: float, allow_chars: bool):
    if num == "q" and allow_chars == True:
        return (True)
    elif num == "b" and allow_chars == True:
        return(True)
    try:
        num = int(num)
        if min <= num <= max:
            return (True)
    except:
        return (False)
    return (False)


def valid_num(num: str, min: float, max: float):
    try:
        num = float(num)
        if min <= num <= max:
            return (True)
    except:
        print("Invalid input")
        return (False)
    return (False)


def valid_string(text: str, max_length: int):
    try:
        text = str(text)
    except:
        print("Invalid input - must be a string")
    if text.isalnum() == True and 1 <= len(text) <= max_length:
        return (True)
    show_location()
    print("Name must consist of letters and numbers and be less than 64 characters.")
    return (False)


def main():
    choice = ""
    while valid_choice(choice, 1, 4, True) == False:
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
    elif choice == "q" or choice == "b":
        quit()


def add_item():
    push_location("Add Item")
    show_location()
    print("b. Back\n")
    name = ""
    price = -1
    quantity = -1
    while valid_string(name, 64) == False:
        name = input("Enter item name: \n").strip().lower().capitalize()
    while valid_num(price, 0, 9999) == False:
        price = input("Enter item price: \n").strip()
    while valid_num(quantity, 0, 9999) == False:
        quantity = input("Enter item quantity: \n").strip()
    result = datahandler.add_item(name, price, quantity)
    main()
    print(result)
    pop_location()


# Displays all items in stock.
def view_stock():
    push_location("View Stock")
    show_location()
    stock = datahandler.view_all()
    if not stock:
        print("Nothing is in stock")
    else:
        print("-------------------")
        for item, data in stock.items():
            print(item)
            print(f"Item ID: {data['item_id']}")
            print(f"Quantity: {data['quantity']}")
            print(f"Price: £{data['price']}")
            print("-------------------")
    main()
    pop_location()


# Includes delete item function.
def update_item():
    push_location("Update Item")
    show_location()
    update_search = ""
    while valid_choice(update_search, 1, 2, True) == False:
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
        main()
    pop_location()


# Dysfunctional - awaiting full implementation.
def edit_item():
    # Initialise loop
    running = True
    name = ""
    new_value = -1
    while running:
        push_location("Edit Item")
        show_location()
        stock = datahandler.view_all()

        while valid_string(name, 64) == False:
            name = input("Which item would you like to edit: ").strip().capitalize()
        # Checks if item is not inside the stock

        if name not in stock:
            print("Item with that name couldn't be found")
            edit_item()

        new_property = input("Which property would like to edit"
                                 "\n1. Price"
                                 "\n2. Quantity\n").lower()
        while valid_choice(new_property, 1, 2, False) == False:
            new_property = input("Which property would like to edit"
                                 "\n1. Price"
                                 "\n2. Quantity\n").lower()
        # Assigns property to its relevant property
        if new_property == "1":
            new_property = "price"
        elif new_property == "2":
            new_property = "quantity"
        else:
            print("Property couldn't be edited")
            main()

        try:
            while valid_num(new_value, 0, 9999) == False:
                new_value = int(input(f"Enter the new value for {new_property}: "))
        except ValueError:
            print("Value should a number")
        else:
            # Item is updated and saved inside the datahandler
            updated_item = datahandler.update_item(name, new_property, new_value)
            print(f"Edited {updated_item['item_id']} -> {new_property}={name or '(unchanged)'}")
            break
        main()
    pop_location()
    main()

def delete_item():
    item = ""

    while True:
        push_location("Delete Item")
        show_location()
        # Displays the stock
        stock = datahandler.view_all()

        if len(stock) == 0:
            print("No items in stock")
            main()

        else:
            for item, data in stock.items():
                print(item)
            while valid_string(item, 64) == False:
                item = input("Which item would you like to delete: ").capitalize()
            if item not in stock:
                print("item could not be found")
                main()
            deleted_item = datahandler.delete_item(item)
            # Prints the deleted item's id
            print(f"Deleted ({deleted_item[1]}) ")
            main()
    pop_location()


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


def search_by_name():
    push_location("Search by Name")
    show_location()
    q = input("Name: ")
    item = datahandler.view_item(q)
    if type(item) == str:
        print(item)
    else:
        print(f"Results for item {q}")
        print(f"ID: {item['item_id']}")
        print(f"Price: {item['price']}")
        print(f"Quantity: {item['quantity']}")
    pop_location()


def search_by_price():
    push_location("Search by Price")
    show_location()
    q = input("Price: ")
    results = datahandler.search_by_price(q)

    # Check if there are any results
    if len(results) < 1:
        print("No items found")
    else:
        for item, value in results.items():
            print(f"Item name: {item}")
            print(f"Item ID: {value['item_id']}")
            print(f"Price: {value['price']}")
            print(f"Quantity: {value['quantity']}")
            print("\n--------\n")

    pop_location()


def search_by_quantity():
    push_location("Search by Quantity")
    show_location()
    q = input("Quantity: ")
    results = datahandler.search_by_quantity(q)

    # Check if there are any results
    if len(results) < 1:
        print("No items found")
    else:
        for item, value in results.items():
            print(f"Item name: {item}")
            print(f"Item ID: {value['item_id']}")
            print(f"Price: {value['price']}")
            print(f"Quantity: {value['quantity']}")

            print("\n--------\n")
    pop_location()


if __name__ == "__main__":
    main()
