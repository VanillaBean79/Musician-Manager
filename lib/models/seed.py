from __init__ import CONN, CURSOR
from musician import Musician 
from manager import Manager

def seed_database():
    manager = [
        ("Juan Doe", 30)
    ]

    for name, age in manager:
        Manager.create(name, age)


print("database seeded!")
seed_database()