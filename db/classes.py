from pydantic import BaseModel
from typing import Optional

class Document(BaseModel):
  id: int
  titre: str
  description: Optionnal[str] = None
  auteur: Optionnal[str] = None
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