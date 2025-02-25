import sqlite3

# Database connection and cursor
CONN = sqlite3.connect('musicians.db')
CURSOR = CONN.cursor()

# Create tables if they don't exist
def create_tables():
    with CONN:
        CONN.execute("""
            CREATE TABLE IF NOT EXISTS managers (
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     age INTEGER NOT NULL
                     )
                     """)
        
        CONN.execute("""
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

# Manager class
class Manager:
    all = {}  # Dictionary of manager data.

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Manager.all[name] = self

    def __repr__(self):
        return f"< {self.name}, {self.age} years old>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")
        
        # Create manager
def create_manager(name, age):
     with CONN:
        CONN.execute("""
         INSERT INTO managers (name, age)
             VALUES (?, ?)
        """, (name, age))

# Delete manager
def delete_manager(name):
    CURSOR.execute("DELETE FROM managers WHERE name = ?", (name,))
    CONN.commit()
    print(f"Manager {name} deleted.")

# Find manager by name
def find_manager_by_name(name):
    CURSOR.execute("SELECT * FROM managers WHERE name = ?", (name,))
    row = CURSOR.fetchone()
    if row:
        print(row)
    else:
        print(f"Manager with name {name} not found.")

# View all managers
def view_all_managers():
    CURSOR.execute("SELECT * FROM managers")
    rows = CURSOR.fetchall()
    for row in rows:
        print(row)

# Musician class
class Musicians:
    all_musicians = {}#Dictionary of musicians

    def __init__(self, name, age, instrument, category, manager_id):
        self.name = name
        self.age = age
        self.instrument = instrument
        self.category = category
        self.manager_id = manager_id
        Musicians.all_musicians[name] = self #adds the musician to the dictionary

    def __repr__(self):
        return f"< {self.name}, {self.age} years old, plays {self.instrument} in the {self.category}>"



# Create musician
def create_musician(name, age, instrument, category, manager_id):
    with CONN:
        CONN.execute("""
            INSERT INTO musicians (name, age, instrument, category, manager_id)
            VALUES (?, ?, ?, ?, ?)
        """, (name, age, instrument, category, manager_id))


# View all musicians
def view_all_musicians():
    CURSOR.execute("SELECT * FROM musicians")
    rows = CURSOR.fetchall()
    for row in rows:
        print(row)

# View musicians by manager ID
def view_musicians_by_manager(manager_id):
    CURSOR.execute("""
        SELECT * FROM musicians WHERE manager_id = ?
    """, (manager_id,))
    rows = CURSOR.fetchall()
    for row in rows:
        print(row)


# Find musician by name
def find_musician_by_name(name):
    CURSOR.execute("SELECT * FROM musicians WHERE name LIKE ?", (name + '%',))
    rows = CURSOR.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print(f"No Musician found with the name starting with {name}.")


# Delete musician
def delete_musician(name):
    CURSOR.execute("DELETE FROM musicians WHERE name = ?", (name,))
    CONN.commit()
    print(f"Musician {name} deleted.")

# CLI Menu
def cli():
    while True:
        print("\n=== Musician Manager CLI ===")
        print("1. Create Manager")
        print("2. Create Musician")
        print("3. View All Managers")
        print("4. View All Musicians")
        print("5. View Musicians by Manager")
        print("6. Find Manager by Name")
        print("7. Find Musician by Name")
        print("8. Delete Manager")
        print("9. Delete Musician")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter manager's name: ")
            age = int(input("Enter manager's age: "))
            create_manager(name, age)
        
        elif choice == '2':
            name = input("Enter musician name:")
            age = int(input("Enter musician age:"))
            instrument = input("Enter musician's instrument:")
            category = input("Enter musician's category:")
            manager_id = int(input("Enter the manager's id:"))
            print(f"Manager ID entered: {manager_id}") #Debugging print
            create_musician(name, age, instrument, category, manager_id)

        elif choice == '3':
            view_all_managers()

        elif choice == '4':
            view_all_musicians()

        elif choice == '5':
            manager_id = int(input("Enter manager's ID:"))
            view_musicians_by_manager()

        elif choice == '6':
            name = input("Enter manager's name:")
            find_manager_by_name(name)

        elif choice == '7':
            first_name = input("Enter musician's first name:")
            find_musician_by_name(first_name)

        elif choice == '8':
            name = input("Enter manager's name:")
            delete_manager(name)

        elif choice == '9':
            name = input("Enter musician's name:")
            delete_musician(name)

        elif choice == '0':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the CLI
if __name__ == "main":
    create_tables()
    cli()
    
#Close the database connection
CONN.close()