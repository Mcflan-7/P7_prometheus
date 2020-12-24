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

      const title = document.createTextNode(data.title);
      const question = document.createTextNode(data.question);
      const extract = document.createTextNode(data.article);
      const url = document.createTextNode(data.url);
      para.appendChild(title);
      para.appendChild(extract);
      para.appendChild(question);

      const elementTitle = document.getElementById("bot-title");
      const elementExtract = document.getElementById("bot-extract");
      const elementUrl = document.getElementById("bot-url");
      const elementQuestion = document.getElementById("guest-question");

      elementTitle.appendChild(title);
      elementExtract.appendChild(extract);
      elementUrl.appendChild(url);
      elementQuestion.appendChild(question);
    });
});
