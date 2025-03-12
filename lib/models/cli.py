# cli.py

from manager import Manager
from musician import Musician
from helpers import format_manager, format_musician




def cli():
    while True:
        print("\n=== Musician Manager CLI ===")
        print("1. Managers")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            managers()

        elif choice == '0':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")


def managers():
    choice = ""
    while True:
        print("\n=== Manage Managers ===")
        print("1. View All Managers")
        print("2. Find Manager by Name")
        print("0. Go Back")

        choice = input("Choose an option: ")

        if choice == '1':
            print("\n--- All Managers ---")
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
                    continue  # Go back to the main menu

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

        elif choice == '2':
            name = input("Enter manager's name: ")
            manager = Manager.find_by_name(name)

            if manager:
                print(format_manager(manager))
                view_musicians_choice = input(f"Do you want to view musicians assigned to {manager.name}? y/n: ")

                if view_musicians_choice.lower() == 'y':
                    musicians = Musician.view_by_manager_id(manager.id)

                    if musicians:
                        print(f"\nMusicians assigned to {manager.name}:")
                        for i, musician in enumerate(musicians, start=1):
                            print(f"{i}. {format_musician(musician)}")
                    else:
                        print(f"No musicians found for {manager.name}.")
                
                
                action_choice = input(f"Would you like to delete, create or update a musician for {manager.name}? y/n: ")
                if action_choice.lower() == 'y':
                    action = input("Choose action: (d) Delete, (c) Create, (u) Update: ").lower()
                    
                    if action == 'd':
                        # Deleting musician logic
                        musicians = Musician.view_by_manager_id(manager.id)
                        if musicians:
                            for i, musician in enumerate(musicians, start=1):
                                print(f"{i}. Musician: {musician.name}, ID: {musician.id}")
                            musician_id_input = input("Enter the musicians ID to delete:")
                            try:
                                musician_id_input = int(musician_id_input)
                                musician = next((m for m in musicians if m.id == musician_id_input), None)

                                if musician:
                                    musician.delete()
                                    print(f"Selected {musician.name} was deleted.")
                                else:
                                    print("No musician found with that ID.")
                            except ValueError:
                                print("Invalid ID entered.")
                        else:
                            print("No musicians found for this manager.")

                    elif action == 'c':
                        # Creating musician logic
                        print("\nYou chose to create a new musician.")
                        musician_name = input("Enter new musician name: ")

                        try:
                            musician_age = int(input("Enter musician's age: "))
                        except ValueError:
                            print("Invalid input! Please enter a valid integer for age.")
                            return

                        musician_instrument = input("Enter musician's instrument: ")
                        musician_category = input("Enter musician's category: ")
                        musician_manager_id = manager.id

                        try:
                            new_musician = Musician.create(musician_name, musician_age, musician_instrument, musician_category, musician_manager_id)
                            print(f"New musician {new_musician.name} has been created and assigned to {manager.name}")
                        except Exception as e:
                            print(f"An error occurred while creating musician: {e}")

                    elif action == 'u':
                        # Updating musician logic
                        print("\nYou chose to update a musician.")
                        musician_id_input = input("Enter musician's ID you want to update: ")

                        try:
                            musician_id = int(musician_id_input)
                            musician = Musician.view_by_id(musician_id)  
                            if musician:
                                new_name = input(f"Enter new name for {musician.name} (leave blank to keep current): ")
                                if new_name:
                                    musician.name = new_name  

                                try:
                                    new_age = int(input(f"Enter new age for {musician.name}: "))
                                    musician.age = new_age  
                                except ValueError:
                                    print("Invalid input for age. Age update skipped.")
                                
                                musician.update()  
                                print(f"Musician {musician.name} has been updated.")

                            else:
                                print("No musician found with that ID.")

                        except ValueError:
                            print("Invalid ID entered. Please try again.")

                else:
                    print("Returning to the menu or skipping musician actions.")


                        


                

        elif choice == '0':
            break
        else:
            print("Invalid option. Please try again.")






if __name__ == "__main__":
     
    cli()

  
