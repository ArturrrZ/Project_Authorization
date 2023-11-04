import sqlite3

db=sqlite3.connect("users.db")

cursor=db.cursor()
#create table
cursor.execute("""
        CREATE TABLE users (
            login TEXT PRIMARY KEY,
            password TEXT
        )
""")
