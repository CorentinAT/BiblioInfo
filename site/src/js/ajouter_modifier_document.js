// Fonction pour initialiser les listes de rayons, thèmes et genres sur la page en fonction de ce qu'il y a dans la base de données (via l'api)
function initialiserListe(url, idListe, idElement, nomElement) {
  // Requête pour récupérer la liste voulue
  fetch(url, {
    method: 'GET',
    headers: {
      'accept': 'application/json'
    }
  })
  .then(response => response.json())
  .then(data => {
    console.log(data);
    var contentDiv = document.getElementById(idListe);
    let options = "";
    for (var i = 0; i < data.length; i++) {
      if(idListe==="rayons") {
        options = options + `
          <option value=${data[i][idElement]} id=${data[i][idElement]}>${data[i][nomElement]}</option>
        `;
      } else {
        options = options + `
          <div class="elementliste">
            <input type="checkbox" id=${data[i][idElement]}${idListe==="genres"?"genre":"theme"} value=${data[i][idElement]}>
            <label for=${data[i][idElement]}${idListe==="genres"?"genre":"theme"}>${data[i][nomElement]}</label>
          </div>
        `
      }
    }
    contentDiv.innerHTML = options; // Insère les données récupérées dans le code HTML
  })
  .catch(error => {
    console.error('Une erreur s\'est produite:', error);
  });
}

// Fonction pour ajouter les genres sélectionnés au document
function ajouterGenres(idDoc) {
  var fieldset = document.getElementById('genres');
  var checkboxes = fieldset.querySelectorAll('input[type="checkbox"]');

  // Fait une requête de liaison genre-document pour chacun des genres
  checkboxes.forEach(function(checkbox) {
    if (checkbox.checked) {
      fetch(`http://api.biblioinfo.live/document/${idDoc}/add_genre?idGenre=${checkbox.value}`, {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        }
      })
    }
  });
}

// Fonction pour ajouter les thèmes sélectionnés au document
function ajouterThemes(idDoc) {
  var fieldset = document.getElementById('themes');
  var checkboxes = fieldset.querySelectorAll('input[type="checkbox"]');

  // Fait une requête de liaison thème-document pour chacun des thèmes
  checkboxes.forEach(function(checkbox) {
    if (checkbox.checked) {
      fetch(`http://api.biblioinfo.live/document/${idDoc}/add_theme?idTheme=${checkbox.value}`, {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        }
      })
    }
  });
}

// Fonction qui récupère le bouton radio sélectionné, qui indique si l'utilisateur a indiqué que le document était disponible ou non, et renvoie true ou false en fonction
function estDispo() {
  var fieldset = document.getElementById('disponible');
  var radioButtons = fieldset.querySelectorAll('input[type="radio"][name="estdispo"]');

  var disponible = null;
  radioButtons.forEach(function(radioButton) {
    if (radioButton.checked) { // Regarde pour chaque bouton radio s'il est coché
      disponible = radioButton.value;
    }
  });

  if(disponible === "true") {
    disponible = true;
  } else {
    disponible = false;
  }
  return disponible;
}

// Fonction qui affiche un overlay qui indique que le document a été ajouté, avec un lien de redirection vers celui-ci
function afficherOverlayValidation(idDoc) {
  var contentDiv = document.getElementById("overlay");
  var overlay = `
  <div class="case">
    <div class="contenu">
      <p>Opération réussie</p>
      <a href="../pages/page_doc.html?id=${idDoc}"><button>Ok</button></a>
    </div>
  </div>
  `;
  contentDiv.innerHTML = overlay;
}

// Fonction lancée à la validation du formulaire sur la page
function ajouterDoc(event) {
  event.preventDefault();

  // Récupère les éléments du formulaire donnés par l'utilisateur
  const titre = document.getElementById("titre").value;
  const liencouverture = document.getElementById("liencouverture").value;
  const auteur = document.getElementById("auteur").value;
  const description = document.getElementById("description").value;
  const idrayon = document.getElementById("rayons").value;

  let idDoc;

  // Fait une requête à l'api pour ajouter le document selon les informations entrées par l'utilisateur
  fetch('http://api.biblioinfo.live/create_document', {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    titre,
    ...(liencouverture!=="" && {liencouverture}),
    ...(description!=="" && {description}),
    ...(auteur!=="" && {auteur}),
    disponible: estDispo(),
    idrayon
  }),
  mode: 'cors'
})
  .then(response => response.json())
  .then(data => {
    idDoc = data;
    console.log(idDoc);
    ajouterGenres(idDoc); // Ajoute les genres cochés au document
    ajouterThemes(idDoc); // Ajoute les thèmes cochés au document
    return idDoc
  })
  .then(idDoc => {
    afficherOverlayValidation(idDoc); // Affiche l'overlay de validation, avec la redirection
  })
  .catch(error => {
    console.error('Une erreur s\'est produite:', error);
  });
}

