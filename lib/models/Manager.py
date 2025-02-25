import sqlite3

CONN = sqlite3.connect('musicians.db')
CURSOR = CONN.cursor()

#Create the tables
def create_tables():
    with CONN:
        CONN.execute("""
            CREATE TABLE IF NOT EXISTS managers (
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     age INTEGER NOT NULL )
                     """)
            
        CONN.execute("""
            CREATE TABLE IF NOT EXISTS musicians (
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     age INTEGER NOT NULL,
                     instrument TEXT NOT NULL,
                     category TEXT NOT NULL,
                     manager_id INTEGER,
                     FOREIGN KEY(manager_id) REFERENCES manager(id)
                     )
                     """)

class Manager:
    all = {} # A dictionary of manager data

    #Create Manager
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Manager.all[name] = self

    def __repr__(self):
        return f"<The manager is {self.name} and is {self.age} years young.>"
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a string.")
        
    def create_manager(name, age):
        with CONN:
            CONN.execute("""
            INSERT INTO managers (name, age)
                VALUES (?, ?)
            """, (name, age))
            print(f"Manager {name} created successfully.")

    def delete_manager(name):
        CURSOR.execute("DELETE FROM manager WHERE name = ?", (name))
        CONN.commit()
        print(f"Manager {name} deleted.") #Bug catcher

    def find_manager_by_name(name):
        CURSOR.execute("SELECT * FROM manager WHERE name = ?", (name))
        row = CURSOR.fetchone()
        if row:
            print(row)
        else:
            print(f"Manager with name {name} not found.")

    def view_all_managers():
        CURSOR.execute("SELECT * FROM manager")
        rows = CURSOR.fetchall()
        for row in rows:
            print(row)

class Musicians:
    all = {} #Dictionary of musician names stored in memory NOT in database.

    def __init__(self, name, age, instrument, category, manager_id):
        self.name = name
        self.age = age
        self.instrument = instrument
        self.category = category
        self.manager_id = manager_id
        Musicians.all[name] = self

    def __repr__(self):
        return f"< {self.name}, is {self.age} years young., They play {self.instrument}, in the {self.category} section."
    
    def create_musician(name, age, instrument, category, manager_id):
        with CONN:
            CONN.execute("""
                INSERT INTO musicians (name, age, instrument, category, manager_id)
                         VALUES (?, ?, ?, ?, ?)""", (name, age, instrument, category, manager_id))
            
    def view_all_musicians():
        CURSOR.execute("SELECT * FROM musicians")
        rows = CURSOR.fetchall()
        for row in rows:
            print(row)

    def view_musicians_by_manager(manager_id):
        CURSOR.execute("""SELECET * FROM musicians WHERE manager id = ?
                       """, (manager_id))
        rows = CURSOR.fetchall()
        for row in rows:
            print(row)

    def find_musicians_by_name(name):
        CURSOR.execute("""SELECT * FROM musicians WHERE musician name LIKE ?""",
                       (name + '%'))
        rows = CURSOR.fetchall()
        if rows:
            for row in rows:
                print(row)
            else:
                print(f"No musician found with that name.")

    def delete_musician(name):
        CURSOR.execute("""DELET FROM musicians WHERE name = ? """,
                       (name))
        CONN.commit()
        print(f"Musician {name} deleted.")


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

        choice = input("Choose an option:")

        
    

create_tables()
Manager.create_manager("Bob Loblaw", 55)

CONN.close()