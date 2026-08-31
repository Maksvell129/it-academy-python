import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
""")
connection.commit()
connection.close()
