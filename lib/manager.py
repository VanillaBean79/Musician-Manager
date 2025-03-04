import sqlite3


def get_connection():
    return sqlite3.connect('musicians.db')

class Manager:

    def __init__(self, name, age, id=None):
        self.id = id
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Manager {self.name} is {self.age} years old and their id is {self.id}."

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            print(f"Name must be a string.")



def create_manager(name, age):
    
    conn = get_connection()
    with conn:
        conn.execute("""
            INSERT INTO managers (name, age)
            VALUES (?, ?)
        """, (name, age))
    print(f"Manager {name} added successfully.")
    conn.close() 


def view_all_managers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM managers")
    rows = cursor.fetchall()
    conn.close()  
    return rows


def find_manager_by_name(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM managers WHERE name = ?", (name,))
    row = cursor.fetchone()
    conn.close()  
    return row


def delete_manager(name):
    conn = get_connection()
    with conn:
        conn.execute("DELETE FROM managers WHERE name = ?", (name,))
    print(f"Manager {name} deleted.")
    conn.close()  


manager1 = Manager("Jill", 43, 7)
create_manager(manager1.name, manager1.age)
print(manager1)