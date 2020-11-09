/* Main JS for P7 - https://github.com/Mcflan-7/P7_prometheus  */
"use strict";

// MODAL SETTINGS

const modal = document.querySelector(".modal");
const overlay = document.querySelector(".overlay");
const btnCloseModal = document.querySelector(".close-modal");
const btnsOpenModal = document.querySelectorAll(".show-modal");

const openModal = function () {
  modal.classList.remove("hidden");
  overlay.classList.remove("hidden");
};

const closeModal = function () {
  modal.classList.add("hidden");
  overlay.classList.add("hidden");
};

for (let i = 0; i < btnsOpenModal.length; i++)
  btnsOpenModal[i].addEventListener("click", openModal);

btnCloseModal.addEventListener("click", closeModal);
overlay.addEventListener("click", closeModal);

document.addEventListener("keydown", function (e) {
  // console.log(e.key);

  if (e.key === "Escape" && !modal.classList.contains("hidden")) {
    closeModal();
  }
});

// Hamburger menu

function displayMenu() {
  const burgerMenu = document.getElementById("myLinks");
  if (burgerMenu.style.display === "block") {
    burgerMenu.style.display = "none";
  } else {
    burgerMenu.style.display = "block";
  }
}
