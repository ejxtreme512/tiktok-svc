import sqlite3
from sqlite3.dbapi2 import Connection

connection = sqlite3.connect('tokifydb.db')

#Create a cursor
c = connection.cursor()

#Create a table
c.execute("""CREATE TABLE users (
    user_id INTEGER,
    last_login INTEGER,
    email TEXT,
    first_name TEXT,
    last_name TEXT
)""")

#Commit our command
connection.commit()

connection.close()