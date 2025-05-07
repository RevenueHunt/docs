# App Settings - Store Settings

## General

=== "Shopify"

    ![app settings general](/images/manual_appsettings_general.png)

    **Your Profile**

    **Shop email** - Your main store contact email. We automatically update this email each time we sync your store. You can change this email in your store settings (not the app).

    **Your best email** -  Provide your best email (not your store email) for communication in case of issues.

    **Send notifications to email** - Toggle the button to activate the notification emails to your best email. Once active we will send the notifications that appear on the dashboard to your best email. For example, in case you go over your plan's limits, CSV export completions or connection issues.

    **Data & GDPR**

    **Anonymize quiz respones after 30 days** - Some jurisdictions require merchants to delete any Personal Identifiable Information (PII) they hold from customers upon request. To comply with GDPR legislation, you can choose to anonymize all of your quiz responses by automatically deleting any Personal Identifiable Information from the responses 30 days after being collected. To activate this setting toggle the icon.

=== "Shopify V2"

    Navigate to the Settings tab in the app.

    ![manual_shopifyV2_appsettings](/images/manual_shopifyV2_appsettings.png)

    From the Store settings menu you can:
    
    - Assign quizzes to different markets and languges via the [Shopify Markets](#markets) tab.
    - Run a catalog sync from the [Catalogue](#catalogue) tab or check when the last sync was completed.
    - Provide your email [SMTP scredentials](#smtp) to send result emails from your email provider.

=== "WooCommerce"

    ![app settings general](/images/manual_appsettings_general.png)

    **Your Profile**

    **Shop email** - Your main store contact email. We automatically update this email each time we sync your store. You can change this email in your store settings (not the app).

    **Your best email** -  Provide your best email (not your store email) for communication in case of issues.

    **Send notifications to email** - Toggle the button to activate the notification emails to your best email. Once active we will send the notifications that appear on the dashboard to your best email. For example, in case you go over your plan's limits, CSV export completions or connection issues.

    **Data & GDPR**

    **Anonymize quiz respones after 30 days** - Some jurisdictions require merchants to delete any Personal Identifiable Information (PII) they hold from customers upon request. To comply with GDPR legislation, you can choose to anonymize all of your quiz responses by automatically deleting any Personal Identifiable Information from the responses 30 days after being collected. To activate this setting toggle the icon.

=== "Magento"

    ![app settings general](/images/manual_appsettings_general.png)

    **Your Profile**

    **Shop email** - Your main store contact email. We automatically update this email each time we sync your store. You can change this email in your store settings (not the app).

    **Your best email** -  Provide your best email (not your store email) for communication in case of issues.

    **Send notifications to email** - Toggle the button to activate the notification emails to your best email. Once active we will send the notifications that appear on the dashboard to your best email. For example, in case you go over your plan's limits, CSV export completions or connection issues.

    **Data & GDPR**

    **Anonymize quiz respones after 30 days** - Some jurisdictions require merchants to delete any Personal Identifiable Information (PII) they hold from customers upon request. To comply with GDPR legislation, you can choose to anonymize all of your quiz responses by automatically deleting any Personal Identifiable Information from the responses 30 days after being collected. To activate this setting toggle the icon.

=== "BigCommerce"

    ![app settings general](/images/manual_appsettings_general.png)

    **Your Profile**

    **Shop email** - Your main store contact email. We automatically update this email each time we sync your store. You can change this email in your store settings (not the app).

    **Your best email** -  Provide your best email (not your store email) for communication in case of issues.

    **Send notifications to email** - Toggle the button to activate the notification emails to your best email. Once active we will send the notifications that appear on the dashboard to your best email. For example, in case you go over your plan's limits, CSV export completions or connection issues.

    **Data & GDPR**

    **Anonymize quiz respones after 30 days** - Some jurisdictions require merchants to delete any Personal Identifiable Information (PII) they hold from customers upon request. To comply with GDPR legislation, you can choose to anonymize all of your quiz responses by automatically deleting any Personal Identifiable Information from the responses 30 days after being collected. To activate this setting toggle the icon.

=== "Standalone"

    ![app settings general](/images/manual_appsettings_general.png)

    **Your Profile**

    **Shop email** - Your main store contact email. We automatically update this email each time we sync your store. You can change this email in your store settings (not the app).

    **Your best email** -  Provide your best email (not your store email) for communication in case of issues.

    **Send notifications to email** - Toggle the button to activate the notification emails to your best email. Once active we will send the notifications that appear on the dashboard to your best email. For example, in case you go over your plan's limits, CSV export completions or connection issues.

    **Data & GDPR**

    **Anonymize quiz respones after 30 days** - Some jurisdictions require merchants to delete any Personal Identifiable Information (PII) they hold from customers upon request. To comply with GDPR legislation, you can choose to anonymize all of your quiz responses by automatically deleting any Personal Identifiable Information from the responses 30 days after being collected. To activate this setting toggle the icon.

## Catalogue

=== "Shopify"

    ![app settings catalogue](/images/manual_appsettings_catalogue.png)

    **Metafields Namespaces** - We will import the metafields information for the following namespaces. You will then be able to display this information on the product's result page. In this section, we'll display a list of metafield categories found in your store. You can toggle the button to activate the metafields and follow this article to show them in the quiz: [How to Add Product Metafields](/how-to-guides/add-product-metafields/).

=== "Shopify V2"

    ![manual_shopifyV2_appsettings_catalogue](/images/manual_shopifyV2_appsettings_catalogue.png)

    Our app automatically updates your store's catalog daily and after changes. This includes products, collections, tags, variants, and vendors. You can also manually pull the catalog anytime to ensure that all information is up-to-date and accurate.

    **Import Catalogue** - Start a new catlogue sync. This takes a few minutes.

    **Last catalogue import:** - The last time an item from a catalog was updated (in real time) in the app.

    **Catalogue processed at:** - The last time the product catalog was fully processed and updated.

    **Inventory Filter** - This setting lets you control which products are eligible to be recommended in the quiz results based on stock levels.   

    If you check the `Filter products by inventory level` box, the app will hide any products that are low or out of stock from quiz recommendations. This prevents customers from seeing or clicking on products that are unavailable to purchase. If left unchecked, the app may still recommend products even if they are sold out. Once checked, the **`Minimum stock level`** option will become avilable. You can set the minimum stock level for products to be eligible for recommendations.



=== "WooCommerce"

    ![manual_appsettings_catalogue_woo](/images/manual_appsettings_catalogue_woo.png)

    **What information to pull from your products** - Choose custom settings for your products within the app.

    - **Short/Long description in products** - By selecting one or the other you can choose which description of your products will be shown on the results page.
    - **Pass attribute information to result page** - Toggle to activate/desactivate. Once this option is active, the app will pass attributes to your results page. You need to [run a catalog sync](/how-to-guides/sync-catalog/) after activating this option. Follow this article to learn how to show these attributes on the results page once they are synced: [How to Add Product Metafields](/how-to-guides/how-to-add-product-metafields/).
    - **Use attributes as categories** - Allows you to use your store's attributes to group products into categories that can be then linked to choices via the [Link Collections/Link Categories tab](/reference/quiz-builder/link-collections/).

=== "Magento"


=== "BigCommerce"


=== "Standalone"

    To access the **Catalogue** settings in the standalone version of the Product Recommendation Quiz, open the [Success Checklist](/reference/dashboard/#success-checklist) or [this link](https://admin.revenuehunt.com/catalogue).

## SMTP

=== "Shopify"

    ![app settings smtp](/images/manual_appsettings_smtp.png)

    **SMTP Settings** 

    SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt: Product Recommendation Quiz) to send emails through your email server.

    When you connect the RevenueHunt app to your SMTP Server, the follow-up emails with the quiz results that are sent to your customers won't be sent from our *no-reply@prq.email* email account, they'll be sent from your email account. 

    Check [How to Send Result Emails from your own server](/how-to-guides/send-result-emails-from-custom-server/) for detailed instructions on how to set this up.

    **Name to display(From):** - Set what name and email the customer will see when they receive the email.

    **SMTP Server** - Set your server URL.

    **SMTP Username** - Set your SMTP Username.

    **SMTP Password**  - Provide the password associated with the username.

    **SMTP Port** - Set the SMTP port (25, 465, 587 or 2525)
        
    **test connection & activate** - Once you've provided all your credentials you can test if the connection to your SMTP server is successful. If you see an error check your SMTP settings with the help of a third-party tool such as [Gmass](https://www.gmass.co/smtp-test) or any other SMTP test site. If your settings work as intended there, they should work on our end, too. If you're having issues, please get in touch with your developer / SMTP provider.

=== "Shopify V2"

    ![app settings smtp](/images/manual_shopifyV2_appsettings_smtp.png)

    **SMTP Settings** 

    SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt: Product Recommendation Quiz) to send emails through your email server.

    When you connect the RevenueHunt app to your SMTP Server, the follow-up emails with the quiz results that are sent to your customers won't be sent from our *no-reply@prq.email* email account, they'll be sent from your email account. 

    Check [How to Send Result Emails from your own server](/how-to-guides/send-result-emails-from-custom-server/) for detailed instructions on how to set this up.

    **SMTP From** - Set what name and email the customer will see when they receive the email. The "From" field must be in format: `"Full Name" <name@company.com>`.

    **SMTP Server** - Set your server URL. The "Server" field must be in format: `smtp.example.com`.

    **SMTP Username** - Set your SMTP Username.

    **SMTP Password**  - Provide the password associated with the username.

    **SMTP Port** - Set the SMTP port (25, 465, 587 or 2525)

    **SMTP Authentication**  - Select from teh dropdown your SMTP email authentication method.

    **Enable STARTTLS** - Check to enable STARTTLS. *STARTTLS is a protocol command used to upgrade an existing insecure connection to a secure, encrypted connection using TLS (Transport Layer Security). It typically runs over port 587. You should check this if your mail server supports STARTTLS".* Note that this option is enabled by default, but you should untick it if your SMTP server does not support STARTTLS, as this could prevent successful connections.

    **Enable SSL** - Check to enable SLL. *SSL (Secure Sockets Layer) is an older protocol for encrypting connections. If enabled, your connection starts as secure from the beginning (unlike STARTTLS which upgrades after connecting). This is usually used on port 465. Only enable SSL if your SMTP provider specifies SSL.* This option is enabled by default, but should be unticked for SMTP servers that don't use SSL encryption.
       
    **Test connection** - Once you've provided all your credentials you can test if the connection to your SMTP server is successful by clicking the `Test` button. If you see an error check your SMTP settings with the help of a third-party tool such as [Gmass](https://www.gmass.co/smtp-test) or any other SMTP test site. If your settings work as intended there, they should work on our end, too. If you're having issues, please get in touch with your developer / SMTP provider.

=== "WooCommerce"

    ![app settings smtp](/images/manual_appsettings_smtp.png)

    **SMTP Settings** 

    SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt: Product Recommendation Quiz) to send emails through your email server.

    When you connect the RevenueHunt app to your SMTP Server, the follow-up emails with the quiz results that are sent to your customers won't be sent from our *no-reply@prq.email* email account, they'll be sent from your email account. 

    Check [How to Send Result Emails from your own server](/how-to-guides/how-to-send-result-emails-from-custom-server/) for detailed instructions on how to set this up.

    **Name to display(From):** - Set what name and email the customer will see when they receive the email.

    **SMTP Server** - Set your server URL.

    **SMTP Username** - Set your SMTP Username.

    **SMTP Password**  - Provide the password associated with the username.

    **SMTP Port** - Set the SMTP port (25, 465, 587 or 2525)
        
    **test connection & activate** - Once you've provided all your credentials you can test if the connection to your SMTP server is successful. If you see an error check your SMTP settings with the help of a third-party tool such as [Gmass](https://www.gmass.co/smtp-test) or any other SMTP test site. If your settings work as intended there, they should work on our end, too. If you're having issues, please get in touch with your developer / SMTP provider.

=== "Magento"

    ![app settings smtp](/images/manual_appsettings_smtp.png)

    **SMTP Settings** 

    SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt: Product Recommendation Quiz) to send emails through your email server.

    When you connect the RevenueHunt app to your SMTP Server, the follow-up emails with the quiz results that are sent to your customers won't be sent from our *no-reply@prq.email* email account, they'll be sent from your email account. 

    Check [How to Send Result Emails from your own server](/how-to-guides/how-to-send-result-emails-from-custom-server/) for detailed instructions on how to set this up.

    **Name to display(From):** - Set what name and email the customer will see when they receive the email.

    **SMTP Server** - Set your server URL.

    **SMTP Username** - Set your SMTP Username.

    **SMTP Password**  - Provide the password associated with the username.

    **SMTP Port** - Set the SMTP port (25, 465, 587 or 2525)
        
    **test connection & activate** - Once you've provided all your credentials you can test if the connection to your SMTP server is successful. If you see an error check your SMTP settings with the help of a third-party tool such as [Gmass](https://www.gmass.co/smtp-test) or any other SMTP test site. If your settings work as intended there, they should work on our end, too. If you're having issues, please get in touch with your developer / SMTP provider.

