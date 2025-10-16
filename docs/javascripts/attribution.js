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
        if (hostname.indexOf('duckduckgo.') !== -1) { return 'duckduckgo'; }
        if (hostname.indexOf('baidu.') !== -1) { return 'baidu'; }
        if (hostname.indexOf('yandex.') !== -1) { return 'yandex'; }
        return null;
    }

    function getDeviceType() {
        const ua = navigator.userAgent;
      
        if (/mobile/i.test(ua)) return "mobile";
        if (/tablet|ipad|playbook|silk/i.test(ua)) return "tablet";
        return "desktop";
    }

    function getBrowser() {
        const ua = navigator.userAgent;
      
        if (ua.includes("Chrome") && !ua.includes("Edg") && !ua.includes("OPR")) return "Chrome";
        if (ua.includes("Edg")) return "Edge";
        if (ua.includes("Firefox")) return "Firefox";
        if (ua.includes("Safari") && !ua.includes("Chrome")) return "Safari";
        if (ua.includes("OPR") || ua.includes("Opera")) return "Opera";
        if (ua.includes("Brave")) return "Brave";
      
        return "Unknown";
    }

    function getOS() {
        const ua = navigator.userAgent || navigator.vendor || window.opera;
      
        if (/windows phone/i.test(ua)) return "Windows Phone";
        if (/win/i.test(ua)) return "Windows";
        if (/android/i.test(ua)) return "Android";
        if (/linux/i.test(ua)) return "Linux";
        if (/iPad|iPhone|iPod/.test(ua) && !window.MSStream) return "iOS";
        if (/Macintosh|MacIntel|MacPPC|Mac68K/i.test(ua)) return "macOS";
      
        return "Unknown";
    }

    function getSystemTimezone() {
        const tz = Intl.DateTimeFormat().resolvedOptions().timeZone;
        const offset = -new Date().getTimezoneOffset() / 60;
        const sign = offset >= 0 ? '+' : '';
        return `${tz} (UTC${sign}${offset})`;
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
            landing: window.location.pathname + window.location.search,
            device: getDeviceType(),
            browser: getBrowser(),
            os: getOS(),
            timezone: getSystemTimezone(),
            language: (navigator.language || navigator.userLanguage).split('-')[0],
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
        var existingRaw = getCookie('revenuehunt_attribution');
        if (existingRaw) { return; }
        var current = buildAttribution();
        setCookie('revenuehunt_attribution', JSON.stringify(current), 180);
    }

    if (!getCookie('revenuehunt_attribution')) { captureMarketingAttribution(); }
})();
/* end of the code for the marketing attribution */