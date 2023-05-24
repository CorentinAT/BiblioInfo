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
  sql = "INSERT INTO DefinitGenre (iddoc, idgenre) VALUES (?, ?)"
  cur = conn.cursor()
  cur.execute(sql, (idDoc, idGenre))
  conn.commit()
  return cur.lastrowid

def link_document_theme(conn, idDoc, idTheme):
  sql = "INSERT INTO DefinitTheme (iddoc, idtheme) VALUES (?, ?)"
  cur = conn.cursor()
  cur.execute(sql, (idDoc, idTheme))
  conn.commit()
  return cur.lastrowid

def select_document_by_id(conn, idDoc):
  sql = "SELECT * FROM Document WHERE id = ?;"
  cur = conn.cursor()
  cur.execute(sql, (idDoc,))
  row = cur.fetchall()
  return row[0]

def select_genre_by_id(conn, idGenre):
  sql = "SELECT * FROM Genre WHERE idgenre = ?"
  cur = conn.cursor()
  cur.execute(sql, (idGenre,))
  row = cur.fetchall()
  return row[0]

def select_theme_by_id(conn, idTheme):
  sql = "SELECT * FROM Theme WHERE idtheme = ?"
  cur = conn.cursor()
  cur.execute(sql, (idTheme,))
  row = cur.fetchall()
  return row[0]

def select_note_avg_doc(conn, idDoc):
  sql = "SELECT AVG(note) FROM Note WHERE iddoc = ?;"
  cur = conn.cursor()
  cur.execute(sql, (idDoc,))
  row = cur.fetchall()
  return row[0][0]

def select_all_genres(conn):
  sql = "SELECT * FROM Genre;"
  cur = conn.cursor()
  cur.execute(sql)
  row = cur.fetchall()
  return row

def select_all_themes(conn):
  sql = "SELECT * FROM Theme;"
  cur = conn.cursor()
  cur.execute(sql)
  row = cur.fetchall()
  return row

def select_genres_document(conn, idDoc):
  sql = "SELECT g.idgenre, g.nomgenre FROM Genre g JOIN DefinitGenre dg ON g.idgenre=dg.idgenre WHERE dg.iddoc=?;"
  cur = conn.cursor()
  cur.execute(sql, (idDoc,))
  row = cur.fetchall()
  return row

def select_themes_document(conn, idDoc):
  sql = "SELECT t.idtheme, t.nomtheme FROM Theme t JOIN DefinitTheme dt ON t.idtheme=dt.idtheme WHERE dt.iddoc=?;"
  cur = conn.cursor()
  cur.execute(sql, (idDoc,))
  row = cur.fetchall()
  return row

def select_rayon_by_id(conn, idRayon):
  sql = "SELECT * from Rayon WHERE idrayon=?;"
  cur = conn.cursor()
  cur.execute(sql, (idRayon,))
  row = cur.fetchall()
  return row[0]

def update_info_document(conn, idDoc, info, donnee):
  sql = f"UPDATE Document SET {info}=? WHERE id=?;"
  cur = conn.cursor()
  cur.execute(sql, (donnee, idDoc,))
  conn.commit()

def delete_document(conn, idDoc):
  sql = "DELETE FROM Document WHERE id = ?;"
  cur = conn.cursor()
  cur.execute(sql, (idDoc,))
  conn.commit()

def delete_note_from_document(conn, idDoc):
  sql = "DELETE FROM Note WHERE iddoc = ?"
  cur = conn.cursor()
  cur.execute(sql, (idDoc,))
  conn.commit()

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
    titre VARCHAR NOT NULL,
    description TEXT,
    auteur VARCHAR,
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
    idgenre VARCHAR,
    PRIMARY KEY(iddoc, idgenre),
    FOREIGN KEY(iddoc) REFERENCES Document(id),
    FOREIGN KEY(idgenre) REFERENCES Genre(idgenre)
  );"""

  sql_create_definit_theme_table = """
  CREATE TABLE IF NOT EXISTS DefinitTheme (
    iddoc INT,
    idtheme VARCHAR,
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
  else:
    print("Error, can't create the database connection")

if __name__ == '__main__':
  main()