# How to Get an External Quiz Link for Emails and Newsletters

This guide walks you through the process of creating an external quiz link that can be embedded in emails and newsletters. This is an effective way to engage your subscribers by incorporating interactive content directly into your email marketing campaigns.

Make sure you have: 

- Access to the quiz app dashboard.
- An active email or newsletter campaign setup.

## Link Popup for Emails

=== "Shopify"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/PkWI1OnP6gg?si=eTHrvNekv3WhUKOr" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **Obtain the Popup Link Code**: Go to the [`Share`](/reference/quiz-builder/share-publish/) section of the app, then open the [`Email`](/reference/quiz-builder/share-publish/#email) tile and `Show Instructions for legacy themes`. 
    2. **Customize Popup Dimensions**: Input your desired dimensions for the width and height to optimize the viewer's experience.
    3. **Generate popup link**: Click on the `Get the code` button to create your unique quiz link. This link is now ready to be shared via email.
    4. **Embed in Emails or Newsletters**: Copy the newly generated link. Paste it into the body of your emails or newsletters wherever you wish the quiz to appear.

=== "Shopify V2"

    <div style="position: relative; padding-bottom: 53.125%; height: 0;"><iframe src="https://www.loom.com/embed/2687bd6629c64e67b5d257d33683531d?sid=9aad21fe-47b0-4ec3-a231-4941e26768f7" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "Shopify 1.0 Theme Compatibility"
        Quizzes created with Shopify V2 cannot be published on Shopify 1.0 themes. Shopify 1.0 themes do not support app embeds, which are required for the V2 integration. App embeds are a feature available in Online Store 2.0 themes, which allow you to add app functionality without touching any code. If you want to use app embeds, you would need to upgrade to an Online Store 2.0 theme.

    1. **Access Theme Customization**: Log in to your Shopify admin dashboard. Navigate to `Online Store > Themes`. Find your current theme and click on the `Customize` button.
    2. **Activate App Embeds**: Within the theme customization area, go to `App Embeds`. Look for the `Link Popup Quiz` option and toggle it on. This action will automatically add the RevenueHunt script to your site, enabling quiz links to load in a popup.
        ![how to publish quiz link popup app embeds](/images/how_to_publish_quiz_link_popup_app_embeds.png)
    3. **Save changes**: Click on the Save button to ensure all changes are saved before exiting the theme editor.
    4. **Copy the link to the quiz popup**: The direct link to your quiz popup is https://yourstore.myshopify.com/#quiz.
    5. **Share the link**: Share the link to the quiz popup with your audience. You can add it to your email campaigns, social media posts, or any other communication channel.

    When clicked, the default quiz for your store will open. If you've configured [Shopify Markets](/reference/app-settings/#__tabbed_5_2), the default quiz for that specific market will be shown instead.

