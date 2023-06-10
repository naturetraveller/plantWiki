// JavaScript code to handle language switching
document.addEventListener("DOMContentLoaded", function() {
  var urlParams = new URLSearchParams(window.location.search);
  var lang = urlParams.get("lang");
  
  if (lang === "en") {
    // Code zum Anzeigen der englischen Inhalte hier
  } else if (lang === "fr") {
    // Code zum Anzeigen der französischen Inhalte hier
  } else if (lang === "it") {
    // Code zum Anzeigen der italienischen Inhalte hier
  } else {
    // Standardcode zum Anzeigen der deutschen Inhalte hier
  }
});
