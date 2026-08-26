---
description: "Learn how to integrate RevenueHunt quiz with PageFly page builder using the legacy app version."
icon: material/butterfly-outline
---

# How to Publish Quiz on PageFly Page

=== "Shopify"

    PageFly currently integrates only with the legacy version of the RevenueHunt app for Shopify. The new `💎Built for Shopify` version of the RevenueHunt app **does not** support embedding quizzes directly into PageFly pages.

    !!! tip "Possible Workaround"

        Publish the quiz on its own Shopify page, then point a **button or link** on your PageFly page at it.

        1. Publish the quiz on a new page in Shopify by following the instructions on [How to Publish the Quiz on a New Page in Shopify](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page).
        2. Open the PageFly editor and create a new page or open an existing page.
        3. In the page builder, go to `Elements` and add a `Button` element to your page by dragging it.
        4. In Button settings, under Action select `Go to URL` and enter the URL of the page where the quiz is embedded.
            ![Button Settings](/images/how_to_pagefly_addbutton.png)
        5. Click `Save` and the button will be added to your page.
        6. Click `Preview` to see the button on the page.

=== "Shopify (Legacy)"

    PageFly currently integrates only with the **legacy** version of the RevenueHunt app for Shopify. There are several ways to embed a quiz on a PageFly page. Check the instructions below for the method that suits you best.

    **Embedding a Quiz Inline on a PageFly Page**

    1. Open the PageFly editor and create a new page or open an existing page.
    2. Integrate RevenueHunt. Go to `Third-party elements` > `+Add app`.
        ![Add App](/images/how_to_pagefly_connectrevenuehunt.png)
    3. Search for `RevenueHunt`. Click `Activate`.
        ![Activate App](/images/how_to_pagefly_connectrevenuehunt_activate.png)
    4. Go back to `Third-party elements`. Click `RevenueHunt`, and a new quiz embed element becomes available. Drag and drop it onto the page.
        ![Third-party elements](/images/how_to_pagefly_connectrevenuehunt_dragdrop.png)
    5. Click the element. A settings panel opens on the right of the screen. Enter the shortcode of the quiz you want to embed.

        !!! info "Shortcode Format"
            The shortcode is the quiz URL:
            `https://admin.revenuehunt.com/public/quiz/QUIZ_ID`

            `QUIZ_ID` is the ID of the quiz you want to embed.

            ![shortcode example](/images/how_to_pagefly_connectrevenuehunt_provideshortcode.png)

            To find your Quiz ID check the [Quiz Settings](/reference/quiz-builder/quiz-settings/).
    6. Click `Save` and the quiz will be embedded on the page.
    7. Click `Preview` to see the quiz on the page.
        ![Preview](/images/how_to_pagefly_connectrevenuehunt_preview.png)

    **Adding a Link to the Quiz via PageFly Button**

    1. Open the PageFly editor and create a new page or open an existing page.
    2. In the page builder, go to `Elements` and add a `Button` element to your page by dragging it.
    3. In Button settings, under Action select `Go to URL` and enter the [URL of the quiz link](/how-to-guides/publish-quiz-external-link/) or the [URL of the page where the quiz is embedded](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page).
        ![Button Settings](/images/how_to_pagefly_addbutton.png)
    4. Click `Save` and the button will be added to your page.
    5. Click `Preview` to see the button on the page.

=== "WooCommerce"

    !!! note "Platform Availability"

        PageFly is a Shopify page builder, so this does not apply to WooCommerce.

=== "Magento"

    !!! note "Platform Availability"

        PageFly is a Shopify page builder, so this does not apply to Magento.

=== "BigCommerce"

    !!! note "Platform Availability"

        PageFly is a Shopify page builder, so this does not apply to BigCommerce.

=== "Standalone"

    !!! note "Platform Availability"

        PageFly is a Shopify page builder, so this does not apply to Standalone.

---
This article explains how to publish a RevenueHunt quiz on a PageFly page in Shopify.