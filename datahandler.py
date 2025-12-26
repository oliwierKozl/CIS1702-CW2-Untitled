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

        return f"Added: Name={item_name}, Price={price}, Qty={quantity}"