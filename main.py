import sqlite3

db=sqlite3.connect("users.db")

cursor=db.cursor()
#create table
# cursor.execute("""
#         CREATE TABLE users (
#             login TEXT PRIMARY KEY,
#             password TEXT
#         )
# """)


def insert_data(login,password):
    with db:
        cursor.execute("INSERT INTO users VALUES (?,?)",(login,password))


insert_data('admin','admin')