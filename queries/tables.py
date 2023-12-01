tables: dict[str, str] = {}

tables["Artistas"] = (
    "CREATE TABLE IF NOT EXISTS Artistas ("
    "id_artista INT(10) NOT NULL, "
    "nombre VARCHAR(50), NOT NULL "
    "apellidos VARCHAR(50), NOT NULL "
    "nombre_artistico VARCHAR(50) UNIQUE NOT NULL, "
    "edad INT(2), "
    "cache DOUBLE(10, 4), "
    "descripcion VARCHAR(100), "
    "papeles_afin VARCHAR(100), "
    "veces_interpretado INT(3), "
    "PRIMARY KEY (id_artista)"
    ") ENGINE = INNODB;"
)

tables["Papeles"] = (
    "CREATE TABLE IF NOT EXISTS Papeles ("
    "id_papeles INT(10) NOT NULL, "
    "nombre_personaje VARCHAR(50) UNIQUE NOT NULL, "
    "duracion_en_escena INT(10), "
    "descripcion_atrezo VARCHAR(100), "
    "id_obra INT(10), "
    "PRIMARY KEY (id_papeles), "
    "FOREIGN KEY (id_obra) REFERENCES Obras(id_obra) "
    "ON DELETE CASCADE"
    ") ENGINE = INNODB;"
)

tables["Obras"] = (
    "CREATE TABLE IF NOT EXISTS Obras ("
    "id_obra INT(10) NOT NULL, "
    "titulo VARCHAR(50) UNIQUE, "
    "ano_publicacion YEAR, "
    "veces_representado INT(3), "
    "autor INT(10), "
    "PRIMARY KEY (titulo), "
    "FOREIGN KEY (autor) REFERENCES Autores(id_autor) "
    "ON DELETE CASCADE "
    "ON UPDATE CASCADE"
    ") ENGINE = INNODB;"
)

tables["Autores"] = (
    "CREATE TABLE IF NOT EXISTS Autores ("
    "id_autor INT(10), "
    "nombre VARCHAR(50) NOT NULL, "
    "apellidos VARCHAR(50) NOT NULL, "
    "nombre_artistico VARCHAR(50), "
    "edad INT(3), "
    "cobro_x_libreto DOUBLE(10,4), "
    "cobro_x_representacion DOUBLE(10,4), "
    "PRIMARY KEY (id_autor)"
    ") ENGINE = INNODB;"
)

# Tabla de relacion N:M de "Papeles" y "Artistas"
tables["Representan"] = (
    "CREATE TABLE IF NOT EXISTS Representan ("
    "id_artista VARCHAR(50), "
    "id_papel VARCHAR(50), "
    "veces_interpretado INT(3), "
    "PRIMARY KEY (id_artista, id_papel), "
    "FOREIGN KEY (id_artista) REFERENCES Artistas(id_artista) "
    "ON DELETE CASCADE "
    "FOREIGN KEY (id_papel) REFERENCES Papeles(id_papel) "
    "ON DELETE CASCADE"
    ") ENGINE = INNODB;"
)

tables["Teatros"] = (
    "CREATE TABLE IF NOT EXISTS Teatros ("
    "id_teatro INT(3) NOT NULL"
    "nombre VARCHAR(50) NOT NULL, "
    "direccion VARCHAR(100) NOT NULL, "
    "localidad VARCHAR(100), "
    "provincia VARCHAR(100), "
    "telefono INT(12), "
    "categoria VARCHAR(100), "
    "aforo INT(6), "
    "PRIMARY KEY (nombre)"
    ") ENGINE = INNODB;"
)

tables["Funciones"] = (
    "CREATE TABLE IF NOT EXISTS Funciones ("
    "id_funcion INT"
    "id_teatro INT(10), "
    "id_obra INT(10), "
    "fecha DATE NOT NULL, "
    "PRIMARY KEY (id_teatro,id_obra), "
    "FOREIGN KEY (id_teatro) REFERENCES Teatros(id_teatro) "
    "ON DELETE CASCADE "
    "FOREIGN KEY (id_obra) REFERENCES Obras(id_obra) "
    "ON DELETE SET NULL"
    ") ENGINE = INNODB;"
)

tables["Participaciones"] = (
    "CREATE TABLE IF NOT EXISTS Participaciones ("
    "id_artista INT(10)"
    "id_obra INT(10)"
    ") ENGINE = INNODB;"
)
