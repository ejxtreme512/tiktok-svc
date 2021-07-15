import sqlite3
from sqlite3.dbapi2 import Connection


# create query will be the string passed into create table (ie:Create table users (user_id INTEGER,last_login INTEGER,) )
def create_table(create_query):
    print(f'my query is {create_query} ')
    connection = sqlite3.connect('tokifydb.db')
    c = connection.cursor()  # create a cursor
    # c.execute(create_query) #execute table
    connection.commit()  # Commit our command
    connection.close()


def create_query(name, fields):
    my_query = f'Create table {name} ('
    for item in fields:
        my_query = my_query + (f'{item[0]} {item[1]},')
    my_query = my_query + ")"
    return my_query

# def BuildDatabase():
#     my_tables = ['FAVORITES', 'USER FAVORITES', 'USERS']
#     my_queries = 
#     for table in my_tables:

def buildsum():
    my_var = [[1,2],[10,12],[15,20],[14,17][8,6]]
    # create a new list with the sum of each item in my_var
    for list in my_var:
        my_new_var = 

if __name__ == "__main__":
    my_user_name = 'USER_FAVORITES'
    my_user_fields = [
        ('user_id', 'INTEGER'),
        ('list id', 'INTEGER'),
        ('list name', 'STRING'),
    ]  
    # Create table users (user_id INTEGER,last_login INTEGER,)
    my_query = create_query(my_user_name, my_user_fields)
    create_table(my_query)

    my_query_name = 'USERS'
    my_query_fields = [
        ('user_id', 'INTEGER'),
        ('last_login', 'INTEGER'),
        ('email', 'STRING'),
        ('first_name', 'STRING'),
        ('last_name', 'STRING')
    ]
    my_user_query = create_query(my_query_name, my_query_fields)
    create_table(my_user_query)

    my_favorites_name = 'FAVORITES'
    my_favorites_fields = [
        ('user_id', 'INTEGER')
        ('list_id',	'INTEGER')
        ('video_id','INTEGER')
        ]
    my_favorite_query = create_query(my_favorites_name, my_favorites_fields)
    create_table(my_favorite_query)
