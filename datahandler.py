# // Imports \\
import sys
import json

# // Functions \\ 

def add_item(itemName, price, quantity):
    with open("data.json", "r+") as file:
        file.seek(0)
        json_file = json.load(file)
        print(json_file)
