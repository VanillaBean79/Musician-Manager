#!/usr/bin/env python3
# lib/debug.py

# from models.__init__ import CONN, CURSOR
from models.musician import Musician 
from models.manager import Manager

def reset_database():
    """
    Function to reset the database by dropping and creating database.
    This will reset the state of the tables."""

    print("Dropping musicians table.")
    Musician.drop_table()

    # breakpoint()
    print("Creating musicians table.")
    Musician.create_table()

    print("Dropping managers table.")
    Manager.drop_table()
    print("Creating manager table.")
    Manager.create_table()

    print("Database reset complete")
    
# reset_database()

breakpoint()
