---
icon: material/wordpress
---

# Troubleshooting Product Recommendation Quiz App Issues for WordPress / WooCommerce

Our Product Recommendation Quiz app is designed to integrate seamlessly with most e-commerce stores. However, due to the high level of customization in WordPress / WooCommerce stores, conflicts with other plugins or store settings can occasionally arise, impacting the app’s functionality. This guide aims to address common issues and provide clear solutions.

!!! tip "General Troubleshooting Tip"
    
    If you’ve exhausted all listed solutions without success, it may be due to specific configurations in your website. In such cases, consult your developer or hosting provider and review server logs for potential clues. Unfortunately, our capacity to assist is limited in these scenarios.

!!! warning

    Important Addition: Ensure to whitelist our IP address (`3.14.55.225`) in your store’s settings to facilitate uninterrupted communication between our app and your store.

## Error #1: Request and Data Transmission Issues

!!! example "Error Messages"

    An error occurred in the request and at the time were unable to send the consumer data.

    We tried checking the connection with your WooCommerce API, but was unsuccessful.

    We tried fetching the product varaitions via the WooCommerce API, but was unsuccessful.

    We tried connecting to your WooCommerce API to sync the “products, but got a status 403.

Possible Causes and Solutions:

1. **Outdated WooCommerce Version**: Ensure your store is running a version later than WooCommerce 3.5.
2. **Outdated Plugin Version**: Ensure you’ve downloaded the latest version of the app.
3. **Lack of HTTPS/SSL Certificate**: Install and activate a valid certificate for secure API communication.
4. **Website Accessibility**: Remove password protection or ‘coming soon’ plugins that restrict public access.
5. **Caching Plugin Interference**: Disable caching plugins one by one to identify the culprit.
6. **Server Configuration**: If the above don’t resolve the issue, your server might be stripping the “Authorization” header.
7. **Check Security Settings**: Review your store’s and hosting security settings to ensure they aren’t conflicting with the app.
8. **Disable Other Plugins**: Temporarily deactivate other plugins and try granting access to our app to see if they are causing a conflict.
9. **Cloudflare Cache**: Exclude the WooCommerce API endpoint (/wp-json/wc/v3/) from Cloudflare’s cache. Alternatively, use Cloudflare’s developer mode to bypass the cache temporarily. (Source: https://developers.cloudflare.com/cache/)

![how to troubleshoot wordpress woocommerce image1](/images/how to troubleshoot wordpress woocommerce image1.webp)

Advanced Solutions:

1. Review caching plugin settings related to headers.
2. Generate a new LetsEncrypt certificate.
3. Direct subdomain to bypass Cloudflare CDN Proxy.
4. Switch to a basic WooCommerce Theme like “Storefront” for initial connection.
5. Add to .htaccess: `SetEnvIf Authorization "(.*)" HTTP_AUTHORIZATION=$1`.

**Special Note**: If using CAFE24 hosting, disable the “SPAM Shield” function.

## Error #2: Authentication and Permission Issues

!!! example "Error Messages"

    It seems that something is interfering with your WordPress Rest API. This needs to be fixed in order to grant access to this plugin.

    Missing parameter app_name

    404 Not Found – the requested URL was not found on this server

Possible Causes and Solutions:

1. **WPML or Polylang Plugin Conflict**: Temporarily deactivate WPML/Polylang, authenticate our plugin, then reactivate WPML/Polylang. (As of November 2024, Polylang and Product Recommendation Quiz app cannot be used together.)
2. **Incorrect Callback URL**: Replace `%2F` with `/` in the URL, or remove extra /wp/ from the URL.
3. **Installation Location**: For WooCommerce on a subpage, adjust the URL accordingly (remove /page/). So, instead of `https://yourstore.com/shop/wc-auth/v1/authorize/...` You would use `https://yourstore.com/wc-auth/v1/authorize/...` Even if the first URL is the right path to your WooCommerce store.
4. **Website is not live**: Ensure installation on a live, publicly accessible website. It cannot be hidden by an “under construction” plugin or setting. The app does not work in local environments.
5. **Check WordPress REST API**: To test it visit  `https://yourstore.com/wp-json/`. If you’re getting a “Not Found” or similar error, it’s possible that you need to fix your WordPress installation. It’s a problem with the WordPress REST API in your site and not with the WooCommerce REST API. You’ll have to contact your developer to further investigate this issue as it’s outside of our scope.

!!! example "Error Messages"

    The following REST API endpoint is returning a valid JSON but the returned content-type is text/html instead of the expecred application/json.

Possible Causes and Solutions:

1. **Check JSON format**. This means that even if your site returns a JSON it may not be in the correct format. The WordPress API is returning a response that is encoded as text/html. Normally, it should be application/json.   This is related to your store or server settings, but can also be influenced by another plugin. It is recommended to check it with your developer and fix it.

![how to troubleshoot wordpress woocommerce image2](/images/how to troubleshoot wordpress woocommerce image2.jpg)

!!! example "Error Messages"

    Plugin could not be activated because it triggered a fatal error. Fatal error: Cannot redeclare prq_set_token() (previously declared in…)

Possible Causes and Solutions:

1. **Duplicate Plugin Activation**: Deactivate the existing WordPress Plugin (Product recommendation Quiz for eCommerce) before activating the WooCommerce extension (Product Recommendation Quiz for WooCommerce). Don’t worry, you won’t lose any data because your quizzes and responses are stored in our server.

![how to troubleshoot wordpress woocommerce image3](/images/how to troubleshoot wordpress woocommerce image3.png)

!!! example "Error Messages"

    The plugin does not have a valid header

Possible Causes and Solutions:

1. **Plugins cached**: Your list of Plugins could be cached in whatever WP Object Cache your blog / site is using. (Source: [https://scotty-t.com/2011/03/28/fix-for-the-plugin-does-not-have-a-valid-header/](https://scotty-t.com/2011/03/28/fix-for-the-plugin-does-not-have-a-valid-header/))
2. **Check the Correct Folder Structure**: Ensure that the plugin’s main file is placed correctly in the wp-content/plugins/ directory.
3. **Modify PHP File Headers**: If the headers of PHP files within the plugin resemble the mandatory header of the main plugin file, it can confuse WordPress. Modifying these headers to a different format can resolve the issue. (Source: [https://chattymango.com/how-fix-wordpress-error-plugin-not-valid-header/](https://chattymango.com/how-fix-wordpress-error-plugin-not-valid-header/))
4. **Remove /trunk directory**: Remove `/trunk` directory or activate from the plugin list. (Source: [https://wordpress.org/support/topic/the-plugin-does-not-have-a-valid-header-solution/](https://wordpress.org/support/topic/the-plugin-does-not-have-a-valid-header-solution/))
5. **Outdated Plugin Version**: Ensure you’ve downloaded the latest version of the app.
6. **Two Plugins Installed**: Deactivate and remove the WooCommerce extension before installing the WordPress plugin (or vice versa).
 

---
If you’ve exhausted all listed solutions without success, it may be due to specific configurations in your website. In such cases, consult your developer or hosting provider and review server logs for potential clues. Unfortunately, our capacity to assist is limited in these scenarios.
