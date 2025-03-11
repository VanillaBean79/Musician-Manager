# lib/helpers.py


def format_manager(manager):
    return f"Manager: {manager.name}, Age: {manager.age} years old., ID: {manager.id}"


def format_musician(musician):
    return f"Musician: {musician.name}, Age: {musician.age}, Instrument: {musician.instrument}, Category: {musician.category}, Manager_id: {musician.manager_id}"
