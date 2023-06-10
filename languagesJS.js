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


// Get the language navbar links
const languageLinks = document.querySelectorAll('.language-navbar a');

// Add click event listener to each language link
languageLinks.forEach(link => {
  link.addEventListener('click', function(event) {
    // Remove 'active' class from all language links
    languageLinks.forEach(link => {
      link.classList.remove('active');
    });

    // Add 'active' class to the clicked language link
    this.classList.add('active');
  });
});
