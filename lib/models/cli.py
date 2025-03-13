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
        elif choice == '2':
            print("\nAll Managers")
            view_all_managers()
            # manage_selected_manager()
        elif choice == '0':
            return
        else:
            print("Invalid choice. Please try again.")


def view_all_managers():
    managers = Manager.get_all()  
    if managers:
        for i, manager in enumerate(managers, start=1):
            print(f"{i}. {format_manager(manager)}")
    else:
        print("No managers found.")
        
    action_choice = input("Choose a manager by number or type 'c' to create a manager or go back to menu 'b': ")
    
    if action_choice.lower() == 'c':
        create_manager()
    elif action_choice.lower == 'b':
        return
    else:
        try:
            manager_choice = int(action_choice)
            if 1 <= manager_choice <= len(managers):
                selected_manager = managers[manager_choice - 1]
                manage_selected_manager(selected_manager)
            else:
                print("Invalid manager number.")
        except ValueError:
            print("Invalid input.")

            



def manage_selected_manager(manager):
    print(f"\nYou are now managing <Name: {manager.name} Age: {manager.age}.")

    action = input("Would you like to Delete, Update, or Go Back to Manager menu or Go Home? (d/u/b/h): ").lower()

    if action == 'd':
        delete_manager(manager)  
    elif action == 'u':
        update_manager(manager)  
    elif action == 'b':
        print("Returning to the manager menu.")
    elif action == 'h':
        print("Returning to home page.")
        return "home"
    else:
        print("Invalid choice. Please choose 'd', 'u', or 'b'.")







if __name__ == "__main__":
     
    cli()

  
