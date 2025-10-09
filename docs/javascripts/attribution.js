/* this is the code for the marketing attribution */
(function() {
  if (typeof window === 'undefined' || typeof document === 'undefined') { return; }

  function parseQueryParams(queryString) {
      const params = new URLSearchParams(queryString || window.location.search);
      var result = {};
      params.forEach(function(value, key) {
          result[key] = value;
      });
      return result;
  }

  function detectSearchEngine(hostname) {
      hostname = hostname || '';
      if (hostname.indexOf('google.') !== -1) { return 'google'; }
      if (hostname.indexOf('bing.') !== -1) { return 'bing'; }
      if (hostname.indexOf('yahoo.') !== -1) { return 'yahoo'; }
      if (hostname.indexOf('duckduckgo.') !== -1 || hostname.indexOf('duckduckgo.com') !== -1) { return 'duckduckgo'; }
      if (hostname.indexOf('baidu.') !== -1) { return 'baidu'; }
      if (hostname.indexOf('yandex.') !== -1) { return 'yandex'; }
      return null;
  }

  function buildAttribution() {
      var qs = parseQueryParams(window.location.search);
      var hasUtm = qs.utm_source || qs.utm_medium || qs.utm_campaign || qs.utm_term || qs.utm_content;
      var hasAdClickId = qs.gclid || qs.fbclid || qs.msclkid || qs.dclid || qs.twclid || qs.wbraid || qs.gbraid;
      var referrer = document.referrer || '';
      var refHost = '';
      try {
          refHost = referrer ? (new URL(referrer)).hostname : '';
      } catch (e) {
          refHost = '';
      }
      var searchEngine = detectSearchEngine(refHost);

      var source = '';
      var medium = '';
      var campaign = qs.utm_campaign || '';
      var term = qs.utm_term || '';
      var content = qs.utm_content || '';

      if (hasUtm) {
          source = qs.utm_source || '';
          medium = qs.utm_medium || (hasAdClickId ? 'cpc' : '');
      } else if (hasAdClickId) {
          if (qs.gclid || qs.gbraid || qs.wbraid) { source = 'google'; medium = 'cpc'; }
          else if (qs.msclkid) { source = 'microsoft'; medium = 'cpc'; }
          else if (qs.fbclid) { source = 'facebook'; medium = 'paid_social'; }
          else { source = 'paid'; medium = 'cpc'; }
          if (!campaign) { campaign = '(not set)'; }
      } else if (referrer) {
          if (searchEngine) {
              source = searchEngine;
              medium = 'organic';
          } else {
              source = refHost || 'referral';
              medium = 'referral';
          }
      } else {
          source = 'direct';
          medium = 'direct';
      }

      return {
          source: source || '(not set)',
          medium: medium || '(not set)',
          campaign: campaign || '(not set)',
          term: term || '',
          content: content || '',
          referrer: referrer,
          landingPage: window.location.pathname + window.location.search,
          timestamp: new Date().toISOString()
      };
  }

  function setCookie(name, value, days) {
      var date = new Date();
      var expires = '';
      if (days) {
          date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
          expires = '; expires=' + date.toUTCString();
      }
      var domainAttr = '';
      var host = window.location.hostname || '';
      if (host === 'revenuehunt.com' || (typeof host.endsWith === 'function' && host.endsWith('.revenuehunt.com'))) {
          domainAttr = '; domain=.revenuehunt.com';
      }
      var cookie = name + '=' + encodeURIComponent(value) + expires + '; path=/' + domainAttr + '; SameSite=Lax';
      if (window.location.protocol === 'https:') {
          cookie += '; Secure';
      }
      document.cookie = cookie;
  }

  function getCookie(name) {
      var nameEQ = name + '=';
      var ca = document.cookie.split(';');
      for (var i = 0; i < ca.length; i++) {
          var c = ca[i];
          while (c.charAt(0) === ' ') { c = c.substring(1, c.length); }
          if (c.indexOf(nameEQ) === 0) { return decodeURIComponent(c.substring(nameEQ.length, c.length)); }
      }
      return null;
  }

  function captureMarketingAttribution() {
      var current = buildAttribution();
      var existingRaw = getCookie('revenuehunt_attribution');
      var payload;
      if (existingRaw) {
          try {
              var existing = JSON.parse(existingRaw);
              payload = {
                  firstTouch: existing.firstTouch || current,
                  lastTouch: current
              };
          } catch (e) {
              payload = { firstTouch: current, lastTouch: current };
          }
      } else {
          payload = { firstTouch: current, lastTouch: current };
      }

      setCookie('revenuehunt_attribution', JSON.stringify(payload), 180);
  }

  window.getMarketingAttribution = function() {
      var raw = getCookie('revenuehunt_attribution');
      if (!raw) { return null; }
      try { return JSON.parse(raw); } catch (e) { return null; }
  };

  if (!getCookie('revenuehunt_attribution')) { captureMarketingAttribution(); }
})();
/* end of the code for the marketing attribution */