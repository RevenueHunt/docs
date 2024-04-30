# App Settings

## General

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

    **Metafields Namespaces** - We will import the metafields information for the following namespaces. You will then be able to display this information on the product's result page. In this section, we'll display a list of metafield categories found in your store. You can toggle the button to activate the metafields and follow this article to show them in the quiz: [How to Add Product Metafileds](https://docs.revenuehunt.com/how-to-guides/how-to-add-product-metafields/).

=== "WooCommerce"

    ![manual_appsettings_catalogue_woo](/images/manual_appsettings_catalogue_woo.png)

    **What information to pull from your products** - Choose custom settings for your products within the app.

    - **Short/Long description in products** - By selecting one or the other you can choose which description of your products will be shown on the results page.
    - **Pass attribute information to result page** - Toggle to activate/desactivate. Once this option is active, the app will pass attributes to your results page. You need to [run a catalog sync](https://docs.revenuehunt.com/how-to-guides/sync-catalog/) after activating this option. Follow this article to learn how to show these attributes on the results page once they are synced: [How to Add Product Metafileds](https://docs.revenuehunt.com/how-to-guides/how-to-add-product-metafields/).
    - **Use attributes as categories** - Allows you to use your store's attributes to group products into categories that can be then linked to choices via the [Link Collections/Link Categories tab](https://docs.revenuehunt.com/reference/quiz-builder/#link-collections).

=== "Magento"


=== "BigCommerce"


=== "Standalone"

    To access the **Catalogue** settings in the standalone version of the Product Recommendation Quiz, open the [Success Checklist](https://docs.revenuehunt.com/reference/dashboard/#success-checklist) or [this link](https://admin.revenuehunt.com/catalogue).

## SMTP

![app settings smtp](/images/manual_appsettings_smtp.png)

**SMTP Settings** 

SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. Shop Quiz) to send emails through your email server.

When you connect the Shop Quiz: Product Recommendation Quiz app to your SMTP Server, the follow-up emails with the quiz results that are sent to your customers won’t be sent from our *no-reply@prq.email* email account, they’ll be sent from your email account. 

Check [How to Send Result Emails from your own server](https://docs.revenuehunt.com/how-to-guides/how-to-send-result-emails-from-custom-server/) for detailed instructions on how to set this up.

**Name to display(From):** - Set what name and email the customer will see when they receive the email.

**SMTP Server** - Set your server URL.

**SMTP Username** - Set your SMTP Username.

**SMTP Password**  - Provide the password associated with the username.

**SMTP Port** - Set the SMTP port (25, 465, 587 or 2525)
    
**test connection & activate** - Once you've provided all your credentials you can test if the connection to your SMTP server is successful. If you see an error check your SMTP settings with the help of a third-party tool such as [Gmass](https://www.gmass.co/smtp-test) or any other SMTP test site. If your settings work as intended there, they should work on our end, too. If you’re having issues, please get in touch with your developer / SMTP provider.

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
