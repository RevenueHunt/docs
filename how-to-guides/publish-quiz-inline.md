---
description: "Complete guide to embedding a RevenueHunt inline quiz on your store homepage or dedicated page."
icon: material/page-layout-body
---

# How to Embed an Inline Quiz on Your Store

An inline quiz sits inside a page, as part of it, rather than opening over the top. Put it on your homepage, on a landing page of its own, or on a collection page.

!!! note "Before you start"

    You need a quiz built in the RevenueHunt app, and access to your theme editor.

=== "Shopify"

    On this version the quiz is a theme section, so there is no code to copy.

    1. **Open the Shopify theme editor.**

    2. **Add a section to the page or template you want, and pick `Inline Quiz` from the `Apps` group.**

=== "Shopify (Legacy)"

    On this version the quiz is a theme section, so there is no code to copy.

    1. **Open the Shopify theme editor.**

    2. **Add a section to the page or template you want, and pick `Inline Quiz` from the `Apps` group.**

=== "WooCommerce"

    On this version you paste an embed code into the page.

    1. **Generate the embed code from the [`Share`](/reference/quiz-builder/share-publish/) section of the app.**

    2. **Paste it into an HTML element on the page where you want the quiz.**

=== "Magento"

    On this version you paste an embed code into the page, and the script has to be on the page too.

    1. **Add the `embed.js` script to your store header.**

    2. **Generate the embed code from the [`Share`](/reference/quiz-builder/share-publish/) section of the app.**

    3. **Paste it into an HTML element on the page where you want the quiz.**

=== "BigCommerce"

    On this version you paste an embed code into the page, and the script has to be on the page too.

    1. **Add the `embed.js` script to your store header.**

    2. **Generate the embed code from the [`Share`](/reference/quiz-builder/share-publish/) section of the app.**

    3. **Paste it into an HTML element on the page where you want the quiz.**

=== "Standalone"

    On this version you paste an embed code into the page, and the script has to be on the page too.

    1. **Add the `embed.js` script to your store header.**

    2. **Generate the embed code from the [`Share`](/reference/quiz-builder/share-publish/) section of the app.**

    3. **Paste it into an HTML element on the page where you want the quiz.**

