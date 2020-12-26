const form = document.querySelector("form");

form.addEventListener("submit", function (event) {
  event.preventDefault();
  const data = new FormData(form);

  fetch("/ajax", {
    method: "POST",
    body: data,
  })
    .then((response) => response.json())
    .then((data) => {
      //Ajouter la question de l'utilisateur dans le chatbox
      console.log();

      const para = document.createElement("p");

      const intro = document.createTextNode("Voici votre petite histoire:");
      const guest = document.createTextNode("Vous avez posé une question sur:");
      const title = document.createTextNode(data.title);
      const question = document.createTextNode(data.question);
      const extract = document.createTextNode(data.article);
      const url = document.createTextNode(data.url);

      const lat = document.createTextNode(data.lat);
      const lng = document.createTextNode(data.lng);

      para.appendChild(intro)
      para.appendChild(guest);
      para.appendChild(title);
      para.appendChild(extract);
      para.appendChild(question);

      para.appendChild(lat);
      para.appendChild(lng);

      const elementIntro = document.getElementById("bot-intro");
      const elementGuest = document.getElementById("bot-guest");
      const elementTitle = document.getElementById("bot-title");
      const elementExtract = document.getElementById("bot-extract");
      const elementUrl = document.getElementById("bot-url");
      const elementQuestion = document.getElementById("guest-question");
      
      const elementLat = document.getElementById("lat");
      const elementLng = document.getElementById("lng");

      elementIntro.appendChild(intro)
      elementTitle.appendChild(title);
      elementGuest.appendChild(guest);
      elementExtract.appendChild(extract);
      elementUrl.appendChild(url);
      elementQuestion.appendChild(question);

      elementLat.appendChild(lat);
      elementLng.appendChild(lng);

      
      
    });
});
