---
description: "Learn how to diagnose and optimize RevenueHunt quiz loading speed to ensure smooth user experience on your website."
icon: material/loading
---

# How to Check Quiz Loading Speed

When integrating a quiz into your online store, it's crucial to ensure it loads efficiently to maintain a smooth user experience. If you're encountering slow loading times for your quiz, the issue might not stem from the quiz itself but from other resources on your site affecting its performance. 

This guide outlines steps to diagnose and resolve quiz loading issues by optimizing the loading process.




=== "Shopify"

    **Step 1: Verify Direct Quiz Link Performance**

    First, isolate the quiz from your site's environment to determine if the issue lies within the quiz or your website.

    1. **Locate Your Quiz Link**: In the app, go to your quiz and open the `Share -> External` tab to copy its direct link. With the Built for Shopify version the quiz runs natively inside your theme, so the link is your own storefront URL plus the quiz hash.
        - The link should look something like [https://your-store.com/#quiz-rkHm6Y](https://your-store.com/#quiz-rkHm6Y), where `your-store.com` is your storefront domain and `rkHm6Y` is your unique `quiz ID`.
    2. **Test Loading Speed**: Open the direct link in a browser to see how quickly the quiz loads independently of the rest of your store. Ideally, the quiz should load in less than one second.

    If the quiz loads quickly via the direct link, the slow loading times are likely caused by other elements on your website.


    !!! tip

        Run the direct quiz link through [Google PageSpeed Insights](https://pagespeed.web.dev/) and/or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) to check its performance in isolation.

    ---

    **Step 2: Analyze Your Website's Loading Order**

    !!! info
        The new Built for Shopify version of the RevenueHunt app integrates the quiz as a native Shopify block within the Theme.

    !!! note "About the large inline quiz configuration"

        When inspecting your page source, you may notice a large inline `window.quizzes` JSON object (often 100-200 KB). This is your quiz's configuration: its questions, branching logic, result pages, recommendation rules, design and translations. We embed it directly in the page so the quiz can open instantly, with no extra network request when a shopper interacts.

        That uncompressed size looks alarming, but it isn't the bottleneck:

        - **It's compressed on the wire.** Shopify serves your pages gzip/brotli compressed, so a ~150 KB config typically ships at **10-15 KB** to the browser, often less than a single product thumbnail.
        - **It's not rendered DOM.** It lives inside a `<script>` tag, so it adds no layout or paint cost.
        - **It loads asynchronously.** It never blocks your page from rendering.

        You can confirm the real transferred size in your browser's `Network` tab (look at the `Size` column, not `Content` size).

    Investigating the loading sequence of your website's resources can help identify what's slowing down the quiz when embedded in your site.

    1. **Open Developer Tools**: Right-click on your website in the browser and select `Inspect` to open the developer tools.
    2. **Review Network and Performance**: Navigate to the `Network` or `Performance` tabs to examine which resources are loading and how long each takes.

    Look for resources that significantly delay loading times, as these are likely culprits affecting the quiz's performance on your site.


    !!! tip

        Run your full page through [Google PageSpeed Insights](https://pagespeed.web.dev/) and/or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) to see what's actually slowing it down. The report lists the heaviest offenders (usually images, fonts and third-party scripts) with the estimated time each one costs you.

    

    ---

    **Step 3: Optimize Your Website's Resources**

    Consult your developer to review and optimize the loading of resources on your site. This may involve compressing images, minimizing CSS and JavaScript files, and removing unnecessary plugins or widgets. 

    - **Optimize Third-Party Widgets**: Review any third-party widgets or scripts (e.g., marketing, chat tools) on your site. Ensure that they are loaded asynchronously or deferred to load after the quiz.

    - **Check Shopify Performance Reports**: Use [Shopify’s built-in tools](https://help.shopify.com/en/manual/online-store/web-performance/improving-web-performance) to check for any resources that might be blocking the quiz from loading quickly.





=== "Shopify (Legacy)"

    !!! note "Raw size vs. transferred size"

        The byte sizes you see in your page source are uncompressed. Shopify serves your pages gzip/brotli compressed, and the quiz script is served compressed too, so the browser downloads far less than the raw numbers suggest (a ~150 KB payload typically ships at 10-15 KB). Check the real transferred size in your browser's `Network` tab (the `Size` column, not the `Content` size) before deciding something is heavy.

    **Step 1: Verify Direct Quiz Link Performance**

    First, isolate the quiz from your site's environment to determine if the issue lies within the quiz or your website.

    1. **Locate Your Quiz Link**: Find the direct URL of your quiz. This can be obtained from the `Share -> External` tab of your quiz platform. 
        - The link should look something like [https://admin.revenuehunt.com/public/quiz/rkHm6Y](https://admin.revenuehunt.com/public/quiz/rkHm6Y) or [https://skincarequiz.myshopify.com/#quiz-rkHm6Y](https://skincarequiz.myshopify.com/#quiz-rkHm6Y), where `rkHm6Y` represents your unique `quiz ID`.
    2. **Test Loading Speed**: Open the direct link in a browser to see how quickly the quiz loads independently of your site. Ideally, the quiz should load in less than one second.

    If the quiz loads quickly via the direct link, the slow loading times are likely caused by other elements on your website.


    !!! tip

        Run the direct quiz link through [Google PageSpeed Insights](https://pagespeed.web.dev/) and/or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) to check its performance in isolation.

    ---

    **Step 2: Analyze Your Website's Loading Order**

    Investigating the loading sequence of your website's resources can help identify what's slowing down the quiz when embedded in your site.

    1. **Open Developer Tools**: Right-click on your website in the browser and select `Inspect` to open the developer tools.
    2. **Review Network and Performance**: Navigate to the `Network` or `Performance` tabs to examine which resources are loading and how long each takes.

    Look for resources that significantly delay loading times, as these are likely culprits affecting the quiz's performance on your site.


    !!! tip

        Run your full page through [Google PageSpeed Insights](https://pagespeed.web.dev/) and/or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) to see what's actually slowing it down. The report lists the heaviest offenders (usually images, fonts and third-party scripts) with the estimated time each one costs you.

    ---

    **Step 3: Try Direct iFrame Embedding**

    To circumvent slow loading caused by external scripts, directly embed the quiz using an iFrame.

    **Replace Embed Code**: Instead of using the standard embed code generated from the `Share` tab, which loads the quiz via a JavaScript file (embed.js), use an iFrame embed code. This allows the quiz to load independently of other scripts on your site.

    Replace this code:

    ```html
    <div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/rkHm6Y" style="..."></div>
    ```

    With this:

    ```html
    <div class="rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/rkHm6Y" style="..."><iframe src="https://admin.revenuehunt.com/public/quiz/rkHm6Y" id="DPIyZ" style="..."></iframe></div>
    ```

    This second block of code includes the quiz iFrame directly. This will start rendering the quiz before the embed.js code is loaded.

    ---

    **Step 4: Optimize Your Website's Resources**

    Consult your developer to review and optimize the loading of resources on your site. This may involve compressing images, minimizing CSS and JavaScript files, and removing unnecessary plugins or widgets. 



=== "WooCommerce"

    
    **Step 1: Verify Direct Quiz Link Performance**

    First, isolate the quiz from your site's environment to determine if the issue lies within the quiz or your website.

    1. **Locate Your Quiz Link**: Find the direct URL of your quiz. This can be obtained from the `Share -> External` tab of your quiz platform. 
        - The link should look something like [https://admin.revenuehunt.com/public/quiz/rkHm6Y](https://admin.revenuehunt.com/public/quiz/rkHm6Y) or [https://skincarequiz.myshopify.com/#quiz-rkHm6Y](https://skincarequiz.myshopify.com/#quiz-rkHm6Y), where `rkHm6Y` represents your unique `quiz ID`.
    2. **Test Loading Speed**: Open the direct link in a browser to see how quickly the quiz loads independently of your site. Ideally, the quiz should load in less than one second.

    If the quiz loads quickly via the direct link, the slow loading times are likely caused by other elements on your website.


    !!! tip

        Run the direct quiz link through [Google PageSpeed Insights](https://pagespeed.web.dev/) and/or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) to check its performance in isolation.

    ---

    **Step 2: Analyze Your Website's Loading Order**

    Investigating the loading sequence of your website's resources can help identify what's slowing down the quiz when embedded in your site.

    1. **Open Developer Tools**: Right-click on your website in the browser and select `Inspect` to open the developer tools.
    2. **Review Network and Performance**: Navigate to the `Network` or `Performance` tabs to examine which resources are loading and how long each takes.

    Look for resources that significantly delay loading times, as these are likely culprits affecting the quiz's performance on your site.


    !!! tip

        Run your full page through [Google PageSpeed Insights](https://pagespeed.web.dev/) and/or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) to see what's actually slowing it down. The report lists the heaviest offenders (usually images, fonts and third-party scripts) with the estimated time each one costs you.

    ---

    **Step 3: Try Direct iFrame Embedding**

    To circumvent slow loading caused by external scripts, directly embed the quiz using an iFrame.

    **Replace Embed Code**: Instead of using the standard embed code generated from the `Share` tab, which loads the quiz via a JavaScript file (embed.js), use an iFrame embed code. This allows the quiz to load independently of other scripts on your site.

    Replace this code:

    ```html
    <div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/rkHm6Y" style="..."></div>
    ```

    With this:

    ```html
    <div class="rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/rkHm6Y" style="..."><iframe src="https://admin.revenuehunt.com/public/quiz/rkHm6Y" id="DPIyZ" style="..."></iframe></div>
    ```

    This second block of code includes the quiz iFrame directly. This will start rendering the quiz before the embed.js code is loaded.

    ---

    **Step 4: Optimize Your Website's Resources**

    Consult your developer to review and optimize the loading of resources on your site. This may involve compressing images, minimizing CSS and JavaScript files, and removing unnecessary plugins or widgets. 


=== "Magento"

    
    **Step 1: Verify Direct Quiz Link Performance**

    First, isolate the quiz from your site's environment to determine if the issue lies within the quiz or your website.

    1. **Locate Your Quiz Link**: Find the direct URL of your quiz. This can be obtained from the `Share -> External` tab of your quiz platform. 
        - The link should look something like [https://admin.revenuehunt.com/public/quiz/rkHm6Y](https://admin.revenuehunt.com/public/quiz/rkHm6Y) or [https://skincarequiz.myshopify.com/#quiz-rkHm6Y](https://skincarequiz.myshopify.com/#quiz-rkHm6Y), where `rkHm6Y` represents your unique `quiz ID`.
    2. **Test Loading Speed**: Open the direct link in a browser to see how quickly the quiz loads independently of your site. Ideally, the quiz should load in less than one second.

    If the quiz loads quickly via the direct link, the slow loading times are likely caused by other elements on your website.


    !!! tip

        Run the direct quiz link through [Google PageSpeed Insights](https://pagespeed.web.dev/) and/or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) to check its performance in isolation.

    ---

    **Step 2: Analyze Your Website's Loading Order**

    Investigating the loading sequence of your website's resources can help identify what's slowing down the quiz when embedded in your site.

    1. **Open Developer Tools**: Right-click on your website in the browser and select `Inspect` to open the developer tools.
    2. **Review Network and Performance**: Navigate to the `Network` or `Performance` tabs to examine which resources are loading and how long each takes.

    Look for resources that significantly delay loading times, as these are likely culprits affecting the quiz's performance on your site.


    !!! tip

        Run your full page through [Google PageSpeed Insights](https://pagespeed.web.dev/) and/or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) to see what's actually slowing it down. The report lists the heaviest offenders (usually images, fonts and third-party scripts) with the estimated time each one costs you.

    ---

    **Step 3: Try Direct iFrame Embedding**

    To circumvent slow loading caused by external scripts, directly embed the quiz using an iFrame.

    **Replace Embed Code**: Instead of using the standard embed code generated from the `Share` tab, which loads the quiz via a JavaScript file (embed.js), use an iFrame embed code. This allows the quiz to load independently of other scripts on your site.

    Replace this code:

    ```html
    <div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/rkHm6Y" style="..."></div>
    ```

    With this:

    ```html
    <div class="rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/rkHm6Y" style="..."><iframe src="https://admin.revenuehunt.com/public/quiz/rkHm6Y" id="DPIyZ" style="..."></iframe></div>
    ```

    This second block of code includes the quiz iFrame directly. This will start rendering the quiz before the embed.js code is loaded.

    ---

    **Step 4: Optimize Your Website's Resources**

    Consult your developer to review and optimize the loading of resources on your site. This may involve compressing images, minimizing CSS and JavaScript files, and removing unnecessary plugins or widgets. 

=== "BigCommerce"

    
    **Step 1: Verify Direct Quiz Link Performance**

    First, isolate the quiz from your site's environment to determine if the issue lies within the quiz or your website.

    1. **Locate Your Quiz Link**: Find the direct URL of your quiz. This can be obtained from the `Share -> External` tab of your quiz platform. 
        - The link should look something like [https://admin.revenuehunt.com/public/quiz/rkHm6Y](https://admin.revenuehunt.com/public/quiz/rkHm6Y) or [https://skincarequiz.myshopify.com/#quiz-rkHm6Y](https://skincarequiz.myshopify.com/#quiz-rkHm6Y), where `rkHm6Y` represents your unique `quiz ID`.
    2. **Test Loading Speed**: Open the direct link in a browser to see how quickly the quiz loads independently of your site. Ideally, the quiz should load in less than one second.

    If the quiz loads quickly via the direct link, the slow loading times are likely caused by other elements on your website.


    !!! tip

        Run the direct quiz link through [Google PageSpeed Insights](https://pagespeed.web.dev/) and/or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) to check its performance in isolation.

    ---

    **Step 2: Analyze Your Website's Loading Order**

    Investigating the loading sequence of your website's resources can help identify what's slowing down the quiz when embedded in your site.

    1. **Open Developer Tools**: Right-click on your website in the browser and select `Inspect` to open the developer tools.
    2. **Review Network and Performance**: Navigate to the `Network` or `Performance` tabs to examine which resources are loading and how long each takes.

    Look for resources that significantly delay loading times, as these are likely culprits affecting the quiz's performance on your site.


    !!! tip

        Run your full page through [Google PageSpeed Insights](https://pagespeed.web.dev/) and/or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) to see what's actually slowing it down. The report lists the heaviest offenders (usually images, fonts and third-party scripts) with the estimated time each one costs you.

    ---

    **Step 3: Try Direct iFrame Embedding**

    To circumvent slow loading caused by external scripts, directly embed the quiz using an iFrame.

    **Replace Embed Code**: Instead of using the standard embed code generated from the `Share` tab, which loads the quiz via a JavaScript file (embed.js), use an iFrame embed code. This allows the quiz to load independently of other scripts on your site.

    Replace this code:

    ```html
    <div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/rkHm6Y" style="..."></div>
    ```

    With this:

    ```html
    <div class="rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/rkHm6Y" style="..."><iframe src="https://admin.revenuehunt.com/public/quiz/rkHm6Y" id="DPIyZ" style="..."></iframe></div>
    ```

    This second block of code includes the quiz iFrame directly. This will start rendering the quiz before the embed.js code is loaded.

    ---

    **Step 4: Optimize Your Website's Resources**

    Consult your developer to review and optimize the loading of resources on your site. This may involve compressing images, minimizing CSS and JavaScript files, and removing unnecessary plugins or widgets. 


=== "Standalone"

    
    **Step 1: Verify Direct Quiz Link Performance**

    First, isolate the quiz from your site's environment to determine if the issue lies within the quiz or your website.

    1. **Locate Your Quiz Link**: Find the direct URL of your quiz. This can be obtained from the `Share -> External` tab of your quiz platform. 
        - The link should look something like [https://admin.revenuehunt.com/public/quiz/rkHm6Y](https://admin.revenuehunt.com/public/quiz/rkHm6Y) or [https://skincarequiz.myshopify.com/#quiz-rkHm6Y](https://skincarequiz.myshopify.com/#quiz-rkHm6Y), where `rkHm6Y` represents your unique `quiz ID`.
    2. **Test Loading Speed**: Open the direct link in a browser to see how quickly the quiz loads independently of your site. Ideally, the quiz should load in less than one second.

    If the quiz loads quickly via the direct link, the slow loading times are likely caused by other elements on your website.


    !!! tip

        Run the direct quiz link through [Google PageSpeed Insights](https://pagespeed.web.dev/) and/or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) to check its performance in isolation.

    ---

    **Step 2: Analyze Your Website's Loading Order**

    Investigating the loading sequence of your website's resources can help identify what's slowing down the quiz when embedded in your site.

    1. **Open Developer Tools**: Right-click on your website in the browser and select `Inspect` to open the developer tools.
    2. **Review Network and Performance**: Navigate to the `Network` or `Performance` tabs to examine which resources are loading and how long each takes.

    Look for resources that significantly delay loading times, as these are likely culprits affecting the quiz's performance on your site.


    !!! tip

        Run your full page through [Google PageSpeed Insights](https://pagespeed.web.dev/) and/or the [Lighthouse Chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) to see what's actually slowing it down. The report lists the heaviest offenders (usually images, fonts and third-party scripts) with the estimated time each one costs you.

    ---

    **Step 3: Try Direct iFrame Embedding**

    To circumvent slow loading caused by external scripts, directly embed the quiz using an iFrame.

    **Replace Embed Code**: Instead of using the standard embed code generated from the `Share` tab, which loads the quiz via a JavaScript file (embed.js), use an iFrame embed code. This allows the quiz to load independently of other scripts on your site.

    Replace this code:

    ```html
    <div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/rkHm6Y" style="..."></div>
    ```

    With this:

    ```html
    <div class="rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/rkHm6Y" style="..."><iframe src="https://admin.revenuehunt.com/public/quiz/rkHm6Y" id="DPIyZ" style="..."></iframe></div>
    ```

    This second block of code includes the quiz iFrame directly. This will start rendering the quiz before the embed.js code is loaded.

    ---

    **Step 4: Optimize Your Website's Resources**

    Consult your developer to review and optimize the loading of resources on your site. This may involve compressing images, minimizing CSS and JavaScript files, and removing unnecessary plugins or widgets. 





---
This article explains how to check and improve the loading speed of your quiz.