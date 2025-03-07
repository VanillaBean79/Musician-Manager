import sqlite3

CONN = sqlite3.connect("musicians.db")
CURSOR = CONN.cursor()

class Manager:
    all = {}

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

    def save(self):
        """Save the manager to the database."""
        sql = """
            INSERT INTO managers (name, age)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.age))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, age):
        """Create and save a new manager to the database."""
        manager = cls(name, age)
        manager.save()
        return manager

    @classmethod
    def instance_from_db(cls, row):
        """Return a Manager object from a database row."""
        # Check if an instance with the same id already exists
        manager = cls.all.get(row[0])
        
        if manager:
            # If instance exists, just update its attributes if needed
            manager.name = row[1]
            manager.age = row[2]
        else:
            # If instance doesn't exist, create a new one
            manager = cls(row[1], row[2])
            manager.id = row[0]
            cls.all[manager.id] = manager
        
        return manager

    @classmethod
    def get_all(cls):
        """Return a list of all managers."""
        sql = "SELECT * FROM managers"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_name(cls, name):
        """Find and return the first manager matching the given name."""
        sql = """
            SELECT * FROM managers
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        if row:
            return cls.instance_from_db(row)
        return None

    def delete(self):
        """Delete the manager from the database."""
        sql = "DELETE FROM managers WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Remove the manager instance from the `all` dictionary
        del type(self).all[self.id]
        self.id = None



# CONN.close()
