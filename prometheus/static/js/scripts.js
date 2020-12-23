/* Main JS for P7 - https://github.com/gaetangr/P7_prometheus  */
"use strict";


let form = document.querySelector("#user-text-form");

function postFormData(url, data) {
  return;
  // Envoyer contenu formulaire au serveur
  fetch(url, {
    method: "POST",
    body: data,
  })
    .then((response) => response.json())
    .catch((error) => console.log(error));
}

form.addEventListener("submit", function (event) {
  event.preventDefault();

  // Envoyer contenu formulaire au serveur
  postFormData("/ajax", new FormData(form)).then((response) => {
    console.log(response);
  });
});
