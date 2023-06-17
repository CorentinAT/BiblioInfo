from fastapi import FastAPI, Path, Query, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
import bdd
import classes
import verifs

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

database = r"bdd.db"

@app.get("/document/{idDoc}")
def get_document_by_id(idDoc: int):
  """Récupère l'ensemble des informations liées à un document via son ID"""
  conn = bdd.create_connection(database)
  verifs.verif_doc_existe(conn, idDoc)
  document = bdd.select_document_by_id(conn, idDoc)
  document = classes.to_object_document(document)
  note_moyenne = bdd.select_note_avg_doc(conn, idDoc)
  if note_moyenne == None:
    note_moyenne = 0
  rayon = bdd.select_rayon_by_id(conn, document.idrayon)
  rayon = classes.to_object_rayon(rayon)
  listegenres = bdd.select_genres_document(conn, idDoc)
  for i in range (len(listegenres)):
    listegenres[i] = classes.to_object_genre(listegenres[i])
  listethemes = bdd.select_themes_document(conn, idDoc)
  for i in range (len(listethemes)):
    listethemes[i] = classes.to_object_theme(listethemes[i])
  documentComplet = classes.to_object_document_complet(document, rayon, note_moyenne, listegenres, listethemes)
  return documentComplet

@app.get("/search_documents_by_title_genres")
def get_documents_by_title_and_genres(titre: str, doitEtreDispo: bool, idsGenres: list = Query(default=[], alias="idGenre")):
  """Renvoie les documents contenants le(s) mot(s)-clé(s) donné(s) et ayant comme genre(s) le(s) genre(s) donné(s), si doitEtreDispo est à True, renvoie uniquement les documents disponibles"""
  conn = bdd.create_connection(database)
  for idGenre in idsGenres:
    verifs.verif_genre_existe(conn, idGenre)
  documents = bdd.select_documents_by_title_and_genres(conn, titre, doitEtreDispo, idsGenres)
  for i in range (len(documents)):
    documents[i] = classes.to_object_document(documents[i])
  return documents

@app.get("/genres")
def get_liste_genres():
  """Renvoie la liste de l'ensemble des genres de la bibliothèque"""
  conn = bdd.create_connection(database)
  listegenres = bdd.select_all_genres(conn)
  for i in range (len(listegenres)):
    listegenres[i] = classes.to_object_genre(listegenres[i])
  return listegenres

@app.get("/themes")
def get_liste_themes():
  """Renvoie la liste de l'ensemble des thèmes de la bibliothèque"""
  conn = bdd.create_connection(database)
  listethemes = bdd.select_all_themes(conn)
  for i in range (len(listethemes)):
    listethemes[i] = classes.to_object_theme(listethemes[i])
  return listethemes

@app.get("/rayons")
def get_liste_rayons():
  """Renvoie la liste de l'ensemble des rayons de la bibliothèque"""
  conn = bdd.create_connection(database)
  listerayons = bdd.select_all_rayons(conn)
  for i in range (len(listerayons)):
    listerayons[i] = classes.to_object_rayon(listerayons[i])
  return listerayons

@app.post("/create_note")
def create_note(note : classes.Note):
  """Créer une note (de 0 à 5) attribuée à un document via son ID, renvoie l'ID de la note"""
  conn = bdd.create_connection(database)
  verifs.verif_doc_existe(conn, note.iddoc)
  if note.note<0 or note.note>5:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La note doit être entre 0 et 5 (inclus)")
  note_id = bdd.create_note(conn, (note.note, note.iddoc))
  return note_id

@app.post("/create_document")
def create_document(document: classes.UpdateDocument):
  """Créer un document, l'id est créé automatiquement, liencouverture, auteur et description facultatif, renvoie l'id du document"""
  conn = bdd.create_connection(database)
  verifs.verif_rayon_existe(conn, document.idrayon)
  document_id = bdd.create_document(conn, (document.titre, document.disponible, document.idrayon))
  if document.liencouverture != None:
    bdd.update_info_document(conn, document_id, "liencouverture", document.liencouverture)
  if document.description != None:
    bdd.update_info_document(conn, document_id, "description", document.description)
  if document.auteur != None:
    bdd.update_info_document(conn, document_id, "auteur", document.auteur)
  return document_id

@app.post("/document/{idDoc}/add_genre")
def add_genre_to_document(idDoc: int, idGenre: str):
  """Attribuer un genre à un document depuis leurs identifiants"""
  conn = bdd.create_connection(database)
  verifs.verif_doc_existe(conn, idDoc)
  verifs.verif_genre_existe(conn, idGenre)
  bdd.link_document_genre(conn, idDoc, idGenre)

@app.post("/document/{idDoc}/add_theme")
def add_theme_to_document(idDoc: int, idTheme: str):
  """Attribuer un thème à un document depuis leurs identifiants"""
  conn = bdd.create_connection(database)
  verifs.verif_doc_existe(conn, idDoc)
  verifs.verif_theme_existe(conn, idTheme)
  bdd.link_document_theme(conn, idDoc, idTheme)

@app.put("/document/{idDoc}/update")
def update_document(idDoc: int, document: classes.UpdateDocument):
  """Modifier des informations sur un document via son ID, tout est facultatif, renvoie l'id du document"""
  conn = bdd.create_connection(database)
  verifs.verif_doc_existe(conn, idDoc)
  if document.idrayon != None:
    verifs.verif_rayon_existe(conn, document.idrayon)
  if document.titre != None:
    bdd.update_info_document(conn, idDoc, "titre", document.titre)
  if document.liencouverture != None:
    bdd.update_info_document(conn, idDoc, "liencouverture", document.liencouverture)
  if document.auteur != None:
    bdd.update_info_document(conn, idDoc, "auteur", document.auteur)
  if document.disponible != None:
    bdd.update_info_document(conn, idDoc, "disponible", document.disponible)
    bdd.update_info_document(conn, idDoc, "idrayon", document.idrayon)
  if document.description != None:
    bdd.update_info_document(conn, idDoc, "description", document.description)
  return idDoc

@app.delete("/document/{idDoc}/delete")
def delete_document(idDoc: int):
  """Supprimer un document via son ID et toutes les notes liées à ce document"""
  conn = bdd.create_connection(database)
  verifs.verif_doc_existe(conn, idDoc)
  bdd.delete_document(conn, idDoc)
  bdd.delete_note_from_document(conn, idDoc)
  bdd.delete_genres_from_document(conn, idDoc)
  bdd.delete_themes_from_document(conn, idDoc)

@app.delete("/document/{idDoc}/delete_genres_themes")
def delete_genres_themes_from_document(idDoc: int):
  """Supprimer les genres et thèmes liées à un document, via l'id de ce document"""
  conn = bdd.create_connection(database)
  verifs.verif_doc_existe(conn, idDoc)
  bdd.delete_genres_from_document(conn, idDoc)
  bdd.delete_themes_from_document(conn, idDoc)