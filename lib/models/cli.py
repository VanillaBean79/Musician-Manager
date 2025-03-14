# cli.py

from manager import Manager
from musician import Musician
from helpers import (
    format_manager, 
    format_musician,
    view_all_managers,
    find_manager_by_name,
    find_manager_by_id,
    create_manager,
    update_manager,
    delete_manager,
    list_musicians)




def cli():
    while True:
        print("\n=== Musician Manager CLI ===")
        print("1. Managers")
       
        choice = input("Choose an option: ")

        if choice == '1':
            managers()

        else:
            print("Invalid choice. Please try again.")


def managers():
    while True:
        print("\n=== Manage Managers ===")
        print("1. Manager by Name")
        print("2. View All Managers")
        print("0. Go Back")

        choice = input("Choose an option: ")

        if choice == '1':
            print("\n--- Manager ---")
            find_manager_by_name()
            
            # After displaying manager details, ask for further action
            print("\nWhat would you like to do?")
            print("1. View musicians assigned to this manager")
            print("0. Go Back")

            choice = input("Choose an option: ")

            if choice == '1':
                manager_name = input("Enter the manager's name to view musicians: ")
                manager = Manager.find_by_name(manager_name)
                if manager:
                    list_musicians(manager.id)  # Pass manager.id to the list_musicians function
                else:
                    print(f"Manager {manager_name} not found.")

            elif choice == '0':
                break

        elif choice == '2':
            print("\nAll Managers")
            view_all_managers()
            print("\nWhat would you like to do with a manager?")
            print("1. Create a new manager")
            print("2. Delete an existing manager")
            print("3. Update an existing manager")
            print("0. Go Back")
            
            manager_action_choice = input("Choose an option:")

            if manager_action_choice == '1':
                create_manager()
            elif manager_action_choice == '2':
                delete_manager()
            elif manager_action_choice == '3':
                update_manager()



if __name__ == "__main__":
     
    cli()

  
