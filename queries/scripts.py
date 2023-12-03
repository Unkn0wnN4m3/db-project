from mariadb import Cursor, Error
from queries.registration import add_reg_statement, add_records


def set_db(cursor: Cursor, dbname: str) -> None:
    try:
        print("Creando al base de datos... ")
        cursor.execute("CREATE DATABASE IF NOT EXISTS {};".format(dbname))
    except Error as e:
        print(e)
    else:
        cursor.execute("USE {};".format(dbname))
        print("Listo! usando: {}".format(dbname))


def create_tables(cursor: Cursor, tables: dict[str, str]) -> None:
    for table_name in tables:
        table_desc = tables[table_name]

        try:
            print("Creando la tabla {}... ".format(table_name), end="")
            cursor.execute(table_desc)
        except Error as e:
            print(e.msg)
        else:
            print("OK")


def add_to_db(cursor: Cursor, table_name) -> None:
    for table_name in add_reg_statement:
        statement = "INSERT INTO {} VALUES {}".format(
            table_name, add_reg_statement[table_name]
        )

        data = add_records[table_name]

        try:
            print("Agregando datos a {}... ".format(table_name), end="")
            cursor.executemany(statement, data)
            print(statement, data)
        except Error as e:
            print(e)
        else:
            print("OK")
