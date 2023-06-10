// Get the current URL path
var path = window.location.pathname;

// Get the language code from the URL
var langCode = path.substring(path.lastIndexOf('_') + 1, path.lastIndexOf('.'));

// Find the corresponding language link and add the 'active' class
var languageLinks = document.querySelectorAll('.navbar a');
languageLinks.forEach(function(link) {
  var linkLangCode = link.href.substring(link.href.lastIndexOf('_') + 1, link.href.lastIndexOf('.'));
  if (linkLangCode === langCode) {
    link.classList.add('active');
  }
});
