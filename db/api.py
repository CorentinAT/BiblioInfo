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
    document = classes.to_object_document(document)
    return document
  except:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ce document n'existe pas")

@app.get("/document/{idDoc}/note")
def get_note_avg_doc(idDoc: int):
  conn = bdd.create_connection(database)
  try:
    bdd.select_document_by_id(conn, idDoc)
  except:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ce document n'existe pas")
  note_moyenne = bdd.select_note_avg_doc(conn, idDoc)
  if note_moyenne == None:
    note_moyenne = classes.to_object_note_moyenne(0)
  else:
    note_moyenne = classes.to_object_note_moyenne(note_moyenne)
  return note_moyenne

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

@app.get("/document/{idDoc}/genres")
def get_genres_document(idDoc: int):
  conn = bdd.create_connection(database)
  try:
    bdd.select_document_by_id(conn, idDoc)
  except:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ce document n'existe pas")
  listegenres = bdd.select_genres_document(conn, idDoc)
  listegenres = classes.to_object_liste_genres(listegenres)
  return listegenres

@app.get("/document/{idDoc}/themes")
def get_themes_document(idDoc: int):
  conn = bdd.create_connection(database)
  try:
    bdd.select_document_by_id(conn, idDoc)
  except:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ce document n'existe pas")
  listethemes = bdd.select_themes_document(conn, idDoc)
  listethemes = classes.to_object_liste_themes(listethemes)
  return listethemes

@app.post("/create_note")
def create_note(note : classes.Note):
  conn = bdd.create_connection(database)
  note_id = bdd.create_note(conn, (note.note, note.iddoc))
  return note_id