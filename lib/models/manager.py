import sqlite3

from __init__ import CURSOR, CONN


class Manager:
        
    all = {}

    def __init__(self, name, age, id=None):
        self.id = id
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Name: {self.name} Age: {self.age} ID: {self.id}>"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(f"Name must be a string.")

    @property
    def age(self):
        return self._age  
    
    @age.setter
    def age(self, age):
        if isinstance(age, int) and 10 <= age <= 120:
            self._age = age
        else:
            raise ValueError(f"Age must me an integer.")
        
    
    @classmethod
    def create_table(cls):
        """Create a new table to persist the attribute of Manager instances"""
    print("Creating managers table...")  # Debugging line
    sql = """
    CREATE TABLE IF NOT EXISTS managers (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER)
    """
    CURSOR.execute(sql)
    CONN.commit()
    print("Managers table created.")  # Debugging line


    @classmethod
    def drop_tables(cls):
       """Drop the table that persist
         Manager instance."""
       sql = """
        DROP TABLE IF EXISTS managers;
        """
       CURSOR.execute(sql)
       CONN.commit()

    def save(self):
        """Save the manager to the database."""
        if not self.name or not self.age:
            raise ValueError("Name and age must be provided and valid.")

        self.name = self.name  # This invokes the setter
        self.age = self.age  # This invokes the setter
    
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
    
    def update(self):
        """Update the table row corresponding to 
        the Manager instance.
        """
        sql = """
        UPDATE managers
        SET name = ?, age = ?
        WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.age))
        CONN.commit()

    def delete(self):
        """Delete table row corresponding to 
        the manager instance."""
        sql = """DELETE FROM managers 
        WHERE id = ?"""
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Remove the manager instance from the `all` dictionary
        del type(self).all[self.id]
        self.id = None

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
            manager = cls(row[1], row[2], id=row[0])  # Ensure the id is passed correctly
            cls.all[manager.id] = manager
        
        return manager

    @classmethod
    def get_all(cls):
        """Return a list of all managers."""
        sql = """SELECT * FROM managers"""
        rows = CURSOR.execute(sql).fetchall()
        
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Find and return the first manager matching the given name."""
        sql = """
            SELECT * FROM managers
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        if row:
            return cls.instance_from_db(row)
        return None
    
    @classmethod
    def find_by_name(cls, name):
        """Return a Manager object corresponding
        to the first table row matching specified name.
        """
        sql = """
        SELECT * FROM managers
        WHERE name is ? 
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def musicians(self):
        """Return list of musicians associated with 
        current manager"""
        from musician import Musician
        sql = """
        SELECT * FROM musicians
        WHERE manager_id = ? 
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Musician.instance_from_db(row) for row in rows
                ]


Manager.create_table()