=== "BigCommerce"

    ![app settings smtp](/images/manual_appsettings_smtp.png)

    **SMTP Settings** 

    SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt: Product Recommendation Quiz) to send emails through your email server.

    When you connect the RevenueHunt app to your SMTP Server, the follow-up emails with the quiz results that are sent to your customers won't be sent from our *no-reply@prq.email* email account, they'll be sent from your email account. 

    Check [How to Send Result Emails from your own server](/how-to-guides/how-to-send-result-emails-from-custom-server/) for detailed instructions on how to set this up.

    **Name to display(From):** - Set what name and email the customer will see when they receive the email.

    **SMTP Server** - Set your server URL.

    **SMTP Username** - Set your SMTP Username.

    **SMTP Password**  - Provide the password associated with the username.

    **SMTP Port** - Set the SMTP port (25, 465, 587 or 2525)
        
    **test connection & activate** - Once you've provided all your credentials you can test if the connection to your SMTP server is successful. If you see an error check your SMTP settings with the help of a third-party tool such as [Gmass](https://www.gmass.co/smtp-test) or any other SMTP test site. If your settings work as intended there, they should work on our end, too. If you're having issues, please get in touch with your developer / SMTP provider.

=== "Standalone"

    ![app settings smtp](/images/manual_appsettings_smtp.png)

    **SMTP Settings** 

    SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt: Product Recommendation Quiz) to send emails through your email server.

    When you connect the RevenueHunt app to your SMTP Server, the follow-up emails with the quiz results that are sent to your customers won't be sent from our *no-reply@prq.email* email account, they'll be sent from your email account. 

    Check [How to Send Result Emails from your own server](/how-to-guides/how-to-send-result-emails-from-custom-server/) for detailed instructions on how to set this up.

    **Name to display(From):** - Set what name and email the customer will see when they receive the email.

    **SMTP Server** - Set your server URL.

    **SMTP Username** - Set your SMTP Username.

    **SMTP Password**  - Provide the password associated with the username.

    **SMTP Port** - Set the SMTP port (25, 465, 587 or 2525)
        
    **test connection & activate** - Once you've provided all your credentials you can test if the connection to your SMTP server is successful. If you see an error check your SMTP settings with the help of a third-party tool such as [Gmass](https://www.gmass.co/smtp-test) or any other SMTP test site. If your settings work as intended there, they should work on our end, too. If you're having issues, please get in touch with your developer / SMTP provider.

