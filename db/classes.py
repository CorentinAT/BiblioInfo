from pydantic import BaseModel
from typing import Optional

# Classes qui correspondent aux tables de la base de données pour pouvoir traiter et renvoyer les données
class Document(BaseModel):
  titre: str
  liencouverture: Optional[str] = None
  description: Optional[str] = None
  auteur: Optional[str] = None
  disponible: bool
  idrayon: str

class UpdateDocument(BaseModel):
  titre: Optional[str] = None
  liencouverture: Optional[str] = None
  auteur: Optional[str] = None
  disponible: Optional[bool] = None
  idrayon: Optional[str] = None

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
  note: int
  iddoc: int

class Genre(BaseModel):
  idgenre: str
  nomgenre: str

class Theme(BaseModel):
  idtheme: str
  nomtheme: str

class DocumentComplet(BaseModel):
  titre: str
  liencouverture: Optional[str] = None
  description: Optional[str] = None
  auteur: Optional[str] = None
  disponible: bool
  rayon: Rayon
  note_moyenne: float
  themes: list[Theme]
  genres: list[Genre]

# Fonctions pour passer les données récupérées dans la base en objets et pouvoir les traiter et renvoyer dans l'api
def to_object_document(document)->Document:
  """Convertit une liste d'attributs en un objet Document"""
  objDoc = Document(titre=document[1], liencouverture=document[2], description=document[3], auteur=document[4], disponible=document[5], idrayon=document[6])
  return objDoc

def to_object_rayon(rayon)->Rayon:
  """Convertit une liste d'attributs en un objet Rayon"""
  objRayon = Rayon(idrayon=rayon[0], nomrayon=rayon[1], etage=rayon[2])
  return objRayon

def to_object_genre(genre)->Genre:
  """Convertit une liste d'attributs en un objet Genre"""
  objGenre = Genre(idgenre=genre[0], nomgenre=genre[1])
  return objGenre

def to_object_theme(theme)->Theme:
  """Convertit une liste d'attributs en un objet Theme"""
  objTheme = Theme(idtheme=theme[0], nomtheme=theme[1])
  return objTheme

def to_object_note(note)->Note:
  """Convertit une liste d'attributs en un objet Note"""
  objNote = Note(note=note[1], iddoc=note[2])
  return objNote

def to_object_document_complet(document: Document, rayon: Rayon, note_moyenne: float, listegenres: list[Genre], listethemes: list[Theme])->DocumentComplet:
  """Assemble des objets Document, Rayon, ListeGenres, ListeThemes et une note moyenne (float) en un objet DocumentComplet"""
  objDocumentComplet = DocumentComplet(titre=document.titre, description=document.description, auteur=document.auteur, disponible=document.disponible, rayon=rayon, note_moyenne=note_moyenne, genres=listegenres, themes=listethemes)
  return objDocumentComplet