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

window.addEventListener('DOMContentLoaded', function() {
  initialiserGenres();
})