TABLES = {}

TABLES["Artistas"] = (
    "CREATE TABLE IF NOT EXISTS Artistas ("
    "nombre_artistico VARCHAR(50) NOT NULL, "
    "nombre VARCHAR(50) NOT NULL, "
    "apellidos VARCHAR(50) NOT NULL, "
    "edad INT(2) NOT NULL, "
    "cache DOUBLE(10, 4) NOT NULL, "
    "descripcion VARCHAR(100) NOT NULL, "
    "papeles_afin VARCHAR(100) NOT NULL, "
    "veces_interpretado INT(3) NOT NULL, "
    "PRIMARY KEY (nombre_artistico)"
    ") ENGINE = INNODB;"
)

TABLES["Autores"] = (
    "CREATE TABLE IF NOT EXISTS Autores ("
    "id_autor INT(10) NOT NULL, "
    "nombre VARCHAR(50) NOT NULL, "
    "apellidos VARCHAR(50) NOT NULL, "
    "nombre_artistico VARCHAR(50), "
    "edad INT(3) NOT NULL, "
    "cobro_x_libreto DOUBLE(10,4) NOT NULL, "
    "cobro_x_representacion DOUBLE(10,4) NOT NULL, "
    "PRIMARY KEY (id_autor)"
    ") ENGINE = INNODB;"
)

TABLES["Teatros"] = (
    "CREATE TABLE IF NOT EXISTS Teatros ("
    "nombre VARCHAR(50) NOT NULL, "
    "direccion VARCHAR(100) NOT NULL, "
    "localidad VARCHAR(100) NOT NULL, "
    "provincia VARCHAR(100) NOT NULL, "
    "telefono INT(12) NOT NULL, "
    "categoria VARCHAR(100) NOT NULL, "
    "aforo INT(6) NOT NULL, "
    "PRIMARY KEY (nombre)"
    ") ENGINE = INNODB;"
)

TABLES["Obras"] = (
    "CREATE TABLE IF NOT EXISTS Obras ("
    "titulo VARCHAR(50) NOT NULL, "
    "ano_publicacion DATE NOT NULL, "
    "veces_representado INT(3) NOT NULL, "
    "autor INT(10) NOT NULL, "
    "PRIMARY KEY (titulo), "
    "FOREIGN KEY (autor) REFERENCES Autores(id_autor) "
    "ON DELETE NO ACTION "
    "ON UPDATE NO ACTION"
    ") ENGINE = INNODB;"
)

TABLES["Papeles"] = (
    "CREATE TABLE IF NOT EXISTS Papeles ("
    "nombre_personaje VARCHAR(50) NOT NULL, "
    "duracion_en_escena TIME NOT NULL, "
    "descripcion_atrezo VARCHAR(100) NOT NULL, "
    "PRIMARY KEY (nombre_personaje) "
    ") ENGINE = INNODB;"
)

# WARN: Necesito verificar las constraints
TABLES["Funciones"] = (
    "CREATE TABLE IF NOT EXISTS Funciones ("
    "nombre_teatro VARCHAR(50) NOT NULL, "
    "titulo_obra VARCHAR(50) NOT NULL, "
    "fecha DATE NOT NULL, "
    "PRIMARY KEY (nombre_teatro,titulo_obra), "
    "FOREIGN KEY (nombre_teatro) REFERENCES Teatros(nombre) "
    "ON DELETE NO ACTION "
    "ON UPDATE NO ACTION, "
    "FOREIGN KEY (titulo_obra) REFERENCES Obras(titulo) "
    "ON DELETE NO ACTION "
    "ON UPDATE NO ACTION"
    ") ENGINE = INNODB;"
)

# Tabla de relacion N:M de "Papeles" y "Artistas"
# WARN: Necesito verificar las constraints
TABLES["Representan"] = (
    "CREATE TABLE IF NOT EXISTS Representan ("
    "nombre_artistico VARCHAR(50) NOT NULL, "
    "nombre_personaje VARCHAR(50) NOT NULL, "
    "asignado BOOLEAN NOT NULL, "
    "PRIMARY KEY (nombre_artistico,nombre_personaje), "
    "FOREIGN KEY (nombre_artistico) REFERENCES Artistas(nombre_artistico) "
    "ON DELETE NO ACTION "
    "ON UPDATE NO ACTION, "
    "FOREIGN KEY (nombre_personaje) REFERENCES Papeles(nombre_personaje) "
    "ON DELETE NO ACTION "
    "ON UPDATE NO ACTION"
    ") ENGINE = INNODB;"
)
