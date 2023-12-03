add_records = {}
add_reg_statement = {
    "Artistas": "(?, ?, ?, ?, ?, ?, ?, ?)",
    "Autores": "(?, ?, ?, ?, ?, ?, ?)",
    "Obras": "(?, ?, ?, ?, ?, ?, ?)",
    "Papeles": "(?, ?, ?, ?, ?)",
    "Representaciones": "(?, ?, ?)",
    "Teatros": "(?, ?, ?, ?, ?, ?, ?, ?)",
    "Funciones": "(?, ?, ?, ?)",
    "Participaciones": "(?, ?)"
}

add_records["Artistas"] = [
    (1, "Alejandro", "Rodriguez", "alro", 34, 3500.50, "alguna descripcion", "papel1"),
    (2, "Valeria", "Perez", "vape", 54, 45000.50, "alguna descripcion", "papel2"),
    (3, "Javier", "Gonzales", "jago", 21, 4500.50, "alguna descripcion", "papel3"),
    (4, "Camila", "Lopez", "calo", 32, 5540.50, "alguna descripcion", "papel4"),
    (5, "Ricardo", "Martinez", "rima", 54, 6500.50, "alguna descripcion", "papel5"),
    (6, "Isabella", "Sanchez", "issa", 65, 7500.50, "alguna descripcion", "papel6"),
    (7, "Diego", "Romero", "diro", 47, 4400.50, "alguna descripcion", "papel7"),
    (8, "Gabriela", "Diaz", "gadi", 56, 9000.50, "alguna descripcion", "papel8"),
]

add_records["Autores"] = [
    (1, "Natalia", "Vargas", "nava", 24, 1234.12, 5678.90),
    (2, "Juan Carlos", "Moreno", "jamo", 35, 1234.12, 5678.90),
    (3, "Ana", "Ramirez", "anra", 34, 1234.12, 5678.90),
    (4, "Sergio", "Herrera", "sehe", 44, 1234.12, 5678.90),
    (5, "Gabriela", "Fernandez", "gafe", 54, 1234.12, 5678.90),
    (6, "Luis", "Garcia", "luga", 64, 1234.12, 5678.90),
    (7, "Carolina", "Torres", "cato", 74, 1234.12, 5678.90),
    (8, "Andres", "Silva", "ansi", 84, 1234.12, 5678.90),
]

add_records["Obras"] = [
    (1, "El Jardín de los Cerezos", 2023, 43, 0, 0, 1),
    (2, "Romeo y Julieta", 2023, 354, 0, 0, 2),
    (3, "La Casa de Bernarda Alba", 2023, 236, 0, 0, 3),
    (4, "Esperando a Godot", 2023, 543, 0, 0, 4),
    (5, "Don Juan Tenorio", 2023, 390, 0, 0, 5),
    (6, "La Gaviota", 2023, 67, 0, 0, 6),
    (7, "Un Tranvía Llamado Deseo", 2023, 546, 0, 0, 7),
    (8, "El Fantasma de la Ópera", 2023, 123, 0, 0, 8),
]

add_records["Papeles"] = [
    (1, "Elena Garcia", 234, "atrezo 1", 1),
    (2, "Julieta Capuleto", 123, "atrezo 2", 2),
    (3, "Adela Alba", 387, "atrezo 3", 3),
    (4, "Vladimir", 980, "atrezo 4", 4),
    (5, "Don Juan Tenorio", 345, "atrezo 5", 5),
    (6, "Konstantin Treplev", 657, "atrezo 6", 6),
    (7, "Blanche DuBois", 934, "atrezo 7", 7),
    (8, "Fantasma", 145, "atrezo 8", 8),
]

add_records["Representaciones"] = [
    (1, 2, 23),
    (2, 1, 54),
    (2, 4, 10),
    (4, 3, 20),
    (5, 6, 30),
    (6, 5, 40),
    (7, 8, 50),
    (8, 7, 60),
]

add_records["Teatros"] = [
    (1, "Teatro Estelar", "direccion 1", "localidad 1", "provincia 1", 5512345678, "categoria 1", 100),
    (2, "Gran Escenario Dramático", "direccion 2", "localidad 2", "provincia 2", 5522365678, "categoria 2", 200),
    (3, "Teatro Aurora", "direccion 3", "localidad 3", "provincia 3", 5532379678, "categoria 3", 300),
    (4, "Palacio de las Artes", "direccion 4", "localidad 4", "provincia 4", 5509345678, "categoria 4", 400),
    (5, "Teatro del Crepúsculo", "direccion 5", "localidad 5", "provincia 5", 5552350678, "categoria 5", 500),
    (6, "Escenario Mágico", "direccion 6", "localidad 6", "provincia 6", 5562345508, "categoria 6", 600),
    (7, "Teatro de las Estrellas", "direccion 7", "localidad 7", "provincia 7", 5554345678, "categoria 7", 700),
    (8, "Sala de las Emociones", "direccion 8", "localidad 8", "provincia 8", 5582340078, "categoria 8", 800)
]

add_records["Funciones"] = [
    (1, 1, 1, "2001-01-01"),
    (2, 2, 2, "2002-02-02"),
    (3, 3, 3, "2003-03-03"),
    (4, 4, 4, "2004-04-04"),
    (5, 5, 5, "2005-05-05"),
    (6, 6, 6, "2006-06-06"),
    (7, 7, 7, "2007-07-07"),
    (8, 8, 8, "2008-08-08")
]

add_records["Participaciones"] = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8)
]
