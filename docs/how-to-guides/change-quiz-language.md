---
description: "Learn how to change your RevenueHunt quiz language and translate it for different languages using Shopify Markets."
icon: material/translate-variant
---

# How to Change the Language of Your Quiz

This article explains how to change the language of your quiz, translate it into other languages, and set up Shopify Markets. The quiz can then follow the market and language preference.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/c0exzYPtydo?si=tuNPV9eOsXRLRKi-" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! tip "Tutorial"
        For a step-by-step walkthrough, see [Assign Quizzes to Shopify Markets and Languages](/tutorials/shopify-markets/).

=== "Shopify (Legacy)"

=== "WooCommerce"

=== "Magento"

=== "BigCommerce"

=== "Standalone"

## Change quiz language in settings

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/c0exzYPtydo?si=X5ULbSjqG7wQ2Izd&amp;start=106" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    Before you assign quizzes to markets and languages, create a quiz version for each language:

    1. Create a [`new quiz`](/reference/dashboard/#new-quiz) with the content and questions you want. This is your base version.
    2. From the [Dashboard](/reference/dashboard/), click `Duplicate` on that quiz, once for each language.

        ![Quiz management options on the Dashboard](/images/manual_shopifyV2_quizmanagementoptions.png)

        !!! tip

            [Quiz Copilot](/how-to-guides/use-quiz-copilot/) can translate and duplicate a quiz in one go. Open a chat with it and ask it to duplicate the main quiz in another language.

    3. In each duplicate, open [`Quiz settings > Quiz content`](/reference/quiz-builder/quiz-settings/#messages-quiz-content) and translate the buttons, popups and other interface text.

        ![Quiz content tab in Quiz settings](/images/manual_shopifyV2_quizbuilder_quizsettings_quizcontent.png)

    4. Translate the questions and answer choices. Duplicating a quiz does not translate them, so edit each one by hand or ask [Quiz Copilot](/how-to-guides/use-quiz-copilot/) to translate them for you.
    5. Go to [App settings > Shopify Markets](/reference/app-settings/#shopify-markets). Link each translated quiz to its market and language, so every customer gets the right one.

        !!! tip "Tutorial"

            For a step-by-step walkthrough, see [Assign Quizzes to Shopify Markets and Languages](/tutorials/shopify-markets/).

    Each market and language now has its own quiz, and you manage them all in the Shopify Markets tab of your app settings.

    ## Automatic product translation

    !!! info "Translated product titles and descriptions"

        The `💎 Built for Shopify` version of the RevenueHunt app shows **translated product titles, descriptions and prices** on the quiz results page based on the customer's market and language.

        This works through the `@inContext` directive of the Shopify Storefront API. When a customer views the quiz in a given market and language, the app fetches product data in that locale directly from Shopify.

    **How it works:**

    1. The theme extension detects the customer's **country** and **language** from the Shopify storefront context.
    2. When the results page loads, the app fetches the product titles, descriptions, prices and URLs for that locale.
    3. Translations made with the Shopify **Translate & Adapt** app, or a third-party translation app, appear automatically in the quiz results.

    **Requirements:**

    - Your store must have the [Translate & Adapt](https://apps.shopify.com/translate-and-adapt) app (or equivalent) installed and configured with product translations.
    - [Shopify Markets](/how-to-guides/show-quiz-based-on-markets/) must be set up with the appropriate languages and regions.
    - Product translations must be published for the relevant locales in your Shopify store.

    !!! note

        Automatic product translation applies to the **results page** only, where the recommended products appear. It does not cover the quiz itself. Translate the quiz **questions, choices and UI text** yourself, or with [Quiz Copilot](/how-to-guides/use-quiz-copilot/), as [Change quiz language in settings](#change-quiz-language-in-settings) describes.


=== "Shopify (Legacy)"

    !!! note

        The legacy version of the RevenueHunt app for Shopify does not support Shopify Markets.

    1. **Open Quiz Settings**: To change the quiz language navigate to [Quiz Settings](/reference/quiz-builder/quiz-settings/) or [`Quiz Settings -> Messages`](/reference/quiz-builder/quiz-settings/#messages-quiz-content).

        ![how to change quiz language messages](/images/manual_quizbuilder_quizsettings_messages.png){width="300"}

    2. **Language**: Choose a language from the dropdown. It changes the text on the quiz buttons and placeholders.
    3. **Add your own translations**: If your language is missing, or you prefer different wording, edit the entries in [Messages](/reference/quiz-builder/quiz-settings/#messages-quiz-content) tab.
    4. **Override the translations**: If a button reverts to English, set its text yourself in [`Quiz Builder -> Question settings`](/reference/quiz-builder/questions/#question-settings).

=== "WooCommerce"

    1. **Open Quiz Settings**: To change the quiz language navigate to [Quiz Settings](/reference/quiz-builder/quiz-settings/) or [`Quiz Settings -> Messages`](/reference/quiz-builder/quiz-settings/#messages-quiz-content).

        ![how to change quiz language messages](/images/manual_quizbuilder_quizsettings_messages.png){width="300"}

    2. **Language**: Choose a language from the dropdown. It changes the text on the quiz buttons and placeholders.
    3. **Add your own translations**: If your language is missing, or you prefer different wording, edit the entries in [Messages](/reference/quiz-builder/quiz-settings/#messages-quiz-content) tab.
    4. **Override the translations**: If a button reverts to English, set its text yourself in [`Quiz Builder -> Question settings`](/reference/quiz-builder/questions/#question-settings).

=== "Magento"

    1. **Open Quiz Settings**: To change the quiz language navigate to [Quiz Settings](/reference/quiz-builder/quiz-settings/) or [`Quiz Settings -> Messages`](/reference/quiz-builder/quiz-settings/#messages-quiz-content).

        ![how to change quiz language messages](/images/manual_quizbuilder_quizsettings_messages.png){width="300"}

    2. **Language**: Choose a language from the dropdown. It changes the text on the quiz buttons and placeholders.
    3. **Add your own translations**: If your language is missing, or you prefer different wording, edit the entries in [Messages](/reference/quiz-builder/quiz-settings/#messages-quiz-content) tab.
    4. **Override the translations**: If a button reverts to English, set its text yourself in [`Quiz Builder -> Question settings`](/reference/quiz-builder/questions/#question-settings).

=== "BigCommerce"

    1. **Open Quiz Settings**: To change the quiz language navigate to [Quiz Settings](/reference/quiz-builder/quiz-settings/) or [`Quiz Settings -> Messages`](/reference/quiz-builder/quiz-settings/#messages-quiz-content).

        ![how to change quiz language messages](/images/manual_quizbuilder_quizsettings_messages.png){width="300"}

    2. **Language**: Choose a language from the dropdown. It changes the text on the quiz buttons and placeholders.
    3. **Add your own translations**: If your language is missing, or you prefer different wording, edit the entries in [Messages](/reference/quiz-builder/quiz-settings/#messages-quiz-content) tab.
    4. **Override the translations**: If a button reverts to English, set its text yourself in [`Quiz Builder -> Question settings`](/reference/quiz-builder/questions/#question-settings).

=== "Standalone"

    1. **Open Quiz Settings**: To change the quiz language navigate to [Quiz Settings](/reference/quiz-builder/quiz-settings/) or [`Quiz Settings -> Messages`](/reference/quiz-builder/quiz-settings/#messages-quiz-content).

        ![how to change quiz language messages](/images/manual_quizbuilder_quizsettings_messages.png){width="300"}

    2. **Language**: Choose a language from the dropdown. It changes the text on the quiz buttons and placeholders.
    3. **Add your own translations**: If your language is missing, or you prefer different wording, edit the entries in [Messages](/reference/quiz-builder/quiz-settings/#messages-quiz-content) tab.
    4. **Override the translations**: If a button reverts to English, set its text yourself in [`Quiz Builder -> Question settings`](/reference/quiz-builder/questions/#question-settings).

## Set up multilingual quizzes

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/c0exzYPtydo?si=e_mX9xdaiB24xXaT&amp;start=175" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! tip "Tutorial"

        For a step-by-step walkthrough, see [Assign Quizzes to Shopify Markets and Languages](/tutorials/shopify-markets/).

    The RevenueHunt app lets you pick a quiz for each Shopify Market and its languages. These steps set the quiz language from the market and language preference.

    1. In Shopify Admin, go to Apps and select `RevenueHunt`.
    2. Open [App settings > Shopify Markets](/reference/app-settings/#shopify-markets).

        ![Shopify Markets tab in App settings](/images/manual_shopifyV2_appsettings_markets.png)

    3. Select the market you want to assign a quiz to, then pick its default quiz from the `dropdown list`.

        ![Choosing the default quiz for a market](/images/manual_shopifyV2_appsettings_markets_pickquiz.png)

    4. To set a quiz per language as well, click the `>` arrow on a market. It then expands into its languages.

        !!! example "One market, two languages"

            In the United States market, set one quiz for English-speaking customers and another for Spanish-speaking customers.

    5. For each locale, pick the quiz from its dropdown and save.
    6. To go back to one quiz per market, whatever the language, click `Hide All Locales`. The default quiz is then shown to every customer in that region.

        ![A market expanded into its languages in the Shopify Markets tab](/images/manual_shopifyV2_appsettings_markets_showall.png)

    Your quizzes are now set per market and language.


=== "Shopify (Legacy)"

    The app has no native multi-language support, but there are workarounds for presenting a quiz in several languages.

    How does it work?

    - For now, you can [create multiple quizzes](#legacy-create-quizzes-in-different-languages), each one in a different language.
    - Then, each of these quizzes will have a **unique quiz ID**.
    - Embed each quiz on its own page, such as quiz-en, quiz-de or quiz-fr. Your developer can also write a [script that displays the correct quiz](#legacy-display-the-correct-quiz) popup depending on the browser language.
    - The app **syncs only the base products from your store, in the main language**. An automatically translated product has no unique ID to sync against. The quiz language changes, but the product names and descriptions stay in the original language. See the [workarounds](#legacy-redirect-to-translated-product-url).

    To set this up:

    1. **Create quizzes in different languages**{ #legacy-create-quizzes-in-different-languages }

        - **Manual Translation**: Begin by manually translating your quizzes into the desired languages. Each translated quiz will have a unique quiz ID.
        - **Quiz Settings Adjustment**: Navigate to the [Quiz Settings](/reference/quiz-builder/quiz-settings/) to modify the language of interactive elements like buttons. However, note that questions and choices need manual translation.

    2. **Display the correct quiz based on browser language**{ #legacy-display-the-correct-quiz }

        Use JavaScript to show the right quiz for the browser language. The script should:

        - Detect the browser's language.
        - Map this language to the corresponding quiz ID.
        - Update quiz links and iframes on your site to point to the correct quiz version.

        Script sample code:

        ```javascript
        document.addEventListener("DOMContentLoaded", function() {
          // Check browser's preferred language (get the first two characters to ignore region)
          const language = navigator.language.substring(0,2);

          // Your mapping of languages to quiz IDs
          const quizMapping = {
            'en': 'abc123',
            'fr': 'dfg456',
            'de': 'xyz423'
          };

          // Default language (fallback to English if not found)
          const defaultQuizId = quizMapping[language] || quizMapping['en'];

          // Find all quiz links and update the href
          const quizLinks = document.querySelectorAll('a[href^="#quiz-"]');
          quizLinks.forEach(link => {
            link.setAttribute('href', '#quiz-' + defaultQuizId);
          });

          // Find all iframes with quiz URLs and update the src attribute and the data-url attribute of the parent div
          const quizIframes = document.querySelectorAll('iframe[src^="https://admin.revenuehunt.com/public/quiz/"]');
          quizIframes.forEach(iframe => {
            const newSrc = iframe.src.replace(/quiz\/\w+/, 'quiz/' + defaultQuizId);
            iframe.src = newSrc;

            // If the parent div has the data-url attribute, update it as well
            const parentDiv = iframe.parentElement;
            if (parentDiv && parentDiv.hasAttribute('data-url')) {
              const newDataUrl = parentDiv.getAttribute('data-url').replace(/quiz\/\w+/, 'quiz/' + defaultQuizId);
              parentDiv.setAttribute('data-url', newDataUrl);
            }
          });
        });
        ```

        !!! warning

            Do not publish two quizzes on the same page. That leads to unwanted behavior.

    3. **Redirect to translated product URL**{ #legacy-redirect-to-translated-product-url }

        The app syncs only the base products from your store. A product translated into another language has no unique ID to sync against. The quiz language changes, but the product names and descriptions stay in the original language.

        A workaround for this could be creating quizzes in different languages and redirecting users to the translated product pages with [JavaScript](/how-to-guides/add-javascript/).

        1. Instead of adding a product to cart, you can change the [checkout settings](/how-to-guides/change-checkout-settings/) to `link to product` and point customers to the translated product page.
        2. By default the customer goes to the original product URL. JavaScript can change that URL automatically.
        3. For example, the Results Page can change every link from `https://www.example.com/products/productA` to `https://www.example.com/en/products/productA`. The customer is then sent to the translated product page.
        4. To redirect to an English translation of a product, one can use:
                ```javascript
                let shopURL = "https://www.example.com";

                var links = document.querySelectorAll(".lq-product a");

                for (let i = 0; i < links.length; i++) {
                var href = links[i].href;
                links[i].href = href.replace(shopURL,shopURL+"/en");
                }
                ```

        5. Replace `https://www.example.com` with your store URL. Change `shopURL+"/en"` to the language code you set up in your store (for example, `shopURL+"/fr"` for French).



=== "WooCommerce"


    The app has no native multi-language support, but there are workarounds for presenting a quiz in several languages.

    How does it work?

    - For now, you can [create multiple quizzes](#woocommerce-create-quizzes-in-different-languages), each one in a different language.
    - Then, each of these quizzes will have a **unique quiz ID**.
    - Embed each quiz on its own page, such as quiz-en, quiz-de or quiz-fr. Your developer can also write a [script that displays the correct quiz](#woocommerce-display-the-correct-quiz) popup depending on the browser language.
    - The app **syncs only the base products from your store, in the main language**. An automatically translated product has no unique ID to sync against. The quiz language changes, but the product names and descriptions stay in the original language. See the [workarounds](#woocommerce-redirect-to-translated-product-url).

    To set this up:

    1. **Create quizzes in different languages**{ #woocommerce-create-quizzes-in-different-languages }

        - **Manual Translation**: Begin by manually translating your quizzes into the desired languages. Each translated quiz will have a unique quiz ID.
        - **Quiz Settings Adjustment**: Navigate to the [Quiz Settings](/reference/quiz-builder/quiz-settings/) to modify the language of interactive elements like buttons. However, note that questions and choices need manual translation.

    2. **Display the correct quiz based on browser language**{ #woocommerce-display-the-correct-quiz }

        Use JavaScript to show the right quiz for the browser language. The script should:

        - Detect the browser's language.
        - Map this language to the corresponding quiz ID.
        - Update quiz links and iframes on your site to point to the correct quiz version.

        Script sample code:

        ```javascript
        document.addEventListener("DOMContentLoaded", function() {
          // Check browser's preferred language (get the first two characters to ignore region)
          const language = navigator.language.substring(0,2);

          // Your mapping of languages to quiz IDs
          const quizMapping = {
            'en': 'abc123',
            'fr': 'dfg456',
            'de': 'xyz423'
          };

          // Default language (fallback to English if not found)
          const defaultQuizId = quizMapping[language] || quizMapping['en'];

          // Find all quiz links and update the href
          const quizLinks = document.querySelectorAll('a[href^="#quiz-"]');
          quizLinks.forEach(link => {
            link.setAttribute('href', '#quiz-' + defaultQuizId);
          });

          // Find all iframes with quiz URLs and update the src attribute and the data-url attribute of the parent div
          const quizIframes = document.querySelectorAll('iframe[src^="https://admin.revenuehunt.com/public/quiz/"]');
          quizIframes.forEach(iframe => {
            const newSrc = iframe.src.replace(/quiz\/\w+/, 'quiz/' + defaultQuizId);
            iframe.src = newSrc;

            // If the parent div has the data-url attribute, update it as well
            const parentDiv = iframe.parentElement;
            if (parentDiv && parentDiv.hasAttribute('data-url')) {
              const newDataUrl = parentDiv.getAttribute('data-url').replace(/quiz\/\w+/, 'quiz/' + defaultQuizId);
              parentDiv.setAttribute('data-url', newDataUrl);
            }
          });
        });
        ```

        !!! warning

            Do not publish two quizzes on the same page. That leads to unwanted behavior.

    3. **Redirect to translated product URL**{ #woocommerce-redirect-to-translated-product-url }

        The app syncs only the base products from your store. A product translated into another language has no unique ID to sync against. The quiz language changes, but the product names and descriptions stay in the original language.

        A workaround for this could be creating quizzes in different languages and redirecting users to the translated product pages with [JavaScript](/how-to-guides/add-javascript/).

        1. Instead of adding a product to cart, you can change the [checkout settings](/how-to-guides/change-checkout-settings/) to `link to product` and point customers to the translated product page.
        2. By default the customer goes to the original product URL. JavaScript can change that URL automatically.
        3. For example, the Results Page can change every link from `https://www.example.com/products/productA` to `https://www.example.com/en/products/productA`. The customer is then sent to the translated product page.
        4. To redirect to an English translation of a product, one can use:
                ```javascript
                let shopURL = "https://www.example.com";

                var links = document.querySelectorAll(".lq-product a");

                for (let i = 0; i < links.length; i++) {
                var href = links[i].href;
                links[i].href = href.replace(shopURL,shopURL+"/en");
                }
                ```

        5. Replace `https://www.example.com` with your store URL. Change `shopURL+"/en"` to the language code you set up in your store (for example, `shopURL+"/fr"` for French).



=== "Magento"


    The app has no native multi-language support, but there are workarounds for presenting a quiz in several languages.

    How does it work?

    - For now, you can [create multiple quizzes](#magento-create-quizzes-in-different-languages), each one in a different language.
    - Then, each of these quizzes will have a **unique quiz ID**.
    - Embed each quiz on its own page, such as quiz-en, quiz-de or quiz-fr. Your developer can also write a [script that displays the correct quiz](#magento-display-the-correct-quiz) popup depending on the browser language.
    - The app **syncs only the base products from your store, in the main language**. An automatically translated product has no unique ID to sync against. The quiz language changes, but the product names and descriptions stay in the original language. See the [workarounds](#magento-redirect-to-translated-product-url).

    To set this up:

    1. **Create quizzes in different languages**{ #magento-create-quizzes-in-different-languages }

        - **Manual Translation**: Begin by manually translating your quizzes into the desired languages. Each translated quiz will have a unique quiz ID.
        - **Quiz Settings Adjustment**: Navigate to the [Quiz Settings](/reference/quiz-builder/quiz-settings/) to modify the language of interactive elements like buttons. However, note that questions and choices need manual translation.

    2. **Display the correct quiz based on browser language**{ #magento-display-the-correct-quiz }

        Use JavaScript to show the right quiz for the browser language. The script should:

        - Detect the browser's language.
        - Map this language to the corresponding quiz ID.
        - Update quiz links and iframes on your site to point to the correct quiz version.

        Script sample code:

        ```javascript
        document.addEventListener("DOMContentLoaded", function() {
          // Check browser's preferred language (get the first two characters to ignore region)
          const language = navigator.language.substring(0,2);

          // Your mapping of languages to quiz IDs
          const quizMapping = {
            'en': 'abc123',
            'fr': 'dfg456',
            'de': 'xyz423'
          };

          // Default language (fallback to English if not found)
          const defaultQuizId = quizMapping[language] || quizMapping['en'];

          // Find all quiz links and update the href
          const quizLinks = document.querySelectorAll('a[href^="#quiz-"]');
          quizLinks.forEach(link => {
            link.setAttribute('href', '#quiz-' + defaultQuizId);
          });

          // Find all iframes with quiz URLs and update the src attribute and the data-url attribute of the parent div
          const quizIframes = document.querySelectorAll('iframe[src^="https://admin.revenuehunt.com/public/quiz/"]');
          quizIframes.forEach(iframe => {
            const newSrc = iframe.src.replace(/quiz\/\w+/, 'quiz/' + defaultQuizId);
            iframe.src = newSrc;

            // If the parent div has the data-url attribute, update it as well
            const parentDiv = iframe.parentElement;
            if (parentDiv && parentDiv.hasAttribute('data-url')) {
              const newDataUrl = parentDiv.getAttribute('data-url').replace(/quiz\/\w+/, 'quiz/' + defaultQuizId);
              parentDiv.setAttribute('data-url', newDataUrl);
            }
          });
        });
        ```

        !!! warning

            Do not publish two quizzes on the same page. That leads to unwanted behavior.

    3. **Redirect to translated product URL**{ #magento-redirect-to-translated-product-url }

        The app syncs only the base products from your store. A product translated into another language has no unique ID to sync against. The quiz language changes, but the product names and descriptions stay in the original language.

        A workaround for this could be creating quizzes in different languages and redirecting users to the translated product pages with [JavaScript](/how-to-guides/add-javascript/).

        1. Instead of adding a product to cart, you can change the [checkout settings](/how-to-guides/change-checkout-settings/) to `link to product` and point customers to the translated product page.
        2. By default the customer goes to the original product URL. JavaScript can change that URL automatically.
        3. For example, the Results Page can change every link from `https://www.example.com/products/productA` to `https://www.example.com/en/products/productA`. The customer is then sent to the translated product page.
        4. To redirect to an English translation of a product, one can use:
                ```javascript
                let shopURL = "https://www.example.com";

                var links = document.querySelectorAll(".lq-product a");

                for (let i = 0; i < links.length; i++) {
                var href = links[i].href;
                links[i].href = href.replace(shopURL,shopURL+"/en");
                }
                ```

        5. Replace `https://www.example.com` with your store URL. Change `shopURL+"/en"` to the language code you set up in your store (for example, `shopURL+"/fr"` for French).



=== "BigCommerce"


    The app has no native multi-language support, but there are workarounds for presenting a quiz in several languages.

    How does it work?

    - For now, you can [create multiple quizzes](#bigcommerce-create-quizzes-in-different-languages), each one in a different language.
    - Then, each of these quizzes will have a **unique quiz ID**.
    - Embed each quiz on its own page, such as quiz-en, quiz-de or quiz-fr. Your developer can also write a [script that displays the correct quiz](#bigcommerce-display-the-correct-quiz) popup depending on the browser language.
    - The app **syncs only the base products from your store, in the main language**. An automatically translated product has no unique ID to sync against. The quiz language changes, but the product names and descriptions stay in the original language. See the [workarounds](#bigcommerce-redirect-to-translated-product-url).

    To set this up:

    1. **Create quizzes in different languages**{ #bigcommerce-create-quizzes-in-different-languages }

        - **Manual Translation**: Begin by manually translating your quizzes into the desired languages. Each translated quiz will have a unique quiz ID.
        - **Quiz Settings Adjustment**: Navigate to the [Quiz Settings](/reference/quiz-builder/quiz-settings/) to modify the language of interactive elements like buttons. However, note that questions and choices need manual translation.

    2. **Display the correct quiz based on browser language**{ #bigcommerce-display-the-correct-quiz }

        Use JavaScript to show the right quiz for the browser language. The script should:

        - Detect the browser's language.
        - Map this language to the corresponding quiz ID.
        - Update quiz links and iframes on your site to point to the correct quiz version.

        Script sample code:

        ```javascript
        document.addEventListener("DOMContentLoaded", function() {
          // Check browser's preferred language (get the first two characters to ignore region)
          const language = navigator.language.substring(0,2);

          // Your mapping of languages to quiz IDs
          const quizMapping = {
            'en': 'abc123',
            'fr': 'dfg456',
            'de': 'xyz423'
          };

          // Default language (fallback to English if not found)
          const defaultQuizId = quizMapping[language] || quizMapping['en'];

          // Find all quiz links and update the href
          const quizLinks = document.querySelectorAll('a[href^="#quiz-"]');
          quizLinks.forEach(link => {
            link.setAttribute('href', '#quiz-' + defaultQuizId);
          });

          // Find all iframes with quiz URLs and update the src attribute and the data-url attribute of the parent div
          const quizIframes = document.querySelectorAll('iframe[src^="https://admin.revenuehunt.com/public/quiz/"]');
          quizIframes.forEach(iframe => {
            const newSrc = iframe.src.replace(/quiz\/\w+/, 'quiz/' + defaultQuizId);
            iframe.src = newSrc;

            // If the parent div has the data-url attribute, update it as well
            const parentDiv = iframe.parentElement;
            if (parentDiv && parentDiv.hasAttribute('data-url')) {
              const newDataUrl = parentDiv.getAttribute('data-url').replace(/quiz\/\w+/, 'quiz/' + defaultQuizId);
              parentDiv.setAttribute('data-url', newDataUrl);
            }
          });
        });
        ```

        !!! warning

            Do not publish two quizzes on the same page. That leads to unwanted behavior.

    3. **Redirect to translated product URL**{ #bigcommerce-redirect-to-translated-product-url }

        The app syncs only the base products from your store. A product translated into another language has no unique ID to sync against. The quiz language changes, but the product names and descriptions stay in the original language.

        A workaround for this could be creating quizzes in different languages and redirecting users to the translated product pages with [JavaScript](/how-to-guides/add-javascript/).

        1. Instead of adding a product to cart, you can change the [checkout settings](/how-to-guides/change-checkout-settings/) to `link to product` and point customers to the translated product page.
        2. By default the customer goes to the original product URL. JavaScript can change that URL automatically.
        3. For example, the Results Page can change every link from `https://www.example.com/products/productA` to `https://www.example.com/en/products/productA`. The customer is then sent to the translated product page.
        4. To redirect to an English translation of a product, one can use:
                ```javascript
                let shopURL = "https://www.example.com";

                var links = document.querySelectorAll(".lq-product a");

                for (let i = 0; i < links.length; i++) {
                var href = links[i].href;
                links[i].href = href.replace(shopURL,shopURL+"/en");
                }
                ```

        5. Replace `https://www.example.com` with your store URL. Change `shopURL+"/en"` to the language code you set up in your store (for example, `shopURL+"/fr"` for French).



=== "Standalone"


    The app has no native multi-language support, but there are workarounds for presenting a quiz in several languages.

    How does it work?

    - For now, you can [create multiple quizzes](#standalone-create-quizzes-in-different-languages), each one in a different language.
    - Then, each of these quizzes will have a **unique quiz ID**.
    - Embed each quiz on its own page, such as quiz-en, quiz-de or quiz-fr. Your developer can also write a [script that displays the correct quiz](#standalone-display-the-correct-quiz) popup depending on the browser language.
    - The app **syncs only the base products from your store, in the main language**. An automatically translated product has no unique ID to sync against. The quiz language changes, but the product names and descriptions stay in the original language. See the [workarounds](#standalone-redirect-to-translated-product-url).

    To set this up:

    1. **Create quizzes in different languages**{ #standalone-create-quizzes-in-different-languages }

        - **Manual Translation**: Begin by manually translating your quizzes into the desired languages. Each translated quiz will have a unique quiz ID.
        - **Quiz Settings Adjustment**: Navigate to the [Quiz Settings](/reference/quiz-builder/quiz-settings/) to modify the language of interactive elements like buttons. However, note that questions and choices need manual translation.

    2. **Display the correct quiz based on browser language**{ #standalone-display-the-correct-quiz }

        Use JavaScript to show the right quiz for the browser language. The script should:

        - Detect the browser's language.
        - Map this language to the corresponding quiz ID.
        - Update quiz links and iframes on your site to point to the correct quiz version.

        Script sample code:

        ```javascript
        document.addEventListener("DOMContentLoaded", function() {
          // Check browser's preferred language (get the first two characters to ignore region)
          const language = navigator.language.substring(0,2);

          // Your mapping of languages to quiz IDs
          const quizMapping = {
            'en': 'abc123',
            'fr': 'dfg456',
            'de': 'xyz423'
          };

          // Default language (fallback to English if not found)
          const defaultQuizId = quizMapping[language] || quizMapping['en'];

          // Find all quiz links and update the href
          const quizLinks = document.querySelectorAll('a[href^="#quiz-"]');
          quizLinks.forEach(link => {
            link.setAttribute('href', '#quiz-' + defaultQuizId);
          });

          // Find all iframes with quiz URLs and update the src attribute and the data-url attribute of the parent div
          const quizIframes = document.querySelectorAll('iframe[src^="https://admin.revenuehunt.com/public/quiz/"]');
          quizIframes.forEach(iframe => {
            const newSrc = iframe.src.replace(/quiz\/\w+/, 'quiz/' + defaultQuizId);
            iframe.src = newSrc;

            // If the parent div has the data-url attribute, update it as well
            const parentDiv = iframe.parentElement;
            if (parentDiv && parentDiv.hasAttribute('data-url')) {
              const newDataUrl = parentDiv.getAttribute('data-url').replace(/quiz\/\w+/, 'quiz/' + defaultQuizId);
              parentDiv.setAttribute('data-url', newDataUrl);
            }
          });
        });
        ```

        !!! warning

            Do not publish two quizzes on the same page. That leads to unwanted behavior.

    3. **Redirect to translated product URL**{ #standalone-redirect-to-translated-product-url }

        The app syncs only the base products from your store. A product translated into another language has no unique ID to sync against. The quiz language changes, but the product names and descriptions stay in the original language.

        A workaround for this could be creating quizzes in different languages and redirecting users to the translated product pages with [JavaScript](/how-to-guides/add-javascript/).

        1. Instead of adding a product to cart, you can change the [checkout settings](/how-to-guides/change-checkout-settings/) to `link to product` and point customers to the translated product page.
        2. By default the customer goes to the original product URL. JavaScript can change that URL automatically.
        3. For example, the Results Page can change every link from `https://www.example.com/products/productA` to `https://www.example.com/en/products/productA`. The customer is then sent to the translated product page.
        4. To redirect to an English translation of a product, one can use:
                ```javascript
                let shopURL = "https://www.example.com";

                var links = document.querySelectorAll(".lq-product a");

                for (let i = 0; i < links.length; i++) {
                var href = links[i].href;
                links[i].href = href.replace(shopURL,shopURL+"/en");
                }
                ```

        5. Replace `https://www.example.com` with your store URL. Change `shopURL+"/en"` to the language code you set up in your store (for example, `shopURL+"/fr"` for French).



    ---
    This article explains how to change the language of your quiz, translate it into other languages, and set up Shopify Markets. The quiz can then follow the market and language preference.