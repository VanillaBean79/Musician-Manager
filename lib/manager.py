import sqlite3

def get_connection():
    return sqlite3.connect('musicians.db')


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
