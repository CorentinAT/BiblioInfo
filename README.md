# BiblioInfo
Site de gestion de bilbiothèque, projet fait en BUT1 Informatique.

https://www.biblioinfo.live/

## Consigne du projet

Faire une application informatique utilisant une base de données, en ayant établi au préalable des spécifications techniques/fonctionnelles, une maquette, une répartition des tâches, un planning...

## Technologies utilisées

- HTML, CSS et Javascript pour la partie front-end
- Python avec SQLite3 pour la création et la gestion de la base de données
- Python avec FastAPI pour la communication entre le site et la base de données
- ChatGPT pour la création du jeu de données

## Structure du projet

- Le dossier **db** contient toute la partie back-end de l'application
- Le dossier **site** qui contient le code du site web (le front-end)


### DB

Divisé en 5 fichiers :
- **bdd.py** : création de la base de données (en l'exécutant) et fonctions qui la modifie directement
- **api.py** : Api FastAPI, reçoit les requêtes et les interprète en utilisant les fonctions de **bdd.py**
- **insertions_donnees.py** : À lancer juste après la création de la BD, insertion d'un jeu de données dans celle-c

## API

La documentation de l'API est disponible à l'adresse suivante :

https://api.biblioinfo.live/docs
