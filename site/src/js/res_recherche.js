// Au chargement de la page, pré-rempli le titre recherché, puis fait la requête de recherche
window.addEventListener('DOMContentLoaded', function() {
  const urlParams = new URLSearchParams(window.location.search);
  let titre = urlParams.get("titre");

  inputTitre = document.getElementById("titre");
  inputTitre.value = titre;

  titre = titre.replace(/ /g, "%20");
  const autresParametres = [];
  urlParams.forEach((value, key) => {
    if (key !== "titre") {
      autresParametres.push(key);
    }
  });
  let url = `http://api.biblioinfo.live/search_documents_by_title_genres?titre=${titre}&doitEtreDispo=false`;
  autresParametres.forEach(genre => {
    url += `&idGenre=${genre}`;
  });
  console.log(url);
  fetch(url, {
    method: 'GET',
    headers: {
      'accept': 'application/json'
    }
  }).then(response => response.json())
  .then(data => {
    afficherRes(data);
  });
})

// Fonction qui affiche sur la page la liste des livres trouvés avec la recherche
function afficherRes(listeRes) {
  const div = document.getElementById("listecases");
  let cases = "";
  listeRes.forEach(doc => {
    cases += `<a class="case" href="./page_doc.html?id=${doc.id}">`;
    if(doc.disponible) {
      cases += "<img class='img_dispo' src='../img/logo_dispo_true.PNG'>"
    } else {
      cases += "<img class='img_dispo' src='../img/logo_dispo_false.PNG'>"
    }
    cases += `
      <img src=${doc.liencouverture} class="case-image">
      <span class="case-text">${doc.titre}</span>
      <span class="case-text">${doc.auteur}</span>
      </a>
    `
  });
  if(listeRes.length === 0) {
    cases += '<p>Aucun document ne correspond à la recherche</p>'
  }
  div.innerHTML = cases;
  cocherGenres();
}

// Les genres recherchés sont pré-cochés dans les filtres
function cocherGenres() {
  const urlParams = new URLSearchParams(window.location.search);
  urlParams.forEach((value, key) => {
    if (key !== "titre") {
      checkbox = document.getElementById(key);
      checkbox.checked = true;
    }
  });
}