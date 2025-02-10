# Dictionary to store shopping list items
shopping_list = {}

def add_item():
    """Dynamically add an item to the shopping list"""
    item = input("Enter item name: ").strip()
    quantity = int(input("Enter quantity: ").strip())
    price = float(input("Enter price per item: ").strip())

    if item in shopping_list:
        shopping_list[item]['quantity'] += quantity
    else:
        shopping_list[item] = {'quantity': quantity, 'price': price}

    print(f"{quantity} of {item} at ${price} each has been added to your shopping list.")

def remove_item():
    """Dynamically remove an item from the shopping list"""
    item = input("Enter item name to remove: ").strip()
    if item in shopping_list:
        del shopping_list[item]
        print(f"{item} has been removed from your shopping list.")
    else:
        print(f"{item} is not in your shopping list.")

def display_list():
    """Display the current shopping list"""
    print("\nYour Shopping List:")
    if shopping_list:
        for item, details in shopping_list.items():
            total_price = details['quantity'] * details['price']
            print(f"{item}: {details['quantity']} @ ${details['price']} each = ${total_price:.2f}")
    else:
        print("Your shopping list is empty.")

def calculate_total():
    """Calculate the total cost of items in the shopping list"""
    total = sum(details['quantity'] * details['price'] for details in shopping_list.values())
    print(f"\nTotal cost: ${total:.2f}")

# Main loop to dynamically get user input
while True:
    action = input("\nChoose an action - Add (A), Remove (R), Display (D), Total (T), Quit (Q): ").strip().upper()

    if action == 'A':
        add_item()

    elif action == 'R':
        remove_item()

    elif action == 'D':
        display_list()

    elif action == 'T':
        calculate_total()

    elif action == 'Q':
        print("Exiting Shopping List Manager. Goodbye!")
        break

    else:
        print("Invalid choice, please try again.")
