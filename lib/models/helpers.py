# lib/helpers.py
from manager import Manager
from musician import Musician 
import sqlite3



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
        print(f"\n<Name: {manager.name} Age: {manager.age}>")  # Check manager.id
    else:
        print(f"Manager '{name}' not found.")

        
        


def find_manager_by_id():
    managers = Manager.get_all()
    print("Managers List:")
    for i, manager in enumerate(managers, start=1):
        print(f"{i}. Manager: {manager.name}.")
    while True:
        try:
            selected_index = int(input("Enter the number corresponding to the manager."))
            if 1 <= selected_index <= len(managers):
                selected_manager = managers[selected_index -1]
                print(f"Selected Manager: {selected_manager.name}.")
                break
            else:
                print("Manager not found with that ID.")
        except ValueError:
            print("Invalid input.")



    


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


def update_manager():
    name = input("Enter managers name:")
    if manager := Manager.find_by_name(name):
       new_name = input(f"Enter the manager's new name:")
       if new_name:
           manager.name = new_name
       new_age_input = input(f"Enter manager's new age:")
       if new_age_input:
           try:
               new_age = int(new_age_input)
               if 10 <= new_age <= 120:
                   manager.age = new_age
               else:
                   print("Please enter a valid number.")
                   return
           except ValueError:
               print("Age must be an integer.")
                
    manager.update()
    print(f"\n Success! {manager}\n")


def delete_manager():
    name = input("Enter the name of the manager.")
    manager = Manager.find_by_name(name)
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


def list_managers_musicians():
    name = input("Enter manager's name: ")
    if manager := Manager.find_by_name(name):
        for musician in manager.musicians():
            print(f"\n{musician}\n")
    else:
        print(f'\n{manager} not found\n')


def create_musician():
    name = input("Enter the new musician's name: ")
    age = input("Enter the musician's age:")

    try:
        age = int(age)
    except ValueError:
        print("Age must be an integer.")
        return
    instrument = input("Enter instrument:")
    category = input("Enter category:")
    manager_id = input("Enter manager ID:")
    
    new_musician = Musician.create(name, age, instrument, category, manager_id)
    print(f"Manager: {new_musician.name} (age: {new_musician.age}) instrument: {new_musician.instrument}, category: {new_musician.category}, manager_id: {new_musician.manager_id}) has been created successfully.")

def delete_musician():
    name = input("Enter musician's name: ")
    if musician := Musician.name(name):
        musician.delete()
        print(f'\nMusician {name} has been deleted\n')
    else:
        print(f'\nMusician {name} not found\n')


def update_musician():
    
    name = input("Enter musician's name: ")
    musician = Musician.name(name)  
    if musician is None:
        print(f"Musician with the name '{name}' not found.")
        return  
    

    new_name = input(f"Enter the musician's new name (or press Enter to keep the same): ")
    if new_name:
        musician.name = new_name
    
    
    new_age_input = input(f"Enter musician's new age (or press Enter to keep the same): ")
    if new_age_input:
        try:
            new_age = int(new_age_input)
            if 10 <= new_age <= 120:
                musician.age = new_age
            else:
                print("Please enter a valid age between 10 and 120.")
                return
        except ValueError:
            print("Age must be an integer.")
            return
    
    new_instrument = input(f"Enter the musician's new instrument (or press Enter to keep the same): ")
    if new_instrument:
        musician.instrument = new_instrument
    
    new_category = input(f"Enter the musician's new category (or press Enter to keep the same): ")
    if new_category:
        musician.category = new_category
    
    new_manager_id = input(f"Enter the musician's new manager ID (or press Enter to keep the same): ")
    if new_manager_id:
        try:
            new_manager_id = int(new_manager_id)  
            musician.manager_id = new_manager_id  
        except ValueError:
            print("Manager ID must be an integer.")
            return
    
    print("Musician details updated successfully.")
    musician.update() 





def get_all_musicians():
    musicians = Musician.get_all()
    if musicians:
        for i, musician in enumerate(musicians, start=1):
            if musician:  # Ensure musician is not None
                print(f"{i}. Musician: {musician.name}, Age: {musician.age} years old. "
                      f"Instrument: {musician.instrument}, category: {musician.category}, "
                      f"manager_id: {musician.manager_id}.")
            else:
                print(f"{i}. Musician data is incomplete or invalid.")
    else:
        print("No musicians found.")








# Test calls

# Testing view_all_managers
# print("Testing view_all_managers()...\n")
# view_all_managers()


# print("\nTesting find_manager_by_name()...\n")

# find_manager_by_name()

# # Testing create_manager
# print("\nTesting create_manager()...\n")
# create_manager()

# # Testing update_manager
# print("\nTesting update_manager()...\n")
# # Here, you would need to mock a manager object. Assuming a mock manager is used here.
# mock_manager = Manager.find_by_id(4)  # Assuming this returns a manager
# update_manager(mock_manager)

# Testing delete_manager
# print("\nTesting delete_manager()...\n")
# # Assuming mock manager
# delete_manager()

# Testing list_musicians
# print("\nTesting list_musicians()...\n")
# # Testing with manager ID 4
# list_musicians()

# find_manager_by_id()





                       