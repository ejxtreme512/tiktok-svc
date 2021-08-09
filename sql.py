import sqlite3
from contextlib import closing

USER_FAVORITES = 'USER_FAVORITES'
USERS = 'USERS'
FAVORITES = 'FAVORITES'


def add_tiktok_to_favorites_list(user_id, list_id, tiktok_id):
    execute_query(generate_insert_query(
        FAVORITES, (user_id, list_id, tiktok_id)), {})


def add_user_to_users(email, first_name, last_name):
    execute_query(generate_insert_query(
        USERS, (email, first_name, last_name, None)))


def add_user_favorites_list(user_id, list_name):
    execute_query(generate_insert_query(
        USER_FAVORITES, (user_id, list_name)), {})


def get_favorite_items_by_list_id(id):
    query = '''
        SELECT UF.user_id, UF.list_id, UF.list_name, F.tiktok_id
        FROM 
            USER_FAVORITES AS UF,
            FAVORITES AS F
        WHERE UF.list_id = F.list_id
        AND F.list_id = :id
    '''
    parameters = {'id': id}
    return execute_query(query, parameters)


def get_favorites_list_by_user_id(user_id):
    query = '''
        SELECT * 
        FROM 
            USER_FAVORITES AS UF
        WHERE UF.user_id = :userId
    '''
    parameters = {'userId': user_id}
    return execute_query(query, parameters)


def execute_query(query, parameters):
    return execute_queries([[query, parameters]])[0]


def execute_queries(queries):
    results = []
    with closing(sqlite3.connect('tokifydb.db')) as connection:
        with connection:
            for query, parameters in queries:
                result = connection.execute(query, parameters)
                results.append(result.fetchall())
    return results


def generate_create_query(name, fields):
    my_query = f"Create table {name} ("
    for i, item in enumerate(fields):
        colName, colType, colConnection, foreignTable = item
        if colConnection == 'FOREIGN':
            new_phrase = (f"FOREIGN KEY({colName}) REFERENCES {foreignTable}({colType})")
        else:
            new_phrase = (f"{colName} {colType}")
        if i != len(fields) - 1:
            new_phrase += ","
        my_query = my_query + new_phrase
    my_query = my_query + ")"
    print(my_query)
    return my_query


def generate_insert_query(table_name, values):
    return f"INSERT INTO {table_name} VALUES {values}"


def buildDataBase():
    tables = [
        (USERS, [
            ('user_id', 'INTEGER PRIMARY KEY', None, None),
            ('last_login', 'INTEGER', None, None),
            ('email', 'STRING', None, None),
            ('first_name', 'STRING', None, None),
            ('last_name', 'STRING', None, None)
        ]),
        (USER_FAVORITES, [
            ('list_id', 'INTEGER PRIMARY KEY', None, None),
            ('user_id', 'INTEGER', 'FOREIGN', USERS),
            ('list_name', 'STRING', None, None),
        ]),
        (FAVORITES, [
            ('user_id', 'INTEGER', None, None),
            ('list_id',	'INTEGER', None, None),
            ('tiktok_id', 'INTEGER', None, None)
        ])
    ]
    queries = []
    for table_name, table_fields in tables:
        table_create_query = generate_create_query(table_name, table_fields)
        queries.append([table_create_query, {}])
    # execute_queries(queries)


if __name__ == "__main__":
    # add_user_favorites_list(2, 30, 'testABC')
    # add_tiktok_to_favorites_list(1,100, 3420)
    buildDataBase()
