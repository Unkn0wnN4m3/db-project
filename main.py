import os
import sys

import mariadb

from queries import TABLES, create_tables, set_db

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
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    cur = conn.cursor()

    # Creacion de la db
    print("*** table creation ***\n")
    set_db(cur, "proyectofinal")

    # Cracion de las tablas
    print("\n*** table creation ***\n")
    create_tables(cur, TABLES)
