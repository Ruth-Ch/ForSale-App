
class Item:
    """Represents an item for sale."""

    def __init__(self, name, description, price, seller_contact, category):
        """
        Initializes an Item instance w/h specific attributes.
        
        Parameters:
            name (str): The name of the item.
            description (str): A brief description of the item.
            price (str): The price of the item.
            seller_contact (str): Contact information for the seller.
            category (str): The category the item belongs to.
        """
        self.name = name
        self.description = description
        self.price = price
        self.seller_contact = seller_contact
        self.category = category
        self.is_available = True  # Indicates whether the item is available


    def mark_as_sold(self):
        """Marks the item as sold by setting its availability to False."""
        self.is_available = False

    def __str__(self):
        """
        Returns a formatted string representation of the item.
        
        Includes details such as name, description, price, seller contact, 
        category, and availability status.
        """
        status = "Available" if self.is_available else "Sold"
        return (
            f"{self.name} - {self.description} - ${self.price} - Contact: {self.seller_contact} "
            f"- Category: {self.category} ({status})"
        )


class Marketplace:
    """Represents the marketplace where items are listed."""
      #Provides methods to interact with the items.

    def __init__(self):
        """Initializes a Marketplace instance with an empty list of items."""
        self.items = []

    def add_item(self, item):
        """
        Adds a new item to the marketplace.
        
        Parameters:
            item (Item): An instance of the Item class.
        """
        self.items.append(item)

    def view_items(self):
        """Displays all items that are currently available for sale."""
        print("\nAvailable Items:")
        # Create a list of formatted strings for available items
        available_items = [
            f"{idx + 1}. {item}" for idx, item in enumerate(self.items) if item.is_available
        ]
        if available_items:
            print("\n".join(available_items))
        else:
            print("No items available.")  # Message if no items are available
        print()

    def view_items_by_category(self):
        """Displays items grouped by their categories."""
        categories = {}  # Dictionary to group items by category
        for item in self.items:
            if item.category not in categories:
                categories[item.category] = []
            categories[item.category].append(item)

        print("\nItems by Category:")
        if categories:
            # Loop through categories and display items under each category
            for category, items in categories.items():
                print(f"\nCategory: {category}")
                for item in items:
                    if item.is_available:
                        print(f"  - {item}")
        else:
            print("No items available.")  # Message if no items exist
        print()

    def search_items(self, keyword):
        """
        Searches for items by a keyword in their name or description.
        
        Parameters:
            keyword (str): The keyword to search for.
        """
        print(f"\nSearch Results for '{keyword}':")
        # Use list comprehension to find items containing the keyword
        results = [
            item for item in self.items
            if keyword.lower() in item.name.lower() or keyword.lower() in item.description.lower()
        ]
        if results:
            for item in results:
                print(item)
        else:
            print("No matching items found.")  # Message if no matches are found
        print()

    def purchase_item(self, item_index):
        """
        Marks an item as sold based on its index in the items list.
        
        Parameters:
            item_index (int): The index of the item in the items list.
        """
        try:
            item = self.items[item_index]
            if item.is_available:
                item.mark_as_sold()
                print(f"\nYou have purchased: {item.name}")
            else:
                print("\nThis item is already sold.")
        except IndexError:
            print("\nInvalid item number.")  # Handles invalid index
        except ValueError:
            print("\nInvalid input. Please enter a number.")  # Handles non-integer input


def display_menu():
    """Displays the main menu of the Forsale App."""
    print(
        """
Welcome to the Forsale App!
1. Post an Item
2. View Items
3. View Items by Category
4. Search for an Item
5. Purchase an Item
6. Exit
"""
    )


def main():
    """
    Main function to run the app.
    
    Handles user input and calls appropriate Marketplace methods
    based on the user's choice.
    """
    marketplace = Marketplace()  # Create an instance of Marketplace

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            # Collect item details from the user
            name = input("Enter the item name: ")
            description = input("Enter the item description: ")
            price = input("Enter the item price: ")
            seller_contact = input("Enter your contact information: ")
            category = input("Enter the item category: ")
            # Create a new Item instance and add it to the marketplace
            item = Item(name, description, price, seller_contact, category)
            marketplace.add_item(item)
            print("\nItem posted successfully!")

        elif choice == "2":
            # View all available items
            marketplace.view_items()

        elif choice == "3":
            # View items grouped by category
            marketplace.view_items_by_category()

        elif choice == "4":
            # Search for items by keyword
            keyword = input("Enter a keyword to search: ")
            marketplace.search_items(keyword)

        elif choice == "5":
            # Purchase an item
            marketplace.view_items()
            try:
                item_index = int(input("Enter the item number to purchase: ")) - 1
                marketplace.purchase_item(item_index)
            except ValueError:
                print("\nInvalid input. Please enter a number.")  # Handle invalid input

        elif choice == "6":
            # Exit the program
            print("\nThank you for using the Forsale App. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.")  # Handle invalid menu choice


if __name__ == "__main__":
    main()  # Entry point of the program
