import sqlite3

CONN = sqlite3.connect('musicians.db')
CURSOR = CONN.cursor()

#Create the tables
def create_tables():
    with CONN:
        CONN.execute("""
            CREATE TABLE IF NOT EXIST managers (
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     age INTEGER NOT NULL )
                     """)
            
        CONN.execute("""
            CREATE TABLE IF NOT EXIST musicians (
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

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Manager.all[name] = self