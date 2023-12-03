import os
import sys

import mariadb

from queries.tables import tables
from queries.registration import add_reg_statement
from queries.scripts import set_db, create_tables, add_to_db


if __name__ == "__main__":
    try:
        conn = mariadb.connect(
            # NOTE: configurar contrasena y usuario a traves de:
            # export username="username"
            # export password="password"
            user=os.environ.get("username"),
            password=os.environ.get("password"),
            host="127.0.0.1",
            port=3306,
            autocommit=True,
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    cur = conn.cursor()

    # Creacion de la db
    print("*** DB init ***\n")
    set_db(cur, "proyectofinal")

    # Cracion de las tablas
    print("\n*** Creacion de las tablas ***\n")
    create_tables(cur, tables)

    # Agregar valores a las tablas
    print("\n*** Agregar valores a las tablas ***\n")
    add_to_db(cur, add_reg_statement)

    cur.close()
