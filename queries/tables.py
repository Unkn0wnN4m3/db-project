TABLES = {}

TABLES["Artistas"] = (
    "CREATE TABLE IF NOT EXISTS Artistas ("
    "nombre_artistico VARCHAR(50), "
    "nombre VARCHAR(50), "
    "apellidos VARCHAR(50), "
    "edad INT(2), "
    "cache DOUBLE(10, 4), "
    "descripcion VARCHAR(100), "
    "papeles_afin VARCHAR(100), "
    "veces_interpretado INT(3), "
    "PRIMARY KEY (nombre_artistico)"
    ") ENGINE = INNODB;"
)

TABLES["Autores"] = (
    "CREATE TABLE IF NOT EXISTS Autores ("
    "id_autor INT(10), "
    "nombre VARCHAR(50), "
    "apellidos VARCHAR(50), "
    "nombre_artistico VARCHAR(50), "
    "edad INT(3), "
    "cobro_x_libreto DOUBLE(10,4), "
    "cobro_x_representacion DOUBLE(10,4), "
    "PRIMARY KEY (id_autor)"
    ") ENGINE = INNODB;"
)

TABLES["Teatros"] = (
    "CREATE TABLE IF NOT EXISTS Teatros ("
    "nombre VARCHAR(50), "
    "direccion VARCHAR(100), "
    "localidad VARCHAR(100), "
    "provincia VARCHAR(100), "
    "telefono INT(12), "
    "categoria VARCHAR(100), "
    "aforo INT(6), "
    "PRIMARY KEY (nombre)"
    ") ENGINE = INNODB;"
)

TABLES["Obras"] = (
    "CREATE TABLE IF NOT EXISTS Obras ("
    "titulo VARCHAR(50), "
    "ano_publicacion YEAR, "
    "veces_representado INT(3), "
    "autor INT(10), "
    "PRIMARY KEY (titulo), "
    "FOREIGN KEY (autor) REFERENCES Autores(id_autor) "
    "ON DELETE CASCADE "
    "ON UPDATE CASCADE"
    ") ENGINE = INNODB;"
)

TABLES["Papeles"] = (
    "CREATE TABLE IF NOT EXISTS Papeles ("
    "nombre_personaje VARCHAR(50), "
    "duracion_en_escena TIME, "
    "descripcion_atrezo VARCHAR(100), "
    "PRIMARY KEY (nombre_personaje) "
    ") ENGINE = INNODB;"
)

TABLES["Funciones"] = (
    "CREATE TABLE IF NOT EXISTS Funciones ("
    "nombre_teatro VARCHAR(50), "
    "titulo_obra VARCHAR(50), "
    "fecha DATE, "
    "PRIMARY KEY (nombre_teatro,titulo_obra), "
    "FOREIGN KEY (nombre_teatro) REFERENCES Teatros(nombre) "
    "ON DELETE RESTRICt "
    "ON UPDATE RESTRICt, "
    "FOREIGN KEY (titulo_obra) REFERENCES Obras(titulo) "
    "ON DELETE RESTRICt "
    "ON UPDATE RESTRICt"
    ") ENGINE = INNODB;"
)

# Tabla de relacion N:M de "Papeles" y "Artistas"
TABLES["Representan"] = (
    "CREATE TABLE IF NOT EXISTS Representan ("
    "nombre_artistico VARCHAR(50), "
    "nombre_personaje VARCHAR(50), "
    "asignado BOOLEAN , "
    "PRIMARY KEY (nombre_artistico,nombre_personaje), "
    "FOREIGN KEY (nombre_artistico) REFERENCES Artistas(nombre_artistico) "
    "ON DELETE SET NULL "
    "ON UPDATE SET NULL, "
    "FOREIGN KEY (nombre_personaje) REFERENCES Papeles(nombre_personaje) "
    "ON DELETE SET NULL "
    "ON UPDATE SET NULL"
    ") ENGINE = INNODB;"
)
