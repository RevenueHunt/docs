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

    1. **Access Theme Customization**: Log in to your Shopify admin dashboard. Navigate to `Online Store > Themes`. Find your current theme and click on the `Customize` button.
    2. **Activate App Embeds**: Within the theme customization area, go to `App Embeds`. Look for the V2 - Link Popup Quiz option and toggle it on. This action will automatically add the RevenueHunt script to your site, enabling quiz links to load in a popup.
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

---
Integrating an interactive quiz into your email or newsletter is straightforward with these steps. By embedding a custom quiz link, you can significantly increase engagement and provide value to your subscribers, making your email campaigns more interactive and fun.
