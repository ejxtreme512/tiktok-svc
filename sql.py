import sqlite3
from contextlib import closing


def execute_queries(queries):
    with closing(sqlite3.connect('tokifydb.db')) as connection:
        with connection:
            for query in queries:
                print(query)
                result = connection.execute(query)


def create_query(name, fields):
    my_query = f"Create table {name} ("
    for i, item in enumerate(fields):
        new_phrase = (f"{item[0]} {item[1]}")
        if i != len(fields) - 1:
            new_phrase += ","
        my_query = my_query + new_phrase
    my_query = my_query + ")"
    return my_query

def buildDataBase():
    tables = [
        ('USER_FAVORITES', [
            ('user_id', 'INTEGER'),
            ('list_id', 'INTEGER'),
            ('list_name', 'STRING'),
        ]),
        ('USERS', [
            ('user_id', 'INTEGER'),
            ('last_login', 'INTEGER'),
            ('email', 'STRING'),
            ('first_name', 'STRING'),
            ('last_name', 'STRING')
        ]),
        ('FAVORITES', [
            ('user_id', 'INTEGER'),
            ('list_id',	'INTEGER'),
            ('video_id', 'INTEGER')
        ])
    ]
    queries = []
    for table_name, table_fields in tables:
        table_create_query = create_query(table_name, table_fields)
        queries.append(table_create_query)
    execute_queries(queries)

if __name__ == "__main__":
    buildDataBase()