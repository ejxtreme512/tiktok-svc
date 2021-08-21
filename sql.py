import sqlite3
from contextlib import closing

USER_FAVORITES = 'USER_FAVORITES'
USERS = 'USERS'
FAVORITES = 'FAVORITES'


def add_tiktok_to_favorites_list(tiktok_id, user_id, list_id):
    execute_query(generate_insert_query(
        FAVORITES, (tiktok_id, user_id, list_id)), {})


def add_user_to_users(email, last_name, first_name, last_login):
    execute_query(generate_insert_query(
        USERS, (email, last_name, first_name, last_login), ("email", "last_name", "first_name", "last_login")), {})


def add_user_favorites_list(user_id, list_name):
    execute_query(generate_insert_query(
        USER_FAVORITES, (user_id, list_name), ("user_id", "list_name")), {})


def buildDataBase():
    tables = [
        (USERS, [
            ('user_id', 'INTEGER PRIMARY KEY', None, None),
            ('email', 'STRING', None, None),
            ('last_name', 'STRING', None, None),
            ('first_name', 'STRING', None, None),
            ('last_login', 'INTEGER', None, None),
        ]),
        (USER_FAVORITES, [
            ('list_id', 'INTEGER PRIMARY KEY', None, None),
            ('list_name', 'STRING', None, None),
            ('user_id', 'INTEGER', 'FOREIGN', USERS),
        ]),
        (FAVORITES, [
            ('tiktok_id', 'INTEGER', None, None),
            ('list_id',	'INTEGER', 'FOREIGN', USER_FAVORITES),
            ('user_id', 'INTEGER', 'FOREIGN', USERS),
        ])
    ]
    queries = []
    for table_name, table_fields in tables:
        table_create_query = generate_create_query(table_name, table_fields)
        queries.append([table_create_query, {}])
    execute_queries(queries)


def execute_query(query, parameters):
    return execute_queries([[query, parameters]])[0]


def execute_queries(queries):
    results = []
    with closing(sqlite3.connect('tokifydb.db')) as connection:
        with connection:
            connection.execute("PRAGMA foreign_keys = 1")
            for query, parameters in queries:
                result = connection.execute(query, parameters)
                results.append(result.fetchall())
    return results


def generate_create_query(name, fields):
    foreigns = []
    my_query = f'Create table "{name}" ('
    for i, item in enumerate(fields):
        colName, colType, colConnection, foreignTable = item
        new_phrase = (f'"{colName}" {colType}')
        if colConnection == 'FOREIGN':
            foreigns.append(
                f'FOREIGN KEY("{colName}") REFERENCES "{foreignTable}"("{colName}")')
        if i != len(fields) - 1:
            new_phrase += ","
        my_query = my_query + new_phrase
    if foreigns:
        my_query = my_query + ',' + ','.join(foreigns)
    my_query += ")"
    return my_query


def generate_insert_query(table_name, values, columns=None):
    insert = f"INSERT INTO {table_name}"
    if columns:
        insert += f"({','.join(columns)})"
    return insert + f" VALUES {values}"


def generate_update_query(table_name, values, condition):
    update_statement = f"UPDATE {table_name} "
    set_statement = ','.join([f"{col} = '{val}' " for col, val in values])
    update_statement += f"SET {set_statement}"
    update_statement += f"WHERE {condition}"
    return update_statement


def get_favorite_list_items_by_list_id(id):
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


def update_list_name_by_list_id(list_id, list_name):
    values = [("list_name", list_name)]
    return generate_update_query(FAVORITES, values, f"list_id = {list_id}")

# if __name__ == "__main__":
#     update = generate_update_query(USER_FAVORITES, [('list_name', 'abc123')], 'LIST_ID = 2')
#     print(update)
