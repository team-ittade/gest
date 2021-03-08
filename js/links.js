function addTargetBlank() {
  document.querySelectorAll(".external-link").forEach((link) => {
    link.setAttribute("target", "_blank");
  });
}

function replaceClass() {
  document.querySelectorAll(".elink").forEach((link) => {
    link.classList.remove("elink");
    link.classList.add("external-link");
  });
}

function updateLinks() {
  replaceClass();
  addTargetBlank();
}

updateLinks();
