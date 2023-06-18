// Fonction pour récupérer les genres de la base de données et les mettre dans la liste de cases à cocher
function initialiserGenres() {
  // Requête pour récupérer la liste des genres
  fetch("http://api.biblioinfo.live/genres", {
    method: 'GET',
    headers: {
      'accept': 'application/json'
    }
  })
  .then(response => response.json())
  .then(data => {
    console.log(data);
    var contentDiv = document.getElementById("genres");
    let options = "";
    for (var i = 0; i < data.length; i++) {
      options = options + `
        <div class="elementliste">
          <input type="checkbox" id=${data[i]["idgenre"]} value=${data[i]["idgenre"]}>
          <label for=${data[i]["idgenre"]}>${data[i]["nomgenre"]}</label>
        </div>
      `
    }
    contentDiv.innerHTML = options;
  })
  .catch(error => {
    console.error('Une erreur s\'est produite:', error);
  });
}

// Fonction qui récupère le titre entré et les genres cochés, et qui renvoie vers la page de resultats de recherche avec les paramètres correspondants
function recherche(event) {
  event.preventDefault();
  const checkboxes = document.querySelectorAll('input[type="checkbox"]:not(#checkboxGenres):checked');
  const titre = document.getElementById("titre").value;
  
  if (checkboxes.length > 0) {
    const checkedIds = [];
    checkboxes.forEach((checkbox) => {
      checkedIds.push(checkbox.id);
    });
    const queryString = checkedIds.join('&');
    window.location.href = `../pages/res_de_rech.html?titre=${titre}&${queryString}`;
  } else {
    window.location.href = `../pages/res_de_rech.html?titre=${titre}`;
  }
}

window.addEventListener('DOMContentLoaded', function() {
  initialiserGenres();
})