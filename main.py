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
import sys, uuid
import datahandler

# Default path variable
CurrentPath = ["Inventory Management System", "Main Menu"]
PersistantLogs = []

# Clears screen when going to a new menu.
def ClearScreen():
    if sys.stdout.isatty():
        print("\033[2J\033[H", end="", flush=True)
    else:
        print("\n" * 100, end="", flush=True)

# Keeps persistance for important stuff like search results or view stock etc..
def log(msg: str):
    PersistantLogs.append(msg)
    print(msg)
# current path and location
def PushLocation(name: str):
    CurrentPath.append(name)

def PopLocation():
    if len(CurrentPath) > 1:
        CurrentPath.pop()

# actual string formatting for the directory tree
def ShowLocation():
    ClearScreen()
    app = CurrentPath[0]
    parts = CurrentPath[1:]
    if parts:
        location = " > ".join(parts[:-1] + [f"«{parts[-1]}»"]) if len(parts) > 1 else f"«{parts[0]}»"
    else:
        location = f"«{app}»"
    print(f"{app} - {location}")
    if PersistantLogs:
        print()  # space between header and logs
        for msg in PersistentLogs:
            print(msg)

# main and submenu function
def Main():
    while True:
        ShowLocation()
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
    PushLocation("Add Item")
    ShowLocation()
    name = input("Enter item name: ")
    price = input("Enter item price: ")
    quantity = input("Enter item quantity: ")

    result = datahandler.AddItem(name, price, quantity)
    log(result) # Print if item has been added or not. 
    PopLocation()

def ViewStock():
    PushLocation("View Stock (placeholder)")
    ShowLocation()
    log("(no items yet)")
    PopLocation()

def UpdateItem():
    PushLocation("Update Item")
    while True:
        ShowLocation()
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
    PopLocation()

def EditItem():
    PushLocation("Edit Item")
    ShowLocation()
    new_name = input("New name (leave blank to keep): ")
    log(f"Edited {item_id} -> Name={new_name or '(unchanged)'}")
    PopLocation()

def DeleteItem():
    PushLocation("Delete Item")
    ShowLocation
    log(f"Deleted (placeholder) {item_id}")
    PopLocation()

def Search():
    PushLocation("Search")
    while True:
        ShowLocation()
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
    PopLocation()

# this is kinda fucked rn but we ball
def SearchByName():
    PushLocation("Search by Name")
    ShowLocation()
    q = input("Name: ")
    log(f"Searching for '{q}' (placeholder)")
    PopLocation()

def SearchByPrice():
    PushLocation("Search by Price")
    ShowLocation()
    q = input("Price: ")
    log(f"Searching for '{q}' (placeholder)")
    PopLocation()

def SearchByQuantity():
    PushLocation("Search by Quantity")
    ShowLocation()
    q = input("Quantity: ")
    log(f"Searching for '{q}' (placeholder)")
    PopLocation()

if __name__ == "__main__":
    Main()
