---
description: "Learn how to diagnose and optimize RevenueHunt quiz loading speed to ensure smooth user experience on your website."
icon: material/loading
---

# How to Check Quiz Loading Speed

A quiz on your store has to load quickly. When one is slow, the cause is usually not the quiz but something else on the same page.

This article explains how to find what is holding the quiz up, and what to do about it.

=== "Shopify"

    1. **Find the direct link to your quiz.** It is in the `Share > External` tab of the quiz.

        A Shopify link looks like `https://your-store.com/#quiz-rkHm6Y`, where `rkHm6Y` is your quiz ID. In this version the quiz runs natively inside your theme, so the address is your own storefront.

    2. **Open that link in a browser and time it.** A quiz on its own should be ready in under a second.

        A quiz that loads quickly here, but slowly on your site, is not the thing slowing your site down.

        !!! tip "Measure it rather than eyeball it"

            Run the direct link through [Google PageSpeed Insights](https://pagespeed.web.dev/) or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) to see its performance in isolation.

    3. **Right-click your page and select `Inspect` to open the developer tools.**

    4. **Open the `Network` or `Performance` tab and reload the page.** Each row shows a resource and how long it took.

        Look for whatever delays the page most. Those are the items holding the quiz up.

        !!! tip "Let a report rank them for you"

            Run the whole page through [Google PageSpeed Insights](https://pagespeed.web.dev/) or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk). The report lists the heaviest items, usually images, fonts and third-party scripts, with the cost of each.

    5. **Ask your developer to lighten the page.** Compress the images, minify the CSS and JavaScript, and remove any plugin or widget you do not need.

        - **Third-party widgets.** Marketing and chat scripts should load asynchronously, or be deferred until after the quiz.
        - **Shopify's own reports.** [Improving web performance](https://help.shopify.com/en/manual/online-store/web-performance/improving-web-performance) shows what is blocking your storefront.

    !!! note "The large inline quiz configuration is not the problem"

        Inspecting your page source, you may find a `window.quizzes` JSON object of 100 to 200 KB. That is your quiz: its questions, logic, results pages, recommendation rules, design and translations. It is embedded in the page so the quiz opens at once, with no extra request when the customer starts it.

        The uncompressed size looks alarming, and it is not the bottleneck.

        - **It is compressed on the wire.** Shopify serves pages gzip or brotli compressed, so a 150 KB configuration usually ships at 10 to 15 KB, less than one product thumbnail.
        - **It is not rendered DOM.** It sits inside a `<script>` tag, so it costs no layout or paint.
        - **It loads asynchronously.** It never blocks the page from rendering.

        Check the real transferred size in the `Network` tab, in the `Size` column rather than `Content`.

=== "Shopify (Legacy)"

    1. **Find the direct link to your quiz.** It is in the `Share > External` tab of the quiz.

        The link looks like `https://admin.revenuehunt.com/public/quiz/rkHm6Y`, or `https://your-store.com/#quiz-rkHm6Y` if the quiz is embedded in your storefront. `rkHm6Y` is your quiz ID.

    2. **Open that link in a browser and time it.** A quiz on its own should be ready in under a second.

        A quiz that loads quickly here, but slowly on your site, is not the thing slowing your site down.

        !!! tip "Measure it rather than eyeball it"

            Run the direct link through [Google PageSpeed Insights](https://pagespeed.web.dev/) or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) to see its performance in isolation.

    3. **Right-click your page and select `Inspect` to open the developer tools.**

    4. **Open the `Network` or `Performance` tab and reload the page.** Each row shows a resource and how long it took.

        Look for whatever delays the page most. Those are the items holding the quiz up.

        !!! tip "Let a report rank them for you"

            Run the whole page through [Google PageSpeed Insights](https://pagespeed.web.dev/) or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk). The report lists the heaviest items, usually images, fonts and third-party scripts, with the cost of each.

    5. **Try embedding the quiz in an iframe instead.** The standard embed loads the quiz through `embed.js`, so it waits its turn behind your other scripts. An iframe starts rendering the quiz before `embed.js` has loaded.

        Replace this:

        ```html
        <div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/rkHm6Y" style="..."></div>
        ```

        With this:

        ```html
        <div class="rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/rkHm6Y" style="..."><iframe src="https://admin.revenuehunt.com/public/quiz/rkHm6Y" id="DPIyZ" style="..."></iframe></div>
        ```

    6. **Ask your developer to lighten the page.** Compress the images, minify the CSS and JavaScript, and remove any plugin or widget you do not need.

    !!! note "Raw size is not transferred size"

        The byte sizes in your page source are uncompressed. Shopify serves your pages, and the quiz script, gzip or brotli compressed, so the browser downloads far less than those numbers suggest. A 150 KB payload usually ships at 10 to 15 KB.

        Check the real transferred size in the `Network` tab, in the `Size` column rather than `Content`, before deciding something is heavy.

=== "WooCommerce"

    1. **Find the direct link to your quiz.** It is in the `Share > External` tab of the quiz.

        The link looks like `https://admin.revenuehunt.com/public/quiz/rkHm6Y`, or `https://your-site.com/#quiz-rkHm6Y` if the quiz is embedded in your site. `rkHm6Y` is your quiz ID.

    2. **Open that link in a browser and time it.** A quiz on its own should be ready in under a second.

        A quiz that loads quickly here, but slowly on your site, is not the thing slowing your site down.

        !!! tip "Measure it rather than eyeball it"

            Run the direct link through [Google PageSpeed Insights](https://pagespeed.web.dev/) or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) to see its performance in isolation.

    3. **Right-click your page and select `Inspect` to open the developer tools.**

    4. **Open the `Network` or `Performance` tab and reload the page.** Each row shows a resource and how long it took.

        Look for whatever delays the page most. Those are the items holding the quiz up.

        !!! tip "Let a report rank them for you"

            Run the whole page through [Google PageSpeed Insights](https://pagespeed.web.dev/) or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk). The report lists the heaviest items, usually images, fonts and third-party scripts, with the cost of each.

    5. **Try embedding the quiz in an iframe instead.** The standard embed loads the quiz through `embed.js`, so it waits its turn behind your other scripts. An iframe starts rendering the quiz before `embed.js` has loaded.

        Replace this:

        ```html
        <div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/rkHm6Y" style="..."></div>
        ```

        With this:

        ```html
        <div class="rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/rkHm6Y" style="..."><iframe src="https://admin.revenuehunt.com/public/quiz/rkHm6Y" id="DPIyZ" style="..."></iframe></div>
        ```

    6. **Ask your developer to lighten the page.** Compress the images, minify the CSS and JavaScript, and remove any plugin or widget you do not need.

=== "Magento"

    1. **Find the direct link to your quiz.** It is in the `Share > External` tab of the quiz.

        The link looks like `https://admin.revenuehunt.com/public/quiz/rkHm6Y`, or `https://your-site.com/#quiz-rkHm6Y` if the quiz is embedded in your site. `rkHm6Y` is your quiz ID.

    2. **Open that link in a browser and time it.** A quiz on its own should be ready in under a second.

        A quiz that loads quickly here, but slowly on your site, is not the thing slowing your site down.

        !!! tip "Measure it rather than eyeball it"

            Run the direct link through [Google PageSpeed Insights](https://pagespeed.web.dev/) or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) to see its performance in isolation.

    3. **Right-click your page and select `Inspect` to open the developer tools.**

    4. **Open the `Network` or `Performance` tab and reload the page.** Each row shows a resource and how long it took.

        Look for whatever delays the page most. Those are the items holding the quiz up.

        !!! tip "Let a report rank them for you"

            Run the whole page through [Google PageSpeed Insights](https://pagespeed.web.dev/) or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk). The report lists the heaviest items, usually images, fonts and third-party scripts, with the cost of each.

    5. **Try embedding the quiz in an iframe instead.** The standard embed loads the quiz through `embed.js`, so it waits its turn behind your other scripts. An iframe starts rendering the quiz before `embed.js` has loaded.

        Replace this:

        ```html
        <div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/rkHm6Y" style="..."></div>
        ```

        With this:

        ```html
        <div class="rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/rkHm6Y" style="..."><iframe src="https://admin.revenuehunt.com/public/quiz/rkHm6Y" id="DPIyZ" style="..."></iframe></div>
        ```

    6. **Ask your developer to lighten the page.** Compress the images, minify the CSS and JavaScript, and remove any plugin or widget you do not need.

=== "BigCommerce"

    1. **Find the direct link to your quiz.** It is in the `Share > External` tab of the quiz.

        The link looks like `https://admin.revenuehunt.com/public/quiz/rkHm6Y`, or `https://your-site.com/#quiz-rkHm6Y` if the quiz is embedded in your site. `rkHm6Y` is your quiz ID.

    2. **Open that link in a browser and time it.** A quiz on its own should be ready in under a second.

        A quiz that loads quickly here, but slowly on your site, is not the thing slowing your site down.

        !!! tip "Measure it rather than eyeball it"

            Run the direct link through [Google PageSpeed Insights](https://pagespeed.web.dev/) or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) to see its performance in isolation.

    3. **Right-click your page and select `Inspect` to open the developer tools.**

    4. **Open the `Network` or `Performance` tab and reload the page.** Each row shows a resource and how long it took.

        Look for whatever delays the page most. Those are the items holding the quiz up.

        !!! tip "Let a report rank them for you"

            Run the whole page through [Google PageSpeed Insights](https://pagespeed.web.dev/) or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk). The report lists the heaviest items, usually images, fonts and third-party scripts, with the cost of each.

    5. **Try embedding the quiz in an iframe instead.** The standard embed loads the quiz through `embed.js`, so it waits its turn behind your other scripts. An iframe starts rendering the quiz before `embed.js` has loaded.

        Replace this:

        ```html
        <div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/rkHm6Y" style="..."></div>
        ```

        With this:

        ```html
        <div class="rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/rkHm6Y" style="..."><iframe src="https://admin.revenuehunt.com/public/quiz/rkHm6Y" id="DPIyZ" style="..."></iframe></div>
        ```

    6. **Ask your developer to lighten the page.** Compress the images, minify the CSS and JavaScript, and remove any plugin or widget you do not need.

=== "Standalone"

    1. **Find the direct link to your quiz.** It is in the `Share > External` tab of the quiz.

        The link looks like `https://admin.revenuehunt.com/public/quiz/rkHm6Y`, or `https://your-site.com/#quiz-rkHm6Y` if the quiz is embedded in your site. `rkHm6Y` is your quiz ID.

    2. **Open that link in a browser and time it.** A quiz on its own should be ready in under a second.

        A quiz that loads quickly here, but slowly on your site, is not the thing slowing your site down.

        !!! tip "Measure it rather than eyeball it"

            Run the direct link through [Google PageSpeed Insights](https://pagespeed.web.dev/) or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) to see its performance in isolation.

    3. **Right-click your page and select `Inspect` to open the developer tools.**

    4. **Open the `Network` or `Performance` tab and reload the page.** Each row shows a resource and how long it took.

        Look for whatever delays the page most. Those are the items holding the quiz up.

        !!! tip "Let a report rank them for you"

            Run the whole page through [Google PageSpeed Insights](https://pagespeed.web.dev/) or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk). The report lists the heaviest items, usually images, fonts and third-party scripts, with the cost of each.

    5. **Try embedding the quiz in an iframe instead.** The standard embed loads the quiz through `embed.js`, so it waits its turn behind your other scripts. An iframe starts rendering the quiz before `embed.js` has loaded.

        Replace this:

        ```html
        <div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/rkHm6Y" style="..."></div>
        ```

        With this:

        ```html
        <div class="rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/rkHm6Y" style="..."><iframe src="https://admin.revenuehunt.com/public/quiz/rkHm6Y" id="DPIyZ" style="..."></iframe></div>
        ```

    6. **Ask your developer to lighten the page.** Compress the images, minify the CSS and JavaScript, and remove any plugin or widget you do not need.

---

This article explains how to check the loading speed of your quiz, and how to find what is slowing it down.