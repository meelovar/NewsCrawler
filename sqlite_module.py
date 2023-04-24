import json
import sqlite3

DEFAULT_DB_NAME = "profile.sqlite3"


def init_database(path):
    with sqlite3.connect(path) as connection:
        create_table(connection)

        if len(get_profiles(connection)) == 0:
            populate_table(connection)


def create_table(connection):
    sql_query = (
        "create table if not exists cookie_profile ("
        "   id integer primary key autoincrement,"
        "   creation_time datetime not null,"
        "   cookie text,"
        "   last_execution_time datetime,"
        "   execution_count integer"
        ")"
    )
    cursor = connection.cursor()

    cursor.execute(sql_query)


def populate_table(connection, rows_count=15):
    sql_query = "insert into cookie_profile (creation_time) values (current_timestamp)"
    cursor = connection.cursor()

    for _ in range(rows_count):
        cursor.execute(sql_query)


def update_cookies(connection, profile_id, cookies):
    sql_query = (
        "update cookie_profile"
        "   set cookie = (?),"
        "       last_execution_time = current_timestamp,"
        "       execution_count = coalesce(execution_count, 0) + 1"
        "   where id = (?)"
    )
    cursor = connection.cursor()

    cursor.execute(sql_query, (cookies, profile_id))


def get_profiles(connection):
    sql_query = "select id, cookie from cookie_profile"
    cursor = connection.cursor()
    result = []

    for row in cursor.execute(sql_query):
        profile = {
            "id": row[0],
            "cookie": json.loads(row[1]) if row[1] else [],
        }

        result.append(profile)

    return result
