# How to Add a Quiz Popup via a Chat-Like Button on Your Store

Enhance your Shopify / eCommerce store's interactivity by integrating a chat-like button that triggers a quiz popup. This guide provides step-by-step instructions on how to implement this feature, offering both theme-based and manual methods.

Make sure you have:

- Access to your eCommerce store's admin dashboard.
- An existing quiz created with the RevenueHunt app.
- Familiarity with your eCommerce website theme customization options.

## Chat Button on the Homepage

=== "Shopify"

    ### Option 1: Through Shopify Theme

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/oQyIiA2GwjY?si=X5Pd4YUR5O-sby3u" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **Copy Quiz ID**: Go to your RevenueHunt app [dashboard](/reference/dashboard/), select a quiz and click the `...` button. Copy your Quiz ID.
    2. **Open Store Themes**: Go to `Online Store > Themes`, click `Customize`, then open `App Embeds`.
    3. **Embed the Chat Button Quiz**: Select `Chat Button Quiz` from the list.
    4. **Customize the Chat Button**: Enter your Quiz ID into the appropriate field. Adjust the chat button settings as needed. Activate the chat button by toggling it on.
    5. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

    ### Option 2: Manual

    1. **Obtain Chat Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Chat button`](/reference/quiz-builder/share-publish/#chat) mode, and `Show Instructions for Legacy Themes`.
    2. **Generate Popup Code**: Adjust settings like welcome message, width or height and click `Get code` to generate an HTML code.
    3. **Open Store Themes**: In `Themes`, click `Customize`, add a `Custom content` section, then a `Custom HTML`/`Custom liquid` block.
    4. **Paste Popup Code**: In the HTML/custom liquid block, paste your popup code. paste this code into the HTML of your desired pages.
    5. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

=== "Shopify V2"

    Coming Soon

=== "WooCommerce"

    1. **Obtain Chat Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Chat button`](/reference/quiz-builder/share-publish/#chat) mode.
    2. **Generate Popup Code**: Adjust settings like welcome message, width or height and click `Get code` to generate an HTML code. Copy the code.
    3. In WordPress, open `Pages` and find the Front Page. Click `Edit` to open the page.
    4. In the editor, find a `Custom HTML` element and add it to the page.
    5. In the element, paste the code copied from the app.
    6. Save the changes and `update` the page.
    7. From now on, the chat icon popup quiz will be visible on the main page.

=== "Magento"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Chat Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Chat button`](/reference/quiz-builder/share-publish/#chat) mode.
    3. **Generate Popup Code**: Adjust settings like welcome message, width or height and click `Get code` to generate an HTML code. Copy the code.  
    4. In your Magento dashboard go to `Content` > `Blocks`. Click `Add New Block`.
    5. Edit the Block Title, Identifier and Store View and click `Edit with Page Builder`. 
    6. Select `Elements` > `Rows` and drag a row into the canvas. 
    7. Next open `Elements` and pick `HTML Code`. Drag the `HTML Code` onto the Row.
    8. Click the gear icon to open `HTML settings`.
    9. Under `Enter HTML, CSS or JavaScript code` paste the HTML code copied from the app. 
    10. Remember to save the changes.
    11. From now on, the chat icon popup quiz will be visible on the main page.

=== "BigCommerce"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Chat Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Chat button`](/reference/quiz-builder/share-publish/#chat) mode.
    3. **Generate Popup Code**: Adjust settings like welcome message, width or height and click `Get code` to generate an HTML code. Copy the code.  
    4. In BigCommerce, go to `Storefront` > `Web Pages`. Find the main page.
    5. Switch to the `HTML` editor. Paste the HTML code copied from the app.
    6. Save the changes.
    7. From now on, the chat icon popup quiz will be visible on the main page.

=== "Standalone"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Chat Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Chat button`](/reference/quiz-builder/share-publish/#chat) mode.
    3. **Generate Popup Code**: Adjust settings like welcome message, width or height and click `Get code` to generate an HTML code. Copy the code.  
    4. In your store customization options find the main page.
    5. Find a `Custom HTML` element. In the element settings paste the code copied from the app.
    6. Save the changes.
    7. From now on, the chat icon popup quiz will be visible on the main page.

## Chat Button on All Pages

If you want the chat button to appear across your entire store, follow the [Manual Instructions](#option-2-manual) and insert the code before the `</body>` closing tag in your shop's theme.


## The quiz you are looking for does not exist

![docs/images/how_to_publish_shipifyV2_V1publisherror.png](/images/how_to_publish_shipifyV2_V1publisherror.png)

=== "Shopify"

    If you see the error message "The quiz you are looking for does not exist" when trying to activate an chat button popup quiz, follow these steps:

    1. Go back to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    2. Go to [Quiz Settings](/reference/quiz-builder/quiz-settings/) and **copy the Quiz ID**. Then in Shopify, go back to Online Store > Themes > Customize and under the `App Embeds` select the `Chat Button Quiz` option.
    3. Paste the Quiz ID in the `Quiz ID` field. *Note: the Quiz ID is case-sensitive.*
        ![how_to_publish_shipifyV2_V1publisherrorchatbutton](/images/how_to_publish_shipifyV2_V1publisherrorchatv1.png)
    4. Save your changes and refresh the page.
    
=== "Shopify V2"

    Coming Soon

=== "WooCommerce"

    If you see the error message "The quiz you are looking for does not exist" when trying to activate an chat button popup quiz, follow these steps:

    1. Make sure to generate the correct embed code from the [Share](/reference/quiz-builder/share-publish/) section. If in doubt, regenerate the embed code and re-paste it in the page.
    2. Ensure that the quiz is published and active. Go to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    3. If the quiz is still not displayed,try adding our embed.js script to the page via a custom HTML element.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
    4. Save the changes and refresh the page.

=== "Magento"

    If you see the error message "The quiz you are looking for does not exist" when trying to activate an chat button popup quiz, follow these steps:

    1. Make sure to generate the correct embed code from the [Share](/reference/quiz-builder/share-publish/) section. If in doubt, regenerate the embed code and re-paste it in the page.
    2. Ensure that the quiz is published and active. Go to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    3. If the quiz is still not displayed,try adding our embed.js script to the page via a custom HTML element.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
    4. Save the changes and refresh the page.

=== "BigCommerce"

    If you see the error message "The quiz you are looking for does not exist" when trying to activate an chat button popup quiz, follow these steps:

    1. Make sure to generate the correct embed code from the [Share](/reference/quiz-builder/share-publish/) section. If in doubt, regenerate the embed code and re-paste it in the page.
    2. Ensure that the quiz is published and active. Go to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    3. If the quiz is still not displayed,try adding our embed.js script to the page via a custom HTML element.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
    4. Save the changes and refresh the page.

=== "Standalone"

    If you see the error message "The quiz you are looking for does not exist" when trying to activate an chat button popup quiz, follow these steps:

    1. Make sure you have added our embed.js script to the page via a custom HTML element.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
    2. Make sure to generate the correct embed code from the [Share](/reference/quiz-builder/share-publish/) section. If in doubt, regenerate the embed code and re-paste it in the page.
    3. Ensure that the quiz is published and active. Go to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    4. Save the changes and refresh the page.   

---
By following these instructions, you can successfully add a chat-like button to your Shopify/eCommerce store that opens a quiz popup.