function modifierDoc(event) {
  event.preventDefault();

  // Récupère les éléments du formulaire donnés par l'utilisateur
  const titre = document.getElementById("titre").value;
  const liencouverture = document.getElementById("liencouverture").value;
  const auteur = document.getElementById("auteur").value;
  const description = document.getElementById("description").value;
  const idrayon = document.getElementById("rayons").value;

  var urlParams = new URLSearchParams(window.location.search);
  const idDoc = urlParams.get('id');

  // Fait une requête à l'api pour ajouter le document selon les informations entrées par l'utilisateur
  fetch(`http://api.biblioinfo.live/document/${idDoc}/update`, {
    method: 'PUT',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      ...(titre!=="" && {titre}),
      ...(liencouverture!=="" && {liencouverture}),
      ...(description!=="" && {description}),
      ...(auteur!=="" && {auteur}),
      disponible: estDispo(),
      idrayon
    }),
    mode: 'cors'
  })
  .then(response => response.json())
  .then(() => {
    fetch(`http://api.biblioinfo.live/document/${idDoc}/delete_genres_themes`, {
      method: 'DELETE',
      headers: {
        'Accept': 'application/json'
      }
    })
    .then(() => {
      ajouterGenres(idDoc); // Ajoute les genres cochés au document
      ajouterThemes(idDoc); // Ajoute les thèmes cochés au document
    })
  })
  .then(() => {
    afficherOverlayValidation(idDoc); // Affiche l'overlay de validation, avec la redirection
  })
  .catch(error => {
    console.error('Une erreur s\'est produite:', error);
  });
}

async function chargerDoc(documentId) {
  const response = await fetch(`http://api.biblioinfo.live/document/${documentId}`, {
    method: 'GET',
    headers: {
      'accept': 'application/json'
    }
  });
  return await response.json();
}

async function remplir_input(documentId) {
  const dataDocument = await chargerDoc(documentId);
  console.log(dataDocument);
  let zoneSelectionnee = document.getElementById("titre_page");
  zoneSelectionnee.innerHTML = "Modifier le document - "+dataDocument.titre;
  zoneSelectionnee = document.getElementById("titre");
  zoneSelectionnee.value = dataDocument.titre;
  if(dataDocument.auteur) {
    zoneSelectionnee = document.getElementById("auteur");
    zoneSelectionnee.value = dataDocument.auteur;
  }
  if(dataDocument.description) {
    zoneSelectionnee = document.getElementById("description");
    zoneSelectionnee.value = dataDocument.description;
  }
  zoneSelectionnee = document.getElementById("liencouverture");
  zoneSelectionnee.value = dataDocument.liencouverture;
  zoneSelectionnee = document.getElementById("rayons");
  var idrayon = dataDocument.rayon.idrayon;
  var option = zoneSelectionnee.querySelector(`#${idrayon}`);
  option.selected = true;
  if(dataDocument.disponible) {
    zoneSelectionnee = document.getElementById("dispo");
    zoneSelectionnee.checked = true;
  } else {
    zoneSelectionnee = document.getElementById("pasdispo");
    zoneSelectionnee.checked = true;
  }
  cocher_themes_genres(dataDocument);
}

function cocher_themes_genres(dataDocument) {
  var fieldset = document.getElementById('themes');
  var checkboxes = fieldset.querySelectorAll('input[type="checkbox"]');

  checkboxes.forEach(function(checkbox) {
    for(let i=0; i<dataDocument.themes.length; i++) {
      if(checkbox.id===dataDocument.themes[i].idtheme+"theme") {
        checkbox.checked = true;
      }
    }
  });

  var fieldset = document.getElementById('genres');
  var checkboxes = fieldset.querySelectorAll('input[type="checkbox"]');
  checkboxes.forEach(function(checkbox) {
    for(let i=0; i<dataDocument.themes.length; i++) {
      if(checkbox.id===dataDocument.genres[i].idgenre+"genre") {
        checkbox.checked = true;
      }
    }
  });
}

// Initialise les listes de rayon, genres et thèmes au chargement de la page
window.addEventListener('DOMContentLoaded', function() {
  initialiserListe('http://api.biblioinfo.live/rayons', 'rayons', 'idrayon', 'nomrayon');
  initialiserListe('http://api.biblioinfo.live/genres', 'genres', 'idgenre', 'nomgenre');
  initialiserListe('http://api.biblioinfo.live/themes', 'themes', 'idtheme', 'nomtheme');
  var urlParams = new URLSearchParams(window.location.search);
  var documentId = urlParams.get('id');
  if(documentId) {
    remplir_input(documentId);
  }
})