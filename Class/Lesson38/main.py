import sqlite3
db=sqlite3.connect('user.db')
sql=db.cursor() #Добавить/редактировать
sql.execute(""" CREATE TABLE IF NOT EXISTS user(
    login TEXT,
    password TEXT,
    cash INT
)""")
db.commit()