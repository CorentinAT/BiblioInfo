from fastapi import FastAPI, Path, Query, HTTPException, status
import bdd
import classes

app = FastAPI()

database = r"bdd.db"

@app.get("/document/{idDoc}")
def get_document_by_id(idDoc: int):
  conn = bdd.create_connection(database)
  try:
    document = bdd.select_document_by_id(conn, idDoc)
  except:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ce document n'existe pas")
  document = classes.to_object_document(document)
  note_moyenne = bdd.select_note_avg_doc(conn, idDoc)
  if note_moyenne == None:
    note_moyenne = 0
  rayon = bdd.select_rayon_by_id(conn, document.idrayon)
  rayon = classes.to_object_rayon(rayon)
  listegenres = bdd.select_genres_document(conn, idDoc)
  listegenres = classes.to_object_liste_genres(listegenres)
  listethemes = bdd.select_themes_document(conn, idDoc)
  listethemes = classes.to_object_liste_themes(listethemes)
  documentComplet = classes.to_object_document_complet(document, rayon, note_moyenne, listegenres, listethemes)
  return documentComplet

@app.get("/genres")
def get_liste_genres():
  conn = bdd.create_connection(database)
  listegenres = bdd.select_all_genres(conn)
  listegenres = classes.to_object_liste_genres(listegenres)
  return listegenres

@app.get("/themes")
def get_liste_themes():
  conn = bdd.create_connection(database)
  listethemes = bdd.select_all_themes(conn)
  listethemes = classes.to_object_liste_themes(listethemes)
  return listethemes

@app.post("/create_note")
def create_note(note : classes.Note):
  conn = bdd.create_connection(database)
  try:
    bdd.select_document_by_id(conn, note.iddoc)
  except:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ce document n'existe pas")
  note_id = bdd.create_note(conn, (note.note, note.iddoc))
  return note_id

@app.put("/document/{idDoc}/update")
def update_document(idDoc: int, document: classes.UpdateDocument):
  conn = bdd.create_connection(database)
  try:
    bdd.select_document_by_id(conn, idDoc)
  except:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ce document n'existe pas")
  if document.titre != None:
    document_id = bdd.update_info_document(conn, idDoc, "titre", document.titre)
  if document.auteur != None:
    document_id = bdd.update_info_document(conn, idDoc, "auteur", document.auteur)
  if document.disponible != None:
    document_id = bdd.update_info_document(conn, idDoc, "disponible", document.disponible)
  if document.idrayon != None:
    try:
      bdd.select_rayon_by_id(conn, document.idrayon)
    except:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Le rayon n'existe pas")
    document_id = bdd.update_info_document(conn, idDoc, "idrayon", document.idrayon)
  return document_id

@app.post("/create_document")
def create_document(document: classes.Document):
  conn = bdd.create_connection(database)
  try:
    bdd.select_rayon_by_id(conn, document.idrayon)
  except:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Le rayon n'existe pas")
  document_id = bdd.create_document(conn, (document.titre, document.disponible, document.idrayon))
  if document.description != None:
    bdd.update_info_document(conn, document_id, "description", document.description)
  if document.auteur != None:
    bdd.update_info_document(conn, document_id, "auteur", document.auteur)
  return document_id