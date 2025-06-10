def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            # Add item functionality
            item = input("Enter the item to add: ").strip()
            if item:
                if item.lower() in [x.lower() for x in shopping_list]:
                    print(f"'{item}' is already in the list!")
                else:
                    shopping_list.append(item)
                    print(f"'{item}' has been added to your shopping list.")
            else:
                print("Item name cannot be empty!")
                
        elif choice == '2':
            # Remove item functionality
            if not shopping_list:
                print("Your shopping list is empty!")
                continue
                
            item = input("Enter the item to remove: ").strip()
            found_items = [x for x in shopping_list if x.lower() == item.lower()]
            
            if not found_items:
                print(f"'{item}' was not found in your shopping list.")
            elif len(found_items) == 1:
                shopping_list.remove(found_items[0])
                print(f"'{found_items[0]}' has been removed from your list.")
            else:
                print(f"Multiple items found matching '{item}':")
                for i, match in enumerate(found_items, 1):
                    print(f"{i}. {match}")
                selection = input("Enter the number of the item to remove: ")
                try:
                    index = int(selection) - 1
                    if 0 <= index < len(found_items):
                        shopping_list.remove(found_items[index])
                        print(f"'{found_items[index]}' has been removed.")
                    else:
                        print("Invalid selection number.")
                except ValueError:
                    print("Please enter a valid number.")
                    
        elif choice == '3':
            # View list functionality
            if not shopping_list:
                print("Your shopping list is empty!")
            else:
                print("\nYour Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                print(f"\nTotal items: {len(shopping_list)}")
                
        elif choice == '4':
            # Exit program
            print("Goodbye! Your shopping list has been saved.")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