## Embed an inline quiz on the homepage

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/OCX0EgfERpc?si=w4RwuW79QYodjRWz" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "Shopify 1.0 themes cannot run this"

        A quiz built in the Built for Shopify version needs an app section, and app sections are an Online Store 2.0 feature. A Shopify 1.0 theme does not support them.

        Upgrade to an Online Store 2.0 theme to use them.

    1. **In your Shopify admin, go to `Online Store > Themes` and click `Customize` on your live theme.**

    2. **Click `Add section`, open the `Apps` group, and add `Inline Quiz` from RevenueHunt.** Your default quiz renders straight away.

        ![The Inline Quiz section added to the homepage](/images/how_to_publish_inline_quiz_shopify_v2_main_page.png)

    3. **Click the quiz section and set it up.**

        ![The Inline Quiz settings panel](/images/manual_shopifyV2_quizbuilder_share_publish_onlinestore_inline_settings.png)

        | Setting | What it does |
        |---|---|
        | `Quiz height` | The starting height. The first question always uses it, which is a Shopify requirement that stops the page jumping as it loads |
        | `Quiz height (unit)` | `Pixels (px)` by default. `Viewport height percentage (vh)` is the alternative |
        | `Fixed height` | Holds that height for the whole quiz. Off means the quiz grows to fit each question after the first |
        | `Full width quiz` | Spans the quiz across the screen |
        | `Auto-scroll on retake quiz` | Where the page scrolls when a customer retakes the quiz: `Disabled`, `Top of the page` or `Top of the quiz` |
        | `Auto-scroll on question change` | The same, each time the customer moves to another question |
        | `Quiz ID (optional)` | The quiz to show. Leave it empty for your default quiz |
        | `Manage app` | Opens the RevenueHunt dashboard |

    4. **Click `Save`.** The quiz then shows on every page using this template.

        ![The inline quiz running on the homepage](/images/how_to_publish_inline_quiz_shopify_v2_main_page_2.png)

    5. **Open the page in your store and check the quiz is there.**

    !!! note "Which quiz appears"

        Your default quiz appears, unless you name another one.

        With [Shopify Markets](/reference/app-settings/#shopify-markets) set up, the default quiz for that market appears instead.

        To show a particular quiz, set the `Quiz ID`. See [Embed a specific quiz](#embed-a-specific-quiz).

    !!! warning "One quiz per page"

        Embed a single quiz on a page. Two on the same page conflict, and neither loads reliably.

=== "Shopify (Legacy)"

    **With the theme section**

    <div class="videoWrapper"><iframe src="https://www.youtube.com/embed/SGEfb-EPCcE?si=ZmignNyehGwF4Ysa" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

    1. **In your Shopify admin, go to `Online Store > Themes` and click `Customize` on your live theme.**

    2. **Click `Add section`, open the `Apps` group, and add `Inline Quiz` from RevenueHunt.**

    3. **Click the quiz section, pick the Quiz ID, and set the height, the fixed height and the auto-scroll.**

    4. **Click `Save`.**

    5. **Open the page in your store and check the quiz is there.**

    **With pasted code**

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder, pick [`Inline`](/reference/quiz-builder/share-publish/#inline), then `Show Instructions for Legacy Themes`.**

    2. **Click `Get the code`** and copy the HTML.

    3. **In the theme editor, click `Add section` and pick `Custom content`.** Remove the default content and add a `Custom HTML` block.

    4. **Paste the code into the `HTML` input, then save.**

    5. **Open the page in your store and check the quiz is there.**

    !!! warning "One quiz per page"

        Embed a single quiz on a page. Two on the same page conflict, and neither loads reliably.

=== "WooCommerce"

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Inline`](/reference/quiz-builder/share-publish/#inline).**

    2. **Adjust the inline settings, then click `Get the code`.** Copy the HTML it gives you.

    3. **In your WordPress admin, open `Pages`, find your front page and click `Edit`.**

    4. **Add a `Custom HTML` block where you want the quiz.**

    5. **Paste the code into that block.**

    6. **Click `Update`.**

    7. **Open the page in your store and check the quiz is there.**

    !!! warning "One quiz per page"

        Embed a single quiz on a page. Two on the same page conflict, and neither loads reliably.

=== "Magento"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Inline`](/reference/quiz-builder/share-publish/#inline).**

    3. **Adjust the inline settings, then click `Get the code`.** Copy the HTML it gives you.

    4. **In your Magento admin, go to `Content > Blocks` and click `Add New Block`.**

    5. **Fill in the block title, identifier and store view, then click `Edit with Page Builder`.**

    6. **Drag a row in from `Elements > Rows`, then drag `HTML Code` onto that row.**

    7. **Click the gear icon to open `HTML settings`, then paste the code under `Enter HTML, CSS or JavaScript code`.**

    8. **Save the block.**

    9. **Open the page in your store and check the quiz is there.**

    !!! warning "One quiz per page"

        Embed a single quiz on a page. Two on the same page conflict, and neither loads reliably.

=== "BigCommerce"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Inline`](/reference/quiz-builder/share-publish/#inline).**

    3. **Adjust the inline settings, then click `Get the code`.** Copy the HTML it gives you.

    4. **In BigCommerce, go to `Storefront > Web Pages` and open your main page.**

    5. **Switch to the `HTML` editor and paste the code in.**

    6. **Save the page.**

    7. **Open the page in your store and check the quiz is there.**

    !!! warning "One quiz per page"

        Embed a single quiz on a page. Two on the same page conflict, and neither loads reliably.

=== "Standalone"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Inline`](/reference/quiz-builder/share-publish/#inline).**

    3. **Adjust the inline settings, then click `Get the code`.** Copy the HTML it gives you.

    4. **In your store editor, open the main page.**

    5. **Find a `Custom HTML` element and paste the code into its settings.**

    6. **Save the page.**

    7. **Open the page in your store and check the quiz is there.**

    !!! warning "One quiz per page"

        Embed a single quiz on a page. Two on the same page conflict, and neither loads reliably.

## Embed an inline quiz on a dedicated landing page

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/d6Q9K0AHyHo?si=f06WCz5pWXLR1eQ-" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "Shopify 1.0 themes cannot run this"

        A quiz built in the Built for Shopify version needs an app section, and app sections are an Online Store 2.0 feature. A Shopify 1.0 theme does not support them.

        Upgrade to an Online Store 2.0 theme to use them.

    1. **In your Shopify admin, go to `Online Store > Themes` and click `Customize` on your live theme.**

    2. **Click the `Templates` menu in the header.**

        ![The Templates menu in the Shopify theme editor](/images/landing-page-create-a.png)

    3. **Go to `Pages`, click `Create template`, and name it**, such as `quiz-page`. Set `Based on` to your default page template.

        ![Naming the new page template](/images/landing-page-create-b.png)

    4. **Click `Add section`, open the `Apps` group, and add `Inline Quiz` from RevenueHunt.** Your default quiz renders straight away.

        ![Adding the Inline Quiz section from the Apps group](/images/landing-page-add-section-app-inline-quiz.png)

    5. **Click the quiz section and set it up.**

        ![The Inline Quiz settings panel](/images/manual_shopifyV2_quizbuilder_share_publish_onlinestore_inline_settings.png)

        | Setting | What it does |
        |---|---|
        | `Quiz height` | The starting height. The first question always uses it, which is a Shopify requirement that stops the page jumping as it loads |
        | `Quiz height (unit)` | `Pixels (px)` by default. `Viewport height percentage (vh)` is the alternative |
        | `Fixed height` | Holds that height for the whole quiz. Off means the quiz grows to fit each question after the first |
        | `Full width quiz` | Spans the quiz across the screen |
        | `Auto-scroll on retake quiz` | Where the page scrolls when a customer retakes the quiz: `Disabled`, `Top of the page` or `Top of the quiz` |
        | `Auto-scroll on question change` | The same, each time the customer moves to another question |
        | `Quiz ID (optional)` | The quiz to show. Leave it empty for your default quiz |
        | `Manage app` | Opens the RevenueHunt dashboard |

    6. **Go to `Online Store > Pages` and click `Add page`, or open an existing page.**

    7. **Under `Template`, pick the template you just built, then click `Save`.**

        ![Choosing the new template on a Shopify page](/images/how_to_publish_inline_quiz_shopify_v2_new_page.png)

    8. **Click `View Template`** and check the quiz is on the page.

        ![The quiz running on the published landing page](/images/how_to_publish_inline_quiz_shopify_v2_main_page_2.png)

    !!! note "Which quiz appears"

        Your default quiz appears, unless you name another one.

        With [Shopify Markets](/reference/app-settings/#shopify-markets) set up, the default quiz for that market appears instead.

        To show a particular quiz, set the `Quiz ID`. See [Embed a specific quiz](#embed-a-specific-quiz).

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

    6. **Open the page in your store and check the quiz is there.**

    !!! warning "One quiz per page"

        Embed a single quiz on a page. Two on the same page conflict, and neither loads reliably.

=== "WooCommerce"

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Inline`](/reference/quiz-builder/share-publish/#inline).**

    2. **Adjust the inline settings, then click `Get the code`.** Copy the HTML it gives you.

    3. **In your WordPress admin, open `Pages` and click `Add New Page`.**

    4. **Give the page a title, then add a `Custom HTML` block where you want the quiz.**

    5. **Paste the code into that block.**

    6. **Click `Update`.**

    7. **Open the page in your store and check the quiz is there.**

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

    9. **Open the page in your store and check the quiz is there.**

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

    7. **Open the page in your store and check the quiz is there.**

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

    7. **Open the page in your store and check the quiz is there.**

    !!! warning "One quiz per page"

        Embed a single quiz on a page. Two on the same page conflict, and neither loads reliably.

!!! tip "Use the page address"

    A landing page gives you an ordinary URL. Put it in your store menu, your email campaigns, your social posts or your ads.

## Embed an inline quiz on a specific collection/category

=== "Shopify"

    !!! warning "Shopify 1.0 themes cannot run this"

        A quiz built in the Built for Shopify version needs an app section, and app sections are an Online Store 2.0 feature. A Shopify 1.0 theme does not support them.

        Upgrade to an Online Store 2.0 theme to use them.

    1. **In your Shopify admin, go to `Online Store > Themes` and click `Customize`.**

    2. **Open the template menu in the header, go to `Collections`, and click `Create template`.**

    3. **Click `Add section`, open the `Apps` group, and add `Inline Quiz` from RevenueHunt.**

    4. **Click the quiz section and set it up.**

        ![The Inline Quiz settings panel](/images/manual_shopifyV2_quizbuilder_share_publish_onlinestore_inline_settings.png)

        | Setting | What it does |
        |---|---|
        | `Quiz height` | The starting height. The first question always uses it, which is a Shopify requirement that stops the page jumping as it loads |
        | `Quiz height (unit)` | `Pixels (px)` by default. `Viewport height percentage (vh)` is the alternative |
        | `Fixed height` | Holds that height for the whole quiz. Off means the quiz grows to fit each question after the first |
        | `Full width quiz` | Spans the quiz across the screen |
        | `Auto-scroll on retake quiz` | Where the page scrolls when a customer retakes the quiz: `Disabled`, `Top of the page` or `Top of the quiz` |
        | `Auto-scroll on question change` | The same, each time the customer moves to another question |
        | `Quiz ID (optional)` | The quiz to show. Leave it empty for your default quiz |
        | `Manage app` | Opens the RevenueHunt dashboard |

    5. **Click `Save`.**

    6. **Apply the template to a collection.** In `Products > Collections`, open the collection and pick the template under `Theme template`.

    7. **Open that collection page in your store and check the quiz is there.**

    !!! warning "One quiz per page"

        Embed a single quiz on a page. Two on the same page conflict, and neither loads reliably.

=== "Shopify (Legacy)"

    **In the collection description**

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder, pick [`Inline`](/reference/quiz-builder/share-publish/#inline), then `Show Instructions for Legacy Themes`.**

    2. **Click `Get the code`** and copy the HTML.

    3. **Paste the code into the HTML field of the collection description.** The quiz then appears under the collection name.

    4. **Open that collection page in your store and check the quiz is there.**

    **In a collection template**

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder, pick [`Inline`](/reference/quiz-builder/share-publish/#inline), then `Show Instructions for Legacy Themes`.**

    2. **Click `Get the code`** and copy the HTML.

    3. **Ask a developer to build a collection template that holds the code**, then apply that template to the collection.

    4. **Open that collection page in your store and check the quiz is there.**

    !!! warning "One quiz per page"

        Embed a single quiz on a page. Two on the same page conflict, and neither loads reliably.

=== "WooCommerce"

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Inline`](/reference/quiz-builder/share-publish/#inline).**

    2. **Adjust the inline settings, then click `Get the code`.** Copy the HTML it gives you.

    3. **Turn on HTML in category descriptions.** See the WooCommerce guide to [allowing HTML in category descriptions](https://woocommerce.com/document/allow-html-in-term-category-tag-descriptions/).

    4. **In your WordPress admin, open `WooCommerce > Products > Categories`.**

    5. **Open a category, click `Edit`, and paste the code into the description field.**

    6. **Save the category.**

    7. **Open the page in your store and check the quiz is there.**

    !!! warning "One quiz per page"

        Embed a single quiz on a page. Two on the same page conflict, and neither loads reliably.

=== "Magento"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Inline`](/reference/quiz-builder/share-publish/#inline).**

    3. **Adjust the inline settings, then click `Get the code`.** Copy the HTML it gives you.

    4. **In your Magento admin, go to `Catalog > Categories` and pick a category.**

    5. **Open `Content` and click `Edit with Page Builder` under `Description`.**

    6. **Drag a row in from `Elements > Rows`, then drag `HTML Code` onto that row.**

    7. **Click the gear icon to open `HTML settings`, then paste the code under `Enter HTML, CSS or JavaScript code`.**

    8. **Save the category.**

    9. **Open the page in your store and check the quiz is there.**

    !!! warning "One quiz per page"

        Embed a single quiz on a page. Two on the same page conflict, and neither loads reliably.

=== "BigCommerce"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Inline`](/reference/quiz-builder/share-publish/#inline).**

    3. **Adjust the inline settings, then click `Get the code`.** Copy the HTML it gives you.

    4. **In BigCommerce, go to `Products > Product Categories` and open a category.**

    5. **Under `Category Details > Description`, switch to the `HTML` editor and paste the code in.**

    6. **Save the category.**

    7. **Open the page in your store and check the quiz is there.**

    !!! warning "One quiz per page"

        Embed a single quiz on a page. Two on the same page conflict, and neither loads reliably.

=== "Standalone"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Inline`](/reference/quiz-builder/share-publish/#inline).**

    3. **Adjust the inline settings, then click `Get the code`.** Copy the HTML it gives you.

    4. **In your store editor, open the collection page you want the quiz on.**

    5. **Find a `Custom HTML` element and paste the code into its settings.**

    6. **Save the page.**

    7. **Open the page in your store and check the quiz is there.**

    !!! warning "One quiz per page"

        Embed a single quiz on a page. Two on the same page conflict, and neither loads reliably.

## FAQs

### Embed a specific quiz

=== "Shopify"

    An inline quiz shows your default quiz. To show another one, put its ID in the `Quiz ID (optional)` field of the `Inline Quiz` section settings.

    ![The Quiz ID field in the Inline Quiz settings](/images/manual_shopifyV2_quizbuilder_share_publish_onlinestore_inline_settings.png)

    !!! info "Finding the Quiz ID"

        In the [Dashboard](/reference/dashboard/), click the `...` beside the quiz and select `Copy Quiz ID`. The ID is case-sensitive.

    !!! note "Shopify Markets"

        With [Shopify Markets](/reference/app-settings/#shopify-markets) set up, the default quiz for the customer's market appears instead of your store default.

=== "Shopify (Legacy)"

    Put the Quiz ID in the `Quiz ID` field of the `Inline Quiz (Legacy)` section settings, then save.

    ![The Quiz ID field in the legacy Inline Quiz settings](/images/how_to_publish_quiz_inline_settings.png)

    If you pasted the code by hand instead, generate it from the [`Share`](/reference/quiz-builder/share-publish/) tab of the quiz you want. The ID is already in the code, as `data-url`.

    !!! info "Finding the Quiz ID"

        In the [Dashboard](/reference/dashboard/), click the `...` beside the quiz and select `Copy Quiz ID`. The ID is case-sensitive.

=== "WooCommerce"

    Generate the embed code from the [`Share`](/reference/quiz-builder/share-publish/) tab of the quiz you want to show. The quiz is named in the code itself, as `data-url`.

    !!! info "Finding the Quiz ID"

        In the [Dashboard](/reference/dashboard/), click the `...` beside the quiz and select `Copy Quiz ID`. The ID is case-sensitive.

=== "Magento"

    Generate the embed code from the [`Share`](/reference/quiz-builder/share-publish/) tab of the quiz you want to show. The quiz is named in the code itself, as `data-url`.

    !!! info "Finding the Quiz ID"

        In the [Dashboard](/reference/dashboard/), click the `...` beside the quiz and select `Copy Quiz ID`. The ID is case-sensitive.

=== "BigCommerce"

    Generate the embed code from the [`Share`](/reference/quiz-builder/share-publish/) tab of the quiz you want to show. The quiz is named in the code itself, as `data-url`.

    !!! info "Finding the Quiz ID"

        In the [Dashboard](/reference/dashboard/), click the `...` beside the quiz and select `Copy Quiz ID`. The ID is case-sensitive.

=== "Standalone"

    Generate the embed code from the [`Share`](/reference/quiz-builder/share-publish/) tab of the quiz you want to show. The quiz is named in the code itself, as `data-url`.

    !!! info "Finding the Quiz ID"

        In the [Dashboard](/reference/dashboard/), click the `...` beside the quiz and select `Copy Quiz ID`. The ID is case-sensitive.

### Fixing the size of the inline quiz

By default the quiz starts at the height you set, then grows to fit each question. Fix the height and it stays as it is throughout.

=== "Shopify"

    1. **In your Shopify admin, go to `Online Store > Themes` and click `Customize`.**

    2. **Click the `Inline Quiz` section already on the page.**

    3. **Set `Quiz height`, and pick the unit under `Quiz height (unit)`.**

        ![The height settings in the Inline Quiz panel](/images/manual_shopifyV2_quizbuilder_share_publish_onlinestore_inline_settings.png)

    4. **Turn `Fixed height` on.** The quiz then keeps that height for every question.

    5. **Click `Save`, then open the page and check the height holds as you answer.**

    !!! note "The first question always uses the set height"

        Shopify requires it, so the page does not jump about as it loads. Without `Fixed height`, the quiz expands to fit from the second question onward.

=== "Shopify (Legacy)"

    **With the theme section**

    1. **In your Shopify admin, go to `Online Store > Themes` and click `Customize`.**

    2. **Click the `Inline Quiz` section already on the page.**

    3. **Set the quiz height and check `Fixed size`.**

    4. **Click `Save`, then open the page and check the height holds as you answer.**

    **With pasted code**

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder, pick [`Inline`](/reference/quiz-builder/share-publish/#inline), then `Show Instructions for Legacy Themes`.**

    2. **Set the quiz height and check `Fixed size`.**

    3. **Click `Get code`** and copy the new HTML.

    4. **Replace the old embed code on your page with the new one.**

    5. **Open the page and check the height holds as you answer.**

=== "WooCommerce"

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Inline`](/reference/quiz-builder/share-publish/#inline).**

    2. **Set the quiz height and check `Fixed size`.**

    3. **Click `Get code`** and copy the new HTML.

    4. **Replace the old embed code on your page with the new one**, on the [homepage](#embed-an-inline-quiz-on-the-homepage), a [landing page](#embed-an-inline-quiz-on-a-dedicated-landing-page) or a [collection page](#embed-an-inline-quiz-on-a-specific-collectioncategory).

    5. **Open the page and check the height holds as you answer.**

=== "Magento"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Inline`](/reference/quiz-builder/share-publish/#inline).**

    3. **Set the quiz height and check `Fixed size`.**

    4. **Click `Get code`** and copy the new HTML.

    5. **Replace the old embed code on your page with the new one**, on the [homepage](#embed-an-inline-quiz-on-the-homepage), a [landing page](#embed-an-inline-quiz-on-a-dedicated-landing-page) or a [collection page](#embed-an-inline-quiz-on-a-specific-collectioncategory).

    6. **Open the page and check the height holds as you answer.**

=== "BigCommerce"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Inline`](/reference/quiz-builder/share-publish/#inline).**

    3. **Set the quiz height and check `Fixed size`.**

    4. **Click `Get code`** and copy the new HTML.

    5. **Replace the old embed code on your page with the new one**, on the [homepage](#embed-an-inline-quiz-on-the-homepage), a [landing page](#embed-an-inline-quiz-on-a-dedicated-landing-page) or a [collection page](#embed-an-inline-quiz-on-a-specific-collectioncategory).

    6. **Open the page and check the height holds as you answer.**

=== "Standalone"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Inline`](/reference/quiz-builder/share-publish/#inline).**

    3. **Set the quiz height and check `Fixed size`.**

    4. **Click `Get code`** and copy the new HTML.

    5. **Replace the old embed code on your page with the new one**, on the [homepage](#embed-an-inline-quiz-on-the-homepage), a [landing page](#embed-an-inline-quiz-on-a-dedicated-landing-page) or a [collection page](#embed-an-inline-quiz-on-a-specific-collectioncategory).

    6. **Open the page and check the height holds as you answer.**

### Preventing auto-scroll in inline quiz

Auto-scroll moves the page as the customer answers, so the quiz stays in view. Turn it off to leave the page where it is.

=== "Shopify"

    This version has two auto-scroll settings, and both are `Disabled` by default, so there is usually nothing to turn off.

    1. **In your Shopify admin, go to `Online Store > Themes` and click `Customize`.**

    2. **Click the `Inline Quiz` section already on the page.**

    3. **Set `Auto-scroll on retake quiz` and `Auto-scroll on question change` to `Disabled`.**

        The alternatives are `Top of the page` and `Top of the quiz`.

        ![The auto-scroll settings in the Inline Quiz panel](/images/manual_shopifyV2_quizbuilder_share_publish_onlinestore_inline_settings.png)

    4. **Click `Save`, then take the quiz and check the page stays put.**

=== "Shopify (Legacy)"

    **With the theme section**

    1. **In your Shopify admin, go to `Online Store > Themes` and click `Customize`.**

    2. **Click the `Inline Quiz` section already on the page.**

    3. **Uncheck `Automatic Scroll into View`.**

    4. **Click `Save`, then take the quiz and check the page stays put.**

    **With pasted code**

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder, pick [`Inline`](/reference/quiz-builder/share-publish/#inline), then `Show Instructions for Legacy Themes`.**

    2. **Click `Get code`** and copy the HTML.

    3. **Add `data-autoscroll="false"` to the quiz element.**

        ```html
        <div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/dbqHqN" data-autoscroll="false" style="margin: 10px auto; width: 100%; height: 600px; display: flex;"></div>
        ```

    4. **Replace the old embed code on your page with the edited one.**

    5. **Take the quiz and check the page stays put.**

=== "WooCommerce"

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Inline`](/reference/quiz-builder/share-publish/#inline).**

    2. **Click `Get code`** and copy the HTML.

    3. **Add `data-autoscroll="false"` to the quiz element.**

        ```html
        <div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/dbqHqN" data-autoscroll="false" style="margin: 10px auto; width: 100%; height: 600px; display: flex;"></div>
        ```

    4. **Replace the old embed code on your page with the edited one**, on the [homepage](#embed-an-inline-quiz-on-the-homepage), a [landing page](#embed-an-inline-quiz-on-a-dedicated-landing-page) or a [collection page](#embed-an-inline-quiz-on-a-specific-collectioncategory).

    5. **Take the quiz and check the page stays put.**

=== "Magento"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Inline`](/reference/quiz-builder/share-publish/#inline).**

    3. **Click `Get code`** and copy the HTML.

    4. **Add `data-autoscroll="false"` to the quiz element.**

        ```html
        <div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/dbqHqN" data-autoscroll="false" style="margin: 10px auto; width: 100%; height: 600px; display: flex;"></div>
        ```

    5. **Replace the old embed code on your page with the edited one**, on the [homepage](#embed-an-inline-quiz-on-the-homepage), a [landing page](#embed-an-inline-quiz-on-a-dedicated-landing-page) or a [collection page](#embed-an-inline-quiz-on-a-specific-collectioncategory).

    6. **Take the quiz and check the page stays put.**

=== "BigCommerce"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Inline`](/reference/quiz-builder/share-publish/#inline).**

    3. **Click `Get code`** and copy the HTML.

    4. **Add `data-autoscroll="false"` to the quiz element.**

        ```html
        <div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/dbqHqN" data-autoscroll="false" style="margin: 10px auto; width: 100%; height: 600px; display: flex;"></div>
        ```

    5. **Replace the old embed code on your page with the edited one**, on the [homepage](#embed-an-inline-quiz-on-the-homepage), a [landing page](#embed-an-inline-quiz-on-a-dedicated-landing-page) or a [collection page](#embed-an-inline-quiz-on-a-specific-collectioncategory).

    6. **Take the quiz and check the page stays put.**

=== "Standalone"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Inline`](/reference/quiz-builder/share-publish/#inline).**

    3. **Click `Get code`** and copy the HTML.

    4. **Add `data-autoscroll="false"` to the quiz element.**

        ```html
        <div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/dbqHqN" data-autoscroll="false" style="margin: 10px auto; width: 100%; height: 600px; display: flex;"></div>
        ```

    5. **Replace the old embed code on your page with the edited one**, on the [homepage](#embed-an-inline-quiz-on-the-homepage), a [landing page](#embed-an-inline-quiz-on-a-dedicated-landing-page) or a [collection page](#embed-an-inline-quiz-on-a-specific-collectioncategory).

    6. **Take the quiz and check the page stays put.**

### The quiz you are looking for does not exist

This error means the quiz cannot be found, either because it is unpublished or because the embed points at the wrong one.

![The error an inline quiz shows when it cannot find the quiz](/images/how_to_publish_shipifyV2_V1publisherror.png)

=== "Shopify"

    !!! warning "Shopify 1.0 themes cannot run this"

        A quiz built in the Built for Shopify version needs an app section, and app sections are an Online Store 2.0 feature. A Shopify 1.0 theme does not support them.

        Upgrade to an Online Store 2.0 theme to use them.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and check the quiz is published.**

    2. **Check you added `Inline Quiz` and not `Inline Quiz (Legacy)`.** The legacy section serves quizzes from the legacy app, so it cannot find a quiz built in this version.

        ![The two inline quiz sections in the Apps group](/images/how_to_publish_shipifyV2_V1publisherrorinlinequiz.png)

    3. **Click the `Inline Quiz` section and check the `Quiz ID (optional)` field.** Leave it empty for your default quiz, or paste the right ID. The ID is case-sensitive.

    4. **Click `Save`, then reload the page.**

=== "Shopify (Legacy)"

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and check the quiz is published**, with the top-right `Publish` button.

    2. **Copy the `Quiz ID` from [Quiz settings](/reference/quiz-builder/quiz-settings/#general).** The ID is case-sensitive.

    3. **Check the `Inline Quiz (Legacy)` section holds that ID**, or that your pasted code carries the matching `data-url`.

        ![Pasting the Quiz ID into the legacy inline quiz settings](/images/how_to_publish_shipifyV2_V1publisherrorinlinev1.png)

    4. **Click `Save`, then reload the page.**

=== "WooCommerce"

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and check the quiz is published**, with the top-right `Publish` button.

    2. **Regenerate the code from [`Share`](/reference/quiz-builder/share-publish/) and paste it in again.** An old code can point at a quiz that has since changed.

    3. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    4. **Save the page, then reload it.**

=== "Magento"

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and check the quiz is published**, with the top-right `Publish` button.

    2. **Regenerate the code from [`Share`](/reference/quiz-builder/share-publish/) and paste it in again.** An old code can point at a quiz that has since changed.

    3. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    4. **Save the page, then reload it.**

=== "BigCommerce"

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and check the quiz is published**, with the top-right `Publish` button.

    2. **Regenerate the code from [`Share`](/reference/quiz-builder/share-publish/) and paste it in again.** An old code can point at a quiz that has since changed.

    3. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    4. **Save the page, then reload it.**

=== "Standalone"

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and check the quiz is published**, with the top-right `Publish` button.

    2. **Regenerate the code from [`Share`](/reference/quiz-builder/share-publish/) and paste it in again.** An old code can point at a quiz that has since changed.

    3. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    4. **Save the page, then reload it.**

---

This article explains how to put a quiz inside a page of your store, and how to control its height and its scrolling.