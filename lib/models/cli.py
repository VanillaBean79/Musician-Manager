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
            
            # action_choice == 'c':

            
            

        elif choice == '2':
            print("\nAll Managers")
            view_all_managers()
            
        elif choice == '0':
            return
        else:
            print("Invalid choice. Please try again.")




if __name__ == "__main__":
     
    cli()

  
