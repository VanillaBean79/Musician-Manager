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
    @staticmethod
    def create_manager(name, age):
        with CONN:
            CONN.execute("""
            INSERT INTO managers (name, age)
                VALUES (?, ?)
            """, (name, age))
            print(f"Manager {name} created successfully.")

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
        
    


create_tables()
Manager.create_manager("Bob Loblaw", 55)

CONN.close()