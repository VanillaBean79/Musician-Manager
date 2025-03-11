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

                
                action_choice = input("\nWould you like to delete, create, or move on to the next option? (D/C/0): ")

                if action_choice.lower() == 'D':
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

                elif action_choice.lower() == 'C':
                    
                    print("\nYou chose to create a new manager.")
                    manager_name = input("Enter the new manager's name: ")

                    
                    try:
                        manager_age = int(input("Enter the new manager's age: "))
                             
                    except ValueError:
                        print("Invalid input! Please enter a valid integer for age.")
                    
                    try:
                        
                        new_manager = Manager.create(manager_name, manager_age)
                        print(f"New manager {manager_name} has been created successfully.")
                    except Exception as e:
                        print(f"An error occurred while creating the manager: {e}")

                elif action_choice == '0':
                    print("Moving on to the next option.")
                    
                    continue  

                else:
                    print("Invalid choice. Please choose 'delete', 'create', or '0'.")
                
            else:
                print("No managers found.")

            
            
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
                
                
                create_musician_choice = input(f"Would you like to create a musician for {manager.name}? y/n: ")
                if create_musician_choice.lower() == 'y':
                    musician_name = input("Enter musician's name: ")
                    
                    
                    while True:
                        try:
                            musician_age = int(input("Enter musician's age: "))
                            break  
                        except ValueError:
                            print("Invalid input! Please enter a valid integer for age.")
                    
                    musician_instrument = input("Enter musician's instrument: ")
                    musician_category = input("Enter musician's category: ")
                    musician_manager_id = manager.id

                    try:
                        
                        new_musician = Musician.create(musician_name, musician_age, musician_instrument, musician_category, musician_manager_id)
                        print(f"Musician {musician_name} has been created and assigned to {manager.name}.")
                    except Exception as e:
                        print(f"An error occurred while creating musician: {e}")

                else:
                    print("Returning to manager menu.")
            else:
                print(f"Manager with name {name} not found.")
                create_choice = input(f"Do you want to create a manager named {name}? (y/n): ")

                if create_choice.lower() == 'y':
                    
                    age = input("Enter manager's age: ")

                    
                    try:
                        age = int(age)
                        new_manager = Manager.create(name, age)  
                        print(f"Manager {name} has been created and saved.")
                    except ValueError:
                        print("Invalid age. Please enter a valid number for the age.")
                else:
                    print("Manager creation canceled.")

        elif choice == '0':
            break
        else:
            print("Invalid option. Please try again.")




if __name__ == "__main__":
     
    cli()

  
