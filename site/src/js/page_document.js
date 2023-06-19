//Chargement de la page
window.addEventListener('DOMContentLoaded', function () {
  var urlParams = new URLSearchParams(window.location.search);
  var documentId = urlParams.get('id');

  //Requête XML vers BD
  var request = new XMLHttpRequest();
  var url = 'http://api.biblioinfo.live/document/' + documentId;
  request.open('GET', url, true);

  //Récupérations des variables de la requête
  request.onload = function () {
    console.log(documentId);
    if (request.status >= 200 && request.status < 400) {
      var response = JSON.parse(request.responseText);

      //Note du document
      var idVal = response.id;
      var noteMoyenneVal = response.note_moyenne;

      //Affichage de la note moyenne sous forme d'étoiles
      etoiles = document.getElementById("etoiles");
      let i = 0;
      imagesEtoiles = "";
      for (i; i < Math.round(noteMoyenneVal); i++) {
        imagesEtoiles += "<img id='etoile_pleine' class='note' src='../img/etoile_pleine.png' alt='' />"
      }
      for (i; i < 5; i++) {
        imagesEtoiles += "<img id='etoile_vide' class='note' src='../img/etoile_vide.png' alt='' />"
      }
      etoiles.innerHTML = imagesEtoiles;

      //Titre
      titre = document.getElementById("titre");
      titre.textContent = response.titre;

      //Synopsis
      synopsis = document.getElementById("synopsis");
      synopsis.textContent = response.description;

      //Genre(s)
      genre = document.getElementById("genres");
      var genreText = response.genres.map(function (genre) {
        return genre.nomgenre;
      }).join(", ");
      genre.textContent = genreText;

      //Auteur
      auteur = document.getElementById("auteur");
      auteur.textContent = response.auteur;

      //Theme(s)
      themes = document.getElementById("themes");
      var themesText = response.themes.map(function (theme) {
        return theme.nomtheme;
      }).join(", ");
      themes.textContent = themesText;

      //Disponibilité et affichage logo dispo
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

      //Rayon
      rayons = document.getElementById("rayons");
      rayons.textContent = response.rayon.nomrayon;

      //Num étage
      etage = document.getElementById("etage");
      etage.textContent = response.rayon.etage;

      //Lien couverture
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

//Modification du document
function modifier() {
  var urlParams = new URLSearchParams(window.location.search);
  var documentId = urlParams.get('id');
  window.location.href = `./modifier_document.html?id=${documentId}`;
}

//Supprimer le document
function supprimer() {
  var urlParams = new URLSearchParams(window.location.search);
  var documentId = urlParams.get('id');
  fetch(`http://api.biblioinfo.live/document/${documentId}/delete`, {
    method: 'DELETE',
    headers: {
      'Accept': 'application/json'
    }
  }).then(() => {window.location.href="../pages/res_de_rech.html?titre="});
}

//Noter le document
function noter() {
  var urlParams = new URLSearchParams(window.location.search);
  var documentId = urlParams.get('id');
  const boutonsRadio = document.getElementsByName('note');
  let note = null;
  //Récupérer la note
  boutonsRadio.forEach((bouton) => {
    if (bouton.checked) {
      note = bouton.value;
    }
  });
  //Envoyer la note à la BD
  fetch('http://api.biblioinfo.live/create_note', {
    method: 'POST',
    headers: {
      'accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      "note": note,
      "iddoc": documentId
    })
  })
    //Recharger la page
    .then(() => {
      window.location.reload();
    })
}