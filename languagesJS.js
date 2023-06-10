// Get the current language from the HTML tag
const currentLanguage = document.documentElement.lang;

// Get all language links in the navigation bar
const languageLinks = document.querySelectorAll('.navbar a[href^="index_"]');

// Loop through each language link
languageLinks.forEach(link => {
  // Get the language code from the link's href attribute
  const languageCode = link.getAttribute('href').split('_')[1].split('.')[0];

  // Add the 'active' class to the current language link
  if (languageCode === currentLanguage) {
    link.classList.add('active');
  }
});

// Get the current page's hash
const currentHash = window.location.hash;

// Get all page links in the navigation bar
const pageLinks = document.querySelectorAll('.navbar a[href^="#"]');

// Loop through each page link
pageLinks.forEach(link => {
  // Add the 'active' class to the current page link
  if (link.getAttribute('href') === currentHash) {
    link.classList.add('active');
  }
});