=== "WooCommerce"

    1. **Obtain the Popup Link Code**: Go to the [`Share`](/reference/quiz-builder/share-publish/) section of the app, then open the [`Email`](/reference/quiz-builder/share-publish/#email) tile. 
    2. **Customize Popup Dimensions**: Input your desired dimensions for the width and height to optimize the viewer's experience.
    3. **Generate popup link**: Click on the `Get the code` button to create your unique quiz link. This link is now ready to be shared via email.
    4. **Embed in Emails or Newsletters**: Copy the newly generated link. Paste it into the body of your emails or newsletters wherever you wish the quiz to appear.

=== "Magento"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain the Popup Link Code**: Go to the [`Share`](/reference/quiz-builder/share-publish/) section of the app, then open the [`Email`](/reference/quiz-builder/share-publish/#email) tile. 
    3. **Customize Popup Dimensions**: Input your desired dimensions for the width and height to optimize the viewer's experience.
    4. **Generate popup link**: Click on the `Get the code` button to create your unique quiz link. This link is now ready to be shared via email.
    5. **Embed in Emails or Newsletters**: Copy the newly generated link. Paste it into the body of your emails or newsletters wherever you wish the quiz to appear.

=== "BigCommerce"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain the Popup Link Code**: Go to the [`Share`](/reference/quiz-builder/share-publish/) section of the app, then open the [`Email`](/reference/quiz-builder/share-publish/#email) tile. 
    3. **Customize Popup Dimensions**: Input your desired dimensions for the width and height to optimize the viewer's experience.
    4. **Generate popup link**: Click on the `Get the code` button to create your unique quiz link. This link is now ready to be shared via email.
    5. **Embed in Emails or Newsletters**: Copy the newly generated link. Paste it into the body of your emails or newsletters wherever you wish the quiz to appear.

=== "Standalone"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain the Popup Link Code**: Go to the [`Share`](/reference/quiz-builder/share-publish/) section of the app, then open the [`Email`](/reference/quiz-builder/share-publish/#email) tile. 
    3. **Customize Popup Dimensions**: Input your desired dimensions for the width and height to optimize the viewer's experience.
    4. **Generate popup link**: Click on the `Get the code` button to create your unique quiz link. Edit the link URL to add your website URL. It should look like this `https://yourwebsite.com/#quiz-QUIZID/`. This link is now ready to be shared via email.
    5. **Embed in Emails or Newsletters**: Copy the newly generated link. Paste it into the body of your emails or newsletters wherever you wish the quiz to appear.


## Inline Quiz on a Landing Page

Create a dedicated landing page for the quiz to drive traffic from email campaigns.

=== "Shopify"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/Zy1ZFpdtLiQ?si=15XisaE-Y-9-6JTf" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    **Option 1: With Embed Code**

    1. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode, and `Show Instructions for Legacy Themes` to copy the HTML embed code.
    2. Create a new page in Shopify Online Store > Pages.
    2. **Insert Quiz into Page**: Navigate to `Online Store > Pages` and select the page to embed the quiz. Click `Show HTML` and paste the embed code into the code editor.
    3. **Single Quiz Per Page**: To avoid issues, embed only one quiz per page. If using a non-Shopify version of the quiz, ensure the `embed.js` code is added to your site's header.

    **Option 2: Via Page Theme Template**

    1. **Navigate to Theme Customization**: Go to `Online Store > Themes` in your Shopify dashboard. Click the `Customize` button for your active theme.

    2. **Create a New Page Template**: click on the `Templates` menu in the header.
        ![Create a new Page template](/images/landing-page-create-a.png)
        Navigate to `Pages` and click on the `Create template` link. Name your template (e.g., quiz-page) and set it as "Based on" your Default page template. 
        ![Create a new Page template](/images/landing-page-create-b.png)
    
    3. **Add Inline Quiz Section**: Click on the `Add section` link and from the `Apps` section, find `Inline Quiz (Legacy)` from RevenueHunt. Select it to add to your quiz page template.
        ![Add section inline quiz](/images/landing-page-add-section-app-inline-quiz.png)

    4. **Configure Quiz Settings**: Click on the added quiz section to configure. Adjust settings like quiz height, disable auto-scroll, or fix quiz height for consistent results page height.

    5. **Assign the Template to a Page**: Go to `Online Store > Pages`. Click `Add page` or select an existing page to edit. In the Template section on the right, choose your new template from the Theme template dropdown. Click `Save` and then `View Template`. 

    6. **Save Changes**: Ensure all changes are saved before exiting the theme editor.
    
    Now, that page will use the custom template with the quiz you created. You can use a direct link to this page in your marketing campaigns or social media posts.


=== "Shopify V2"

    <div style="position: relative; padding-bottom: 53.125%; height: 0;"><iframe src="https://www.loom.com/embed/d560a4cb8a9a42f89eec7cf8a9e94ca4?sid=8199a06a-4aab-41cf-ac6a-b5f8bdffedbe" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Navigate to Theme Customization**: Go to `Online Store > Themes` in your Shopify dashboard. Click the `Customize` button for your active theme.

    2. **Create a New Page Template**: click on the `Templates` menu in the header.
        ![Create a new Page template](/images/landing-page-create-a.png)
        Navigate to `Pages` and click on the `Create template` link. Name your template (e.g., quiz-page) and set it as "Based on" your Default page template. 
        ![Create a new Page template](/images/landing-page-create-b.png)
    
    3. **Add Inline Quiz Section**: Click on the `Add section` link and from the `Apps` section, find `Inline Quiz` from RevenueHunt. Select it to add to your quiz page template.
        ![Add section inline quiz](/images/landing-page-add-section-app-inline-quiz.png)

    4. **Configure Quiz Settings**: Click on the added quiz section to configure. Adjust settings like quiz height, disable auto-scroll, or fix quiz height for consistent results page height.

    5. **Assign the Template to a Page**: Go to `Online Store > Pages`. Click `Add page` or select an existing page to edit. In the Template section on the right, choose your new template from the Theme template dropdown. Click `Save` and then `View Template`. 
        ![how to publish inline quiz shopify v2 new page](/images/how_to_publish_inline_quiz_shopify_v2_new_page.png)

        The default quiz for your store will be rendered. If you’ve configured [Shopify Markets](/reference/app-settings/#__tabbed_5_2), the default quiz for that specific market will be shown instead.
        ![how to publish inline quiz shopify v2 main page 2](/images/how_to_publish_inline_quiz_shopify_v2_main_page_2.png)

    6. **Save Changes**: Ensure all changes are saved before exiting the theme editor.
    
    Now, that page will use the custom template with the quiz you created. You can use a direct link to this page in your marketing campaigns or social media posts.

=== "WooCommerce"

    1. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode.
    2. Edit the inline quiz settings and click `Get the code`. Copy the HTML embed code.
    3. In WordPress, open `Pages` and click `Add New Page`.
    4. In the editor, add a page title. Then, find a `Custom HTML` element and add it to the page in a place where you want the quiz to show.
    5. In the element, paste the code copied from the app.
    6. Save the changes and `update` the page.
    7. From now on, the inline quiz will be visible on that page.

=== "Magento"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode.
    3. Edit the inline quiz settings and click `Get the code`. Copy the HTML embed code.
    4. In your Magento dashbaord go to `Content` > `Pages`. Click `Add New Page`.
    5. Edit the Page Title and open the `Content` tab. Click `Edit with Page Builder`. 
    6. Select `Elements` > `Rows` and drag a row into the canvas. 
    7. Next open `Elements` and pick `HTML Code`. Drag the `HTML Code` onto the Row.
    8. Click the gear icon to open `HTML settings`.
    9. Under `Enter HTML, CSS or JavaScript code` paste the HTML code copied from the app. 
    10. Remember to save the changes.
    11. From now on, the inline quiz will be visible on that page.

=== "BigCommerce"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode.
    3. Edit the inline quiz settings and click `Get the code`. Copy the HTML embed code.
    4. In BigCommerce, go to `Storefront` > `Web Pages`. Click `Create a Web Page`.
    5. Under `Web Page Details` > `Page Content` switch to the `HTML` editor. Paste the HTML code copied from the app.
    6. Save the changes.
    7. From now on, the inline quiz will be visible on that page.

=== "Standalone"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode.
    3. Edit the inline quiz settings and click `Get the code`. Copy the HTML embed code.
    4. In your store customization options find the `Pages` menu and create a new page.
    5. In the page editor find a ` Custom HTML` element. In the element settings paste the code copied from the app.
    6. Save the changes.
    7. From now on, the inline quiz will be visible on that page.

!!! tip

    You can add a link to this page to your website menu or use the link to this new page in your marketing campaigns.



## The quiz you are looking for does not exist

![docs/images/how_to_publish_shipifyV2_V1publisherror.png](/images/how_to_publish_shipifyV2_V1publisherror.png)

=== "Shopify"

    If you see the error message "The quiz you are looking for does not exist" when trying to link to a quiz, follow these steps:

    1. Go back to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    2. Go to [Quiz Settings](/reference/quiz-builder/quiz-settings/) and **copy the Quiz ID**. Then in Shopify, go back to Online Store > Themes > Customize and under the `App Embeds` section active the `Link Popup Quiz`. 
    3. Check the Quiz Link. Ensure that the link you've created is correctly formatted and it follows the format `#quiz-QUIZID`. Where the Quiz ID is the ID you've copied from the Quiz Settings. *Note: the Quiz ID is case-sensitive.*
    4. Save your changes and refresh the page.
    
=== "Shopify V2"

    If you see the error message "The quiz you are looking for does not exist" when trying to link to a quiz, follow these steps:

    1. Ensure that you have activated the `Link Popup Quiz` in the  Online Store > Theme > Customize > `App Embeds` section and **not** the the legacy `Link Popup Quiz Legacy`.
        ![docs/images/how_to_publish_shipifyV2_V1publisherrorlinkpopup.png](/images/how_to_publish_shipifyV2_V1publisherrorlinkpopup.png)

        If a wrong link popup is activated, you will see the error message "The quiz you are looking for does not exist" when trying to link to a V2 quiz. 
        
        To solve this simply deactivate the `Link Popup Quiz Legacy` and activate the `Link Popup Quiz` one. Then, save the changes.
    2. Verify that the link is correctly formatted. Ensure that the link you've created is correctly formatted and it follows the format `#quiz`.

=== "WooCommerce"

    If you see the error message "The quiz you are looking for does not exist" when trying to link to a quiz, follow these steps:

    1. Ensure that the quiz is published and active. Go to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    2. Check that the quiz ID is correct. Go to the [Quiz Settings](/reference/quiz-builder/quiz-settings/) and **copy the Quiz ID**.
    3. Verify that the link is correctly formatted. Ensure that the link you've created is correctly formatted and it follows the format `#quiz-QUIZID`. Where the Quiz ID is the ID you've copied from the Quiz Settings. *Note: the Quiz ID is case-sensitive.*        

=== "Magento"

    If you see the error message "The quiz you are looking for does not exist" when trying to link to a quiz, follow these steps:

    1. Ensure that the quiz is published and active. Go to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    2. Check that the quiz ID is correct. Go to the [Quiz Settings](/reference/quiz-builder/quiz-settings/) and **copy the Quiz ID**.
    3. Verify that the link is correctly formatted. Ensure that the link you've created is correctly formatted and it follows the format `#quiz-QUIZID`. Where the Quiz ID is the ID you've copied from the Quiz Settings. *Note: the Quiz ID is case-sensitive.*   

=== "BigCommerce"

    If you see the error message "The quiz you are looking for does not exist" when trying to link to a quiz, follow these steps:

    1. Ensure that the quiz is published and active. Go to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    2. Check that the quiz ID is correct. Go to the [Quiz Settings](/reference/quiz-builder/quiz-settings/) and **copy the Quiz ID**.
    3. Verify that the link is correctly formatted. Ensure that the link you've created is correctly formatted and it follows the format `#quiz-QUIZID`. Where the Quiz ID is the ID you've copied from the Quiz Settings. *Note: the Quiz ID is case-sensitive.*                     

=== "Standalone"

    If you see the error message "The quiz you are looking for does not exist" when trying to link to a quiz, follow these steps:

    1. Ensure you've added the following embed.js script to your website. Without it, the quiz won't be loaded on your website.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
    2. Ensure that the quiz is published and active. Go to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    3. Check that the quiz ID is correct. Go to the [Quiz Settings](/reference/quiz-builder/quiz-settings/) and **copy the Quiz ID**.
    4. Verify that the link is correctly formatted. Ensure that the link you've created is correctly formatted and it follows the format `#quiz-QUIZID`. Where the Quiz ID is the ID you've copied from the Quiz Settings. *Note: the Quiz ID is case-sensitive.*

---
Integrating an interactive quiz into your email or newsletter is straightforward with these steps. By embedding a custom quiz link, you can significantly increase engagement and provide value to your subscribers, making your email campaigns more interactive and fun.
