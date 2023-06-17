window.addEventListener('DOMContentLoaded', function () {
    var urlParams = new URLSearchParams(window.location.search);
    var documentId = urlParams.get('id');

    var request = new XMLHttpRequest();
    var url = 'http://api.biblioinfo.live/document/' + documentId;
    request.open('GET', url, true);

    request.onload = function () {
        console.log(documentId);
        if (request.status >= 200 && request.status < 400) {
            var response = JSON.parse(request.responseText);

            var idVal = response.id;
            var noteMoyenneVal = response.note_moyenne;

            titre = document.getElementById("titre");
            titre.textContent = response.titre;

            synopsis = document.getElementById("synopsis");
            synopsis.textContent = response.description;

            genre = document.getElementById("genres");
            var genreText = response.genres.map(function (genre) {
                return genre.nomgenre;
            }).join(", ");
            genre.textContent = genreText;

            auteur = document.getElementById("auteur");
            auteur.textContent = response.auteur;

            themes = document.getElementById("themes");
            var themesText = response.themes.map(function (theme) {
                return theme.nomtheme;
            }).join(", ");
            themes.textContent = themesText;

            disponible = document.getElementById("disponible");
            disponibleTxt = document.getElementById("dispoTxt");
            imageDispo = document.getElementById("logoDispo");
            if (response.disponible) {
                imageDispo.src = "../img/logo_dispo_true.PNG";
                disponibleTxt.textContent = "Disponible";
            } else {
                imageDispo.src = "../img/logo_dispo_false.jpg";
                disponibleTxt.textContent = "Indisponible";
            }

            rayons = document.getElementById("rayons");
            rayons.textContent = response.rayon.nomrayon;

            etage = document.getElementById("etage");
            etage.textContent = response.rayon.etage;

            couverture = document.getElementById("couverture");
            couverture.src = response.liencouverture;

            // Autres manipulations des données
        } else {
            // La requête a échoué
            console.error('Erreur lors de la requête. Statut:', request.status);
        }
    };

    request.onerror = function () {
        // Erreur lors de la requête
        console.error('Erreur lors de la requête.');
    };

    request.send();
});

function modifier() {
  var urlParams = new URLSearchParams(window.location.search);
  var documentId = urlParams.get('id');
  window.location.href = `./modifier_document.html?id=${documentId}`;
}

function supprimer() {
  fetch('http://api.biblioinfo.live/document/37/delete', {
    method: 'DELETE',
    headers: {
      'Accept': 'application/json'
    }
  }).then(() => {window.location.href="../../index.html"});
}