import sqlite3

from sqlite3 import Error as error

def create_database(database):
    try:
        database = sqlite3.connect(database)
        return database
    except error:
        print(error)

def create_table(database, sql):
    try:
        connection = database.cursor()
        connection.execute(sql)
        database.commit()
        return True
    except error:
        print(error)
    finally:
        connection.close()

def crud(database, sql, entities):
    try:
        connection = database.cursor()
        connection.execute(sql, entities)
        if str(sql).lower().find("select") == 0:
            rows = connection.fetchall()
            return rows
        return True;
    except error:
        print(error)
    finally:
        database.commit()
        connection.close()


