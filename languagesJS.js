// Get the current language from the HTML lang attribute
const currentLanguage = document.documentElement.lang;

// Find the language buttons and add the "active" class to the current language button
const languageButtons = document.querySelectorAll(".navbar a");
languageButtons.forEach(button => {
  const buttonLanguage = button.getAttribute("href").replace(".html", "");
  if (buttonLanguage === currentLanguage) {
    button.classList.add("active");
  } else {
    button.classList.remove("active");
  }
});
