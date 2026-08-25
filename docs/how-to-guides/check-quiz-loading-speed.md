---
description: "Learn how to diagnose and optimize RevenueHunt quiz loading speed to ensure smooth user experience on your website."
icon: material/loading
---

# How to Check Quiz Loading Speed

A quiz on your store has to load quickly. If yours is slow, the cause is often not the quiz but another resource on the same page.

This article explains how to find what is slowing the quiz down, and how to fix it.




=== "Shopify"

    1. **Verify direct quiz link performance**

        Isolate the quiz from the rest of your site, to see whether the quiz or the site is slow.

        - **Locate Your Quiz Link**: In the app, go to your quiz and open the `Share -> External` tab to copy its direct link. With the Built for Shopify version the quiz runs natively inside your theme, so the link is your own storefront URL plus the quiz hash.
            - The link should look something like [https://your-store.com/#quiz-rkHm6Y](https://your-store.com/#quiz-rkHm6Y), where `your-store.com` is your storefront domain and `rkHm6Y` is your unique `quiz ID`.
        - **Test Loading Speed**: Open the direct link in a browser to see how quickly the quiz loads independently of the rest of your store. Ideally, the quiz should load in less than one second.

        If the quiz loads quickly via the direct link, the slow loading times are likely caused by other elements on your website.


        !!! tip

            Run the direct quiz link through [Google PageSpeed Insights](https://pagespeed.web.dev/) and/or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) to check its performance in isolation.


    2. **Analyze your website's loading order**

        !!! info
            The new Built for Shopify version of the RevenueHunt app integrates the quiz as a native Shopify block within the Theme.

        !!! note "About the large inline quiz configuration"

            When inspecting your page source, you may notice a large inline `window.quizzes` JSON object (often 100-200 KB). This is your quiz's configuration: its questions, conditional logic, results pages, recommendation rules, design and translations. It is embedded in the page so the quiz opens at once, with no extra network request when the customer interacts.

            That uncompressed size looks alarming, but it is not the bottleneck:

            - **It is compressed on the wire.** Shopify serves your pages gzip or brotli compressed. A 150 KB configuration usually ships at **10-15 KB**, less than one product thumbnail.
            - **It is not rendered DOM.** It sits inside a `<script>` tag, so it adds no layout or paint cost.
            - **It loads asynchronously.** It never blocks the page from rendering.

            You can confirm the real transferred size in your browser's `Network` tab (look at the `Size` column, not `Content` size).

        The loading sequence of your own resources shows what is slowing the quiz down on your site.

        - **Open Developer Tools**: Right-click on your website in the browser and select `Inspect` to open the developer tools.
        - **Review Network and Performance**: Navigate to the `Network` or `Performance` tabs to examine which resources are loading and how long each takes.

        Look for resources that significantly delay loading times, as these are likely culprits affecting the quiz's performance on your site.


        !!! tip

            Run your full page through [Google PageSpeed Insights](https://pagespeed.web.dev/) or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk). The report lists the heaviest items, usually images, fonts and third-party scripts, with the time each one costs.




    3. **Optimize your website's resources**

        Ask your developer to compress the images, minify the CSS and JavaScript, and remove any plugin or widget you do not need.

        - **Optimize Third-Party Widgets**: Review any third-party widgets or scripts (e.g., marketing, chat tools) on your site. Ensure that they are loaded asynchronously or deferred to load after the quiz.

        - **Check Shopify Performance Reports**: Use [Shopify’s built-in tools](https://help.shopify.com/en/manual/online-store/web-performance/improving-web-performance) to check for any resources that might be blocking the quiz from loading quickly.

=== "Shopify (Legacy)"

    !!! note "Raw size vs. transferred size"

        The byte sizes in your page source are uncompressed. Shopify serves your pages gzip or brotli compressed, and the quiz script too, so the browser downloads far less than those numbers suggest. A 150 KB payload usually ships at 10-15 KB. Check the real transferred size in the `Network` tab of your browser, in the `Size` column rather than `Content`, before deciding something is heavy.

    1. **Verify direct quiz link performance**

        Isolate the quiz from the rest of your site, to see whether the quiz or the site is slow.

        - **Locate Your Quiz Link**: Find the direct URL of your quiz. This can be obtained from the `Share -> External` tab of your quiz platform.
            - The link should look something like [https://admin.revenuehunt.com/public/quiz/rkHm6Y](https://admin.revenuehunt.com/public/quiz/rkHm6Y) or [https://skincarequiz.myshopify.com/#quiz-rkHm6Y](https://skincarequiz.myshopify.com/#quiz-rkHm6Y), where `rkHm6Y` represents your unique `quiz ID`.
        - **Test Loading Speed**: Open the direct link in a browser to see how quickly the quiz loads independently of your site. Ideally, the quiz should load in less than one second.

        If the quiz loads quickly via the direct link, the slow loading times are likely caused by other elements on your website.


        !!! tip

            Run the direct quiz link through [Google PageSpeed Insights](https://pagespeed.web.dev/) and/or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) to check its performance in isolation.


    2. **Analyze your website's loading order**

        The loading sequence of your own resources shows what is slowing the quiz down on your site.

        - **Open Developer Tools**: Right-click on your website in the browser and select `Inspect` to open the developer tools.
        - **Review Network and Performance**: Navigate to the `Network` or `Performance` tabs to examine which resources are loading and how long each takes.

        Look for resources that significantly delay loading times, as these are likely culprits affecting the quiz's performance on your site.


        !!! tip

            Run your full page through [Google PageSpeed Insights](https://pagespeed.web.dev/) or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk). The report lists the heaviest items, usually images, fonts and third-party scripts, with the time each one costs.


    3. **Try direct iframe embedding**

        An iFrame keeps the quiz clear of the external scripts that slow your page down.

        **Replace Embed Code**: The standard embed code from the `Share` tab loads the quiz through a JavaScript file, `embed.js`. Use an iFrame embed code instead. The quiz then loads independently of the other scripts on your site.

        Replace this code:

        ```html
        <div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/rkHm6Y" style="..."></div>
        ```

        With this:

        ```html
        <div class="rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/rkHm6Y" style="..."><iframe src="https://admin.revenuehunt.com/public/quiz/rkHm6Y" id="DPIyZ" style="..."></iframe></div>
        ```

        This second block of code includes the quiz iFrame directly. This will start rendering the quiz before the embed.js code is loaded.


    4. **Optimize your website's resources**

        Ask your developer to compress the images, minify the CSS and JavaScript, and remove any plugin or widget you do not need.

=== "WooCommerce"


    1. **Verify direct quiz link performance**

        Isolate the quiz from the rest of your site, to see whether the quiz or the site is slow.

        - **Locate Your Quiz Link**: Find the direct URL of your quiz. This can be obtained from the `Share -> External` tab of your quiz platform.
            - The link should look something like [https://admin.revenuehunt.com/public/quiz/rkHm6Y](https://admin.revenuehunt.com/public/quiz/rkHm6Y) or [https://skincarequiz.myshopify.com/#quiz-rkHm6Y](https://skincarequiz.myshopify.com/#quiz-rkHm6Y), where `rkHm6Y` represents your unique `quiz ID`.
        - **Test Loading Speed**: Open the direct link in a browser to see how quickly the quiz loads independently of your site. Ideally, the quiz should load in less than one second.

        If the quiz loads quickly via the direct link, the slow loading times are likely caused by other elements on your website.


        !!! tip

            Run the direct quiz link through [Google PageSpeed Insights](https://pagespeed.web.dev/) and/or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) to check its performance in isolation.


    2. **Analyze your website's loading order**

        The loading sequence of your own resources shows what is slowing the quiz down on your site.

        - **Open Developer Tools**: Right-click on your website in the browser and select `Inspect` to open the developer tools.
        - **Review Network and Performance**: Navigate to the `Network` or `Performance` tabs to examine which resources are loading and how long each takes.

        Look for resources that significantly delay loading times, as these are likely culprits affecting the quiz's performance on your site.


        !!! tip

            Run your full page through [Google PageSpeed Insights](https://pagespeed.web.dev/) or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk). The report lists the heaviest items, usually images, fonts and third-party scripts, with the time each one costs.


    3. **Try direct iframe embedding**

        An iFrame keeps the quiz clear of the external scripts that slow your page down.

        **Replace Embed Code**: The standard embed code from the `Share` tab loads the quiz through a JavaScript file, `embed.js`. Use an iFrame embed code instead. The quiz then loads independently of the other scripts on your site.

        Replace this code:

        ```html
        <div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/rkHm6Y" style="..."></div>
        ```

        With this:

        ```html
        <div class="rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/rkHm6Y" style="..."><iframe src="https://admin.revenuehunt.com/public/quiz/rkHm6Y" id="DPIyZ" style="..."></iframe></div>
        ```

        This second block of code includes the quiz iFrame directly. This will start rendering the quiz before the embed.js code is loaded.


    4. **Optimize your website's resources**

        Ask your developer to compress the images, minify the CSS and JavaScript, and remove any plugin or widget you do not need.

=== "Magento"


    1. **Verify direct quiz link performance**

        Isolate the quiz from the rest of your site, to see whether the quiz or the site is slow.

        - **Locate Your Quiz Link**: Find the direct URL of your quiz. This can be obtained from the `Share -> External` tab of your quiz platform.
            - The link should look something like [https://admin.revenuehunt.com/public/quiz/rkHm6Y](https://admin.revenuehunt.com/public/quiz/rkHm6Y) or [https://skincarequiz.myshopify.com/#quiz-rkHm6Y](https://skincarequiz.myshopify.com/#quiz-rkHm6Y), where `rkHm6Y` represents your unique `quiz ID`.
        - **Test Loading Speed**: Open the direct link in a browser to see how quickly the quiz loads independently of your site. Ideally, the quiz should load in less than one second.

        If the quiz loads quickly via the direct link, the slow loading times are likely caused by other elements on your website.


        !!! tip

            Run the direct quiz link through [Google PageSpeed Insights](https://pagespeed.web.dev/) and/or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) to check its performance in isolation.


    2. **Analyze your website's loading order**

        The loading sequence of your own resources shows what is slowing the quiz down on your site.

        - **Open Developer Tools**: Right-click on your website in the browser and select `Inspect` to open the developer tools.
        - **Review Network and Performance**: Navigate to the `Network` or `Performance` tabs to examine which resources are loading and how long each takes.

        Look for resources that significantly delay loading times, as these are likely culprits affecting the quiz's performance on your site.


        !!! tip

            Run your full page through [Google PageSpeed Insights](https://pagespeed.web.dev/) or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk). The report lists the heaviest items, usually images, fonts and third-party scripts, with the time each one costs.


    3. **Try direct iframe embedding**

        An iFrame keeps the quiz clear of the external scripts that slow your page down.

        **Replace Embed Code**: The standard embed code from the `Share` tab loads the quiz through a JavaScript file, `embed.js`. Use an iFrame embed code instead. The quiz then loads independently of the other scripts on your site.

        Replace this code:

        ```html
        <div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/rkHm6Y" style="..."></div>
        ```

        With this:

        ```html
        <div class="rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/rkHm6Y" style="..."><iframe src="https://admin.revenuehunt.com/public/quiz/rkHm6Y" id="DPIyZ" style="..."></iframe></div>
        ```

        This second block of code includes the quiz iFrame directly. This will start rendering the quiz before the embed.js code is loaded.


    4. **Optimize your website's resources**

        Ask your developer to compress the images, minify the CSS and JavaScript, and remove any plugin or widget you do not need.

=== "BigCommerce"


    1. **Verify direct quiz link performance**

        Isolate the quiz from the rest of your site, to see whether the quiz or the site is slow.

        - **Locate Your Quiz Link**: Find the direct URL of your quiz. This can be obtained from the `Share -> External` tab of your quiz platform.
            - The link should look something like [https://admin.revenuehunt.com/public/quiz/rkHm6Y](https://admin.revenuehunt.com/public/quiz/rkHm6Y) or [https://skincarequiz.myshopify.com/#quiz-rkHm6Y](https://skincarequiz.myshopify.com/#quiz-rkHm6Y), where `rkHm6Y` represents your unique `quiz ID`.
        - **Test Loading Speed**: Open the direct link in a browser to see how quickly the quiz loads independently of your site. Ideally, the quiz should load in less than one second.

        If the quiz loads quickly via the direct link, the slow loading times are likely caused by other elements on your website.


        !!! tip

            Run the direct quiz link through [Google PageSpeed Insights](https://pagespeed.web.dev/) and/or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) to check its performance in isolation.


    2. **Analyze your website's loading order**

        The loading sequence of your own resources shows what is slowing the quiz down on your site.

        - **Open Developer Tools**: Right-click on your website in the browser and select `Inspect` to open the developer tools.
        - **Review Network and Performance**: Navigate to the `Network` or `Performance` tabs to examine which resources are loading and how long each takes.

        Look for resources that significantly delay loading times, as these are likely culprits affecting the quiz's performance on your site.


        !!! tip

            Run your full page through [Google PageSpeed Insights](https://pagespeed.web.dev/) or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk). The report lists the heaviest items, usually images, fonts and third-party scripts, with the time each one costs.


    3. **Try direct iframe embedding**

        An iFrame keeps the quiz clear of the external scripts that slow your page down.

        **Replace Embed Code**: The standard embed code from the `Share` tab loads the quiz through a JavaScript file, `embed.js`. Use an iFrame embed code instead. The quiz then loads independently of the other scripts on your site.

        Replace this code:

        ```html
        <div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/rkHm6Y" style="..."></div>
        ```

        With this:

        ```html
        <div class="rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/rkHm6Y" style="..."><iframe src="https://admin.revenuehunt.com/public/quiz/rkHm6Y" id="DPIyZ" style="..."></iframe></div>
        ```

        This second block of code includes the quiz iFrame directly. This will start rendering the quiz before the embed.js code is loaded.


    4. **Optimize your website's resources**

        Ask your developer to compress the images, minify the CSS and JavaScript, and remove any plugin or widget you do not need.

=== "Standalone"


    1. **Verify direct quiz link performance**

        Isolate the quiz from the rest of your site, to see whether the quiz or the site is slow.

        - **Locate Your Quiz Link**: Find the direct URL of your quiz. This can be obtained from the `Share -> External` tab of your quiz platform.
            - The link should look something like [https://admin.revenuehunt.com/public/quiz/rkHm6Y](https://admin.revenuehunt.com/public/quiz/rkHm6Y) or [https://skincarequiz.myshopify.com/#quiz-rkHm6Y](https://skincarequiz.myshopify.com/#quiz-rkHm6Y), where `rkHm6Y` represents your unique `quiz ID`.
        - **Test Loading Speed**: Open the direct link in a browser to see how quickly the quiz loads independently of your site. Ideally, the quiz should load in less than one second.

        If the quiz loads quickly via the direct link, the slow loading times are likely caused by other elements on your website.


        !!! tip

            Run the direct quiz link through [Google PageSpeed Insights](https://pagespeed.web.dev/) and/or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) to check its performance in isolation.


    2. **Analyze your website's loading order**

        The loading sequence of your own resources shows what is slowing the quiz down on your site.

        - **Open Developer Tools**: Right-click on your website in the browser and select `Inspect` to open the developer tools.
        - **Review Network and Performance**: Navigate to the `Network` or `Performance` tabs to examine which resources are loading and how long each takes.

        Look for resources that significantly delay loading times, as these are likely culprits affecting the quiz's performance on your site.


        !!! tip

            Run your full page through [Google PageSpeed Insights](https://pagespeed.web.dev/) or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk). The report lists the heaviest items, usually images, fonts and third-party scripts, with the time each one costs.


    3. **Try direct iframe embedding**

        An iFrame keeps the quiz clear of the external scripts that slow your page down.

        **Replace Embed Code**: The standard embed code from the `Share` tab loads the quiz through a JavaScript file, `embed.js`. Use an iFrame embed code instead. The quiz then loads independently of the other scripts on your site.

        Replace this code:

        ```html
        <div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/rkHm6Y" style="..."></div>
        ```

        With this:

        ```html
        <div class="rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/rkHm6Y" style="..."><iframe src="https://admin.revenuehunt.com/public/quiz/rkHm6Y" id="DPIyZ" style="..."></iframe></div>
        ```

        This second block of code includes the quiz iFrame directly. This will start rendering the quiz before the embed.js code is loaded.


    4. **Optimize your website's resources**

        Ask your developer to compress the images, minify the CSS and JavaScript, and remove any plugin or widget you do not need.





    This article explains how to check and improve the loading speed of your quiz.
