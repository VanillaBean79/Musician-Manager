# cli.py

from manager import create_manager, view_all_managers, find_manager_by_name, delete_manager
from musician import create_musician, view_all_musicians, view_musicians_by_manager, find_musician_by_name, delete_musician
from helpers import format_manager, format_musician


def create_tables():
    import sqlite3
    conn = sqlite3.connect('musicians.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS managers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS musicians (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            instrument TEXT NOT NULL,
            category TEXT NOT NULL,
            manager_id INTEGER,
            FOREIGN KEY(manager_id) REFERENCES managers(id)
        )
    """)
    conn.commit()
    conn.close()


def cli():
    while True:
        print("\n=== Musician Manager CLI ===")
        print("1. Manage Managers")
        print("2. Manage Musicians")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            manage_managers()

        elif choice == '2':
            manage_musicians()

        elif choice == '0':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")


def manage_managers():
    while True:
        print("\n=== Manage Managers ===")
        print("1. Create Manager")
        print("2. View All Managers")
        print("3. Find Manager by Name")
        print("4. Delete Manager")
        print("0. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter manager's name: ")
            age = int(input("Enter manager's age: "))
            create_manager(name, age)

        elif choice == '2':
            print("\n--- All Managers ---")
            managers = view_all_managers()
            if managers:
                for i, manager in enumerate(managers, start=1):
                    print(f"{i}. {format_manager(manager)}")
            else:
                print("No managers found.")

        elif choice == '3':
            name = input("Enter manager's name: ")
            manager = find_manager_by_name(name)
            if manager:
                print(format_manager(manager))
            else:
                print(f"Manager with name {name} not found.")

        elif choice == '4':
            name = input("Enter manager's name: ")
            delete_manager(name)

        elif choice == '0':
            break

        else:
            print("Invalid choice. Please try again.")


def manage_musicians():
    while True:
        print("\n=== Manage Musicians ===")
        print("1. Create Musician")
        print("2. View All Musicians")
        print("3. View Musicians by Manager")
        print("4. Find Musician by Name")
        print("5. Delete Musician")
        print("0. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == '1':
            create_musician_flow()

        elif choice == '2':
            print("\n--- All Musicians ---")
            musicians = view_all_musicians()
            if musicians:
                for i, musician in enumerate(musicians, start=1):
                    print(f"{i}. {format_musician(musician)}")
            else:
                print("No musicians found.")

        elif choice == '3':
            print("\n--- Available Managers ---")
            managers = view_all_managers()
            for i, manager in enumerate(managers, start=1):
                print(f"{i}. {format_manager(manager)}")
            manager_id = int(input("Enter manager's ID to view their musicians: "))
            musicians = view_musicians_by_manager(manager_id)
            if musicians:
                for i, musician in enumerate(musicians, start=1):
                    print(f"{i}. {format_musician(musician)}")
            else:
                print(f"No musicians found for Manager ID {manager_id}")

        elif choice == '4':
            name = input("Enter musician's name: ")
            musicians = find_musician_by_name(name)
            if musicians:
                for musician in musicians:
                    print(format_musician(musician))
            else:
                print(f"No musicians found with the name starting with {name}.")

        elif choice == '5':
            name = input("Enter musician's name: ")
            delete_musician(name)

        elif choice == '0':
            break

        else:
            print("Invalid choice. Please try again.")


def create_musician_flow():
    print("\n--- Available Managers ---")
    managers = view_all_managers()
    for i, manager in enumerate(managers, start=1):
        print(f"{i}. {format_manager(manager)}")
    manager_id = int(input("Enter the manager's ID for this musician: "))
    
    name = input("Enter musician's name: ")
    age = int(input("Enter musician's age: "))
    instrument = input("Enter musician's instrument: ")
    category = input("Enter musician's category: ")

    create_musician(name, age, instrument, category, manager_id)
    print(f"{name} has been added as a musician under manager ID {manager_id}.")


if __name__ == "__main__":
    create_tables()  
    cli()

  
