---
description: "Step-by-step guide to add a chat button that opens a RevenueHunt quiz popup on your ecommerce store."
icon: material/chat-outline
---

# How to Add a Quiz Popup via a Chat-Like Button on Your Store

A chat button sits in a corner of your store, looking like a support widget. A customer clicks it and the quiz opens in a popup.

Unlike an [automatic popup](/how-to-guides/publish-quiz-automatic-popup/), it waits to be clicked, so it asks nothing of a customer who is not interested.

!!! note "Before you start"

    You need a quiz built in the RevenueHunt app, and access to your theme editor.

## Chat button on the homepage

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/WGfNlVPFA_Q?si=anpiVruoyxR8cKyy" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "Shopify 1.0 themes cannot run this"

        A quiz built in the Built for Shopify version needs an app embed or an app section, and both are Online Store 2.0 features. A Shopify 1.0 theme supports neither.

        Upgrade to an Online Store 2.0 theme to use them.

    1. **In your Shopify admin, go to `Online Store > Themes` and click `Customize` on your live theme.**

    2. **With the home page template open, click `Add section`, open the `Apps` tab, and add `Chat Button Quiz`.**

        ![Adding the Chat Button Quiz section from the Apps tab](/images/manual_shopifyv2_pagelevel_chat_add.png)

    3. **Set up the button.**

        ![The Chat Button Quiz settings panel](/images/manual_shopifyV2_quizbuilder_share_publish_chat_options.png)

        | Setting | What it does |
        |---|---|
        | `Chat button color` | The color of the button itself |
        | `Chat icon color` | The color of the icon inside it |
        | `Chat position` | Which corner the button sits in |
        | `Hide after quiz completion` | Takes the button away once the customer reaches the results page |
        | `Show notification dot` | Puts a small red dot on the icon |
        | `Greeting message` | The line shown beside the icon. Leave it empty to hide it |
        | `Popup width (% of screen)` | How wide the quiz opens |
        | `Popup height (% of screen)` | How tall the quiz opens |
        | `Popup z-index` | Which other elements the quiz sits in front of |
        | `Quiz ID (optional)` | The quiz to open. Leave it empty for your default quiz |

    4. **Click `Save`.**

    5. **Open your store and click the chat button.** The quiz should open in a popup.

    !!! note "Which quiz opens"

        Your default quiz opens, unless you name another one.

        With [Shopify Markets](/reference/app-settings/#shopify-markets) set up, the default quiz for that market opens instead.

        To open a particular quiz, set the `Quiz ID`. See [Open a specific quiz](#open-a-specific-quiz).

=== "Shopify (Legacy)"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/oQyIiA2GwjY?si=X5Pd4YUR5O-sby3u" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    **With the app embed**

    1. **Copy your Quiz ID.** In the [Dashboard](/reference/dashboard/), click the `...` beside the quiz and copy the ID.

    2. **Go to `Online Store > Themes`, click `Customize`, then open `App embeds`.**

    3. **Turn on `Chat Button Quiz (Legacy)` and paste the Quiz ID into its settings.**

        The plain `Chat Button Quiz` embed serves the Built for Shopify version. A legacy quiz opened through it reports that it does not exist.

    4. **Adjust the colors, greeting message and popup size.**

    5. **Click `Save`.**

    6. **Open your store and click the chat button.** The quiz should open in a popup.

    **With pasted code**

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder, pick [`Chat button`](/reference/quiz-builder/share-publish/#chat), then `Show Instructions for Legacy Themes`.**

    2. **Set the colors, greeting message and popup size, then click `Get code`.** Copy the HTML it gives you.

    3. **In `Themes > Customize`, add a `Custom content` section, then a `Custom HTML` or `Custom liquid` block.**

    4. **Paste the code into that block.**

    5. **Click `Save`.**

    6. **Open your store and click the chat button.** The quiz should open in a popup.

=== "WooCommerce"

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Chat button`](/reference/quiz-builder/share-publish/#chat).**

    2. **Set the colors, greeting message and popup size, then click `Get code`.** Copy the HTML it gives you.

    3. **In your WordPress admin, open `Pages`, find your front page and click `Edit`.**

    4. **Add a `Custom HTML` block and paste the code into it.**

    5. **Click `Update`.**

    6. **Open your store and click the chat button.** The quiz should open in a popup.

=== "Magento"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Chat button`](/reference/quiz-builder/share-publish/#chat).**

    3. **Set the colors, greeting message and popup size, then click `Get code`.** Copy the HTML it gives you.

    4. **In your Magento admin, go to `Content > Blocks` and click `Add New Block`.**

    5. **Fill in the block title, identifier and store view, then click `Edit with Page Builder`.**

    6. **Drag a row in from `Elements > Rows`, then drag `HTML Code` onto that row.**

    7. **Click the gear icon to open `HTML settings`, then paste the code under `Enter HTML, CSS or JavaScript code`.**

    8. **Save the block.**

    9. **Open your store and click the chat button.** The quiz should open in a popup.

=== "BigCommerce"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Chat button`](/reference/quiz-builder/share-publish/#chat).**

    3. **Set the colors, greeting message and popup size, then click `Get code`.** Copy the HTML it gives you.

    4. **In BigCommerce, go to `Storefront > Web Pages` and open your main page.**

    5. **Switch to the `HTML` editor and paste the code in.**

    6. **Save the page.**

    7. **Open your store and click the chat button.** The quiz should open in a popup.

=== "Standalone"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Chat button`](/reference/quiz-builder/share-publish/#chat).**

    3. **Set the colors, greeting message and popup size, then click `Get code`.** Copy the HTML it gives you.

    4. **In your store editor, open the main page.**

    5. **Find a `Custom HTML` element and paste the code into its settings.**

    6. **Save the page.**

    7. **Open your store and click the chat button.** The quiz should open in a popup.

## Chat button on all pages

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/RM0MySN9PUU?si=wtcWwFSvN25coodT" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "Shopify 1.0 themes cannot run this"

        A quiz built in the Built for Shopify version needs an app embed or an app section, and both are Online Store 2.0 features. A Shopify 1.0 theme supports neither.

        Upgrade to an Online Store 2.0 theme to use them.

    1. **In your Shopify admin, go to `Online Store > Themes` and click `Customize` on your live theme.**

    2. **Open `App embeds` and turn on `Chat Button Quiz`.** Leave `Chat Button Quiz (Legacy)` off. That one serves quizzes from the legacy app.

        ![The App embeds list, with Chat Button Quiz turned on](/images/manual_shopifyV2_quizbuilder_share_publish_onlinestore_chat.png)

    3. **Set up the button.**

        ![The Chat Button Quiz settings panel](/images/manual_shopifyV2_quizbuilder_share_publish_chat_options.png)

        | Setting | What it does |
        |---|---|
        | `Chat button color` | The color of the button itself |
        | `Chat icon color` | The color of the icon inside it |
        | `Chat position` | Which corner the button sits in |
        | `Hide after quiz completion` | Takes the button away once the customer reaches the results page |
        | `Show notification dot` | Puts a small red dot on the icon |
        | `Greeting message` | The line shown beside the icon. Leave it empty to hide it |
        | `Popup width (% of screen)` | How wide the quiz opens |
        | `Popup height (% of screen)` | How tall the quiz opens |
        | `Popup z-index` | Which other elements the quiz sits in front of |
        | `Quiz ID (optional)` | The quiz to open. Leave it empty for your default quiz |

    4. **Click `Save`.**

    5. **Open your store and click the chat button.** The quiz should open in a popup.

    The button now runs on every page that uses this theme.

    !!! note "Which quiz opens"

        Your default quiz opens, unless you name another one.

        With [Shopify Markets](/reference/app-settings/#shopify-markets) set up, the default quiz for that market opens instead.

        To open a particular quiz, set the `Quiz ID`. See [Open a specific quiz](#open-a-specific-quiz).

=== "Shopify (Legacy)"

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder, pick [`Chat button`](/reference/quiz-builder/share-publish/#chat), then `Show Instructions for Legacy Themes`.**

    2. **Set the colors, greeting message and popup size, then click `Get code`.** Copy the HTML it gives you.

    3. **Go to `Online Store > Themes` and click `Actions > Edit code`.**

    4. **Open `theme.liquid` or `footer.liquid`, and Paste the code just before the closing `</body>` tag**, so it loads on every page.**

    5. **Click `Save`.**

    6. **Open your store and click the chat button.** The quiz should open in a popup.

=== "WooCommerce"

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Chat button`](/reference/quiz-builder/share-publish/#chat).**

    2. **Set the colors, greeting message and popup size, then click `Get code`.** Copy the HTML it gives you.

    3. **In your WordPress admin, open `Appearance > Theme File Editor` and select `footer.php`.**

    4. **Paste the code just before the closing `</body>` tag**, so it loads on every page.

    5. **Click `Update File`.**

    6. **Open your store and click the chat button.** The quiz should open in a popup.

=== "Magento"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Chat button`](/reference/quiz-builder/share-publish/#chat).**

    3. **Set the colors, greeting message and popup size, then click `Get code`.** Copy the HTML it gives you.

    4. **Open the footer template of your Magento theme.**

    5. **Paste the code just before the closing `</body>` tag**, so it loads on every page.

    6. **Save the template, then deploy the static content and flush the cache.**

    7. **Open your store and click the chat button.** The quiz should open in a popup.

=== "BigCommerce"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Chat button`](/reference/quiz-builder/share-publish/#chat).**

    3. **Set the colors, greeting message and popup size, then click `Get code`.** Copy the HTML it gives you.

    4. **Go to `Storefront > My Themes`, then `Advanced > Edit Theme Files`.**

    5. **Open `footer.html` under `Templates`, and Paste the code just before the closing `</body>` tag**, so it loads on every page.

    6. **Save the file and deploy the theme.**

    7. **Open your store and click the chat button.** The quiz should open in a popup.

=== "Standalone"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Chat button`](/reference/quiz-builder/share-publish/#chat).**

    3. **Set the colors, greeting message and popup size, then click `Get code`.** Copy the HTML it gives you.

    4. **In your store editor, open your theme footer.**

    5. **Paste the code just before the closing `</body>` tag**, so it loads on every page.

    6. **Save the theme.**

    7. **Open your store and click the chat button.** The quiz should open in a popup.

## Chat button on a specific page

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/rbweJaslzvo?si=0EZZDjAhO8FfQt3R" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "Shopify 1.0 themes cannot run this"

        A quiz built in the Built for Shopify version needs an app embed or an app section, and both are Online Store 2.0 features. A Shopify 1.0 theme supports neither.

        Upgrade to an Online Store 2.0 theme to use them.

    1. **In your Shopify admin, go to `Online Store > Themes` and click `Customize`.**

    2. **Open the page template menu and pick the template you want the button on, or create a new one.**

    3. **Click `Add section`, open the `Apps` tab, and add `Chat Button Quiz`.**

        ![Adding the Chat Button Quiz section from the Apps tab](/images/manual_shopifyv2_pagelevel_chat_add.png)

        ![The Chat Button Quiz section added to a template](/images/manual_shopifyv2_pagelevel_chat_added.png)

    4. **Set up the button.**

        ![The Chat Button Quiz settings panel](/images/manual_shopifyV2_quizbuilder_share_publish_chat_options.png)

        | Setting | What it does |
        |---|---|
        | `Chat button color` | The color of the button itself |
        | `Chat icon color` | The color of the icon inside it |
        | `Chat position` | Which corner the button sits in |
        | `Hide after quiz completion` | Takes the button away once the customer reaches the results page |
        | `Show notification dot` | Puts a small red dot on the icon |
        | `Greeting message` | The line shown beside the icon. Leave it empty to hide it |
        | `Popup width (% of screen)` | How wide the quiz opens |
        | `Popup height (% of screen)` | How tall the quiz opens |
        | `Popup z-index` | Which other elements the quiz sits in front of |
        | `Quiz ID (optional)` | The quiz to open. Leave it empty for your default quiz |

    5. **Click `Save`.** The button now shows on every page using this template.

    6. **Apply the template to your page.** In `Online Store > Pages`, open the page, or click `Add page` to make one. Set its template to the one you just built, set the visibility to `Visible`, and save.

    7. **Open your store and click the chat button.** The quiz should open in a popup.

    !!! note "Which quiz opens"

        Your default quiz opens, unless you name another one.

        With [Shopify Markets](/reference/app-settings/#shopify-markets) set up, the default quiz for that market opens instead.

        To open a particular quiz, set the `Quiz ID`. See [Open a specific quiz](#open-a-specific-quiz).

=== "Shopify (Legacy)"

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder, pick [`Chat button`](/reference/quiz-builder/share-publish/#chat), then `Show Instructions for Legacy Themes`.**

    2. **Set the colors, greeting message and popup size, then click `Get code`.** Copy the HTML it gives you.

    3. **In Shopify, go to `Online Store > Pages`, open the page, click `Show HTML`, and paste the code in.**

    4. **Click `Save`.**

    5. **Open your store and click the chat button.** The quiz should open in a popup.

=== "WooCommerce"

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Chat button`](/reference/quiz-builder/share-publish/#chat).**

    2. **Set the colors, greeting message and popup size, then click `Get code`.** Copy the HTML it gives you.

    3. **In your WordPress admin, open `Pages`, find the page you want the button on and click `Edit`.**

    4. **Add a `Custom HTML` block and paste the code into it.**

    5. **Click `Update`.**

    6. **Open your store and click the chat button.** The quiz should open in a popup.

=== "Magento"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Chat button`](/reference/quiz-builder/share-publish/#chat).**

    3. **Set the colors, greeting message and popup size, then click `Get code`.** Copy the HTML it gives you.

    4. **In your Magento admin, go to `Content > Pages` and open the page, or click `Add New Page`.**

    5. **Open the `Content` tab and click `Edit with Page Builder`.**

    6. **Drag a row in from `Elements > Rows`, then drag `HTML Code` onto that row.**

    7. **Click the gear icon to open `HTML settings`, then paste the code under `Enter HTML, CSS or JavaScript code`.**

    8. **Save the page.**

    9. **Open your store and click the chat button.** The quiz should open in a popup.

=== "BigCommerce"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Chat button`](/reference/quiz-builder/share-publish/#chat).**

    3. **Set the colors, greeting message and popup size, then click `Get code`.** Copy the HTML it gives you.

    4. **In BigCommerce, go to `Storefront > Web Pages` and open the page, or click `Create a Web Page`.**

    5. **Under `Web Page Details > Page Content`, switch to the `HTML` editor and paste the code in.**

    6. **Save the page.**

    7. **Open your store and click the chat button.** The quiz should open in a popup.

=== "Standalone"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Chat button`](/reference/quiz-builder/share-publish/#chat).**

    3. **Set the colors, greeting message and popup size, then click `Get code`.** Copy the HTML it gives you.

    4. **In your store editor, open the page you want the button on.**

    5. **Find a `Custom HTML` element and paste the code into its settings.**

    6. **Save the page.**

    7. **Open your store and click the chat button.** The quiz should open in a popup.

## FAQs

### Open a specific quiz

=== "Shopify"

    A chat button opens your default quiz. To open another one, put its ID in the `Quiz ID (optional)` field of the `Chat Button Quiz` settings in the theme editor.

    ![The Quiz ID field in the Chat Button Quiz settings](/images/manual_shopifyV2_quizbuilder_share_publish_chat_options.png)

    !!! info "Finding the Quiz ID"

        In the [Dashboard](/reference/dashboard/), click the `...` beside the quiz and select `Copy Quiz ID`. The ID is case-sensitive.

    !!! note "Shopify Markets"

        With [Shopify Markets](/reference/app-settings/#shopify-markets) set up, the default quiz for the customer's market opens instead of your store default.

=== "Shopify (Legacy)"

    Generate the chat button code from the [`Share`](/reference/quiz-builder/share-publish/) tab of the quiz you want to open, then use that code. The quiz ID is baked into it.

=== "WooCommerce"

    Generate the chat button code from the [`Share`](/reference/quiz-builder/share-publish/) tab of the quiz you want to open, then use that code. The quiz ID is baked into it.

=== "Magento"

    Generate the chat button code from the [`Share`](/reference/quiz-builder/share-publish/) tab of the quiz you want to open, then use that code. The quiz ID is baked into it.

=== "BigCommerce"

    Generate the chat button code from the [`Share`](/reference/quiz-builder/share-publish/) tab of the quiz you want to open, then use that code. The quiz ID is baked into it.

=== "Standalone"

    Generate the chat button code from the [`Share`](/reference/quiz-builder/share-publish/) tab of the quiz you want to open, then use that code. The quiz ID is baked into it.

### The quiz you are looking for does not exist

![The error a quiz shows when the chat button points at a quiz it cannot find](/images/how_to_publish_shipifyV2_V1publisherror.png)

=== "Shopify"

    !!! warning "Shopify 1.0 themes cannot run this"

        A quiz built in the Built for Shopify version needs an app embed or an app section, and both are Online Store 2.0 features. A Shopify 1.0 theme supports neither.

        Upgrade to an Online Store 2.0 theme to use them.

    This error means the button is being served by the embed for the other version of the app.

    1. **Go to `Online Store > Themes > Customize > App embeds` and check which chat embed is on.** For a quiz built here, `Chat Button Quiz` is the right one.

        ![The two chat button embeds in the App embeds list](/images/how_to_publish_shipifyV2_V1publisherrorchatpopup.png)

    2. **Turn `Chat Button Quiz (Legacy)` off and turn `Chat Button Quiz` on.** The legacy embed serves quizzes from the legacy app, so it cannot find a quiz built in this version.

    3. **Click `Save`, then reload your store.**

=== "Shopify (Legacy)"

    This error means the button cannot find the quiz, either because it is unpublished or because the wrong embed is on.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and check the quiz is published**, with the top-right `Publish` button.

    2. **Copy the `Quiz ID` from [Quiz settings](/reference/quiz-builder/quiz-settings/#general).** The ID is case-sensitive.

    3. **Go to `Online Store > Themes > Customize > App embeds` and turn on `Chat Button Quiz (Legacy)`.** The plain `Chat Button Quiz` embed serves quizzes from the Built for Shopify version, so it cannot find a legacy quiz.

    4. **Paste the Quiz ID into the `Quiz ID` field.**

        ![Pasting the Quiz ID into the legacy chat button embed settings](/images/how_to_publish_shipifyV2_V1publisherrorchatv1.png)

    5. **Click `Save`, then reload the page.**

=== "WooCommerce"

    This error means the button cannot find the quiz.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and check the quiz is published**, with the top-right `Publish` button.

    2. **Regenerate the code from [`Share`](/reference/quiz-builder/share-publish/) and paste it in again.** An old code can point at a quiz that has since changed.

    3. **Check the `embed.js` script is on the page.** Add it through a custom HTML element if it is missing.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    4. **Save the page, then reload it.**

=== "Magento"

    This error means the button cannot find the quiz.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and check the quiz is published**, with the top-right `Publish` button.

    2. **Regenerate the code from [`Share`](/reference/quiz-builder/share-publish/) and paste it in again.** An old code can point at a quiz that has since changed.

    3. **Check the `embed.js` script is on the page.** Add it through a custom HTML element if it is missing.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    4. **Save the page, then reload it.**

=== "BigCommerce"

    This error means the button cannot find the quiz.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and check the quiz is published**, with the top-right `Publish` button.

    2. **Regenerate the code from [`Share`](/reference/quiz-builder/share-publish/) and paste it in again.** An old code can point at a quiz that has since changed.

    3. **Check the `embed.js` script is on the page.** Add it through a custom HTML element if it is missing.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    4. **Save the page, then reload it.**

=== "Standalone"

    This error means the button cannot find the quiz.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and check the quiz is published**, with the top-right `Publish` button.

    2. **Regenerate the code from [`Share`](/reference/quiz-builder/share-publish/) and paste it in again.** An old code can point at a quiz that has since changed.

    3. **Check the `embed.js` script is on the page.** Add it through a custom HTML element if it is missing.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    4. **Save the page, then reload it.**

---

This article explains how to add a chat button that opens your quiz. It also covers where to run it, and what to check when it does not appear.