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

create_tables()
Manager.create_manager("Bob Loblaw", 55)

CONN.close()