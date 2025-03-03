import sqlite3

def get_connection():
    return sqlite3.connect('musicians.db')

# Create manager
def create_manager(name, age):
    conn = get_connection()
    with conn:
        conn.execute("""
            INSERT INTO managers (name, age)
            VALUES (?, ?)
        """, (name, age))
    print(f"Manager {name} added successfully.")
    conn.close()  # Explicitly close the connection

# View all managers
def view_all_managers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM managers")
    rows = cursor.fetchall()
    conn.close()  # Close connection after the query
    return rows

# Find manager by name
def find_manager_by_name(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM managers WHERE name = ?", (name,))
    row = cursor.fetchone()
    conn.close()  # Close connection after the query
    return row

# Delete manager
def delete_manager(name):
    conn = get_connection()
    with conn:
        conn.execute("DELETE FROM managers WHERE name = ?", (name,))
    print(f"Manager {name} deleted.")
    conn.close()  # Close connection after the operation
