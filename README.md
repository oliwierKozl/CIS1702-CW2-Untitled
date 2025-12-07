# CIS1702 - programming 1 - coursework 2

---

10/11/25 - 6/1/26

This is our group project for our 2025/26 programming 1 module coursework 2. 
Project brief:
"Create a command-line application to help a small business owner track product inventory. The system must allow the user to add, view, update, and remove stock items, and save the data between sessions"

Chosen project: command line inventory management system
Group name: untitled
Group members and roles:
- Oliver Kazlowski: backend/json schema
- Spencer Berry: testing 
- Michael Robertson: UX/frontend
- Luca Ponterosso: documentation

---

Core functionality goals:
- Store data in a file
- On startup, load data from file
- Present the user with a menu to perform:
    - Add a new item to the inventory
    - Update/delete an existing item from the inventory
    - Display all items and characteristics in a table
    - Search for items by name
- Graceful error handling

Potential extensions:
- Generate low stock report for items below a certain threshold
- Add functionality to track sales
- Improve search feature to search by other characteristics (price, stock, etc)

## Testing
Testing will be focused primariliy towards user testing and specifically how the system reacts to user inputs. Our testing plan contains all the testing that will conducted, the testing plan has outcomes the system should do. We document what the system did and specify whether or not the test has passed or failed. If it has failed, we need to address what may have failed. If it has passed after failing beforehand, we will address what has been changed/fixed and document those changes. 
