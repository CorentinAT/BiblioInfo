from pydantic import BaseModel
from typing import Optional

class Document(BaseModel):
  id: int
  titre: str
  description: Optional[str] = None
  auteur: Optional[str] = None
  disponible: bool
  idrayon: str

class Rayon(BaseModel):
  idrayon: str
  nomrayon: str
  etage: int

class Genre(BaseModel):
  idgenre: str
  nomgenre: str

class Theme(BaseModel):
  idtheme: str
  nomtheme: str

class Note(BaseModel):
  idnote: int
  note: int
  iddoc: int

class DefinitGenre(BaseModel):
  iddoc: int
  idgenre: str

class DefinitTheme(BaseModel):
  iddoc: int
  idtheme: str

class NoteMoyenne(BaseModel):
  notemoyenne: float

class ListeGenres(BaseModel):
  listegenres: list

class Genre(BaseModel):
  idgenre: str
  nomgenre: str

class ListeThemes(BaseModel):
  listethemes: list

class Theme(BaseModel):
  idtheme: str
  nomtheme: str

def to_object_document(document)->Document:
  objDoc = Document(id=document[0], titre=document[1], description=document[2], auteur=document[3], disponible=document[4], idrayon=document[5])
  return objDoc

def to_object_rayon(rayon)->Rayon:
  objRayon = Rayon(idrayon=rayon[0], nomrayon=rayon[1], etage=rayon[2])
  return objRayon

def to_object_genre(genre)->Genre:
  objGenre = Genre(idgenre=genre[0], nomgenre=genre[1])
  return objGenre

def to_object_theme(theme)->Theme:
  objTheme = Theme(idtheme=theme[0], nomtheme=theme[1])
  return objTheme

def to_object_note(note)->Note:
  objNote = Note(idnote=note[0], note=note[1], iddoc=note[2])
  return objNote

def to_object_genre(genre)->Genre:
  objGenre = Genre(idgenre=genre[0], nomgenre=genre[1])
  return objGenre

def to_object_theme(theme)->Theme:
  objTheme = Theme(idtheme=theme[0], nomtheme=theme[1])
  return objTheme

def to_object_note_moyenne(notemoyenne)->NoteMoyenne:
  objNoteMoyenne = NoteMoyenne(notemoyenne=notemoyenne)
  return objNoteMoyenne

def to_object_liste_genres(listegenres)->ListeGenres:
  objListeGenres = ListeGenres(listegenres=[])
  for genre in listegenres:
    if genre!=():
      genre = to_object_genre(genre)
      objListeGenres.listegenres.append(genre)
  return objListeGenres

def to_object_liste_themes(listethemes)->ListeThemes:
  objListeThemes = ListeThemes(listethemes=[])
  for theme in listethemes:
    if themes!=():
      theme = to_object_theme(theme)
      objListeTheme.listethemes.append(theme)
  return objListeThemes