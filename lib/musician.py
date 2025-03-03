import sqlite3

def get_connection():
    return sqlite3.connect('musicians.db')


def create_musician(name, age, instrument, category, manager_id):
    conn = get_connection()
    with conn:
        conn.execute("""
            INSERT INTO musicians (name, age, instrument, category, manager_id)
            VALUES (?, ?, ?, ?, ?)
        """, (name, age, instrument, category, manager_id))
    print(f"Musician {name} added successfully.")
    conn.close()  


def view_all_musicians():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM musicians")
    rows = cursor.fetchall()
    conn.close()  
    return rows


def view_musicians_by_manager(manager_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM musicians WHERE manager_id = ?", (manager_id,))
    rows = cursor.fetchall()
    conn.close()  
    return rows


def find_musician_by_name(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM musicians WHERE name LIKE ?", (name + '%',))
    rows = cursor.fetchall()
    conn.close()  
    return rows

# Delete musician
def delete_musician(name):
    conn = get_connection()
    with conn:
        conn.execute("DELETE FROM musicians WHERE name = ?", (name,))
    print(f"Musician {name} deleted.")
    conn.close()  
