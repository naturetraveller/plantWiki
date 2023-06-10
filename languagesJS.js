// Get the current language from the HTML lang attribute
const currentLanguage = document.documentElement.lang;

// Find the corresponding language button and add the "active" class
const languageButtons = document.querySelectorAll(".navbar a");
languageButtons.forEach(button => {
  const buttonLanguage = button.getAttribute("href").replace(".html", "");
  if (buttonLanguage === currentLanguage) {
    button.classList.add("active");
  }
});
