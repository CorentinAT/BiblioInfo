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
    contentDiv.innerHTML = options; // Insère les données récupérées dans le code HTML
  })
  .catch(error => {
    console.error('Une erreur s\'est produite:', error);
  });
}

function recherche(event) {
  event.preventDefault();
  
  // Récupérer toutes les cases cochées
  const checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');

  const titre = document.getElementById("titre").value;
  
  // Vérifier s'il y a des cases cochées
  if (checkboxes.length > 0) {
    // Créer un tableau pour stocker les identifiants des cases cochées
    const checkedIds = [];
    
    // Parcourir les cases cochées et récupérer leurs identifiants
    checkboxes.forEach((checkbox) => {
      checkedIds.push(checkbox.id);
    });
    
    // Convertir les identifiants en une chaîne de requête
    const queryString = checkedIds.join('&');
    
    // Modifier la valeur de window.location.href avec les paramètres de la requête
    window.location.href = `../pages/res_de_rech.html?titre=${titre}&${queryString}`;
  } else {
    // Aucune case cochée, rediriger sans paramètres
    window.location.href = "../pages/res_de_rech.html";
  }
}

window.addEventListener('DOMContentLoaded', function() {
  initialiserGenres();
})