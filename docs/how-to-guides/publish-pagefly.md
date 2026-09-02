---
description: "Learn how to integrate RevenueHunt quiz with PageFly page builder using the legacy app version."
icon: material/butterfly-outline
---

# How to Publish a Quiz on a PageFly Page

PageFly builds Shopify landing pages and product pages. A quiz can sit inside one of those pages, or the page can carry a button that opens it.

## Embed the quiz inline on a PageFly page

=== "Shopify"

    !!! note "Not part of this version"

        The PageFly RevenueHunt element works with the legacy app only. The new 💎 Built for Shopify version cannot be embedded into a PageFly page directly.

        Point a button at the quiz instead. See [Link to the quiz from a PageFly button](#link-to-the-quiz-from-a-pagefly-button).

=== "Shopify (Legacy)"

    PageFly carries a RevenueHunt element. Activate it once, then drop it onto any page you build.

    1. **Open the PageFly editor, on a new page or one you already have.**

    2. **Go to `Third-party elements` and click `+Add app`.**

        ![The Add app button under Third-party elements in PageFly](/images/how_to_pagefly_connectrevenuehunt.png)

    3. **Search for `RevenueHunt` and click `Activate`.**

        ![Activating the RevenueHunt app in PageFly](/images/how_to_pagefly_connectrevenuehunt_activate.png)

    4. **Go back to `Third-party elements`, click `RevenueHunt`, and drag the quiz element onto the page.**

        ![Dragging the RevenueHunt element onto a PageFly page](/images/how_to_pagefly_connectrevenuehunt_dragdrop.png)

    5. **Click the element, then enter your quiz shortcode in the settings panel on the right.**

        !!! info "What the shortcode is"

            The shortcode is the quiz URL, in this shape.

            `https://admin.revenuehunt.com/public/quiz/QUIZ_ID`

            Replace `QUIZ_ID` with the ID of your quiz, which you will find as `Quiz ID` in [Quiz settings](/reference/quiz-builder/quiz-settings/#general).

            ![The shortcode field in the PageFly element settings](/images/how_to_pagefly_connectrevenuehunt_provideshortcode.png)

    6. **Click `Save`.**

    7. **Click `Preview`, then use the page as a customer would and check the quiz opens.**

        ![A RevenueHunt quiz previewed on a PageFly page](/images/how_to_pagefly_connectrevenuehunt_preview.png)

=== "WooCommerce"

    !!! note "PageFly is a Shopify page builder"

        It has no WooCommerce version, so there is no PageFly page to put a quiz on here.

        See [How to Publish a Quiz on Your Website](/how-to-guides/publish-quiz/) for the ways that do work on WooCommerce.

=== "Magento"

    !!! note "PageFly is a Shopify page builder"

        It has no Magento version, so there is no PageFly page to put a quiz on here.

        See [How to Publish a Quiz on Your Website](/how-to-guides/publish-quiz/) for the ways that do work on Magento.

=== "BigCommerce"

    !!! note "PageFly is a Shopify page builder"

        It has no BigCommerce version, so there is no PageFly page to put a quiz on here.

        See [How to Publish a Quiz on Your Website](/how-to-guides/publish-quiz/) for the ways that do work on BigCommerce.

=== "Standalone"

    !!! note "PageFly is a Shopify page builder"

        It has no Standalone version, so there is no PageFly page to put a quiz on here.

        See [How to Publish a Quiz on Your Website](/how-to-guides/publish-quiz/) for the ways that do work on Standalone.

## Link to the quiz from a PageFly button

=== "Shopify"

    The quiz sits on a Shopify page of its own, and the PageFly page carries a button that opens it.

    1. **Publish the quiz on a page of its own in Shopify.** See [How to Embed an Inline Quiz on Your Store](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page).

    2. **Open the PageFly editor, on a new page or one you already have.**

    3. **Go to `Elements` and drag a `Button` element onto the page.**

    4. **In the button settings, set `Action` to `Go to URL` and paste the address of the quiz page.**

        ![The Go to URL action in the PageFly button settings](/images/how_to_pagefly_addbutton.png)

    5. **Click `Save`.**

    6. **Click `Preview`, then use the page as a customer would and check the quiz opens.**

=== "Shopify (Legacy)"

    A button works here too, and it is the simpler route if you would rather not embed the quiz in the page.

    1. **Open the PageFly editor, on a new page or one you already have.**

    2. **Go to `Elements` and drag a `Button` element onto the page.**

    3. **In the button settings, set `Action` to `Go to URL`, then paste one of these.**

        - [A quiz link you can share anywhere](/how-to-guides/publish-quiz-external-link/)
        - [The address of a page with the quiz embedded on it](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page)

        ![The Go to URL action in the PageFly button settings](/images/how_to_pagefly_addbutton.png)

    4. **Click `Save`.**

    5. **Click `Preview`, then use the page as a customer would and check the quiz opens.**

=== "WooCommerce"

    !!! note "PageFly is a Shopify page builder"

        It has no WooCommerce version, so there is no PageFly page to put a quiz on here.

        See [How to Publish a Quiz on Your Website](/how-to-guides/publish-quiz/) for the ways that do work on WooCommerce.

=== "Magento"

    !!! note "PageFly is a Shopify page builder"

        It has no Magento version, so there is no PageFly page to put a quiz on here.

        See [How to Publish a Quiz on Your Website](/how-to-guides/publish-quiz/) for the ways that do work on Magento.

=== "BigCommerce"

    !!! note "PageFly is a Shopify page builder"

        It has no BigCommerce version, so there is no PageFly page to put a quiz on here.

        See [How to Publish a Quiz on Your Website](/how-to-guides/publish-quiz/) for the ways that do work on BigCommerce.

=== "Standalone"

    !!! note "PageFly is a Shopify page builder"

        It has no Standalone version, so there is no PageFly page to put a quiz on here.

        See [How to Publish a Quiz on Your Website](/how-to-guides/publish-quiz/) for the ways that do work on Standalone.

---

This article explains the two ways to get a RevenueHunt quiz onto a PageFly page, and which of them each version supports.