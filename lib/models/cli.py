# cli.py
# from models.__init__ import CURSOR, CONN
from manager import Manager
from musician import Musician
from helpers import (
    format_manager, 
    format_musician,
    view_all_managers,
    find_manager_by_name,
    delete_musician,
    update_musician,
    create_manager,
    update_manager,
    delete_manager,
    list_managers_musicians,
    get_all_musicians,
    create_musician)




def cli():
    while True:
        print("\n=== Musician Manager CLI ===")
        print("1. Managers")
        print("2. Musicians")
       
        choice = input("Choose an option: ")

        if choice == '1':
            managers()

        else:
            print("Invalid choice. Please try again.")

        if choice == '2':
            get_all_musicians()
            print("\nWhat would you like to do with a musicians?")
            print("1. Create a new musician")
            print("2. Delete an existing musician")
            print("3. Update an existing musician")
            print("0. Go Back")

            musician_action_choice = input("Choose an option:")

            if musician_action_choice == '1':
                create_musician()
            elif musician_action_choice == '2':
                delete_musician()
            elif musician_action_choice == '3':
                update_musician()

            



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
            
            print("\nWhat would you like to do?")
            print("1. View musicians assigned to this manager")
            print("0. Go Back")

            choice = input("Choose an option: ")

            if choice == '1':
                list_managers_musicians()
                print("\nWhat would you like to do with a musicians?")
                print("1. Create a new musician")
                print("2. Delete an existing musician")
                print("3. Update an existing musician")
                print("0. Go Back")

                musician_action_choice = input("Choose an option:")

                if musician_action_choice == '1':
                    create_musician()
                elif musician_action_choice == '2':
                    delete_musician()
                elif musician_action_choice == '3':
                    update_musician()
        
                        
            
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

  