## Shop App (Beta)

=== "Shopify"

    ![app settings shop app](/images/manual_appsettings_shopapp.png)

    **Entry Point Settings**

    **Activate Entry Point** - Toggle to activate a quiz in the Shop App.

    **Quiz Dropdown** - Select from a list of quizzes which one should be featured in the Shop App.

    **TITLE** - Type a title for your Shop App quiz.

    **DESCRIPTION** - Provide a short description of the quiz.

    **CTA TEXT** - Type what will be written on the button that opens the quiz.

    **Quiz Image URL** - Provide a URL of an image you'd like to see featured on the Shop App quiz page.

    **Entry Point Preview** - Shows a preview of how the quiz entry point will look on your store's page in the Shop App.

    ![app settings shop app preview](/images/manual_appsettings_shopapp_preview.png)

=== "Shopify V2"

    At this moment in time, there is no way to activate the Shop App in the Shopify V2 version of the app. We are actively working on this feature and will update this section once it's available.


## Shopify Markets

=== "Shopify"

    Shopify Markets integration is only available in the Shopify V2 version of the app. This feature is not supported in the original Shopify app version.

=== "Shopify V2"

    ![manual_shopifyV2_appsettings_markets](/images/manual_shopifyV2_appsettings_markets.png)

    Tailor your customer experience by assigning specific quizzes to each of your store's Shopify Markets. Customize product recommendations, content, and language to meet the unique preferences of your global audience.

    Click the `dropdown list` to select a quiz that will be shown by default to the visitors of that Markets version of your store.

    ![manual_shopifyV2_appsettings_markets_pickquiz](/images/manual_shopifyV2_appsettings_markets_pickquiz.png)

    **Show All Locales** -  Click ➜ to displays a list of all markets, lanugages and currencies. Once activated gives you a chance to pick a different quiz that will be shown by dafault for the customer from that Market **and** lanuguage.

    ![manual_shopifyV2_appsettings_markets_showall](/images/manual_shopifyV2_appsettings_markets_showall.png)

    **Hide All Locales** - Click 🡻 to return to a simplified view of all Markets, without language disctinction. The app will show the default quiz for all the visitors from that Market regardless of the language they chose.

    **Default** - Select the default quiz for a speciifc region.

    **Language** - Selct a default quiz for a specific language in this region.

    **Currency** - Type `{{amount}} EUR` or `${{amount}}` to change the currency format as displayed on the results page.
