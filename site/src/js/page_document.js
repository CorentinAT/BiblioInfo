window.addEventListener('DOMContentLoaded', function () {
    fetch('http://api.biblioinfo.live/document/11')
        .then(response => response.json()) // ou response.text() pour récupérer le corps de la réponse en tant que texte
        .then(data => {
            // Utilisez les données de la réponse ici
            console.log(data);
        })
        .catch(error => {
            // Gérez les erreurs ici
            console.error('Erreur :', error);
        });

    // Extraire le titre de la réponse JSON
    var titre = data.titre;
    var paragraph = document.getElementById('titre');
    paragraph.textContent = titre;


    // Utiliser la variable "titre" comme vous le souhaitez
    console.log(titre); // Affiche "Les Trois Mousquetaires"
})