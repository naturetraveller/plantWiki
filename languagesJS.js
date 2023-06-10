// Function to add the 'active' class to the active language link
function highlightActiveLanguage() {
  const currentLanguage = document.documentElement.lang;
  const languageLinks = document.querySelectorAll('.navbar a[href^="index_"]');
  
  languageLinks.forEach(link => {
    const languageCode = link.getAttribute('href').split('_')[1].split('.')[0];
    if (languageCode === currentLanguage) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });
}

// Function to add the 'active' class to the active page link
function highlightActivePage() {
  const currentHash = window.location.hash;
  const pageLinks = document.querySelectorAll('.navbar a[href^="#"]');
  
  pageLinks.forEach(link => {
    if (link.getAttribute('href') === currentHash) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });
}

// Call the functions to highlight the active language and active page on page load
highlightActiveLanguage();
highlightActivePage();
