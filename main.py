import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
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
    hashed_password=generate_password_hash(password, method='pbkdf2:sha256',salt_length=8)
    with db:
        cursor.execute("INSERT INTO users VALUES (?,?)",(login,hashed_password))

# insert_data("art",'admin')

def get_user_by_login(login):
    #return user or None
    user=cursor.execute("SELECT * FROM users WHERE login = ?",(login,)).fetchone()

    return user


