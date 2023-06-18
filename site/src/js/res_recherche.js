window.addEventListener('DOMContentLoaded', function() {
  const urlParams = new URLSearchParams(window.location.search);
  let titre = urlParams.get("titre");
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
