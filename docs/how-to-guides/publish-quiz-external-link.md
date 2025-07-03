# How to Get an External Quiz Link for Social Media

This guide will show you how to generate an external quiz link suitable for sharing on social media platforms like Twitter, Instagram, and Facebook.

## Link Popup for Socials

=== "Shopify"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/PkWI1OnP6gg?si=eTHrvNekv3WhUKOr" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **Obtain the Popup Link Code**: Go to the [`Share`](/reference/quiz-builder/share-publish/) section of the app, then open the [`External`](/reference/quiz-builder/share-publish/#external) tile and `Show Instructions for legacy themes`. 
    2. **Customize Popup Dimensions**: Set the width and height according to your preference or the requirements of the social media platform you intend to use.
    3. **Generate popup link**: Click on the `Get the code` button to create your unique quiz link. This link is now ready to be shared to your social media.
    4. **Share on Social Media**: Copy the generated link. Paste this link into your social media posts on Twitter, Instagram, Facebook, or any other platform you wish to use.


=== "Shopify V2"

    <div style="position: relative; padding-bottom: 53.125%; height: 0;"><iframe src="https://www.loom.com/embed/2687bd6629c64e67b5d257d33683531d?sid=9aad21fe-47b0-4ec3-a231-4941e26768f7" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "Shopify 1.0 Theme Compatibility"
        Quizzes created with Shopify V2 cannot be published on Shopify 1.0 themes. Shopify 1.0 themes do not support app embeds, which are required for the V2 integration. App embeds are a feature available in Online Store 2.0 themes, which allow you to add app functionality without touching any code. If you want to use app embeds, you would need to upgrade to an Online Store 2.0 theme.

    1. **Access Theme Customization**: Log in to your Shopify admin dashboard. Navigate to `Online Store > Themes`. Find your current theme and click on the `Customize` button.
    2. **Activate App Embeds**: Within the theme customization area, go to `App Embeds`. Look for the `Link Popup Quiz` option and toggle it on. This action will automatically add the RevenueHunt script to your site, enabling quiz links to load in a popup.
        ![how to publish quiz link popup app embeds](/images/how_to_publish_quiz_link_popup_app_embeds.png)
    3. **Save changes**: Click on the Save button to ensure all changes are saved before exiting the theme editor.
    4. **Copy the link to the quiz popup**: The direct link to your quiz popup is https://yourstore.myshopify.com/#quiz.

        !!! tip

            You can get a direct link to any quiz by adding #quiz-QuizID. 
            
            For example, `https://yourstore.myshopify.com/#quiz-123` can open one quiz, while  `https://yourstore.myshopify.com/#quiz-456` can open another. 
            
            To find your Quiz ID, go to the [dashboard](/reference/dashboard/) and identify a quiz. Click on the `...` and copy the ID.


    5. **Share the link**: Share the link to the quiz popup with your audience. You can add it to your email campaigns, social media posts, or any other 
    communication channel.

    When clicked, the default quiz for your store will open. If you've configured [Shopify Markets](/reference/app-settings/#__tabbed_5_2), the default quiz for that specific market will be shown instead.


=== "WooCommerce"

    1. **Obtain the Popup Link Code**: Go to the [`Share`](/reference/quiz-builder/share-publish/) section of the app, then open the [`External`](/reference/quiz-builder/share-publish/#external) tile. 
    2. **Customize Popup Dimensions**: Set the width and height according to your preference or the requirements of the social media platform you intend to use.
    3. **Generate popup link**: Click on the `Get the code` button to create your unique quiz link. This link is now ready to be shared to your social media.
    4. **Share on Social Media**: Copy the generated link. Paste this link into your social media posts on Twitter, Instagram, Facebook, or any other platform you wish to use.

=== "Magento"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain the Popup Link Code**: Go to the [`Share`](/reference/quiz-builder/share-publish/) section of the app, then open the [`External`](/reference/quiz-builder/share-publish/#external) tile. 
    3. **Customize Popup Dimensions**: Set the width and height according to your preference or the requirements of the social media platform you intend to use.
    4. **Generate popup link**: Click on the `Get the code` button to create your unique quiz link. This link is now ready to be shared to your social media.
    5. **Share on Social Media**: Copy the generated link. Paste this link into your social media posts on Twitter, Instagram, Facebook, or any other platform you wish to use.

=== "BigCommerce"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain the Popup Link Code**: Go to the [`Share`](/reference/quiz-builder/share-publish/) section of the app, then open the [`External`](/reference/quiz-builder/share-publish/#external) tile. 
    3. **Customize Popup Dimensions**: Set the width and height according to your preference or the requirements of the social media platform you intend to use.
    4. **Generate popup link**: Click on the `Get the code` button to create your unique quiz link. This link is now ready to be shared to your social media.
    5. **Share on Social Media**: Copy the generated link. Paste this link into your social media posts on Twitter, Instagram, Facebook, or any other platform you wish to use.

=== "Standalone"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain the Popup Link Code**: Go to the [`Share`](/reference/quiz-builder/share-publish/) section of the app, then open the [`External`](/reference/quiz-builder/share-publish/#external) tile. 
    3. **Customize Popup Dimensions**: Set the width and height according to your preference or the requirements of the social media platform you intend to use.
    4. **Generate popup link**: Click on the `Get the code` button to create your unique quiz link. Edit the link URL to add your website URL. It should look like this `https://yourwebsite.com/#quiz-QUIZID/`. This link is now ready to be shared to your social media.
    5. **Share on Social Media**: Copy the generated link. Paste this link into your social media posts on Twitter, Instagram, Facebook, or any other platform you wish to use.

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
By following these steps, you can easily generate an external link for your quiz, making it accessible to your social media audience.
