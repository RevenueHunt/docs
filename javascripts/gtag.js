// Dynamically load the Google Tag Manager script
(function() {
  var s = document.createElement('script');
  s.type = 'text/javascript';
  s.async = true;
  s.src = 'https://www.googletagmanager.com/gtag/js?id=G-31VSB4L8T3';
  var x = document.getElementsByTagName('script')[0];
  x.parentNode.insertBefore(s, x);

  s.onload = function() {
      // Initialize the data layer after the script has loaded
      window.dataLayer = window.dataLayer || [];
      function gtag() { dataLayer.push(arguments); }
      gtag('js', new Date());
      gtag('config', 'G-31VSB4L8T3');
  };
})();