# How to Publish Quiz on PageFly Page

=== "Shopify" 

    PageFly currently integrates only with the legacy version of RevenueHunt app for Shopify. The new `💎Built for Shopify` version of RevenueHunt app **does not** support embedding quizzes directly into PageFly pages.

    !!! example "Possible Workaround"
        A possible workaround is following these instructions on [How to Publish the Quiz on a New Page in Shopify](https://docs.revenuehunt.com/how-to-guides/publish-quiz-inline/#embedding-an-inline-quiz-on-a-dedicated-landing-page) and then adding a link to that page where the quiz is embeded to a **button or a link** on your PageFly page.

        1. Publish the quiz on a new page in Shopify by following the instructions on [How to Publish the Quiz on a New Page in Shopify](https://docs.revenuehunt.com/how-to-guides/publish-quiz-inline/#embedding-an-inline-quiz-on-a-dedicated-landing-page).
        2. Open the PageFly editor and create a new page or open an existing page.
        3. In the page builder, go to `Elements` and add a `Button` element to your page by draggin it.
        4. In Button settings, under Action select `Go to URL` and enter the URL of the page where the quiz is embeded.
            ![Button Settings](/images/how_to_pagefly_addbutton.png)
        5. Click `Save` and the button will be added to your page.
        6. Click `Preview` to see the button on the page.


=== "Shopify (Legacy)"

    PageFly currently integrates only with the **legacy** version of RevenueHunt app for Shopify. There are several ways to embed a quiz on a PageFly page. Check the instructions below for the method that suits you best.

    **Embeding Quiz Inline on Pagefly Page**

    1. Open the PageFly editor and create a new page or open an existing page.
    2. Integrate RevenueHunt. Go to `Third-party elements` > `+Add app`.
        ![Add App](/images/how_to_pagefly_connectrevenuehunt.png)
    3. Search for `RevenueHunt`. Click `Activate`. 
        ![Activate App](/images/how_to_pagefly_connectrevenuehunt_activate.png)
    4. Go back to `Third-party elements`. Click on `RevenueHunt` and a new Shop Quiz embed element will become available. Drag and drop it to the page.
        ![Third-party elements](/images/how_to_pagefly_connectrevenuehunt_dragdrop.png)
    5. Click on the element and a settings panel will appear on the right side of the screen.Enter the shortcode of the quiz you want to embed. The shortcode follows the following format:

        !!! info "Shortcode Format"
            `https://admin.revenuehunt.com/public/quiz/QUIZ_ID` 
            
            where `QUIZ_ID` is the ID of the quiz you want to embed.

            ![shortcode example](/images/how_to_pagefly_connectrevenuehunt_provideshortcode.png)

            To find your Quiz ID check the [Quiz Settings](/reference/quiz-builder/quiz-settings/).
    6. Click `Save` and the quiz will be embedded on the page.
    7. Click `Preview` to see the quiz on the page.
        ![Preview](/images/how_to_pagefly_connectrevenuehunt_preview.png)

    **Adding a Link to the Quiz via PageFly Button**

    1. Open the PageFly editor and create a new page or open an existing page.
    2. In the page builder, go to `Elements` and add a `Button` element to your page by draggin it.
    3. In Button settings, under Action select `Go to URL` and enter the [URL of the quiz link](/how-to-guides/publish-quiz-external-link/) or the [URL of the page where the quiz is embeded](/how-to-guides/publish-quiz-inline/#embedding-an-inline-quiz-on-a-dedicated-landing-page).
        ![Button Settings](/images/how_to_pagefly_addbutton.png)
    4. Click `Save` and the button will be added to your page.
    5. Click `Preview` to see the button on the page.


=== "WooCommerce"

    Not applicable.

=== "Magento"

    Not applicable.

=== "BigCommerce"

    Not applicable.

=== "Standalone"

    Not applicable.

---
This article explains how to publish a Revenue Hunt quiz on a PageFly page in Shopify.