# lib/helpers.py
from manager import Manager
from musician import Musician 

def format_manager(manager):
    return f"Manager: {manager.name}, Age: {manager.age} years old., ID: {manager.id}"


def format_musician(musician):
    return f"Musician: {musician.name}, Age: {musician.age}, Instrument: {musician.instrument}, Category: {musician.category}, Manager_id: {musician.manager_id}"

def view_all_managers():
    managers = Manager.get_all()
    if managers:
                for i, manager in enumerate(managers, start=1):
                    print(f"{i}. Manager: {manager.name}, Age: {manager.age} years old., ID: {manager.id}")
                
                action_choice = input("\nWould you like to delete, create, or update a manager? (y/n): ")
                
                if action_choice.lower() == 'y':
                    action = input("Choose action: (d) Delete, (c) Create, (u) Update: ").lower()

                    if action == 'd':
                        # Delete manager
                        manager_id_input = input("Please enter the ID of the manager you want to delete: ")

                        try:
                            manager_id_input = int(manager_id_input)
                            selected_manager = next((m for m in managers if m.id == manager_id_input), None)

                            if selected_manager:
                                selected_manager.delete()
                                print(f"Manager {selected_manager.name} has been deleted.")
                            else:
                                print("No manager found with that ID.")
                        except ValueError:
                            print("Invalid ID entered. Deletion canceled.")

                    elif action == 'c':
                        # Create new manager
                        print("\nYou chose to create a new manager.")
                        manager_name = input("Enter the new manager's name: ")

                        try:
                            manager_age = int(input("Enter the new manager's age: "))
                            new_manager = Manager.create(manager_name, manager_age)
                            print(f"New manager {manager_name} has been created successfully.")
                        except ValueError:
                            print("Invalid input! Please enter a valid integer for age.")
                        except Exception as e:
                            print(f"An error occurred while creating the manager: {e}")

                    elif action == 'u':
                        # Update manager
                        print(f"\nYou chose to update a manager.")
                        try:
                            manager_id_input = int(input("Enter the ID of the manager to update: "))

                            if selected_manager:
                                new_name = input(f"Enter new name for {manager.name} (leave blank to keep current): ")
                                if new_name:
                                    selected_manager.name = new_name

                                try:
                                    new_age = int(input(f"Enter new age for {manager.name}: "))
                                    manager.age = new_age
                                except ValueError:
                                    print("Invalid input for age. Age update skipped.")
                                manager.update()
                                print(f"Manager {manager.name} has been updated.")
                            else:
                                print("Manager not found.")
                        except ValueError:
                            print("Invalid ID entered.")
                    else:
                        print("Invalid option chosen. Returning to the menu.")
                
                # Now, we move on to view musicians
                manager_choice = input("\nChoose a manager by number to view their musicians (0 to go back): ")
                if manager_choice == '0':
                    continue   
                try:
                    manager_choice = int(manager_choice)
                    if 1 <= manager_choice <= len(managers):
                        selected_manager = managers[manager_choice - 1]
                        print(f"\nShowing musicians for {selected_manager.name}:")
                        musicians = Musician.view_by_manager_id(selected_manager.id)

                        if musicians:
                            for i, musician in enumerate(musicians, start=1):
                                print(f"{i}. {format_musician(musician)}")
                        else:
                            print(f"No musicians found for {selected_manager.name}.")
                    else:
                        print("Invalid manager number. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a valid manager number.")
            
                else:
                    print("No managers found.")