# // Imports \\
import sys
import json
import uuid

# // Functions \\ 

def add_item(itemName, price, quantity):
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
    with open("data.json", "r+") as file:
        json_file = json.load(file)

        # Check if passed in item exists
        if json_file[item]:
            # Check if passed in property exists
            if json_file[item][property]:
                json_file[json_file][property] = value # Update the value of the passed in property with value
            
            else:
                file.close()
                return "Property does not exist"
        else:
            file.close()
            return "Item does not exist"
        
        json.dump(json_file, file, indent=4) # Dump JSON, set indent to 4 for better looking JSON file