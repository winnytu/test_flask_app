import sqlite3
from db import db

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

# 建立table
create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

# 寫入資料
user = (1,'winny','asdf')
insert_query = "INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert_query,user)

users = [
    (2,'winny2','asdf'),
    (3,'winny3','asdf')
]
cursor.executemany(insert_query,users)

# 讀取資料
select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

# 

connection.commit()
connection.close()