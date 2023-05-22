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
  conn = bdd.create_connection(db_file)