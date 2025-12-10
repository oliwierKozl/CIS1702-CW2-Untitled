
# // Imports \\
import sys
import json

# // Functions \\ 

# Adds item into the data.json file
def AddItem(itemName, price, quantity):
    # Open file
    with open("data.json", "r+") as file:
        file.seek(0)
        jsonFile = json.load(file)
        print(jsonFile)