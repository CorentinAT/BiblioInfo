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

def create_theme(conn, theme):
  sql = "INSERT INTO Theme (idtheme, nomtheme) VALUES (?, ?)"
  cur = conn.cursor()
  cur.execute(sql, theme)
  conn.commit()
  return cur.lastrowid

def create_document(conn, document):
  sql = "SELECT MAX(id) FROM Document;"
  cur = conn.cursor()
  cur.execute(sql)
  idMax = cur.fetchall()[0][0]
  if(idMax == None):
    sql = "INSERT INTO Document (id, titre, disponible, idrayon) VALUES (1, ?, ?, ?)"
  else:
    sql = "INSERT INTO Document (id, titre, disponible, idrayon) VALUES (?, ?, ?, ?)"
    document = (idMax + 1,) + document
  cur = conn.cursor()
  cur.execute(sql, document)
  conn.commit()
  return cur.lastrowid

def create_note(conn, note):
  sql = "SELECT MAX(idnote) FROM Note;"
  cur = conn.cursor()
  cur.execute(sql)
  idMax = cur.fetchall()[0][0]
  if(idMax == None):
    sql = "INSERT INTO Note (idnote, note, iddoc) VALUES (1, ?, ?)"
  else:
    sql = "INSERT INTO Note (idnote, note, iddoc) VALUES (?, ?, ?)"
    note = (idMax + 1,) + note
  cur = conn.cursor()
  cur.execute(sql, note)
  conn.commit()
  return cur.lastrowid

def link_document_genre(conn, idDoc, idGenre):
  data = (idDoc, idGenre)
  sql = "INSERT INTO DefinitGenre (iddoc, idgenre) VALUES (?, ?)"
  cur = conn.cursor()
  cur.execute(sql, data)
  conn.commit()
  return cur.lastrowid

def link_document_theme(conn, idDoc, idTheme):
  data = (idDoc, idTheme)
  sql = "INSERT INTO DefinitTheme (iddoc, idtheme) VALUES (?, ?)"
  cur = conn.cursor()
  cur.execute(sql, data)
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
    idgenre VARCHAR PRIMARY KEY,
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
    id INT PRIMARY KEY,
    titre VARCHAR(50) NOT NULL,
    description TEXT,
    auteur VARCHAR(50),
    disponible LOGICAL NOT NULL,
    idrayon VARCHAR NOT NULL,
    FOREIGN KEY(idrayon) REFERENCES Rayon(idrayon)
  );"""

  sql_create_note_table = """
  CREATE TABLE IF NOT EXISTS Note (
    idnote INT,
    note INT NOT NULL,
    iddoc INT NOT NULL,
    PRIMARY KEY(idnote),
    FOREIGN KEY(iddoc) REFERENCES Document(id)
  );"""

  sql_create_definit_genre_table = """
  CREATE TABLE IF NOT EXISTS DefinitGenre (
    iddoc INT,
    idgenre INT,
    PRIMARY KEY(iddoc, idgenre),
    FOREIGN KEY(iddoc) REFERENCES Document(id),
    FOREIGN KEY(idgenre) REFERENCES Genre(idgenre)
  );"""

  sql_create_definit_theme_table = """
  CREATE TABLE IF NOT EXISTS DefinitTheme (
    iddoc INT,
    idtheme VARCHAR(50),
    PRIMARY KEY(iddoc, idtheme),
    FOREIGN KEY(iddoc) REFERENCES Document(id),
    FOREIGN KEY(idtheme) REFERENCES Theme(idtheme)
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

      # Partie tests, sera supprimée une fois la structure de la bd terminée
      create_rayon(conn, ("RA", "Rayon1", 4))

      create_document(conn, ("Dodocucu", True, "RA"))
      create_document(conn, ("Dodocucu", True, "RA"))
      create_document(conn, ("Dodocucu", True, "RA"))
      create_document(conn, ("Dodocucu", True, "RA"))

      create_genre(conn, ("G1", "Genre1"))
      create_genre(conn, ("G2", "Genre2"))

      link_document_genre(conn, 2, "G1")
      link_document_genre(conn, 2, "G2")
      link_document_genre(conn, 3, "G1")
      # Fin de la partie tests
  else:
      print("Error, can't create the database connection")

if __name__ == '__main__':
  main()