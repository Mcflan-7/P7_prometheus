function myFunction() {}
const form = document.querySelector("form");

const spinner = document.getElementById("spinner");

form.addEventListener("submit", function (event) {
  event.preventDefault();
  const data = new FormData(form);
  spinner.removeAttribute("hidden");
  fetch("/ajax", {
    method: "POST",
    body: data,
  })
    .then((response) => response.json())
    .then((data) => {
      //Ajouter la question de l'utilisateur dans le chatbox
    spinner.setAttribute("hidden", "");

       var a = document.createElement("p");
       a.setAttribute("class", "chat-header");
       var linkText = document.createTextNode(
         `Notre petit robot a detecté que vous souhaitiez une information sur: ${data.question}`
       );
       a.appendChild(linkText);
       document.body.appendChild(a);



      var a = document.createElement("h3");
      a.setAttribute("class", "chat-header");
      var linkText = document.createTextNode(`Voici une histoire sur: ${data.title}`);
      a.appendChild(linkText);
      document.body.appendChild(a);

      var a = document.createElement("p");
      var linkText = document.createTextNode(data.article);
      a.setAttribute("class", "msg-box");
      a.appendChild(linkText);
      document.body.appendChild(a);

   var a = document.createElement("a");
   var linkText = document.createTextNode("En savoir plus");
   a.setAttribute("class", "msg-box");
   a.appendChild(linkText);

   a.title = "En savoir plus";
   a.href = data.url;
   document.body.appendChild(a);
      
      var ifrm = document.createElement("iframe");
      ifrm.setAttribute("class", "msg-box");
      ifrm.setAttribute(
        "src",
        `https://www.google.com/maps/embed/v1/view?key=AIzaSyCbn1GQVOld0hvqZI4GmN5vlHunZHWO_DY&center=${data.lat},${data.lng}&zoom=18&maptype=satellite`
      );

      ifrm.style.width = "640px";
      ifrm.style.height = "480px";
      ifrm.style.height = "480px";

      document.body.appendChild(ifrm);


      

      var a = document.createElement("hr");
      var linkText = document.createTextNode("Message suivant");
      a.setAttribute("id", "msg-box");
      a.appendChild(linkText);
      document.body.appendChild(a);


    });
  
  
});


function loadData() {
  
  fetch("https://www.mocky.io/v2/5185415ba171ea3a00704eed?mocky-delay=5000ms")
    .then((response) => response.json())
    .then((data) => {
      spinner.setAttribute("hidden", "");
      console.log(data);
    });
}


