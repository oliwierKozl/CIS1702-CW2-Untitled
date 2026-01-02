# // Imports \\
import sys
import json
import uuid

# // Functions \\ 

def add_item(itemName, price, quantity):
    # Input validation
    if type(price) != int or type(quantity) != int:

        try:
            price = int(price)
            quantity = int(quantity)
        except:
            return "Price and quantity must be integers"

    with open("data.json", "r+") as file:
        json_file = json.load(file) # Load json

        # Prevent duplicates
        if itemName in json_file:
            return "Item already exists"

        # New item
        new_item = {
            "item_id": str(uuid.uuid4())[:4],
            "quantity": quantity,
            "price": price,
        }
        
        json_file[itemName] = new_item # Add new item
        file.seek(0)
        json.dump(json_file, file, indent=4) # Dump JSON, set indent to 4 for better looking JSON file
        file.close() # Close

        return f"Added: Name={itemName}, Price={price}, Qty={quantity}"
    

def view_all():
    with open("data.json", "r") as file:
        json_file = json.load(file)
        
        item_list = {}
        for item in json_file:
            # Ensure item is not a test item, these are noted with "-" at the start
            if item[0] != "-":
                item_list[item] = json_file[item] # Add the non test items to the list for display

        file.close()        
        return item_list # Return a clean list with all items

def view_item(item_name):
    with open("data.json", "r") as file:
        json_file = json.load(file)
        
        # Check if item exists
        if json_file[item_name]:
            file.close()
            return json_file[item_name] # Return a list with the item's properties
        else:
            file.close()
            return "Item not found"
        

def update_item(item, property, value):
    # Input validation
    if type(value) != int:
        try:
            value = int(value)
        except:
            return "New value must be an integer"
        
    with open("data.json", "r+") as file:
        json_file = json.load(file)

        # Check if passed in item exists
        if json_file[item]:
            # Check if passed in property exists
            print(json_file[item][property])
            if json_file[item][property]:
                json_file[item][property] = value # Update the value of the passed in property with value
                print(json_file)
            else:
                file.close()
                return "Property does not exist"
        else:
            file.close()
            return "Item does not exist"
        with open('data.json', 'w') as file:

            # write updated data
            json.dump(json_file, file, indent=4) # Dump JSON, set indent to 4 for better looking JSON file
            file.close()
        return json_file[item]


def search_by_price(price):
    # Input validation
    if type(price) != int:

        try:
            price = int(price)
        except:
            return "Price must be an integer"
        
    with open("data.json", "r") as file:
        json_file = json.load(file)

        results = {} # Dict of all items with the price

        # Search items in the JSON dict
        for item, value in json_file.items():
            
            # Check for test items
            if item[0] == "-":
                continue
            else:
                if value["price"] == price:
                    results[item] = value # Enter the data into the results dict
                    continue
                else:
                    continue
        
        file.close()
        return results

def search_by_quantity(quantity):
    # Input validation
    if type(quantity) != int:

        try:
            quantity = int(quantity)
        except:
            return "Quantity must be an integer"
        
    with open("data.json", "r") as file:
        json_file = json.load(file)

        results = {} # Dict of all items with the price

        # Search items in the JSON dict
        for item, value in json_file.items():
            
            # Check for test items
            if item[0] == "-":
                continue
            else:
                if value["quantity"] == quantity:
                    results[item] = value # Enter the data into the results dict
                    continue
                else:
                    continue
        
        file.close()
        return results

def delete_item(deletedItem):
    with open("data.json", "r") as file:
        json_file = json.load(file)
        found = False

        # Search items in the JSON dict until it finds the item we want to delete
        while not found:
            for item, value in json_file.items():

                if item == deletedItem:
                    # Values to be returned into main
                    item_found = [item, value.get("item_id")]
                    #Stop while loop if found
                    found = True
                else:
                    pass
            print("item not found")
            break
        if found:
            del json_file[item]

        # Write the updated json to json file
        with open('data.json', 'w') as file:

            # write updated data
            json.dump(json_file, file, indent=4)
            file.close()
        return item_found


