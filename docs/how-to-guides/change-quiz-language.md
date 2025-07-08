---
icon: material/translate-variant
---

# How to Change the Language of Your Quiz

This guide will help you change the language of your quiz, translate it into different languages or set up Shopify Markets to display the quiz in different languages based on the visitor's location and language preference.

## Change Quiz Language in Settings

=== "Shopify"

    !!! note
    
        Version 1 of the RevenueHunt App for Shopify doesn't support the Shopify Markets feature. 

    1. **Open Quiz Settings**: To change the quiz language navigate to [Quiz Settings](/reference/quiz-builder/quiz-settings/) or [`Quiz Settings -> Messages`](/reference/quiz-builder/quiz-settings/#messages).

        ![how to change quiz language messages](/images/manual_quizbuilder_quizsettings_messages.png){width="300"}
        
    2. **Language**: Choose a language from a dropdown list to change the text on the quiz buttons and placeholders into that language.
    3. **Add your own translations**: If the desired language is not available or you prefer a different translation you can modify individual instances (such as buttons and placeholders) directly within the [Messages](/reference/quiz-builder/quiz-settings/#messages) tab.
    4. **Override the translations**: Should any buttons revert to their original English translations (overriding your selected quiz language) you can manually adjust the button text in [`Quiz Builder -> Question settings`](/reference/quiz-builder/questions/#question-settings).

=== "Shopify V2"

    <div style="position: relative; padding-bottom: 53.125%; height: 0;"><iframe src="https://www.loom.com/embed/c636603e986a41a6a932c7721add7dcf?sid=5abfc134-cb3d-4ba6-934f-991533d5a11d" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! note
    
        Version 2 of the RevenueHunt App for Shopify fully supports the Shopify Markets feature. 

    Before assigning quizzes to specific markets and languages, you’ll need to create and customize the quiz versions for each language. Here’s how:

    **Step 1: Create Your Initial Quiz:**

    - Start by creating a [`new quiz`](/reference/dashboard/#new-quiz) with the basic content and questions you want to include.

    - Save this quiz as your base version, which you’ll use to duplicate for different languages.

    **Step 2: Duplicate the Quiz for Each Language:**

    - From the [Dashbaord](/reference/dashboard/), select the option to `Duplicate` your original quiz.

      ![manual_shopifyV2_quizmanagementoptions](/images/manual_shopifyV2_quizmanagementoptions.png)

    - For each duplicate quiz, go into the [`Quiz settings > Quiz content`](/reference/quiz-builder/quiz-settings/#messages) and update the language for all buttons, popups, and other interface elements.

      ![/images/manual_shopifyV2_quizbuilder_quizsettings_quizcontent.png](/images/manual_shopifyV2_quizbuilder_quizsettings_quizcontent.png)

    **Step 3: Translate Questions and Choices Separately:**

    The questions and answer choices won’t automatically translate; you’ll need to manually update these for each language version. 

    - Go through each question and answer choice to ensure they are accurately translated and culturally relevant for each target language.

    **Step 4: Change Translations for Buttons and Helpers:**

    - Go to the [Quiz Settings > Content](/reference/quiz-builder/quiz-settings/#content) tab.

    - Change the translations for buttons and helpers for each language version.
    
    **Step 5: Assign the Quiz to the Right Market and Language:**

    - Once each quiz version is ready, go to [App Settings > Shopify Markets](/reference/app-settings/#markets).

    - Select the appropriate market and language, and link each translated quiz to its respective locale. This will ensure that visitors see the correct quiz based on their market and language settings.

    By following these steps, you’ll have a well-localized quiz experience ready for each market and language, which you can then manage seamlessly in the Shopify Markets tab of your app settings.

=== "WooCommerce"

    1. **Open Quiz Settings**: To change the quiz language navigate to [Quiz Settings](/reference/quiz-builder/quiz-settings/) or [`Quiz Settings -> Messages`](/reference/quiz-builder/quiz-settings/#messages).

        ![how to change quiz language messages](/images/manual_quizbuilder_quizsettings_messages.png){width="300"}
        
    2. **Language**: Choose a language from a dropdown list to change the text on the quiz buttons and placeholders into that language.
    3. **Add your own translations**: If the desired language is not available or you prefer a different translation you can modify individual instances (such as buttons and placeholders) directly within the [Messages](/reference/quiz-builder/quiz-settings/#messages) tab.
    4. **Override the translations**: Should any buttons revert to their original English translations (overriding your selected quiz language) you can manually adjust the button text in [`Quiz Builder -> Question settings`](/reference/quiz-builder/questions/#question-settings).

=== "Magento"

    1. **Open Quiz Settings**: To change the quiz language navigate to [Quiz Settings](/reference/quiz-builder/quiz-settings/) or [`Quiz Settings -> Messages`](/reference/quiz-builder/quiz-settings/#messages).

        ![how to change quiz language messages](/images/manual_quizbuilder_quizsettings_messages.png){width="300"}
        
    2. **Language**: Choose a language from a dropdown list to change the text on the quiz buttons and placeholders into that language.
    3. **Add your own translations**: If the desired language is not available or you prefer a different translation you can modify individual instances (such as buttons and placeholders) directly within the [Messages](/reference/quiz-builder/quiz-settings/#messages) tab.
    4. **Override the translations**: Should any buttons revert to their original English translations (overriding your selected quiz language) you can manually adjust the button text in [`Quiz Builder -> Question settings`](/reference/quiz-builder/questions/#question-settings).

=== "BigCommerce"

    1. **Open Quiz Settings**: To change the quiz language navigate to [Quiz Settings](/reference/quiz-builder/quiz-settings/) or [`Quiz Settings -> Messages`](/reference/quiz-builder/quiz-settings/#messages).

        ![how to change quiz language messages](/images/manual_quizbuilder_quizsettings_messages.png){width="300"}
        
    2. **Language**: Choose a language from a dropdown list to change the text on the quiz buttons and placeholders into that language.
    3. **Add your own translations**: If the desired language is not available or you prefer a different translation you can modify individual instances (such as buttons and placeholders) directly within the [Messages](/reference/quiz-builder/quiz-settings/#messages) tab.
    4. **Override the translations**: Should any buttons revert to their original English translations (overriding your selected quiz language) you can manually adjust the button text in [`Quiz Builder -> Question settings`](/reference/quiz-builder/questions/#question-settings).

=== "Standalone"

    1. **Open Quiz Settings**: To change the quiz language navigate to [Quiz Settings](/reference/quiz-builder/quiz-settings/) or [`Quiz Settings -> Messages`](/reference/quiz-builder/quiz-settings/#messages).

        ![how to change quiz language messages](/images/manual_quizbuilder_quizsettings_messages.png){width="300"}
        
    2. **Language**: Choose a language from a dropdown list to change the text on the quiz buttons and placeholders into that language.
    3. **Add your own translations**: If the desired language is not available or you prefer a different translation you can modify individual instances (such as buttons and placeholders) directly within the [Messages](/reference/quiz-builder/quiz-settings/#messages) tab.
    4. **Override the translations**: Should any buttons revert to their original English translations (overriding your selected quiz language) you can manually adjust the button text in [`Quiz Builder -> Question settings`](/reference/quiz-builder/questions/#question-settings).

## Set Up Multilingual Quizzes

=== "Shopify"

    While our application currently lacks native multi-language support, there are effective workarounds to present quizzes in multiple languages.

    How does it work?

    - For now, it is possible to [create multiple quizzes](#step-1-create-quizzes-in-different-languages), each one in a different language. 
    - Then, each of these quizzes will have a **unique quiz ID**. 
    - You can embed each of these quizzes on a separate page on your store (eg quiz-en, quiz-de, quiz-fr…) or have your developer create a [script that displays the correct quiz](#step-2-display-the-correct-quiz-based-on-browser-language) popup depending on the browser language.
    - However, the main problem is that our app **can only sync the base products from your store (in the main language)**, as products translated automatically to other languages don't have unique product IDs that we could sync. So you can change the quiz language but the product names and descriptions will be shown in the original language. There are some [workarounds](#step-3-handling-product-sync-in-multilingual-stores) mentioned in the article that you can try.

    **Step 1: Create Quizzes in Different Languages**

    - **Manual Translation**: Begin by manually translating your quizzes into the desired languages. Each translated quiz will have a unique quiz ID.
    - **Quiz Settings Adjustment**: Navigate to the [Quiz Settings](/reference/quiz-builder/quiz-settings/) to modify the language of interactive elements like buttons. However, note that questions and choices need manual translation.

    **Step 2: Display the Correct Quiz Based on Browser Language**

    Use JavaScript to show the appropriate quiz to users based on their browser's language setting. The script should:

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

        Make sure that you don’t publish two quizzes on the same page, as this may lead to unwanted behavior.

    **Step 3: Redirect to Translated Product URL**

    Our application syncs only the base products from your store. Products translated into other languages won't have unique IDs for sync. Although you can change the quiz language, product names and descriptions will be displayed in the original language. 

    A workaround for this could be creating quizzes in different languages and redirecting users to the translated product pages with [JavaScript](/how-to-guides/add-javascript/).

    1. Instead of adding a product to cart, you can change the [checkout settings](/how-to-guides/change-checkout-settings/) to `link to product` and point customers to the translated product page.
    2. By default, the customer will be redirected to the original product URL, but you can force an automatic URL change via JavaScript. 
    3. For example, you can tell the Results Page to automatically change all the links from this `https://www.example.com/products/productA` to this `https://www.example.com/en/products/productA` This way your customers will be automatically redirected to the translated product page.
    4. To redirect to an English translation of a product, one can use:
            ```javascript
            let shopURL = "https://www.example.com";

            var links = document.querySelectorAll(".lq-product a");

            for (let i = 0; i < links.length; i++) {
            var href = links[i].href;
            links[i].href = href.replace(shopURL,shopURL+"/en");
            }
            ```

    5. Make sure to replace the `https://www.example.com` with your store URL and change the `shopURL+"/en"` to the language code you have set up in your store (for example, `shopURL+"/fr"` for French).



=== "Shopify V2"

    <div style="position: relative; padding-bottom: 53.125%; height: 0;"><iframe src="https://www.loom.com/embed/c636603e986a41a6a932c7721add7dcf?sid=5abfc134-cb3d-4ba6-934f-991533d5a11d" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! note
    
        Version 2 of the RevenueHunt App for Shopify fully supports the Shopify Markets feature. 

    Our RevenueHunt app allows you to tailor the shopping experience for customers worldwide by selecting specific quizzes for each Shopify Market and its associated languages. Here’s a step-by-step guide to help you change your quiz language based on the visitor’s location and language preference.

    **Step 1: Navigate to the Shopify Markets Settings**

    - Log in to your Shopify Admin Panel.

    - In the left-hand menu, go to Apps and select `RevenueHunt`.

    - Once in the app, look for [App Settings](/reference/app-settings/) and select the [Shopify Markets](/reference/app-settings/#markets) tab.

    **Step 2: Assign a Quiz to a Specific Shopify Market**

    - In the [Shopify Markets](/reference/app-settings/#markets) tab, you’ll see a `dropdown list` that shows all available quizzes.
    
    - From the Shopify Markets section, select the Shopify Market where you’d like to assign a quiz.

      ![manual_shopifyV2_appsettings_markets_pickquiz](/images/manual_shopifyV2_appsettings_markets_pickquiz.png)

    - Choose the default quiz you want displayed to visitors in this Market from the dropdown.

    **Step 3: Show All Locales for Language Customization**

    If you want to customize quizzes based on both market and language:

    - Toggle the `Show All Locales` option to display a detailed list of markets and associated languages.

    - You’ll now be able to assign different quizzes for each language within the same market:

      *Example: For the United States market, you can set one quiz for English-speaking customers and another for Spanish-speaking customers.*

    **Step 4: Select the Quiz for Each Locale**

    - With all locales shown, go to the specific language you want to adjust.

    - From the dropdown menu for that locale, pick the quiz that best matches the needs of that language group.

    - Save your changes to ensure the new language-specific quiz assignments are applied.

    **Step 5: Hide All Locales for Simplified View**

    If you’d like to revert to a single quiz for a Market regardless of language:

    ![manual_shopifyV2_appsettings_markets_showall](/images/manual_shopifyV2_appsettings_markets_showall.png)

    - Click the `Hide All Locales` option. This will simplify the view by removing language-specific distinctions.

    - The default quiz you’ve selected for that Market will now display to all visitors from that region, regardless of their language.

    By following these steps, you’ll be able to customize your quizzes by Market and language, ensuring each visitor has a tailored experience that feels relevant and engaging.

=== "WooCommerce"


    While our application currently lacks native multi-language support, there are effective workarounds to present quizzes in multiple languages.

    How does it work?

    - For now, it is possible to [create multiple quizzes](#step-1-create-quizzes-in-different-languages), each one in a different language. 
    - Then, each of these quizzes will have a **unique quiz ID**. 
    - You can embed each of these quizzes on a separate page on your store (eg quiz-en, quiz-de, quiz-fr…) or have your developer create a [script that displays the correct quiz](#step-2-display-the-correct-quiz-based-on-browser-language) popup depending on the browser language.
    - However, the main problem is that our app **can only sync the base products from your store (in the main language)**, as products translated automatically to other languages don't have unique product IDs that we could sync. So you can change the quiz language but the product names and descriptions will be shown in the original language. There are some [workarounds](#step-3-handling-product-sync-in-multilingual-stores) mentioned in the article that you can try.

    **Step 1: Create Quizzes in Different Languages**

    - **Manual Translation**: Begin by manually translating your quizzes into the desired languages. Each translated quiz will have a unique quiz ID.
    - **Quiz Settings Adjustment**: Navigate to the [Quiz Settings](/reference/quiz-builder/quiz-settings/) to modify the language of interactive elements like buttons. However, note that questions and choices need manual translation.

    **Step 2: Display the Correct Quiz Based on Browser Language**

    Use JavaScript to show the appropriate quiz to users based on their browser's language setting. The script should:

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

        Make sure that you don’t publish two quizzes on the same page, as this may lead to unwanted behavior.

    **Step 3: Redirect to Translated Product URL**

    Our application syncs only the base products from your store. Products translated into other languages won't have unique IDs for sync. Although you can change the quiz language, product names and descriptions will be displayed in the original language. 

    A workaround for this could be creating quizzes in different languages and redirecting users to the translated product pages with [JavaScript](/how-to-guides/add-javascript/).

    1. Instead of adding a product to cart, you can change the [checkout settings](/how-to-guides/change-checkout-settings/) to `link to product` and point customers to the translated product page.
    2. By default, the customer will be redirected to the original product URL, but you can force an automatic URL change via JavaScript. 
    3. For example, you can tell the Results Page to automatically change all the links from this `https://www.example.com/products/productA` to this `https://www.example.com/en/products/productA` This way your customers will be automatically redirected to the translated product page.
    4. To redirect to an English translation of a product, one can use:
            ```javascript
            let shopURL = "https://www.example.com";

            var links = document.querySelectorAll(".lq-product a");

            for (let i = 0; i < links.length; i++) {
            var href = links[i].href;
            links[i].href = href.replace(shopURL,shopURL+"/en");
            }
            ```

    5. Make sure to replace the `https://www.example.com` with your store URL and change the `shopURL+"/en"` to the language code you have set up in your store (for example, `shopURL+"/fr"` for French).



=== "Magento"


    While our application currently lacks native multi-language support, there are effective workarounds to present quizzes in multiple languages.

    How does it work?

    - For now, it is possible to [create multiple quizzes](#step-1-create-quizzes-in-different-languages), each one in a different language. 
    - Then, each of these quizzes will have a **unique quiz ID**. 
    - You can embed each of these quizzes on a separate page on your store (eg quiz-en, quiz-de, quiz-fr…) or have your developer create a [script that displays the correct quiz](#step-2-display-the-correct-quiz-based-on-browser-language) popup depending on the browser language.
    - However, the main problem is that our app **can only sync the base products from your store (in the main language)**, as products translated automatically to other languages don't have unique product IDs that we could sync. So you can change the quiz language but the product names and descriptions will be shown in the original language. There are some [workarounds](#step-3-handling-product-sync-in-multilingual-stores) mentioned in the article that you can try.

    **Step 1: Create Quizzes in Different Languages**

    - **Manual Translation**: Begin by manually translating your quizzes into the desired languages. Each translated quiz will have a unique quiz ID.
    - **Quiz Settings Adjustment**: Navigate to the [Quiz Settings](/reference/quiz-builder/quiz-settings/) to modify the language of interactive elements like buttons. However, note that questions and choices need manual translation.

    **Step 2: Display the Correct Quiz Based on Browser Language**

    Use JavaScript to show the appropriate quiz to users based on their browser's language setting. The script should:

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

        Make sure that you don’t publish two quizzes on the same page, as this may lead to unwanted behavior.

    **Step 3: Redirect to Translated Product URL**

    Our application syncs only the base products from your store. Products translated into other languages won't have unique IDs for sync. Although you can change the quiz language, product names and descriptions will be displayed in the original language. 

    A workaround for this could be creating quizzes in different languages and redirecting users to the translated product pages with [JavaScript](/how-to-guides/add-javascript/).

    1. Instead of adding a product to cart, you can change the [checkout settings](/how-to-guides/change-checkout-settings/) to `link to product` and point customers to the translated product page.
    2. By default, the customer will be redirected to the original product URL, but you can force an automatic URL change via JavaScript. 
    3. For example, you can tell the Results Page to automatically change all the links from this `https://www.example.com/products/productA` to this `https://www.example.com/en/products/productA` This way your customers will be automatically redirected to the translated product page.
    4. To redirect to an English translation of a product, one can use:
            ```javascript
            let shopURL = "https://www.example.com";

            var links = document.querySelectorAll(".lq-product a");

            for (let i = 0; i < links.length; i++) {
            var href = links[i].href;
            links[i].href = href.replace(shopURL,shopURL+"/en");
            }
            ```

    5. Make sure to replace the `https://www.example.com` with your store URL and change the `shopURL+"/en"` to the language code you have set up in your store (for example, `shopURL+"/fr"` for French).



=== "BigCommerce"


    While our application currently lacks native multi-language support, there are effective workarounds to present quizzes in multiple languages.

    How does it work?

    - For now, it is possible to [create multiple quizzes](#step-1-create-quizzes-in-different-languages), each one in a different language. 
    - Then, each of these quizzes will have a **unique quiz ID**. 
    - You can embed each of these quizzes on a separate page on your store (eg quiz-en, quiz-de, quiz-fr…) or have your developer create a [script that displays the correct quiz](#step-2-display-the-correct-quiz-based-on-browser-language) popup depending on the browser language.
    - However, the main problem is that our app **can only sync the base products from your store (in the main language)**, as products translated automatically to other languages don't have unique product IDs that we could sync. So you can change the quiz language but the product names and descriptions will be shown in the original language. There are some [workarounds](#step-3-handling-product-sync-in-multilingual-stores) mentioned in the article that you can try.

    **Step 1: Create Quizzes in Different Languages**

    - **Manual Translation**: Begin by manually translating your quizzes into the desired languages. Each translated quiz will have a unique quiz ID.
    - **Quiz Settings Adjustment**: Navigate to the [Quiz Settings](/reference/quiz-builder/quiz-settings/) to modify the language of interactive elements like buttons. However, note that questions and choices need manual translation.

    **Step 2: Display the Correct Quiz Based on Browser Language**

    Use JavaScript to show the appropriate quiz to users based on their browser's language setting. The script should:

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

        Make sure that you don’t publish two quizzes on the same page, as this may lead to unwanted behavior.

    **Step 3: Redirect to Translated Product URL**

    Our application syncs only the base products from your store. Products translated into other languages won't have unique IDs for sync. Although you can change the quiz language, product names and descriptions will be displayed in the original language. 

    A workaround for this could be creating quizzes in different languages and redirecting users to the translated product pages with [JavaScript](/how-to-guides/add-javascript/).

    1. Instead of adding a product to cart, you can change the [checkout settings](/how-to-guides/change-checkout-settings/) to `link to product` and point customers to the translated product page.
    2. By default, the customer will be redirected to the original product URL, but you can force an automatic URL change via JavaScript. 
    3. For example, you can tell the Results Page to automatically change all the links from this `https://www.example.com/products/productA` to this `https://www.example.com/en/products/productA` This way your customers will be automatically redirected to the translated product page.
    4. To redirect to an English translation of a product, one can use:
            ```javascript
            let shopURL = "https://www.example.com";

            var links = document.querySelectorAll(".lq-product a");

            for (let i = 0; i < links.length; i++) {
            var href = links[i].href;
            links[i].href = href.replace(shopURL,shopURL+"/en");
            }
            ```

    5. Make sure to replace the `https://www.example.com` with your store URL and change the `shopURL+"/en"` to the language code you have set up in your store (for example, `shopURL+"/fr"` for French).



=== "Standalone"


    While our application currently lacks native multi-language support, there are effective workarounds to present quizzes in multiple languages.

    How does it work?

    - For now, it is possible to [create multiple quizzes](#step-1-create-quizzes-in-different-languages), each one in a different language. 
    - Then, each of these quizzes will have a **unique quiz ID**. 
    - You can embed each of these quizzes on a separate page on your store (eg quiz-en, quiz-de, quiz-fr…) or have your developer create a [script that displays the correct quiz](#step-2-display-the-correct-quiz-based-on-browser-language) popup depending on the browser language.
    - However, the main problem is that our app **can only sync the base products from your store (in the main language)**, as products translated automatically to other languages don't have unique product IDs that we could sync. So you can change the quiz language but the product names and descriptions will be shown in the original language. There are some [workarounds](#step-3-handling-product-sync-in-multilingual-stores) mentioned in the article that you can try.

    **Step 1: Create Quizzes in Different Languages**

    - **Manual Translation**: Begin by manually translating your quizzes into the desired languages. Each translated quiz will have a unique quiz ID.
    - **Quiz Settings Adjustment**: Navigate to the [Quiz Settings](/reference/quiz-builder/quiz-settings/) to modify the language of interactive elements like buttons. However, note that questions and choices need manual translation.

    **Step 2: Display the Correct Quiz Based on Browser Language**

    Use JavaScript to show the appropriate quiz to users based on their browser's language setting. The script should:

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

        Make sure that you don’t publish two quizzes on the same page, as this may lead to unwanted behavior.

    **Step 3: Redirect to Translated Product URL**

    Our application syncs only the base products from your store. Products translated into other languages won't have unique IDs for sync. Although you can change the quiz language, product names and descriptions will be displayed in the original language. 

    A workaround for this could be creating quizzes in different languages and redirecting users to the translated product pages with [JavaScript](/how-to-guides/add-javascript/).

    1. Instead of adding a product to cart, you can change the [checkout settings](/how-to-guides/change-checkout-settings/) to `link to product` and point customers to the translated product page.
    2. By default, the customer will be redirected to the original product URL, but you can force an automatic URL change via JavaScript. 
    3. For example, you can tell the Results Page to automatically change all the links from this `https://www.example.com/products/productA` to this `https://www.example.com/en/products/productA` This way your customers will be automatically redirected to the translated product page.
    4. To redirect to an English translation of a product, one can use:
            ```javascript
            let shopURL = "https://www.example.com";

            var links = document.querySelectorAll(".lq-product a");

            for (let i = 0; i < links.length; i++) {
            var href = links[i].href;
            links[i].href = href.replace(shopURL,shopURL+"/en");
            }
            ```

    5. Make sure to replace the `https://www.example.com` with your store URL and change the `shopURL+"/en"` to the language code you have set up in your store (for example, `shopURL+"/fr"` for French).



---
This article explains how to change the language of your quiz, translate it into different languages or set up Shopify Markets to display the quiz in different languages based on the visitor's location and language preference.