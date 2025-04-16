# Initialize an empty list to store the customer's order
order = []

# Define the menu items organized by categories
menu_categories = {
    1: {
        "name": "Fruits",
        "items": {
            1: {"Item name": "Apple", "Price": 0.49},
            2: {"Item name": "Banana", "Price": 0.59},
            3: {"Item name": "Orange", "Price": 0.69}
        }
    },
    2: {
        "name": "Beverages",
        "items": {
            1: {"Item name": "Tea - Thai iced", "Price": 3.99},
            2: {"Item name": "Coffee", "Price": 2.99},
            3: {"Item name": "Smoothie", "Price": 4.99}
        }
    },
    3: {
        "name": "Desserts",
        "items": {
            1: {"Item name": "Fried banana", "Price": 4.49},
            2: {"Item name": "Ice cream", "Price": 3.49},
            3: {"Item name": "Mango sticky rice", "Price": 5.49}
        }
    }
}

# Start the ordering process
place_order = True
while place_order:
    # Print the main menu (categories)
    print("\n===== MENU CATEGORIES =====")
    for key, category in menu_categories.items():
        print(f"{key}: {category['name']}")
    
    # Prompt the customer to enter their category selection
    category_selection = input("\nPlease enter the number of the category you would like to browse: ")
    
    # Check if the input is a number
    if not category_selection.isdigit():
        print("Invalid input. Please enter a number.")
        continue
    
    # Convert the input to an integer
    category_selection = int(category_selection)
    
    # Check if the input is in the keys of menu_categories
    if category_selection not in menu_categories.keys():
        print("Invalid selection. Please choose a number from the menu categories.")
        continue
    
    # Display the submenu for the selected category
    selected_category = menu_categories[category_selection]
    print(f"\n===== {selected_category['name']} =====")
    
    for key, item in selected_category['items'].items():
        print(f"{key}: {item['Item name']} - ${item['Price']:.2f}")
    
    # Prompt the customer to enter their item selection
    item_selection = input("\nPlease enter the number of the item you would like to order (or 0 to go back to categories): ")
    
    # Check if the customer wants to go back to the main menu
    if item_selection == "0":
        continue
    
    # Check if the input is a number
    if not item_selection.isdigit():
        print("Invalid input. Please enter a number.")
        continue
    
    # Convert the input to an integer
    item_selection = int(item_selection)
    
    # Check if the input is in the keys of the selected category's items
    if item_selection not in selected_category['items'].keys():
        print("Invalid selection. Please choose a number from the items list.")
        continue
    
    # Get the item name and price
    selected_item = selected_category['items'][item_selection]
    item_name = selected_item["Item name"]
    price = selected_item["Price"]
    
    # Ask the customer for the quantity
    quantity = input(f"How many {item_name}s would you like to order? (Quantity will default to 1 if input is invalid): ")
    
    # Check if the input is a number
    if not quantity.isdigit():
        quantity = 1
    else:
        # Convert the input to an integer
        quantity = int(quantity)
    
    # Append the order to the list
    order.append({"Item name": item_name, "Price": price, "Quantity": quantity})
    
    # Ask the customer if they would like to keep ordering
    while True:
        continue_ordering = input("Would you like to order another item? (y/n): ").lower()
        match continue_ordering:
            case 'y':
                break
            case 'n':
                place_order = False
                print("Thank you for your order.")
                break
            case _:
                print("Invalid input. Please enter 'y' or 'n'.")

# Print the receipt
print("\n" + "="*50)
print("                  RECEIPT                  ")
print("="*50)
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")
for item in order:
    item_name = item["Item name"]
    price = item["Price"]
    quantity = item["Quantity"]

    # Calculate the number of empty spaces
    item_name_spaces = " " * (25 - len(item_name))
    price_spaces = " " * (8 - len(f"${price:.2f}"))

    # Print the line for the receipt
    print(f"{item_name}{item_name_spaces}| ${price:.2f}{price_spaces}| {quantity}")

# Calculate the total price of the order
total_price = sum([item["Price"] * item["Quantity"] for item in order])
print("-"*50)
print(f"Total: ${total_price:.2f}")
print("="*50)
print("Thank you for your order! Please come again.")
