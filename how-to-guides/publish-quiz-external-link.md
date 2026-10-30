---
description: "Step-by-step guide to generate a shareable RevenueHunt quiz link for social media platforms."
icon: material/share-variant
---

# How to Get an External Quiz Link for Social Media

A link in a social post can take someone to a page that holds the quiz. It can also open the quiz as a popup over your store. Either link goes anywhere a link goes, including a bio.

| Route | The link looks like | Pick it when |
|---|---|---|
| [A page that holds the quiz](#quiz-on-a-dedicated-landing-page) | `https://yourstore.com/pages/quiz-page` | You want the traffic to land somewhere your analytics counts as a page |
| [A link popup](#link-popup-for-socials) | `https://yourstore.com/#quiz` | You want the quiz to open over a page you already have |

## Quiz on a dedicated landing page

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/d6Q9K0AHyHo?si=f06WCz5pWXLR1eQ-" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "Shopify 1.0 themes cannot run this"

        A quiz built in the Built for Shopify version needs an app embed, and app embeds are an Online Store 2.0 feature. A Shopify 1.0 theme does not support them.

        Upgrade to an Online Store 2.0 theme to use them.

    1. **In your Shopify admin, go to `Online Store > Themes` and click `Customize` on your live theme.**

    2. **Click the `Templates` menu in the header.**

        ![The Templates menu in the Shopify theme editor](/images/landing-page-create-a.png)

    3. **Go to `Pages`, click `Create template`, and name it**, such as `quiz-page`. Set `Based on` to your default page template.

        ![Naming the new page template](/images/landing-page-create-b.png)

    4. **Click `Add section`, open the `Apps` group, and add `Inline Quiz` from RevenueHunt.** Your default quiz renders in the template straight away.

        ![Adding the Inline Quiz section from the Apps group](/images/landing-page-add-section-app-inline-quiz.png)

    5. **Click the quiz section to adjust its settings.** You can set the quiz height, fix that height so the results page does not resize, and turn auto-scroll off.

    6. **Go to `Online Store > Pages` and click `Add page`, or open an existing page.**

    7. **Under `Template`, pick the template you just built, then click `Save`.**

        ![Choosing the new template on a Shopify page](/images/how_to_publish_inline_quiz_shopify_v2_new_page.png)

    8. **Click `View Template` and check the quiz is on the page.**

        ![The quiz running on the published landing page](/images/how_to_publish_inline_quiz_shopify_v2_main_page_2.png)

    9. **Copy the finished page's address from your browser, and paste it where you want to share it.**

    !!! note "Which quiz opens"

        Your default quiz opens, unless you name another one.

        With [Shopify Markets](/reference/app-settings/#shopify-markets) set up, the default quiz for that market opens instead.

        To open a particular quiz, set the `Quiz ID`. See [Open a specific quiz](#open-a-specific-quiz).

    !!! warning "One quiz per page"

        Embed a single quiz on a page. Two on the same page conflict, and neither loads reliably.

=== "Shopify (Legacy)"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/Zy1ZFpdtLiQ?si=15XisaE-Y-9-6JTf" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder, pick [`Inline`](/reference/quiz-builder/share-publish/#inline), then `Show Instructions for Legacy Themes`.**

    2. **Click `Get the code`** and copy the HTML.

    3. **Go to `Online Store > Pages` and open the page you want the quiz on, or create one.**

    4. **Click `Show HTML` and paste the code into the editor.**

    5. **Click `Save`.**

    6. **Copy the finished page's address from your browser, and paste it where you want to share it.**

    !!! warning "One quiz per page"

        Embed a single quiz on a page. Two on the same page conflict, and neither loads reliably.

=== "WooCommerce"

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Inline`](/reference/quiz-builder/share-publish/#inline).**

    2. **Adjust the inline settings, then click `Get the code`.** Copy the HTML it gives you.

    3. **In your WordPress admin, open `Pages` and click `Add New Page`.**

    4. **Give the page a title, then add a `Custom HTML` block where you want the quiz.**

    5. **Paste the code into that block.**

    6. **Click `Update`.**

    7. **Copy the finished page's address from your browser, and paste it where you want to share it.**

    !!! warning "One quiz per page"

        Embed a single quiz on a page. Two on the same page conflict, and neither loads reliably.

=== "Magento"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Inline`](/reference/quiz-builder/share-publish/#inline).**

    3. **Adjust the inline settings, then click `Get the code`.** Copy the HTML it gives you.

    4. **In your Magento admin, go to `Content > Pages` and click `Add New Page`.**

    5. **Give the page a title, open the `Content` tab, and click `Edit with Page Builder`.**

    6. **Drag a row in from `Elements > Rows`, then drag `HTML Code` onto that row.**

    7. **Click the gear icon to open `HTML settings`, then paste the code under `Enter HTML, CSS or JavaScript code`.**

    8. **Save the page.**

    9. **Copy the finished page's address from your browser, and paste it where you want to share it.**

    !!! warning "One quiz per page"

        Embed a single quiz on a page. Two on the same page conflict, and neither loads reliably.

=== "BigCommerce"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Inline`](/reference/quiz-builder/share-publish/#inline).**

    3. **Adjust the inline settings, then click `Get the code`.** Copy the HTML it gives you.

    4. **In BigCommerce, go to `Storefront > Web Pages` and click `Create a Web Page`.**

    5. **Under `Web Page Details > Page Content`, switch to the `HTML` editor and paste the code in.**

    6. **Save the page.**

    7. **Copy the finished page's address from your browser, and paste it where you want to share it.**

    !!! warning "One quiz per page"

        Embed a single quiz on a page. Two on the same page conflict, and neither loads reliably.

=== "Standalone"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Inline`](/reference/quiz-builder/share-publish/#inline).**

    3. **Adjust the inline settings, then click `Get the code`.** Copy the HTML it gives you.

    4. **In your store editor, open the `Pages` menu and create a new page.**

    5. **Find a `Custom HTML` element and paste the code into its settings.**

    6. **Save the page.**

    7. **Copy the finished page's address from your browser, and paste it where you want to share it.**

    !!! warning "One quiz per page"

        Embed a single quiz on a page. Two on the same page conflict, and neither loads reliably.

!!! tip "The same address works elsewhere"

    Add it to your store menu, your email campaigns or your ads. Nothing about it is specific to social media.

## Link popup for socials

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/X86Vb800gZs?si=0fBO41qui_kTK6TR" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "Shopify 1.0 themes cannot run this"

        A quiz built in the Built for Shopify version needs an app embed, and app embeds are an Online Store 2.0 feature. A Shopify 1.0 theme does not support them.

        Upgrade to an Online Store 2.0 theme to use them.

    The link popup embed adds the RevenueHunt script to your store, so any link ending in `#quiz` opens the quiz over whatever page it lands on.

    1. **In your Shopify admin, go to `Online Store > Themes` and click `Customize` on your live theme.**

    2. **Open `App embeds` and turn on `Link Popup Quiz`.** Leave `Link Popup Quiz (Legacy)` off. That one serves quizzes from the legacy app.

        ![The Link Popup Quiz embed in the App embeds list](/images/how_to_publish_quiz_link_popup_app_embeds.png)

    3. **Click `Save`.**

    4. **Build your link by adding `#quiz` to any page address on your store**, such as `https://yourstore.com/#quiz`.

    5. **Paste that link into your post, your bio or your ad.**

    6. **Open the link yourself before you post it.** The quiz should open.

    !!! note "Which quiz opens"

        Your default quiz opens, unless you name another one.

        With [Shopify Markets](/reference/app-settings/#shopify-markets) set up, the default quiz for that market opens instead.

        To open a particular quiz, set the `Quiz ID`. See [Open a specific quiz](#open-a-specific-quiz).

=== "Shopify (Legacy)"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/PkWI1OnP6gg?si=eTHrvNekv3WhUKOr" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **Go to `Online Store > Themes > Customize > App embeds` and turn on `Link Popup Quiz (Legacy)`.**

        The plain `Link Popup Quiz` embed serves the Built for Shopify version. A legacy quiz opened through it reports that it does not exist.

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder, open the [`External`](/reference/quiz-builder/share-publish/#external) tile, then `Show Instructions for Legacy Themes`.**

    3. **Set the popup width and height.**

    4. **Click `Get the code`** to generate the link.

    5. **Paste that link into your post, your bio or your ad.**

    6. **Open the link yourself before you post it.** The quiz should open.

=== "WooCommerce"

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and open the [`External`](/reference/quiz-builder/share-publish/#external) tile.**

    2. **Set the popup width and height.**

    3. **Click `Get the code`** to generate the link.

    4. **Paste that link into your post, your bio or your ad.**

    5. **Open the link yourself before you post it.** The quiz should open.

=== "Magento"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and open the [`External`](/reference/quiz-builder/share-publish/#external) tile.**

    3. **Set the popup width and height.**

    4. **Click `Get the code`** to generate the link.

    5. **Paste that link into your post, your bio or your ad.**

    6. **Open the link yourself before you post it.** The quiz should open.

=== "BigCommerce"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and open the [`External`](/reference/quiz-builder/share-publish/#external) tile.**

    3. **Set the popup width and height.**

    4. **Click `Get the code`** to generate the link.

    5. **Paste that link into your post, your bio or your ad.**

    6. **Open the link yourself before you post it.** The quiz should open.

=== "Standalone"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and open the [`External`](/reference/quiz-builder/share-publish/#external) tile.**

    3. **Set the popup width and height.**

    4. **Click `Get the code`** to generate the link.

    5. **Put your own domain in front of the fragment.** The finished link looks like `https://yourwebsite.com/#quiz-QUIZID`.

    6. **Paste that link into your post, your bio or your ad.**

    7. **Open the link yourself before you post it.** The quiz should open.

## FAQs

### Open a specific quiz

=== "Shopify"

    A link ending in `#quiz` opens your default quiz. To open another one, put its ID in the `Quiz ID (optional)` field of the `Link Popup Quiz` settings in the theme editor.

    ![The Quiz ID field in the Link Popup Quiz settings](/images/manual_shopifyV2_quizbuilder_share_publish_linkpopup_options.png)

    !!! info "Finding the Quiz ID"

        In the [Dashboard](/reference/dashboard/), click the `...` beside the quiz and select `Copy Quiz ID`. The ID is case-sensitive.

    !!! note "Shopify Markets"

        With [Shopify Markets](/reference/app-settings/#shopify-markets) set up, the default quiz for the customer's market opens instead of your store default.

=== "Shopify (Legacy)"

    Name the quiz in the link itself. End the address with `#quiz-QUIZID`, using the ID of the quiz you want.

    Different links can open different quizzes from the same store. One campaign can send `https://yourstore.com/#quiz-123` while another sends `https://yourstore.com/#quiz-456`.

    !!! info "Finding the Quiz ID"

        In the [Dashboard](/reference/dashboard/), click the `...` beside the quiz and select `Copy Quiz ID`. The ID is case-sensitive.

=== "WooCommerce"

    Name the quiz in the link itself. End the address with `#quiz-QUIZID`, using the ID of the quiz you want.

    Different links can open different quizzes from the same store. One campaign can send `https://yourstore.com/#quiz-123` while another sends `https://yourstore.com/#quiz-456`.

    !!! info "Finding the Quiz ID"

        In the [Dashboard](/reference/dashboard/), click the `...` beside the quiz and select `Copy Quiz ID`. The ID is case-sensitive.

=== "Magento"

    Name the quiz in the link itself. End the address with `#quiz-QUIZID`, using the ID of the quiz you want.

    Different links can open different quizzes from the same store. One campaign can send `https://yourstore.com/#quiz-123` while another sends `https://yourstore.com/#quiz-456`.

    !!! info "Finding the Quiz ID"

        In the [Dashboard](/reference/dashboard/), click the `...` beside the quiz and select `Copy Quiz ID`. The ID is case-sensitive.

=== "BigCommerce"

    Name the quiz in the link itself. End the address with `#quiz-QUIZID`, using the ID of the quiz you want.

    Different links can open different quizzes from the same store. One campaign can send `https://yourstore.com/#quiz-123` while another sends `https://yourstore.com/#quiz-456`.

    !!! info "Finding the Quiz ID"

        In the [Dashboard](/reference/dashboard/), click the `...` beside the quiz and select `Copy Quiz ID`. The ID is case-sensitive.

=== "Standalone"

    Name the quiz in the link itself. End the address with `#quiz-QUIZID`, using the ID of the quiz you want.

    Different links can open different quizzes from the same store. One campaign can send `https://yourstore.com/#quiz-123` while another sends `https://yourstore.com/#quiz-456`.

    !!! info "Finding the Quiz ID"

        In the [Dashboard](/reference/dashboard/), click the `...` beside the quiz and select `Copy Quiz ID`. The ID is case-sensitive.

### The quiz you are looking for does not exist

![The error a quiz shows when the link points at a quiz it cannot find](/images/how_to_publish_shipifyV2_V1publisherror.png)

=== "Shopify"

    This error means the link is being served by the embed for the other version of the app.

    1. **Go to `Online Store > Themes > Customize > App embeds` and check which link embed is on.** For a quiz built here, `Link Popup Quiz` is the right one.

        ![The two link popup embeds in the App embeds list](/images/how_to_publish_shipifyV2_V1publisherrorlinkpopup.png)

    2. **Turn `Link Popup Quiz (Legacy)` off and turn `Link Popup Quiz` on.** The legacy embed serves quizzes from the legacy app, so it cannot find a quiz built in this version.

    3. **Click `Save`.**

    4. **Check your link ends in `#quiz`.**

=== "Shopify (Legacy)"

    This error means the link cannot find the quiz. The quiz may be unpublished, the wrong embed may be on, or the ID may be wrong.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and check the quiz is published**, with the top-right `Publish` button.

    2. **Go to `Online Store > Themes > Customize > App embeds` and turn on `Link Popup Quiz (Legacy)`.** The plain `Link Popup Quiz` embed serves quizzes from the Built for Shopify version, so it cannot find a legacy quiz.

    3. **Copy the `Quiz ID` from [Quiz settings](/reference/quiz-builder/quiz-settings/#general).** The ID is case-sensitive.

    4. **Check your link ends in `#quiz-QUIZID`, with that ID.**

    5. **Click `Save`, then reload the page.**

=== "WooCommerce"

    This error means the link cannot find the quiz.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and check the quiz is published**, with the top-right `Publish` button.

    2. **Copy the `Quiz ID` from [Quiz settings](/reference/quiz-builder/quiz-settings/#general).** The ID is case-sensitive.

    3. **Check your link ends in `#quiz-QUIZID`, with that ID.**

=== "Magento"

    This error means the link cannot find the quiz.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and check the quiz is published**, with the top-right `Publish` button.

    2. **Copy the `Quiz ID` from [Quiz settings](/reference/quiz-builder/quiz-settings/#general).** The ID is case-sensitive.

    3. **Check your link ends in `#quiz-QUIZID`, with that ID.**

=== "BigCommerce"

    This error means the link cannot find the quiz.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and check the quiz is published**, with the top-right `Publish` button.

    2. **Copy the `Quiz ID` from [Quiz settings](/reference/quiz-builder/quiz-settings/#general).** The ID is case-sensitive.

    3. **Check your link ends in `#quiz-QUIZID`, with that ID.**

=== "Standalone"

    This error means the link cannot find the quiz.

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open the [Quiz Builder](/reference/quiz-builder/) and check the quiz is published**, with the top-right `Publish` button.

    3. **Copy the `Quiz ID` from [Quiz settings](/reference/quiz-builder/quiz-settings/#general).** The ID is case-sensitive.

    4. **Check your link ends in `#quiz-QUIZID`, with that ID.**

---

This article explains the two ways to link a quiz from a social post, and what to check when the link does not open it.