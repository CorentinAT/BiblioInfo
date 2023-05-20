import sqlite3
from sqlite3 import Error

def create_connection(db_file):
  conn = None
  try:
    conn = sqlite3.connect(db_file)
    print(sqlite3.version)
  except Error as e:
    print(e)
  return conn

def create_table(conn, create_table_sql):
  try:
    c = conn.cursor()
    c.execute(create_table_sql)
  except Error as e:
    print(e)

def create_rayon(conn, rayon):
  sql = "INSERT INTO Rayon (idrayon, nomrayon, etage) VALUES (?, ?, ?)"
  cur = conn.cursor()
  cur.execute(sql, rayon)
  conn.commit()
  return cur.lastrowid

def create_genre(conn, genre):
  sql = "INSERT INTO Genre (idgenre, nomgenre) VALUES (?, ?)"
  cur = conn.cursor()
  cur.execute(sql, genre)
  conn.commit()
  return cur.lastrowid

def main():
  database = r"bdd.db"

  sql_create_rayon_table = """
  CREATE TABLE IF NOT EXISTS Rayon (
    idrayon VARCHAR PRIMARY KEY,
    nomrayon VARCHAR NOT NULL,
    etage INT NOT NULL,
    UNIQUE(nomrayon)
  );"""

  sql_create_genre_table = """
  CREATE TABLE IF NOT EXISTS Genre (
    idgenre SERIAL PRIMARY KEY,
    nomgenre VARCHAR NOT NULL,
    UNIQUE(nomgenre)
  );"""

  sql_create_theme_table = """
  CREATE TABLE IF NOT EXISTS Theme (
    idtheme VARCHAR PRIMARY KEY,
    nomtheme VARCHAR NOT NULL,
    UNIQUE(nomtheme)
  );"""

  sql_create_document_table = """
  CREATE TABLE IF NOT EXISTS Document (
    id INT,
    titre VARCHAR(50) NOT NULL,
    description TEXT,
    auteur VARCHAR(50),
    disponible LOGICAL NOT NULL,
    idrayon INT NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(idrayon) REFERENCES Rayon(idrayon)
  );"""

  sql_create_note_table = """
  CREATE TABLE IF NOT EXISTS Note (
    idnote INT,
    note INT NOT NULL,
    id INT NOT NULL,
    PRIMARY KEY(idnote),
    FOREIGN KEY(id) REFERENCES Document(id)
  );"""

  sql_create_definit_genre_table = """
  CREATE TABLE IF NOT EXISTS DefinitGenre (
    id INT,
    idgenre INT,
    PRIMARY KEY(id, idgenre),
    FOREIGN KEY(id) REFERENCES Document(id),
    FOREIGN KEY(idgenre) REFERENCES Genre(idgenre)
  );"""

  sql_create_definit_theme_table = """
  CREATE TABLE IF NOT EXISTS DefinitTheme (
    id INT,
    idtheme VARCHAR(50),
    PRIMARY KEY(id, idtheme),
    FOREIGN KEY(id) REFERENCES Document(id),
    FOREIGN KEY(idtheme) REFERENCES Thème(idtheme)
  );"""

  conn = create_connection(database)

  if conn is not None:
      create_table(conn, sql_create_rayon_table)
      create_table(conn, sql_create_genre_table)
      create_table(conn, sql_create_theme_table)
      create_table(conn, sql_create_document_table)
      create_table(conn, sql_create_note_table)
      create_table(conn, sql_create_definit_genre_table)
      create_table(conn, sql_create_definit_theme_table)
  else:
      print("Error, can't create the database connection")

if __name__ == '__main__':
  main()