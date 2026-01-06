# CIS 1702 - CW2 - Inventory Management System
import uuid
import datahandler

# Path always includes "Inventory management system" and "Main Menu"
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
    while True:
        choice = input(
                "1. Add Item\n"
                "2. View Stock\n"
                "3. Update Item\n"
                "4. Search\n"
                "q. Quit\n"
                "Select: "
            ).strip().lower()
        while not valid_choice(choice, 1, 4, True):
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
            quit()
        elif choice == "b":
            continue


def add_item():
    push_location("Add Item")
    show_location()
    print("b. Back\n")

    # Name
    name = input("Enter item name: \n").strip().capitalize()
    while not valid_string(name, 64):
        name = input("Enter item name: \n").strip().capitalize()
        if name.lower() == "b":
            pop_location()
            return

    # Price
    price = input("Enter item price: \n").strip()
    while not valid_num(price, 0, 9999):
        price = input("Enter item price: \n").strip()
        if price.lower() == "b":
            pop_location()
            return

    # Quantity
    quantity = input("Enter item quantity: \n").strip()
    while not valid_num(quantity, 0, 9999):
        quantity = input("Enter item quantity: \n").strip()
        if quantity.lower() == "b":
            pop_location()
            return

    result = datahandler.add_item(name, price, quantity)
    pop_location()
    print(result)
    return

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
    try:
        show_location()
        update_search = input(
            "1. Edit Item\n"
            "2. Delete Item\n"
            "b. Back\n"
            "Select: "
        ).strip().lower()
        while (valid_choice(update_search, 1, 2, False)) == False:
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
    finally:
        pop_location()

# Dysfunctional - awaiting full implementation.
def edit_item():
    push_location("Edit Item")
    try:
        stock = datahandler.view_all()
        if not stock:
            show_location()
            print("No items in stock")
            return

        while True:
            show_location()
            for item_name in stock.keys():
                print(item_name)
            temp = input("Which item would you like to edit (or `b` to go back): ").strip()
            if temp.lower() == "b":
                return
            if not valid_string(temp, 64):
                continue
            name = temp.capitalize()

            if name not in stock:
                print("Item with that name couldn't be found")
                return

            # Property selection with back option
            prop_choice = ""
            while True:
                prop_choice = input(
                    "Which property would you like to edit?\n"
                    "1. Price\n"
                    "2. Quantity\n"
                    "b. Back\n"
                    "Select: "
                ).strip().lower()
                if prop_choice == "b":
                    return
                if valid_choice(prop_choice, 1, 2, False):
                    break

            prop = "price" if prop_choice == "1" else "quantity"

            # New value with back option
            while True:
                temp = input(f"Enter the new value for {prop} (or `b` to go back): ").strip()
                if temp.lower() == "b":
                    return
                if valid_num(temp, 0, 9999):
                    try:
                        new_value = int(temp)
                    except ValueError:
                        new_value = int(float(temp))
                    break

            updated_item = datahandler.update_item(name, prop, new_value)
            print(f"Edited {updated_item.get('item_id', '(unknown)')} -> {prop}={new_value}")
            return
    finally:
        pop_location()


def delete_item():
    push_location("Delete Item")
    try:
        stock = datahandler.view_all()
        if not stock:
            show_location()
            print("No items in stock")
            return

        while True:
            show_location()
            for item_name in stock.keys():
                print(item_name)
            temp = input("Which item would you like to delete (or `b` to go back): ").strip()
            if temp.lower() == "b":
                return
            if not valid_string(temp, 64):
                continue
            item = temp.capitalize()
            if item not in stock:
                print("Item could not be found")
                return
            deleted_item = datahandler.delete_item(item)
            print(f"Deleted ({deleted_item[1]})")
            return
    finally:
        pop_location()


def search():
    push_location("Search")
    try:
        while True:
            show_location()
            search_choice = input(
                "1. By Name\n"
                "2. By Price\n"
                "3. By Quantity\n"
                "b. back\n"
                "Select: "
            ).strip().lower()
            if not valid_choice(search_choice, 1, 3, True):
                continue
            if search_choice == "1":
                search_by_name()
            elif search_choice == "2":
                search_by_price()
            elif search_choice == "3":
                search_by_quantity()
            elif search_choice == "b":
                break
    finally:
        pop_location()


def search_by_name():
    push_location("Search by Name")
    while True:
        show_location()
        while True:
            temp = input("Name: (or `b` to go back)\n").capitalize()
            if temp.lower() == "b":
                pop_location()
                return
            if valid_string(temp, 64):
                q = temp.capitalize()
                pop_location()
                break
        while True:
            item = datahandler.view_item(q)
            if type(item) == str:
                pop_location()
                print(item)
                return
            else:
                print(f"Results for item {q}")
                print(f"ID: {item['item_id']}")
                print(f"Price: {item['price']}")
                print(f"Quantity: {item['quantity']}")
                break
        pop_location()
        return


def search_by_price():
    push_location("Search by Price")
    while True:
        show_location()
        while True:
            temp = input("Price: (or `b` to back out)\n")
            if temp.lower() == "b":
                pop_location()
                return
            if valid_string(temp, 64):
                q = temp.capitalize()
                break
        while True:
            results = datahandler.search_by_price(q)

            # Check if there are any results
            if len(results) < 1:
                print("No items found")
                pop_location()
                return
            elif type(results) == str:
                print(results)
                pop_location()
                return
            else:
                for item, value in results.items():
                    print(f"Item name: {item}")
                    print(f"Item ID: {value['item_id']}")
                    print(f"Price: {value['price']}")
                    print(f"Quantity: {value['quantity']}")
                    print("\n--------\n")
                pop_location()
                return



def search_by_quantity():
    push_location("Search by Quantity")
    while True:
        show_location()
        while True:
            temp = input("Quantity: (click `b` to go back):\n")
            if temp.lower() == 'b':
                return
            if valid_string(temp, 64):
                q = temp.capitalize()

                break
        while True:
            results = datahandler.search_by_quantity(q)

            # Check if there are any results
            if len(results) < 1:
                print("No items found")
                pop_location()
                return
            elif type(results) == str:
                print(results)
                pop_location()
                return
            else:
                for item, value in results.items():
                    print(f"Item name: {item}")
                    print(f"Item ID: {value['item_id']}")
                    print(f"Price: {value['price']}")
                    print(f"Quantity: {value['quantity']}")

                    print("\n--------\n")
                pop_location()
                return


if __name__ == "__main__":
    main()
