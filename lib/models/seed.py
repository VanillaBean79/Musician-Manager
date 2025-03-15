from __init__ import CONN, CURSOR
from musician import Musician 
from manager import Manager

def seed_database():
    manager = [
        ("Juan Doe", 30)
    ]

    for name, age in manager:
        Manager.create(name, age)

def seed_database():
    musician = [
        ("Rex Everything", 30, "Drums", "Rhythm Section", 1)
    ]

    for name, age, instrument, category, manager_id in musician:
        Musician.create(name, age, instrument, category, manager_id)


print("database seeded!")
seed_database()