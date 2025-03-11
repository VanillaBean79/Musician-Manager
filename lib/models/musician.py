import sqlite3

from __init__ import CURSOR, CONN
from manager import Manager


class Musician:
    all = {}
    
    def __init__(self, name, age, instrument, category, manager_id, id = None):
        self.id = id
        self.name = name
        self.age = age
        self.instrument = instrument
        self.category = category
        self.manager_id = manager_id

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
        if isinstance(age, int) and 10 <= age <=120:
            self._age = age
        else:
           raise ValueError(f"Age must be an integer between 10 and 120.")

    @property
    def instrument(self):
        return self._instrument 
    
    @instrument.setter
    def instrument(self, instrument):
        if isinstance(instrument, str) and len(instrument):
            self._instrument = instrument
        else:
            raise ValueError(f"Instrument must be a string.")

    @property
    def category(self):
        return self._category 
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category):
            self._category = category
        else:
            raise ValueError(f"Name of category must be a string.")

    @property
    def manager_id(self):
        return self._manager_id
    
    @manager_id.setter
    def manager_id(self, manager_id):
        if isinstance(manager_id, int) and 1 <= manager_id <= 500:
            self._manager_id = manager_id
        else:
            raise ValueError(f"Manager id must be an integer.")

    def __repr__(self):
        return f"<Name: {self.name} Instrument: {self.instrument} Age: {self.age} Category: {self.category} Manager ID: {self.manager_id}>"
    
    @classmethod
    def create_table(cls):
        """Create a new table to persist the 
        attributes of Musician instances"""
        sql = """
        CREATE TABLE IF NOT EXISTS musicians(
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        instrument TEXT,
        category TEXT,
        manager_id INTEGER,
        FOREIGN KEY (manager_id) REFERENCES
        managers(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the tabel that 
        persists Musician instances"""
        sql = """
        DROP TABLE IF EXISTS musicians;
        """
        CURSOR.execute(sql)
        CONN.commit()


    def save(self):
        """ Insert a new row with the name, instrument, category, and manager_id values of the current Musician object.
        Update object id attribute using the primary key value of the new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO musicians (name, age, instrument, category, manager_id)
                VALUES (?, ?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.age, self.instrument, self.category, self.manager_id))
        CONN.commit()

        self.id = CURSOR.lastrowid #This will set the musician id to the generated id in SQL.  
        
        type(self).all[self.id] = self  #Adds a new musician to the dictonary.

    def update(self):
        """Update the tabel row corresponding t the 
        current Musician instance"""
        sql = """
        UPDATE musicians
        SET name = ?, age = ?, instrument = ?, category = ?, manager_id = ?
        WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.age, self.instrument,
                             self.category, self.manager_id))
        CONN.commit()

    def delete(self):
        """Delete the table row
        corresponding to the musician instance."""
        sql = """
        DELETE FROM  musicians
        WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
    
        del type(self).all[self.id]
        self.id = None


    @classmethod
    def create(cls, name, age, instrument, category, manager_id):
        """Initialize new musician"""
        musician = cls(name, age, instrument, category, manager_id)
        musician.save()
        return musician 
    
    @classmethod
    def instance_from_db(cls, row):
        """Return a musician object having the attribute
        values from the table row."""
        
        # Check the dictionary for existing instance using the row's primary key (ID)
        musician = cls.all.get(row[0])
        
        if musician:
            # Ensure attributes match row values in case the local instance was modified.
            musician.name = row[1]
            musician.age = row[2]
            musician.instrument = row[3]
            musician.category = row[4]
            musician.manager_id = row[5]
        else:
            # Not in dictionary, create new instance and add to dictionary
            musician = cls(row[1], row[2], row[3], row[4], row[5])
            musician.id = row[0]
            cls.all[musician.id] = musician
        
        return musician

    @classmethod
    def get_all(cls):
        """ Fetch all musicians and their attributes from the database"""
        sql = """
            SELECT * FROM musicians
            """
        
        rows = CURSOR.execute(sql).fetchall()#Will return rows of elements inside parentheses. (TUPLES).
        
        return [cls.instance_from_db(row) for row in rows]
    

    @classmethod
    def view_by_id(cls, id):
        """Return Musician object corresponding
        to first table row matching specified primary key."""
        sql = """
            SELECT *
            FROM musicians
            WHERE id = ? 
            """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
        

    @classmethod
    def name(cls, name):
        """Return a musician object and it's row of attributes."""
        sql = """
            SELECT * FROM musicians
            WHERE name is ?
            """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def view_by_manager_id(cls, manager_id):
        """Return a list of musicians rows and attributes
        assigned to a manager"""
        sql = """
        SELECT * FROM musicians
        WHERE manager_id = ?
        """

        rows = CURSOR.execute(sql, (manager_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    

Musician.create_table()
