# lib/helpers.py
from manager import Manager
from musician import Musician 
import sqlite3

def exit_program():
    print("ADIOS!")
    exit()

def format_manager(manager):
    return f"Manager: {manager.name}, Age: {manager.age} years old."


def format_musician(musician):
    return f"Musician: {musician.name}, Age: {musician.age}, Instrument: {musician.instrument}, Category: {musician.category}, Manager_id: {musician.manager_id}"


def view_all_managers():
    managers = Manager.get_all()
    if managers:
        for i, manager in enumerate(managers, start=1):
            print(f"{i}. Manager: {manager.name}, Age: {manager.age} years old.")
                

def find_manager_by_name():
    name = input("Enter the manager's name: ")
    manager = Manager.find_by_name(name)
    
    if manager:
        print(f"\n<Name: {manager.name} Age: {manager.age}>")
        
        action_choice = input("See assigned musicians. (y/n): ")
        
        if action_choice.lower() == 'y':
            
            list_musicians(manager_id) 
    else:
        print(f"Manager '{name}' not found.")

    

def find_manager_by_id():
    managers = Manager.get_all()
    print("Managers List:")
    for i, manager in enumerate(managers, start=1):
        print(f"{i}. Manager: {manager.name}.")

    id_ = int(input("Enter the manager's ID:"))
    selected_manager = Manager.find_by_id(id_)
    if selected_manager:
        print(f"Selected Manager: {selected_manager.name}")
    else:
        print("Manager not found with that ID.")


def create_manager():
    name = input("Enter the new Manager's name: ")
    age = input("Enter the manager's age:")

    try:
        age = int(age)
    except ValueError:
        print("Age must be an integer.")
        return
    
    new_manager = Manager.create(name, age)
    print(f"Manager: {new_manager.name} (age: {new_manager.age}) has been created successfully.")


def update_manager(manager):
    try:
        name = input(f"Enter the manager's new name (current: {manager.name}): ")
        if name:
            manager.name = name  

        # Ask the user for a new age, and only update if the user provides a valid one
        age_input = input(f"Enter the manager's new age (current: {manager.age}): ")
        if age_input: 
            try:
                age = int(age_input)
                if age > 0 and age < 120:
                    manager.age = age
                else:
                    print("Please enter a valid age between 1 and 119.")
                    return  
            except ValueError:
                print("Please enter a valid integer for age.")
                return  # Exit the function if the age input is not an integer

        # After all inputs, save the updated manager object
        manager.save()
        print(f"Success: Manager {manager.name} updated.")
    except Exception as exc:
        print(f"Error updating manager: {exc}")




def delete_manager(manager):
    """Delete the selected manager."""
    if manager:
        print(f"You have selected to delete the following manager: {format_manager(manager)}")
        
        confirm = input(f"Are you sure you want to delete {manager.name}? (y/n): ").lower()
        
        if confirm == 'y':
            manager.delete()
            print(f"Manager {manager.name} has been deleted.")
        else:
            print("Deletion cancelled.")
    else:
        print("No manager selected for deletion.")




def list_musicians(manager_id):
    """Fetch and list musicians assigned to the specified manager."""

    musicians = Musician.view_by_manager_id(manager_id)  # Fetch musicians for the given manager_id
        
    if musicians:
            # Enumerate and list musicians
        for i, musician in enumerate(musicians, start=1):
            print(f"{i}. {musician.name}, {musician.instrument}, {musician.category}")
    else:
        print("No musicians found for this manager.")
       

        


manager_id = 1
# list_musicians(manager_id)
print(list_musicians(manager_id))    
        
           
                


        






                       