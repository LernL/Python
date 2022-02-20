import sqlite3
from random import randint
db=sqlite3.connect('user.db')
sql=db.cursor() #Добавить/редактировать
sql.execute(""" CREATE TABLE IF NOT EXISTS user(
    login TEXT,
    password TEXT,
    cash INT
)""")
db.commit()
def reg():
    user_login = input("Enter login:")
    user_password = input('Enter password:')
    sql.execute(f"""SELECT login FROM user WHERE login='{user_login}'""")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO user VALUES(?,?,?)", (user_login, user_password, 0))
        print("Registered")
        db.commit()
    else:
        print("You are already register")
        for i in sql.execute("SELECT * FROM user"):
            print(i)
def casino():
    user_login=input("Log in:")
    number=randint(1,2)
    sql.execute(f"SELECT login FROM user WHERE login='{user_login}'")
    if sql.fetchone() is None:
        print("You don't registered")
        reg()
    else:
        if number==1:
            print("You win")
            sql.execute(f"UPDATE user SET cash={1000} WHERE login='{user_login}'")
            db.commit()
        else:
            print("You lose")
def enter():
    for i in sql.execute("SELECT login,cash FROM user"):
        print(i)
def start():
    casino()
    enter()
start()