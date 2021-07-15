import sqlite3
from contextlib import closing

USER_FAVORITES = 'USER_FAVORITES'
USERS = 'USERS'
FAVORITES = 'FAVORITES'


def add_favorite_to_list(user_id, list_id, tiktok_id):
    execute_query(generate_insert_query(
        FAVORITES, (user_id, list_id, tiktok_id)))


def add_user_to_users(user_id, email, first_name, last_name):
    execute_query(generate_insert_query(
        USERS, (user_id, None, email, first_name, last_name)))


def add_favorites_list(user_id, list_name):
    execute_query(generate_insert_query(
        USER_FAVORITES, (user_id, list_name)))


def get_user_favorites_list():
    pass


def execute_query(query):
    return execute_queries([query])


def execute_queries(queries):
    with closing(sqlite3.connect('tokifydb.db')) as connection:
        with connection:
            for query in queries:
                print(query)
                result = connection.execute(query)


def generate_create_query(name, fields):
    my_query = f"Create table {name} ("
    for i, item in enumerate(fields):
        new_phrase = (f"{item[0]} {item[1]}")
        if i != len(fields) - 1:
            new_phrase += ","
        my_query = my_query + new_phrase
    my_query = my_query + ")"
    return my_query


def generate_insert_query(table_name, values):
    return f"INSERT INTO {table_name} VALUES {values}"


def buildDataBase():
    tables = [
        (USER_FAVORITES, [
            ('user_id', 'INTEGER'),
            ('list_id', 'INTEGER'),
            ('list_name', 'STRING'),
        ]),
        (USERS, [
            ('user_id', 'INTEGER'),
            ('last_login', 'INTEGER'),
            ('email', 'STRING'),
            ('first_name', 'STRING'),
            ('last_name', 'STRING')
        ]),
        (FAVORITES, [
            ('user_id', 'INTEGER'),
            ('list_id',	'INTEGER'),
            ('tiktok_id', 'INTEGER')
        ])
    ]
    queries = []
    for table_name, table_fields in tables:
        table_create_query = generate_create_query(table_name, table_fields)
        queries.append(table_create_query)
    execute_queries(queries)


if __name__ == "__main__":
    buildDataBase()
