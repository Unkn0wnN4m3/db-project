from mariadb import Cursor, Error


def create_tables(cursor: Cursor, tables: dict[str, str]):
    for table_name in tables:
        table_desc = tables[table_name]

        try:
            print("Creating table {}... ".format(table_name), end="")
            cursor.execute(table_desc)
        except Error as e:
            print(e.msg)
        else:
            print("OK")


def set_db(cursor: Cursor, dbname: str):
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS {};".format(dbname))
        print("Creando al base de datos... ")
    except Error as e:
        print(e)
    else:
        cursor.execute("USE {};".format(dbname))
        print("Listo! usando: {}".format(dbname))
