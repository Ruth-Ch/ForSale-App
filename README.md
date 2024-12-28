# ForSale-App
Author: Ruth Chane
Date: 12/20/2024
Introduction
This program is a console-based marketplace application. It allows users to:
* Post items for sale.
* Search for items by keyword or category.
* View available items.
* Purchase items.
The application demonstrates key concepts such as object-oriented programming, error handling, and modular design in Python.
How to Run the Program
1. System Requirements:
   * Python 3.x installed.
   * Required libraries: None beyond Python's standard library.
2. Running the Program:
   * Open a terminal or command prompt.
   * Navigate to the directory containing forsale.py.
Execute the program by typing:
Copy code
python forsale.py
   * How to Use the Program
1. Upon launching the program, you’ll see a menu with various options.
2. Choose an action by entering the corresponding number:
   * 1. Post an Item:
      * Add an item for sale by providing a name, description, price, and category.
   * 2. Search for Items:
      * Search items using a keyword or category.
   * 3. View All Items:
      * Display all available items in the marketplace.
   * 4. Purchase an Item:
      * Buy an item by selecting an item from the list.
   * 5. Exit the Program:
      * Quit the application.
3. Follow the prompts to complete your selected action.
________________


Known Issues and Bugs
* Input Validation:
   * While most invalid inputs are handled, some edge cases may cause unexpected behavior.
   * Example: Entering an empty string as input might result in an error message.
* Data Persistence:
   * The program does not save data between sessions. All items are cleared when the program exits.
________________


Future Enhancements
* Implement persistent data storage using JSON or a database to save marketplace data.
* Add a graphical user interface (GUI) for improved usability.
* Introduce a user authentication system to track user-specific posts and purchases.
________________


Additional Python Modules
No additional Python modules were required for this project.
