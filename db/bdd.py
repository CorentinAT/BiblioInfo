import sqlite3
from sqlite3 import Error

def create_connection(db_file):
  """Créer une connexion à un fichier de base de données"""
  conn = None
  try:
    conn = sqlite3.connect(db_file)
    print(sqlite3.version)
  except Error as e:
    print(e)
  return conn

def create_table(conn, create_table_sql):
  """Créer une table depuis la requête SQL donnée"""
  try:
    c = conn.cursor()
    c.execute(create_table_sql)
  except Error as e:
    print(e)

def create_rayon(conn, rayon):
  """Ajouter un rayon à la table, avec le paramètre rayon sous cette forme (idrayon:str, nomrayon:str, etage:int)"""
  sql = "INSERT INTO Rayon (idrayon, nomrayon, etage) VALUES (?, ?, ?)"
  cur = conn.cursor()
  cur.execute(sql, rayon)
  conn.commit()

def create_genre(conn, genre):
  """Ajouter un genre à la table, avec le paramètre genre sous cette forme (idgenre:str, nomgenre:str)"""
  sql = "INSERT INTO Genre (idgenre, nomgenre) VALUES (?, ?)"
  cur = conn.cursor()
  cur.execute(sql, genre)
  conn.commit()

def create_theme(conn, theme):
  """Ajouter un theme à la table, avec le paramètre theme sous cette forme (idtheme:str, nomtheme:str)"""
  sql = "INSERT INTO Theme (idtheme, nomtheme) VALUES (?, ?)"
  cur = conn.cursor()
  cur.execute(sql, theme)
  conn.commit()

def create_document(conn, document):
  """Ajouter un document à la table, avec le paramètre document sous cette forme (titre:str, disponible:bool, idrayon:str) avec id rayon l'id du rayon dans lequel le document se trouve, l'id est généré automatiquement et est renvoyé"""
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
  """Ajouter un theme à la table, avec le paramètre note sous cette forme (note:int, iddoc:int), avec note compris entre 0 et 5, et iddoc l'id du doc auquel attribuer la note, l'idnote est généré automatiquement et est renvoyé"""
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
  """Insere dans la table DefinitGenre l'idDoc et l'idGenre donnés (int et str) pour attribuer le genre au document"""
  sql = "INSERT INTO DefinitGenre (iddoc, idgenre) VALUES (?, ?)"
  cur = conn.cursor()
  cur.execute(sql, (idDoc, idGenre))
  conn.commit()

def link_document_theme(conn, idDoc, idTheme):
  """Insere dans la table DefinitTheme l'idDoc et l'idTheme donnés (int et str) pour attribuer le theme au document"""
  sql = "INSERT INTO DefinitTheme (iddoc, idtheme) VALUES (?, ?)"
  cur = conn.cursor()
  cur.execute(sql, (idDoc, idTheme))
  conn.commit()

def select_document_by_id(conn, idDoc):
  """Renvoie les informations du document correspondant à l'idDoc(int) donné"""
  sql = "SELECT * FROM Document WHERE id = ?;"
  cur = conn.cursor()
  cur.execute(sql, (idDoc,))
  row = cur.fetchall()
  return row[0]

def select_documents_by_title_and_genres(conn, titre, idsGenres):
  """Renvoie les informations des documents qui ont comme genres les genres qui ont les idsGenres donnés (facultatif, liste de str, 0 à *), et qui contiennent la chaîne de caractère titre dans leur titre"""
  sql = f"SELECT d.* FROM Document d LEFT JOIN DefinitGenre dg ON d.id = dg.iddoc WHERE LOWER(d.titre) LIKE '%{titre.lower()}%'"
  if idsGenres != []:
    print(idsGenres)
    sql += f" GROUP BY d.id HAVING COUNT(DISTINCT dg.idgenre) = {len(idsGenres)}"
  cur = conn.cursor()
  cur.execute(sql)
  row = cur.fetchall()
  return row

def select_rayon_by_id(conn, idRayon):
  """Renvoie les informations du rayon correspondant à l'idRayon(str) donné"""
  sql = "SELECT * from Rayon WHERE idrayon=?;"
  cur = conn.cursor()
  cur.execute(sql, (idRayon,))
  row = cur.fetchall()
  return row[0]

def select_genre_by_id(conn, idGenre):
  """Renvoie les informations du genre correspondant à l'idGenre(str) donné"""
  sql = "SELECT * FROM Genre WHERE idgenre = ?"
  cur = conn.cursor()
  cur.execute(sql, (idGenre,))
  row = cur.fetchall()
  return row[0]

def select_theme_by_id(conn, idTheme):
  """Renvoie les informations du theme correspondant à l'idTheme(str) donné"""
  sql = "SELECT * FROM Theme WHERE idtheme = ?"
  cur = conn.cursor()
  cur.execute(sql, (idTheme,))
  row = cur.fetchall()
  return row[0]

def select_note_avg_doc(conn, idDoc):
  """Renvoie la note moyenne d'un document d'après son id(int)"""
  sql = "SELECT AVG(note) FROM Note WHERE iddoc = ?;"
  cur = conn.cursor()
  cur.execute(sql, (idDoc,))
  row = cur.fetchall()
  return row[0][0]

def select_all_genres(conn):
  """Renvoie tous les genres de la base de données"""
  sql = "SELECT * FROM Genre;"
  cur = conn.cursor()
  cur.execute(sql)
  row = cur.fetchall()
  return row

def select_all_themes(conn):
  """Renvoie tous les themes de la base de données"""
  sql = "SELECT * FROM Theme;"
  cur = conn.cursor()
  cur.execute(sql)
  row = cur.fetchall()
  return row

def select_all_rayons(conn):
  """Renvoie tous les rayons de la base de données"""
  sql = "SELECT * FROM Rayon;"
  cur = conn.cursor()
  cur.execute(sql)
  row = cur.fetchall()
  return row

def select_genres_document(conn, idDoc):
  """Renvoie tous les genres du document dont l'id est donné"""
  sql = "SELECT g.idgenre, g.nomgenre FROM Genre g JOIN DefinitGenre dg ON g.idgenre=dg.idgenre WHERE dg.iddoc=?;"
  cur = conn.cursor()
  cur.execute(sql, (idDoc,))
  row = cur.fetchall()
  return row

def select_themes_document(conn, idDoc):
  """Renvoie tous les themes du document dont l'id est donné"""
  sql = "SELECT t.idtheme, t.nomtheme FROM Theme t JOIN DefinitTheme dt ON t.idtheme=dt.idtheme WHERE dt.iddoc=?;"
  cur = conn.cursor()
  cur.execute(sql, (idDoc,))
  row = cur.fetchall()
  return row

def update_info_document(conn, idDoc, info, donnee):
  """Met à jour dans la bdd l'information info(str), avec la valeur 'donnee' pour le document ayant comme identifiant idDoc"""
  sql = f"UPDATE Document SET {info}=? WHERE id=?;"
  cur = conn.cursor()
  cur.execute(sql, (donnee, idDoc,))
  conn.commit()

def delete_document(conn, idDoc):
  """Supprime de la base le document d'id idDoc"""
  sql = "DELETE FROM Document WHERE id = ?;"
  cur = conn.cursor()
  cur.execute(sql, (idDoc,))
  conn.commit()

def main():
  """Création de la base de données et des tables"""
  database = r"bdd.db"

  # Définition des différentes tables de la base de données
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
    liencouverture VARCHAR,
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
    # Création des différentes tables depuis leur définition
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