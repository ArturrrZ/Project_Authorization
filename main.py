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

#-----------------------------------------FUNCTIONS------------------------------------------------
def insert_data(login,password):
    hashed_password=generate_password_hash(password, method='pbkdf2:sha256',salt_length=8)
    with db:
        cursor.execute("INSERT INTO users VALUES (?,?)",(login,hashed_password))

# insert_data("art",'admin')

def get_user_by_login(login):
    #return user or None
    user=cursor.execute("SELECT * FROM users WHERE login = ?",(login,)).fetchone()

    return user

def delete_user(login,password):
    with db:
        if get_user_by_login(login) is not None:
            if check_password_hash(get_user_by_login(login)[1],password):

                user=cursor.execute("DELETE from users WHERE login = :login", {'login':password})
                print("you deleted user")
            else:
                print("wrong password")
        else:
            print("not such user")

#-------------------------------------------FUNCTIONS----------------------------------------------

# def login_or_register():
print("Welcome!")
is_authorized=False
while not is_authorized:
    user=input("Write your login to register/login\n")
    if len(user.split()) == 1:
        existed_user=get_user_by_login(user)
        if existed_user:
            password=input("I found user with this login. Type your password to Log in\n")
            if len(password.split()) == 1:



                if check_password_hash(existed_user[1],password):
                    print("You've logged in!")
                    is_authorized = True
                else:
                    print("Wrong password")
            else:
                print("Wrong, password does not have spaces")
        #register
        else:
            print("There is not any user under this login.")
            new_password=input("Type your password to register\n")
            if len(new_password.split()) == 1:
                # hashed_new_password=generate_password_hash(new_password,method="pbkdf2:sha256",salt_length=8)
                insert_data(user,new_password)
                print("You successfully registered!")
                is_authorized=True
            else:
                print("Create password without spaces")



    else:
        print("Login without spaces")

print("----------------")
print("YOU AUTHORIZED!")
print("you can do smth here")

delete_user('kkk','kk')