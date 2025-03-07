import sqlite3

CONN = sqlite3.connect('musicians.db')
CURSOR = CONN.cursor()

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
            print(f"Name must be a string.")

    def __str__(self):
        return f"Musician {self.name}, {self.instrument}, {self.age} years old, Category: {self.category}, Manager ID: {self.manager_id}"



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
        print(f"Assigned ID: {self.id}")
        print(f"Musician added to dictionary: {self}")
        type(self).all[self.id] = self  #Adds a new musician to the dictonary.

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
    def view_by_manager_id(cls, manager_id):
        """View musicians who share the same manager."""
        sql = """
            SELECT id, name, age, instrument, category, manager_id
            FROM musicians
            WHERE manager_id = ? 
            """
        rows = CURSOR.execute(sql, (manager_id,)).fetchall()
        musicians = [cls.instance_from_db(row) for row in rows]
        return musicians


    @classmethod
    def name(cls, name):
        """Return a musician object and it's row of attributes."""
        sql = """
            SELECT * FROM musicians
            WHERE name is ?
            """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    

    
    def delete(self):
        """Delete musician from the database."""
        sql = """
        DELETE FROM  musicians
        WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
    
        del type(self).all[self.id]
        self.id = None


# CONN.close()