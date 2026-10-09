// tawk.to live chat. Property 673f3f364304e3196ae673ec, widget 1jpn75t6m - the
// same widget the merchant CRM and revenuehunt.com load, so every conversation
// lands in one inbox. Widget content is configured in the tawk dashboard.
//
// extra_javascript renders outside [data-md-component=container], so
// navigation.instant does not re-run this; the guard is cheap insurance.
// Tawk_API/Tawk_LoadStart go on window explicitly - the embed script reads
// them as globals and must not find them trapped in a function scope.
if (!window.Tawk_API) {
  window.Tawk_API = {};
  window.Tawk_LoadStart = new Date();

  (function() {
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://embed.tawk.to/673f3f364304e3196ae673ec/1jpn75t6m';
    s.charset = 'UTF-8';
    s.setAttribute('crossorigin', '*');
    var x = document.getElementsByTagName('script')[0];
    x.parentNode.insertBefore(s, x);
  })();
}
