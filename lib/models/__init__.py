import sqlite3

CONN = sqlite3.connect('musicians.db')
CURSOR = CONN.cursor()
