from fastapi import HTTPException, status
import bdd

def verif_doc_existe (conn, idDoc):
  """Vérifie si l'ID donné correspond à un document, erreur 404 s'il n'existe pas"""
  try:
    bdd.select_document_by_id(conn, idDoc)
  except:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ce document n'existe pas")
  
def verif_rayon_existe(conn, idRayon):
  """Vérifie si l'ID donné correspond à un rayon, erreur 404 s'il n'existe pas"""
  try:
    bdd.select_rayon_by_id(conn, idRayon)
  except:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Le rayon n'existe pas")

def verif_genre_existe(conn, idGenre):
  """Vérifie si l'ID donné correspond à un genre, erreur 404 s'il n'existe pas"""
  try:
    bdd.select_genre_by_id(conn, idGenre)
  except:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Le genre n'existe pas")

def verif_theme_existe(conn, idTheme):
  """Vérifie si l'ID donné correspond à un thème, erreur 404 s'il n'existe pas"""
  try:
    bdd.select_theme_by_id(conn, idTheme)
  except:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Le thème n'existe pas")