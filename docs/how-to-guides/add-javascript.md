---
icon: material/language-javascript
---

# How to Add JavaScript to the Quiz

Unlock the full potential of your RevenueHunt Product Recommendation Quiz by integrating custom JavaScript. We made it very easy for developers to tap into the quiz response and get all the information they need: individual answers to questions, triggered tags and recommended products.

!!! info "With custom JavaScript, you can:"

    - add custom behavior, images, texts or logic
    - change quiz layout
    - display custom product recommendations
    - forward to any particular page on your store
    - add tracking codes to specific questions (Google Analytics, Meta Pixel)
    - and more

This guide will walk you through adding JavaScript to quiz questions and the results page. 

!!! warning "For developers and Shopify Partners"
    This guide is meant for developers and Shopify Partners. If you're not familiar with the basics of JavaScript and the Vue.js framework, it is advised to ask for help from a professional to implement this. You can find/hire a developer [here](https://experts.shopify.com/).

## Understanding JavaScript, HTML, and Liquid

Before diving into the implementation, it's important to understand the different technologies you can use to customize your quiz. The available technologies vary by platform.

| Technology | Description | What you can use it for |
|------------|-------------|-------------------------|
| JavaScript | A programming language that adds interactivity and dynamic behavior to web pages. | Adding custom logic and calculations (like BMI calculators) |
| HTML | A markup language that defines the structure and content of web pages. | Adding custom content blocks and layouts |
| Liquid | A templating language specific to Shopify that allows dynamic content insertion. | Displaying quiz answers and user responses dynamically |

**Platform support**

=== "Shopify"

    **Available**: JavaScript + HTML + Liquid  
    Use Liquid when you need Shopify data or server-rendered dynamic content. Use JavaScript for interactivity and logic.

=== "Shopify (Legacy)"

    **Available**: JavaScript + HTML  
    Liquid is not available in Shopify (Legacy).

=== "WooCommerce"

    **Available**: JavaScript + HTML  
    Liquid is not available in WooCommerce.

=== "Magento"

    **Available**: JavaScript + HTML  
    Liquid is not available in Magento.

=== "BigCommerce"

    **Available**: JavaScript + HTML  
    Liquid is not available in BigCommerce.

=== "Standalone"

    **Available**: JavaScript + HTML  
    Liquid is not available in Standalone.

## Access the Custom JavaScript Console

You can add custom JavaScirpt to the quiz results page and the quiz questions.

### Results Page

=== "Shopify"

    ??? info "Use JavaScript on Results Page when you want to:"
        - Access all quiz data - See all answers, scores, and variables after quiz completion
        - Work with recommendations - Access and manipulate recommended products/collections
        - Cart operations - Add products to cart, apply discount codes
        - Display calculations - Show results based on all collected answers (BMI, skin type, etc.)
        - Conversion tracking - Fire analytics events with complete quiz data
        - Customize recommendations - Modify or filter displayed products


    1. Navigate to the [Results Page Settings](/reference/quiz-builder/results-page/) in the Quiz Builder.

        ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_resultspagesettings](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_resultspagesettings.png)

    2. Scroll down to find the **Custom JavaScript** section and open it.

        ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_resultspagesettings_customjs](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_resultspagesettings_customjs.png)

    3. This is your canvas for crafting and deploying custom scripts that can modify the quiz's behavior based on user interactions and results.

        !!! tip "Run the custom code"

            `▷ / ❚❚` - Press this button to run the custom code or enable/disable the custom code execution.

        !!! tip "Get help with custom JavaScript"

            Click on `✨Get help with custom JavaScript` to open a chat window with the Quiz Copilot AI. It can directly write JavaScript code for you.

    4. Remember to click the `Save` button to update the preview/live quiz.

=== "Shopify (Legacy)"

    1. Navigate to the [Results Page Settings](/reference/quiz-builder/results-page/) in the Quiz Builder.
    2. Select [**Advanced Settings**](/reference/quiz-builder/results-page/#advanced-settings).
    3. Scroll down to find the **Custom JavaScript** section and click `add`.
    4. This is your canvas for crafting and deploying custom scripts that can modify the quiz's behavior based on user interactions and results.
    5. Remember to click the `Publish` button to update the preview/live quiz.

=== "WooCommerce"

    1. Navigate to the [Results Page Settings](/reference/quiz-builder/results-page/) in the Quiz Builder.
    2. Select [**Advanced Settings**](/reference/quiz-builder/results-page/#advanced-settings).
    3. Scroll down to find the **Custom JavaScript** section and click `add`.
    4. This is your canvas for crafting and deploying custom scripts that can modify the quiz's behavior based on user interactions and results.
    5. Remember to click the `Publish` button to update the preview/live quiz.

=== "Magento"

    1. Navigate to the [Results Page Settings](/reference/quiz-builder/results-page/) in the Quiz Builder.
    2. Select [**Advanced Settings**](/reference/quiz-builder/results-page/#advanced-settings).
    3. Scroll down to find the **Custom JavaScript** section and click `add`.
    4. This is your canvas for crafting and deploying custom scripts that can modify the quiz's behavior based on user interactions and results.
    5. Remember to click the `Publish` button to update the preview/live quiz.

=== "BigCommerce"

    1. Navigate to the [Results Page Settings](/reference/quiz-builder/results-page/) in the Quiz Builder.
    2. Select [**Advanced Settings**](/reference/quiz-builder/results-page/#advanced-settings).
    3. Scroll down to find the **Custom JavaScript** section and click `add`.
    4. This is your canvas for crafting and deploying custom scripts that can modify the quiz's behavior based on user interactions and results.
    5. Remember to click the `Publish` button to update the preview/live quiz.

=== "Standalone"

    1. Navigate to the [Results Page Settings](/reference/quiz-builder/results-page/) in the Quiz Builder.
    2. Select [**Advanced Settings**](/reference/quiz-builder/results-page/#advanced-settings).
    3. Scroll down to find the **Custom JavaScript** section and click `add`.
    4. This is your canvas for crafting and deploying custom scripts that can modify the quiz's behavior based on user interactions and results.
    5. Remember to click the `Publish` button to update the preview/live quiz.

### Quiz Questions

=== "Shopify"

    ??? info "Use JavaScript on Questions when you want to:"
        - Control quiz flow - Auto-advance, skip questions, or go back based on answers
        - Validate inputs - Check if answers meet certain criteria before allowing progression
        - Dynamic question content - Change question text, show/hide elements based on previous answers
        - Real-time interactions - Update the page as users select answers
        - Set calculated values - Compute values to use in later questions
        - Track individual questions - Fire analytics events for specific questions


    1. Navigate to the [Quiz Builder](/reference/quiz-builder/).
    2. Open [question settings](/reference/quiz-builder/questions/#question-settings).

        ![manual_shopifyV2_quizbuilder_quizbuilder_questionsettings](/images/manual_shopifyV2_quizbuilder_quizbuilder_questionsettings.png)

    3. Scroll down to find the **Custom JavaScript** section and open it.

        ![manual_shopifyV2_quizbuilder_quizbuilder_questionsettings_customJS](/images/manual_shopifyV2_quizbuilder_quizbuilder_questionsettings_customJS.png)

    4. This is your canvas for crafting and deploying custom scripts that can modify the quiz's behavior based on user interactions and results.

        !!! tip "Run the custom code"

            `▷ / ❚❚` - Press this button to run the custom code or enable/disable the custom code execution.

        !!! tip "Get help with custom JavaScript"

            Click on `✨Get help with custom JavaScript` to open a chat window with the Quiz Copilot AI. It can directly write JavaScript code for you.

    5. Remember to click the `Save` button to update the preview/live quiz.

=== "Shopify (Legacy)"

    1. Navigate to the [Quiz Builder](/reference/quiz-builder/).
    2. Open [question settings](/reference/quiz-builder/questions/#question-settings).
    3. Scroll down to find the **Custom JavaScript** section and click `add`.
    4. This is your canvas for crafting and deploying custom scripts that can modify the quiz's behavior based on user interactions and results.
    5. Remember to click the `Publish` button to update the preview/live quiz.

=== "WooCommerce"

    1. Navigate to the [Quiz Builder](/reference/quiz-builder/).
    2. Open [question settings](/reference/quiz-builder/questions/#question-settings).
    3. Scroll down to find the **Custom JavaScript** section and click `add`.
    4. This is your canvas for crafting and deploying custom scripts that can modify the quiz's behavior based on user interactions and results.
    5. Remember to click the `Publish` button to update the preview/live quiz.

=== "Magento"

    1. Navigate to the [Quiz Builder](/reference/quiz-builder/).
    2. Open [question settings](/reference/quiz-builder/questions/#question-settings).
    3. Scroll down to find the **Custom JavaScript** section and click `add`.
    4. This is your canvas for crafting and deploying custom scripts that can modify the quiz's behavior based on user interactions and results.
    5. Remember to click the `Publish` button to update the preview/live quiz.

=== "BigCommerce"

    1. Navigate to the [Quiz Builder](/reference/quiz-builder/).
    2. Open [question settings](/reference/quiz-builder/questions/#question-settings).
    3. Scroll down to find the **Custom JavaScript** section and click `add`.
    4. This is your canvas for crafting and deploying custom scripts that can modify the quiz's behavior based on user interactions and results.
    5. Remember to click the `Publish` button to update the preview/live quiz.
      
=== "Standalone"

    1. Navigate to the [Quiz Builder](/reference/quiz-builder/).
    2. Open [question settings](/reference/quiz-builder/questions/#question-settings).
    3. Scroll down to find the **Custom JavaScript** section and click `add`.
    4. This is your canvas for crafting and deploying custom scripts that can modify the quiz's behavior based on user interactions and results.
    5. Remember to click the `Publish` button to update the preview/live quiz.

### Via Custom HTML Block

??? info "Use Custom HTML Blocks when"

    - You want JavaScript to run in a **specific location** in your layout
    - You need to **combine HTML, Liquid, and JavaScript** together
    - You want **different scripts for different content blocks**
    - You're adding **small, context-specific scripts** (like tracking a specific element)
    - You need JavaScript to run **multiple times** (e.g., once per product in recommendations)
    
=== "Shopify"

    You can also add custom JavaScript directly in HTML blocks throughout your quiz. These blocks support both JavaScript and Liquid templating for dynamic content.

    #### Results Page

    1. Navigate to the [Results Page](/reference/quiz-builder/results-page/) in the Quiz Builder.
    2. Add or edit a [**Custom HTML block**](/reference/quiz-builder/results-page/#custom-html) in your results page layout.
    3. Add your JavaScript using `<script>` tags:

        ```html
        <script>
        // Your JavaScript code here
        console.log('Quiz completed with result:', quiz.currentResult.ref);
        </script>
        ```

    4. Use **Liquid templating** alongside JavaScript for dynamic content:

        ```html
        <script>
        // Access quiz data with Liquid
        const userName = '{{ quiz.answers.byBlock['name-field']?.value || 'Guest' }}';
        console.log('Welcome', userName);
        </script>
        ```

    5. Click `Save` to update the preview/live quiz.

    !!! tip "Run the custom code"

        `▷ / ❚❚` - Press this button to run the custom code or enable/disable the custom code execution.

    #### Questions

    1. Navigate to the [Quiz Builder](/reference/quiz-builder/) and open a question.
    2. Add or edit a [**Custom HTML block**](/reference/quiz-builder/questions/#custom-html) within the question.
    3. Add your JavaScript using `<script>` tags:

        ```html
        <script>
        // JavaScript that runs when this question is displayed
        console.log('Current question:', quiz.currentQuestion.ref);
        </script>
        ```

    4. Combine JavaScript with Liquid templating:

        ```html
        <script>
        // Dynamic content based on previous answers
        const previousAnswer = '{{ quiz.answers.byBlock['previous-question']?.value }}';
        if (previousAnswer === 'yes') {
          // Custom logic based on previous answer
          console.log('User answered yes previously');
        }
        </script>
        ```

    5. Click `Save` to update the preview/live quiz.

    !!! tip "Run the custom code"

        `▷ / ❚❚` - Press this button to run the custom code or enable/disable the custom code execution.



    #### Slot Item Composition

    1. Navigate to the [Results Page Settings](/reference/quiz-builder/results-page/) in the Quiz Builder.
    2. Open the [Product Block](/reference/quiz-builder/results-page/#product-block) and in the [Slot settings](/reference/quiz-builder/results-page/#slot-settings) you can find the [**Slot item composition**](/reference/quiz-builder/results-page/#slot-item-composition) settings for your product recommendations.
    3. Add or edit a **Custom HTML block** within a product slot.
    4. Add JavaScript that interacts with individual product data:

        ```html
        <script>
        // Access the current product in the slot
        const productTitle = '{{ item.title }}';
        const productPrice = '{{ item.priceRange.minVariantPrice.amount }}';

        console.log('Product:', productTitle, 'Price:', productPrice);

        // Add custom behavior for this specific product
        if (productTitle.includes('Premium')) {
          // Special handling for premium products
          console.log('This is a premium product!');
        }
        </script>
        ```

    5. Use Liquid variables like `{{ item }}` to access the current product/variant/collection object.
    6. Click `Save` to update the preview/live quiz.

    !!! tip "Run the custom code"

        `▷ / ❚❚` - Press this button to run the custom code or enable/disable the custom code execution.

=== "Shopify (Legacy)"

    Not available.

=== "WooCommerce"

    Not available.

=== "Magento"

    Not available.

=== "BigCommerce"

    Not available.

=== "Standalone"

    Not available.

## Find Block and Question IDs

=== "Shopify"

    Before you start writing custom JavaScript, you'll need to know how to find the IDs (references) for your questions and blocks. These IDs are used to access specific answers and elements in your quiz.

    !!! info "How to Find Block and Question IDs"

        **Method 1: Copy from Quiz Builder (Recommended)**
        
        1. Open your quiz in the Quiz Builder
        2. Click on any question or block element
        3. Look for the block ID in the settings panel - it's usually displayed at the top
        4. Click the copy icon next to the ID to copy it to your clipboard
        5. Use this ID in your JavaScript (e.g., `quiz.answers.byBlock['your-block-id']`)

        **Method 2: Inspect Element in Browser**
        
        1. Open your quiz in preview or on your live site
        2. Right-click on the question or element you want to reference
        3. Select "Inspect" or "Inspect Element" from the context menu
        4. Look for `id` or `data-block-ref` attributes in the HTML
        5. The value of these attributes is your block reference

        **Example IDs you might see:**
        
        - `qbc-skintype` (question block choice)
        - `qbi-email` (question block input)
        - `q-concerns` (question)
        - `r-results` (result page)

        !!! warning "Use the Exact ID"

            Block references are case-sensitive! Make sure to copy them exactly as they appear. `qbc-skintype` is different from `qbc-SkinType`.

        ??? info "Quick Test"

            To see all your current answers and their block references, add this to your Custom JavaScript section:

            ```javascript
            console.log('All answers by block:', quiz.answers.byBlock);
            ```

            Then open your browser's Console (F12 → Console tab) and take the quiz. You'll see all the block IDs and their corresponding values.
            
=== "Shopify (Legacy)"

    In Shopify Legacy, you'll need to find the **Slide ID** for each question to access its value with `prq.getSlideValue(slideId)`.

    !!! tip "How to Find Slide IDs"

        **Inspect in Browser Console**
        
        1. Open your quiz in preview or live
        2. Press F12 to open Developer Tools → Console tab
        3. Type `prq.quizSlides()` and press Enter
        4. Expand the results to see all slides with their IDs
        5. Look for the `id` property of each slide

        **Method 3: Inspect Element**
        
        1. Right-click on the question element
        2. Select "Inspect Element"
        3. Look for `data-slide-id` or similar attributes in the HTML

    **Example Slide IDs:** `rgiq0oE`, `0Mi2qLN`, `abc123`

=== "WooCommerce"

    In WooCommerce, you'll need to find the **Slide ID** for each question to access its value with `prq.getSlideValue(slideId)`.

    !!! tip "How to Find Slide IDs"

        **Inspect in Browser Console**
        
        1. Open your quiz in preview or live
        2. Press F12 to open Developer Tools → Console tab
        3. Type `prq.quizSlides()` and press Enter
        4. Expand the results to see all slides with their IDs
        5. Look for the `id` property of each slide

        **Method 3: Inspect Element**
        
        1. Right-click on the question element
        2. Select "Inspect Element"
        3. Look for `data-slide-id` or similar attributes in the HTML

    **Example Slide IDs:** `rgiq0oE`, `0Mi2qLN`, `abc123`


=== "Magento"

    In Magento, you'll need to find the **Slide ID** for each question to access its value with `prq.getSlideValue(slideId)`.

    !!! tip "How to Find Slide IDs"

        **Inspect in Browser Console**
        
        1. Open your quiz in preview or live
        2. Press F12 to open Developer Tools → Console tab
        3. Type `prq.quizSlides()` and press Enter
        4. Expand the results to see all slides with their IDs
        5. Look for the `id` property of each slide

        **Method 3: Inspect Element**
        
        1. Right-click on the question element
        2. Select "Inspect Element"
        3. Look for `data-slide-id` or similar attributes in the HTML

    **Example Slide IDs:** `rgiq0oE`, `0Mi2qLN`, `abc123`


=== "BigCommerce"

    In BigCommerce, you'll need to find the **Slide ID** for each question to access its value with `prq.getSlideValue(slideId)`.

    !!! tip "How to Find Slide IDs"

        **Inspect in Browser Console**
        
        1. Open your quiz in preview or live
        2. Press F12 to open Developer Tools → Console tab
        3. Type `prq.quizSlides()` and press Enter
        4. Expand the results to see all slides with their IDs
        5. Look for the `id` property of each slide

        **Method 3: Inspect Element**
        
        1. Right-click on the question element
        2. Select "Inspect Element"
        3. Look for `data-slide-id` or similar attributes in the HTML

    **Example Slide IDs:** `rgiq0oE`, `0Mi2qLN`, `abc123`



=== "Standalone"

    In Standalone, you'll need to find the **Slide ID** for each question to access its value with `prq.getSlideValue(slideId)`.

    !!! tip "How to Find Slide IDs"

        **Inspect in Browser Console**
        
        1. Open your quiz in preview or live
        2. Press F12 to open Developer Tools → Console tab
        3. Type `prq.quizSlides()` and press Enter
        4. Expand the results to see all slides with their IDs
        5. Look for the `id` property of each slide

        **Method 3: Inspect Element**
        
        1. Right-click on the question element
        2. Select "Inspect Element"
        3. Look for `data-slide-id` or similar attributes in the HTML

    **Example Slide IDs:** `rgiq0oE`, `0Mi2qLN`, `abc123`



## Console.log(x) Function

=== "Shopify"

    In the `💎Built for Shopify` version of the RevenueHunt app, custom JavaScript receives two parameters: `quiz` (read-only context) and `actions` (methods).


    ### The `quiz` Object

    Your JavaScript code has access to the `quiz` object containing all the current state data:

    **Quiz Context Properties**

    | Property | Description |
    |----------|-------------|
    | `quiz.metadata.responseId` | Unique response identifier |
    | `quiz.metadata.language` | Quiz language code |
    | `quiz.metadata.inBuilder` | `true` if in builder preview |

    **Question Mode Properties**

    | Property | Type | Description |
    |----------|------|-------------|
    | `quiz.id` | string | Quiz identifier |
    | `quiz.mode` | string | Always `'question'` on question pages |
    | `quiz.currentQuestion` | object | Current question data |
    | `quiz.questions` | array | All quiz questions |
    | `quiz.results` | array | All result pages |

    **Accessing Answers (Question Mode)**

    | Property | Description |
    |----------|-------------|
    | `quiz.answers.list` | Array of all answers in chronological order |
    | `quiz.answers.byBlock['ref']` | Answer object keyed by block reference |
    | `quiz.answers.byQuestion['ref']` | Answers grouped by question reference |
    | `quiz.answers.latest` | Most recent answer |

    Each answer object contains:

    | Property | Description |
    |----------|-------------|
    | `.value` | The answer value (string) |
    | `.blockRef` | Block reference ID |
    | `.questionRef` | Question reference ID |
    | `.choicesRefs` | Array of selected choice IDs |
    | `.isValid` | Whether answer passed validation |

    **Variables & Scoring**

    | Property | Description |
    |----------|-------------|
    | `quiz.variables.scores` | Object with variable scores `{ varName: number }` |
    | `quiz.variables.highest` | Reference of highest-scoring variable |

    **Progress (Question Mode)**

    | Property | Description |
    |----------|-------------|
    | `quiz.progress.index` | 0-based question index |
    | `quiz.progress.displayStep` | 1-based step number (for display) |
    | `quiz.progress.totalQuestions` | Total number of questions |
    | `quiz.progress.percentComplete` | Completion percentage (0-100) |
    | `quiz.progress.hasPrevious` | Can navigate back |
    | `quiz.progress.hasNext` | Can navigate forward |

    **Results Page Properties**

    | Property | Description |
    |----------|-------------|
    | `quiz.mode` | Always `'result'` on results pages |
    | `quiz.currentResult` | Current result page data |
    | `quiz.resultContext.slotItems` | Object of recommended products/collections keyed by Shopify GID |
    | `quiz.resultContext.cartItems` | Array of items currently in cart |
    | `quiz.resultContext.discounts` | Object with `applied` array and `eligible` boolean |

    ### Actions (Methods)

    **Navigation Actions**

    | Method | Description |
    |--------|-------------|
    | `actions.next()` | Navigate to next question |
    | `actions.previous()` | Navigate to previous question |
    | `actions.overrideNext(ref)` | Redirect to specific question/result (e.g., `'q-skintype'`, `'r-results'`) |

    **Answer Management**

    | Method | Description |
    |--------|-------------|
    | `actions.setAnswer(blockRef, value)` | Set answer value |
    | `actions.setAnswers(obj)` | Batch update multiple answers |
    | `actions.clearAnswer(blockRef)` | Clear an answer |
    | `actions.removeAnswer(blockRef)` | Remove answer completely |

    **Cart Actions (Results Page Only)**

    | Method | Description |
    |--------|-------------|
    | `actions.addAllToCart()` | Add all recommended items to cart (async) |
    | `actions.addToCart(variantId, qty, sellingPlanId?)` | Add specific item to cart (async) |
    | `actions.applyDiscountCode(code)` | Apply discount code (async) |

    ### DOM Helpers

    Since the quiz may render in a shadow DOM, use these helpers instead of `document.querySelector`:

    | Method | Description |
    |--------|-------------|
    | `window.quiz.querySelector(selector)` | Find element in quiz |
    | `window.quiz.querySelectorAll(selector)` | Find all matching elements |
    | `window.quiz.getElementById(id)` | Find element by ID |

    ### Global Event Handler

    ```javascript
    window.quiz.onChange = (event) => {
      // event.blockRef - Block that changed
      // event.value - New value
      // event.selectedLabel - Label of selected choice
    };
    ```

    ### JavaScript Examples

    **Conditional navigation based on score:**
    ```javascript
    if ((quiz.variables.scores.sensitive ?? 0) > 80) {
      actions.overrideNext('q-sensitive-routine');
    }
    ```

    **Update element based on answer:**
    ```javascript
    const name = quiz.answers.byBlock['qbi-name']?.value || 'Guest';
    const el = window.quiz.getElementById('greeting');
    if (el) el.textContent = `Welcome, ${name}!`;
    ```

    **Auto-advance based on selection:**
    ```javascript
    window.quiz.onChange = (event) => {
      if (event.blockRef === 'qbc-skintype' && event.selectedLabel === 'Oily') {
        actions.overrideNext('q-oily-concerns');
      }
    };
    ```

    **Batch update answers:**
    ```javascript
    const age = parseInt(quiz.answers.byBlock['qbi-age']?.value || '0');
    actions.setAnswers({
      'qbc-age-group': age < 25 ? 'young' : 'mature',
      'qbc-eligible': age >= 18 ? 'yes' : 'no'
    });
    ```

    **Auto-add to cart for premium customers (Results Page):**
    ```javascript
    if ((quiz.variables.scores.premium ?? 0) > 80) {
      await actions.addAllToCart();
    }
    ```

    **Apply discount based on cart value (Results Page):**
    ```javascript
    const itemCount = Object.keys(quiz.resultContext.slotItems || {}).length;
    if (itemCount >= 3) {
      await actions.applyDiscountCode('BUNDLE20');
    }
    ```

    **Track quiz completion with analytics (Results Page):**
    ```javascript
    // Send quiz completion data to your analytics
    const data = {
      responseId: quiz.metadata.responseId,
      skinType: quiz.variables.highest,
      scores: quiz.variables.scores,
      recommendedProducts: Object.keys(quiz.resultContext.slotItems || {}).length
    };

    // Example: Send to your analytics endpoint
    fetch('/api/quiz-completed', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    ```

    ### Debugging

    To explore available data, you can add a `debugger` statement to your JavaScript code:

    ```javascript
    debugger;
    // Your code goes here
    ```

    When you view the quiz in your browser with Developer Tools open (F12), the code execution will pause at the debugger statement. In the Sources tab, you'll see the `quiz` and `actions` parameters:

    ![debugger statement in browser](/images/how_to_shopifyv2_debugger_browser.png)

    You can then:

    1. Hover over these variables to inspect their values
    2. Use the console panel while paused to evaluate expressions
    3. Type `quiz` or `actions` in the console to examine their structure

    Alternatively, you can use console.log to output these objects to the console:

    ```javascript
    console.log('Quiz context:', quiz);
    console.log('Available actions:', actions);
    console.log('Current answers:', quiz.answers);
    console.log('All answers by block:', quiz.answers.byBlock);
    console.log('Variable scores:', quiz.variables.scores);
    ```

    To access the console in your browser:

    1. Right-click anywhere on the page and select "Inspect" or press F12
    2. Click on the "Console" tab
    3. Look for your logged output

    This will help you understand the structure of these objects so you can access the specific properties you need in your custom JavaScript.

    !!! tip "Finding Block References"
    
        Not sure what block reference to use? See [Finding Your Block and Question References](#finding-your-block-and-question-references) above for detailed instructions.


=== "Shopify (Legacy)"

    To begin, let's log the quiz response object to the console:

    ```javascript
    console.log(prq);
    console.log(prq.quizSlides()); // See all slides and their IDs
    ```

    This line of code will display the available Vue.js functions and properties within the prq scope in your browser's console, allowing you to inspect the quiz data in real-time.

    ![how to add javascript consolelog](/images/how_to_add_javascript_consolelog.png)

    **Custom JavaScript Capabilities**

    The `prq` object is your gateway to customizing the quiz experience. Here's how you can use it:

    **Quiz Data Manipulation**

    - **Accessing Quiz Slides and Responses**: Use `prq.quizSlides()` to retrieve all quiz slides/questions, including user responses.
    - **Fetching Specific Slide Values**: Obtain the value of a particular slide by using `prq.getSlideValue(slideId)`.

    **Participant Information Retrieval**

    - **Lead Details**: Easily fetch the quiz participant's email, phone number, and name using `prq.leadEmail()`, `prq.leadPhone()`, and `prq.leadName()`, respectively.

    **Results Page Customization**

    - **Manipulating Results Page Content**: Access and modify the contents of the results page, including blocks and products, using `prq.resultsPage()`.
    - **Product Recommendations**: Leverage `prq.recommendedProducts()` and `prq.mostVotedProduct()` to customize product suggestions.
    - **Automatic Actions**: Automatically add products to the cart or proceed to checkout using `prq.addAllToCart()` and `prq.checkout()`.
    - **Discount Codes**: Apply specific discount codes with `prq.setDiscountCode('10-OFF')`.

    **Navigation and Engagement**

    - **Quiz Navigation**: Offer options to retake the quiz, close it, or open it in a popup through `prq.retakeQuiz()`, `prq.closeQuiz()`, and `window.openQuizPopup('quizID')`.

    ```html
    /* List of all the quiz slides/questions (including the responded values) */
    prq.quizSlides();

    /* get the slide/question value by passing the slide ID  */
    prq.getSlideValue(slideId);

    /* get the lead's email  */
    prq.leadEmail();

    /* get the lead's phone  */
    prq.leadPhone();

    /* get the lead's name  */
    prq.leadName();

    /* List contents of the results page, blocks, products, etc. */
    prq.resultsPage();

    /* List recommended products, sorted by number of votes */
    prq.recommendedProducts();

    /* Show most voted product */
    prq.mostVotedProduct();

    /* adds all the products to cart automatically */
    prq.addAllToCart();

    /* proceeds to cart/checkout automatically */
    prq.checkout();

    /* set specific discount code \*/
    prq.setDiscountCode('10-OFF');

    /* get the response permalink url */
    prq.getResponsePermalink();

    /* retake quiz */
    prq.retakeQuiz();

    /* close quiz */
    prq.closeQuiz();

    /* open quiz popup */
    window.openQuizPopup('dbqHqN');
    dbqHqN is the quiz ID
    ```

    For other functions and properties refer to the [console.log(prq)](#consolelogprq-function).

=== "WooCommerce"

    To begin, let's log the quiz response object to the console:

    ```javascript
    console.log(prq);
    console.log(prq.quizSlides()); // See all slides and their IDs
    ```

    This line of code will display the available Vue.js functions and properties within the prq scope in your browser's console, allowing you to inspect the quiz data in real-time.

    ![how to add javascript consolelog](/images/how_to_add_javascript_consolelog.png)

    **Custom JavaScript Capabilities**

    The `prq` object is your gateway to customizing the quiz experience. Here's how you can use it:

    **Quiz Data Manipulation**

    - **Accessing Quiz Slides and Responses**: Use `prq.quizSlides()` to retrieve all quiz slides/questions, including user responses.
    - **Fetching Specific Slide Values**: Obtain the value of a particular slide by using `prq.getSlideValue(slideId)`.

    **Participant Information Retrieval**

    - **Lead Details**: Easily fetch the quiz participant's email, phone number, and name using `prq.leadEmail()`, `prq.leadPhone()`, and `prq.leadName()`, respectively.

    **Results Page Customization**

    - **Manipulating Results Page Content**: Access and modify the contents of the results page, including blocks and products, using `prq.resultsPage()`.
    - **Product Recommendations**: Leverage `prq.recommendedProducts()` and `prq.mostVotedProduct()` to customize product suggestions.
    - **Automatic Actions**: Automatically add products to the cart or proceed to checkout using `prq.addAllToCart()` and `prq.checkout()`.
    - **Discount Codes**: Apply specific discount codes with `prq.setDiscountCode('10-OFF')`.

    **Navigation and Engagement**

    - **Quiz Navigation**: Offer options to retake the quiz, close it, or open it in a popup through `prq.retakeQuiz()`, `prq.closeQuiz()`, and `window.openQuizPopup('quizID')`.

    ```html
    /* List of all the quiz slides/questions (including the responded values) */
    prq.quizSlides();

    /* get the slide/question value by passing the slide ID  */
    prq.getSlideValue(slideId);

    /* get the lead's email  */
    prq.leadEmail();

    /* get the lead's phone  */
    prq.leadPhone();

    /* get the lead's name  */
    prq.leadName();

    /* List contents of the results page, blocks, products, etc. */
    prq.resultsPage();

    /* List recommended products, sorted by number of votes */
    prq.recommendedProducts();

    /* Show most voted product */
    prq.mostVotedProduct();

    /* adds all the products to cart automatically */
    prq.addAllToCart();

    /* proceeds to cart/checkout automatically */
    prq.checkout();

    /* set specific discount code \*/
    prq.setDiscountCode('10-OFF');

    /* get the response permalink url */
    prq.getResponsePermalink();

    /* retake quiz */
    prq.retakeQuiz();

    /* close quiz */
    prq.closeQuiz();

    /* open quiz popup */
    window.openQuizPopup('dbqHqN');
    dbqHqN is the quiz ID
    ```

    For other functions and properties refer to the [console.log(prq)](#consolelogprq-function).

=== "Magento"

    To begin, let's log the quiz response object to the console:

    ```javascript
    console.log(prq);
    console.log(prq.quizSlides()); // See all slides and their IDs
    ```

    This line of code will display the available Vue.js functions and properties within the prq scope in your browser's console, allowing you to inspect the quiz data in real-time.

    ![how to add javascript consolelog](/images/how_to_add_javascript_consolelog.png)

    **Custom JavaScript Capabilities**

    The `prq` object is your gateway to customizing the quiz experience. Here's how you can use it:

    **Quiz Data Manipulation**

    - **Accessing Quiz Slides and Responses**: Use `prq.quizSlides()` to retrieve all quiz slides/questions, including user responses.
    - **Fetching Specific Slide Values**: Obtain the value of a particular slide by using `prq.getSlideValue(slideId)`.

    **Participant Information Retrieval**

    - **Lead Details**: Easily fetch the quiz participant's email, phone number, and name using `prq.leadEmail()`, `prq.leadPhone()`, and `prq.leadName()`, respectively.

    **Results Page Customization**

    - **Manipulating Results Page Content**: Access and modify the contents of the results page, including blocks and products, using `prq.resultsPage()`.
    - **Product Recommendations**: Leverage `prq.recommendedProducts()` and `prq.mostVotedProduct()` to customize product suggestions.
    - **Automatic Actions**: Automatically add products to the cart or proceed to checkout using `prq.addAllToCart()` and `prq.checkout()`.
    - **Discount Codes**: Apply specific discount codes with `prq.setDiscountCode('10-OFF')`.

    **Navigation and Engagement**

    - **Quiz Navigation**: Offer options to retake the quiz, close it, or open it in a popup through `prq.retakeQuiz()`, `prq.closeQuiz()`, and `window.openQuizPopup('quizID')`.

    ```html
    /* List of all the quiz slides/questions (including the responded values) */
    prq.quizSlides();

    /* get the slide/question value by passing the slide ID  */
    prq.getSlideValue(slideId);

    /* get the lead's email  */
    prq.leadEmail();

    /* get the lead's phone  */
    prq.leadPhone();

    /* get the lead's name  */
    prq.leadName();

    /* List contents of the results page, blocks, products, etc. */
    prq.resultsPage();

    /* List recommended products, sorted by number of votes */
    prq.recommendedProducts();

    /* Show most voted product */
    prq.mostVotedProduct();

    /* adds all the products to cart automatically */
    prq.addAllToCart();

    /* proceeds to cart/checkout automatically */
    prq.checkout();

    /* set specific discount code \*/
    prq.setDiscountCode('10-OFF');

    /* get the response permalink url */
    prq.getResponsePermalink();

    /* retake quiz */
    prq.retakeQuiz();

    /* close quiz */
    prq.closeQuiz();

    /* open quiz popup */
    window.openQuizPopup('dbqHqN');
    dbqHqN is the quiz ID
    ```

    For other functions and properties refer to the [console.log(prq)](#consolelogprq-function).

=== "BigCommerce"

    To begin, let's log the quiz response object to the console:

    ```javascript
    console.log(prq);
    console.log(prq.quizSlides()); // See all slides and their IDs
    ```

    This line of code will display the available Vue.js functions and properties within the prq scope in your browser's console, allowing you to inspect the quiz data in real-time.

    ![how to add javascript consolelog](/images/how_to_add_javascript_consolelog.png)

    **Custom JavaScript Capabilities**

    The `prq` object is your gateway to customizing the quiz experience. Here's how you can use it:

    **Quiz Data Manipulation**

    - **Accessing Quiz Slides and Responses**: Use `prq.quizSlides()` to retrieve all quiz slides/questions, including user responses.
    - **Fetching Specific Slide Values**: Obtain the value of a particular slide by using `prq.getSlideValue(slideId)`.

    **Participant Information Retrieval**

    - **Lead Details**: Easily fetch the quiz participant's email, phone number, and name using `prq.leadEmail()`, `prq.leadPhone()`, and `prq.leadName()`, respectively.

    **Results Page Customization**

    - **Manipulating Results Page Content**: Access and modify the contents of the results page, including blocks and products, using `prq.resultsPage()`.
    - **Product Recommendations**: Leverage `prq.recommendedProducts()` and `prq.mostVotedProduct()` to customize product suggestions.
    - **Automatic Actions**: Automatically add products to the cart or proceed to checkout using `prq.addAllToCart()` and `prq.checkout()`.
    - **Discount Codes**: Apply specific discount codes with `prq.setDiscountCode('10-OFF')`.

    **Navigation and Engagement**

    - **Quiz Navigation**: Offer options to retake the quiz, close it, or open it in a popup through `prq.retakeQuiz()`, `prq.closeQuiz()`, and `window.openQuizPopup('quizID')`.

    ```html
    /* List of all the quiz slides/questions (including the responded values) */
    prq.quizSlides();

    /* get the slide/question value by passing the slide ID  */
    prq.getSlideValue(slideId);

    /* get the lead's email  */
    prq.leadEmail();

    /* get the lead's phone  */
    prq.leadPhone();

    /* get the lead's name  */
    prq.leadName();

    /* List contents of the results page, blocks, products, etc. */
    prq.resultsPage();

    /* List recommended products, sorted by number of votes */
    prq.recommendedProducts();

    /* Show most voted product */
    prq.mostVotedProduct();

    /* adds all the products to cart automatically */
    prq.addAllToCart();

    /* proceeds to cart/checkout automatically */
    prq.checkout();

    /* set specific discount code \*/
    prq.setDiscountCode('10-OFF');

    /* get the response permalink url */
    prq.getResponsePermalink();

    /* retake quiz */
    prq.retakeQuiz();

    /* close quiz */
    prq.closeQuiz();

    /* open quiz popup */
    window.openQuizPopup('dbqHqN');
    dbqHqN is the quiz ID
    ```

    For other functions and properties refer to the [console.log(prq)](#consolelogprq-function).

=== "Standalone"

    To begin, let's log the quiz response object to the console:

    ```javascript
    console.log(prq);
    console.log(prq.quizSlides()); // See all slides and their IDs
    ```

    This line of code will display the available Vue.js functions and properties within the prq scope in your browser's console, allowing you to inspect the quiz data in real-time.

    ![how to add javascript consolelog](/images/how_to_add_javascript_consolelog.png)

    **Custom JavaScript Capabilities**

    The `prq` object is your gateway to customizing the quiz experience. Here's how you can use it:

    **Quiz Data Manipulation**

    - **Accessing Quiz Slides and Responses**: Use `prq.quizSlides()` to retrieve all quiz slides/questions, including user responses.
    - **Fetching Specific Slide Values**: Obtain the value of a particular slide by using `prq.getSlideValue(slideId)`.

    **Participant Information Retrieval**

    - **Lead Details**: Easily fetch the quiz participant's email, phone number, and name using `prq.leadEmail()`, `prq.leadPhone()`, and `prq.leadName()`, respectively.

    **Results Page Customization**

    - **Manipulating Results Page Content**: Access and modify the contents of the results page, including blocks and products, using `prq.resultsPage()`.
    - **Product Recommendations**: Leverage `prq.recommendedProducts()` and `prq.mostVotedProduct()` to customize product suggestions.
    - **Automatic Actions**: Automatically add products to the cart or proceed to checkout using `prq.addAllToCart()` and `prq.checkout()`.
    - **Discount Codes**: Apply specific discount codes with `prq.setDiscountCode('10-OFF')`.

    **Navigation and Engagement**

    - **Quiz Navigation**: Offer options to retake the quiz, close it, or open it in a popup through `prq.retakeQuiz()`, `prq.closeQuiz()`, and `window.openQuizPopup('quizID')`.

    ```html
    /* List of all the quiz slides/questions (including the responded values) */
    prq.quizSlides();

    /* get the slide/question value by passing the slide ID  */
    prq.getSlideValue(slideId);

    /* get the lead's email  */
    prq.leadEmail();

    /* get the lead's phone  */
    prq.leadPhone();

    /* get the lead's name  */
    prq.leadName();

    /* List contents of the results page, blocks, products, etc. */
    prq.resultsPage();

    /* List recommended products, sorted by number of votes */
    prq.recommendedProducts();

    /* Show most voted product */
    prq.mostVotedProduct();

    /* adds all the products to cart automatically */
    prq.addAllToCart();

    /* proceeds to cart/checkout automatically */
    prq.checkout();

    /* set specific discount code \*/
    prq.setDiscountCode('10-OFF');

    /* get the response permalink url */
    prq.getResponsePermalink();

    /* retake quiz */
    prq.retakeQuiz();

    /* close quiz */
    prq.closeQuiz();

    /* open quiz popup */
    window.openQuizPopup('dbqHqN');
    dbqHqN is the quiz ID
    ```

    For other functions and properties refer to the [console.log(prq)](#consolelogprq-function).


## Customization Examples

### Example 1: Trigger functions from an element in the results page

=== "Shopify"

    In the `💎Built for Shopify` version of the RevenueHunt app, you can add interactive elements to your quiz results page:

    1. Create an element in the result page and add the `onclick` functionality later via the Custom Javascript.

    
        !!! example "Add the `onclick` functionality via the Custom Javascript."

            ```html
            <!-- In Result page in a HTML block -->
            <!-- add a HTML element such as -->
            <a id="special_retake_quiz">Click here to retake the quiz</a>
            ```

            ```javascript
            /* In the Custom Javascript section */
            // get the element
            var element = document.getElementById("special_retake_quiz");

            // add the onclick function to the element
            element.onclick = function() {
                // You'll need to implement retake functionality using V2 objects
                // For example, you could redirect to the quiz URL
                window.location.href = window.location.href.split('#')[0] + '#quiz';
            }
            ```

    2. Or you can create the element in the Custom Javascript section and inject it into the results page.

        !!! example "Create the element with an `onclick` event first and then inject it in the results page."

            ```javascript
            /* In the Custom Javascript section */
            // create the element
            const element = document.createElement("a");
            element.innerHTML = "Click here to retake the quiz";
            element.style.cursor = "pointer";

            // add the onclick function
            element.onclick = function() {
              window.location.href = window.location.href.split('#')[0] + '#quiz';
            };

            // find a place to append the element
            const container = window.quiz.querySelector('.result-section');
            if (container) container.appendChild(element);
            ```


=== "Shopify (Legacy)"

    You can do it two ways: 

    1. Create an element in the result page and add the `onclick` functionality later via the Custom Javascript.

        !!! example "Add the `onclick` functionality via the Custom Javascript."

            ```html
            <!-- In Result page in a HTML block -->
            <!-- add a HTML element such as -->
            <a id="special_retake_quiz">Click here to retake the quiz</a>
            ```

            ```javascript
            /* In the Custom Javascript section */
            // get the element
            var element = document.getElementById("special_retake_quiz");

            // add the onclick function to the element
            element.onclick = function() {
                prq.retakeQuiz();
            }
            ```

    2. Or you can create the element in the Custom Javascript section with an `onclick` event first and then inject it in the results page.

        !!! example "Create the element with an `onclick` event first and then inject it in the results page."

            ```javascript
            /* In the Custom Javascript section */
            // create the element
            var element = document.createElement("a");
            element.innerHTML = "Click here to retake the quiz"

            // add the onclick function to the element
            element.onclick = function() {
                prq.retakeQuiz();
            }

            // get element that we are going to append in the result
            // in this case at the end of the first block
            var destination_element = document.querySelectorAll(".lq-block")[0];
            destination_element.appendChild(element);
            ```

=== "WooCommerce"

    You can do it two ways: 

    1. Create an element in the result page and add the `onclick` functionality later via the Custom Javascript.

        !!! example "Add the `onclick` functionality via the Custom Javascript."

            ```html
            <!-- In Result page in a HTML block -->
            <!-- add a HTML element such as -->
            <a id="special_retake_quiz">Click here to retake the quiz</a>
            ```

            ```html
            /* In the Custom Javascript section */
            // get the element
            var element = document.getElementById("special_retake_quiz");

            // add the onclick function to the element
            element.onclick = function() {
                prq.retakeQuiz();
            }
            ```

    2. Or you can create the element in the Custom Javascript section with an `onclick` event first and then inject it in the results page.

        !!! example "Create the element with an `onclick` event first and then inject it in the results page."

            ```html
            /* In the Custom Javascript section */
            // create the element
            var element = document.createElement("a");
            element.innerHTML = "Click here to retake the quiz"

            // add the onclick function to the element
            element.onclick = function() {
                prq.retakeQuiz();
            }

            // get element that we are going to append in the result
            // in this case at the end of the first block
            var destination_element = document.querySelectorAll(".lq-block")[0];
            destination_element.appendChild(element);
            ```

=== "Magento"
    You can do it two ways: 

    1. Create an element in the result page and add the `onclick` functionality later via the Custom Javascript.

        !!! example "Add the `onclick` functionality via the Custom Javascript."

            ```html
            <!-- In Result page in a HTML block -->
            <!-- add a HTML element such as -->
            <a id="special_retake_quiz">Click here to retake the quiz</a>
            ```

            ```html
            /* In the Custom Javascript section */
            // get the element
            var element = document.getElementById("special_retake_quiz");

            // add the onclick function to the element
            element.onclick = function() {
                prq.retakeQuiz();
            }
            ```

    2. Or you can create the element in the Custom Javascript section with an `onclick` event first and then inject it in the results page.

        !!! example "Create the element with an `onclick` event first and then inject it in the results page."

            ```html
            /* In the Custom Javascript section */
            // create the element
            var element = document.createElement("a");
            element.innerHTML = "Click here to retake the quiz"

            // add the onclick function to the element
            element.onclick = function() {
                prq.retakeQuiz();
            }

            // get element that we are going to append in the result
            // in this case at the end of the first block
            var destination_element = document.querySelectorAll(".lq-block")[0];
            destination_element.appendChild(element);
            ```

=== "BigCommerce"

    You can do it two ways: 

    1. Create an element in the result page and add the `onclick` functionality later via the Custom Javascript.

        !!! example "Add the `onclick` functionality via the Custom Javascript."

            ```html
            <!-- In Result page in a HTML block -->
            <!-- add a HTML element such as -->
            <a id="special_retake_quiz">Click here to retake the quiz</a>
            ```

            ```html
            /* In the Custom Javascript section */
            // get the element
            var element = document.getElementById("special_retake_quiz");

            // add the onclick function to the element
            element.onclick = function() {
                prq.retakeQuiz();
            }
            ```

    2. Or you can create the element in the Custom Javascript section with an `onclick` event first and then inject it in the results page.

        !!! example "Create the element with an `onclick` event first and then inject it in the results page."

            ```html
            /* In the Custom Javascript section */
            // create the element
            var element = document.createElement("a");
            element.innerHTML = "Click here to retake the quiz"

            // add the onclick function to the element
            element.onclick = function() {
                prq.retakeQuiz();
            }

            // get element that we are going to append in the result
            // in this case at the end of the first block
            var destination_element = document.querySelectorAll(".lq-block")[0];
            destination_element.appendChild(element);
            ```

=== "Standalone"
    You can do it two ways: 

    1. Create an element in the result page and add the `onclick` functionality later via the Custom Javascript.

        !!! example "Add the `onclick` functionality via the Custom Javascript."

            ```html
            <!-- In Result page in a HTML block -->
            <!-- add a HTML element such as -->
            <a id="special_retake_quiz">Click here to retake the quiz</a>
            ```

            ```html
            /* In the Custom Javascript section */
            // get the element
            var element = document.getElementById("special_retake_quiz");

            // add the onclick function to the element
            element.onclick = function() {
                prq.retakeQuiz();
            }
            ```

    2. Or you can create the element in the Custom Javascript section with an `onclick` event first and then inject it in the results page.

        !!! example "Create the element with an `onclick` event first and then inject it in the results page."

            ```html
            /* In the Custom Javascript section */
            // create the element
            var element = document.createElement("a");
            element.innerHTML = "Click here to retake the quiz"

            // add the onclick function to the element
            element.onclick = function() {
                prq.retakeQuiz();
            }

            // get element that we are going to append in the result
            // in this case at the end of the first block
            var destination_element = document.querySelectorAll(".lq-block")[0];
            destination_element.appendChild(element);
            ```

### Example 2: Insert calculations

=== "Shopify"

    In the `💎Built for Shopify` version of the RevenueHunt app, you can access the answers from the `answers` object to perform calculations. Here's how to create a BMI calculator:

    !!! example "Create a BMI calculator"

        Step 1: Add a placeholder element in the Results page (HTML block)

        ```html
        <div id="body_mass_index_calculation"></div>
        ```

        Step 2: Add custom JavaScript

        ```javascript
        /* In the Custom Javascript section */

        // Get the target element inside the quiz
        const element = window.quiz.getElementById("body_mass_index_calculation");

        // Use quiz.answers to find responses for weight and height
        // Replace these IDs with your actual block references from your quiz
        const weightAnswer = quiz.answers.byBlock['weight-question-id']?.value;
        const heightAnswer = quiz.answers.byBlock['height-question-id']?.value;

        if (element && weightAnswer && heightAnswer) {
          const weight = parseFloat(weightAnswer);
          const height = parseFloat(heightAnswer);

          if (!isNaN(weight) && !isNaN(height) && height > 0) {
            // Calculate BMI: weight (kg) / height^2 (m)
            const bmi = weight / (height * height);
            element.innerHTML = `Your BMI is: <b>${bmi.toFixed(2)}</b>`;
          } else {
            element.innerHTML = "Invalid data for BMI calculation.";
          }
        } else if (element) {
          element.innerHTML = "Required data not found.";
        }
        ```

        Step 3: Debugging (find your actual block references)

        ```javascript
        console.log("All Answers:", quiz.answers);
        console.log("Answers by block:", quiz.answers.byBlock);
        ```

        When you run the quiz, check the Console in DevTools to see the structure of `Quiz.answers` and copy the correct IDs to use in the code above.


=== "Shopify (Legacy)"

    You can display the information you have gathered throughout the quiz and mash it up however you want. For example, you could create a BMI (body mass index) calculator the following way.

    !!! example "Create a BMI calculator"

        ```html
        <!-- In Result page in a HTML block -->
        <!-- add an HTML element such as -->
        <div id="body_mass_index_calculation"></div>
        ```

        ```javascript
        /* In the Custom Javascript section */
        // get the element
        var element = document.getElementById("body_mass_index_calculation");

        // get the values of the slides
        var weight = prq.getSlideValue("rgiq0oE");
        var height = prq.getSlideValue("0Mi2qLN");

        // instead of using prq.getSlideValue you could do the same with this code:
        /*
        var slide_weight = prq.quiz.attributes.slides.data.find(s => s.id === "rgiq0oE");
        var slide_height = prq.quiz.attributes.slides.data.find(s => s.id === "0Mi2qLN");

        var weight = slide_weight.attributes.values[0];
        var height = slide_height.attributes.values[0];
        */

        // calculate the Body Mass Index
        var bmi = weight / (height * height);

        // insert the calculation on the element in the result page
        element.innerHTML = bmi.toFixed(2); 
        ```

    You can also load jQuery [this way](https://stackoverflow.com/questions/10113366/load-jquery-with-javascript-and-use-jquery).

=== "WooCommerce"
    You can display the information you have gathered throughout the quiz and mash it up however you want. For example, you could create a BMI (body mass index) calculator the following way.

    !!! example "Create a BMI calculator"

        ```html
        <!-- In Result page in a HTML block -->
        <!-- add an HTML element such as -->
        <div id="body_mass_index_calculation"></div>
        ```

        ```javascript
        /* In the Custom Javascript section */
        // get the element
        var element = document.getElementById("body_mass_index_calculation");

        // get the values of the slides
        var weight = prq.getSlideValue("rgiq0oE");
        var height = prq.getSlideValue("0Mi2qLN");

        // instead of using prq.getSlideValue you could do the same with this code:
        /*
        var slide_weight = prq.quiz.attributes.slides.data.find(s => s.id === "rgiq0oE");
        var slide_height = prq.quiz.attributes.slides.data.find(s => s.id === "0Mi2qLN");

        var weight = slide_weight.attributes.values[0];
        var height = slide_height.attributes.values[0];
        */

        // calculate the Body Mass Index
        var bmi = weight / (height * height);

        // insert the calculation on the element in the result page
        element.innerHTML = bmi.toFixed(2); 
        ```

    You can also load jQuery [this way](https://stackoverflow.com/questions/10113366/load-jquery-with-javascript-and-use-jquery).

=== "Magento"

    You can display the information you have gathered throughout the quiz and mash it up however you want. For example, you could create a BMI (body mass index) calculator the following way.

    !!! example "Create a BMI calculator"

        ```html
        <!-- In Result page in a HTML block -->
        <!-- add an HTML element such as -->
        <div id="body_mass_index_calculation"></div>
        ```

        ```javascript
        /* In the Custom Javascript section */
        // get the element
        var element = document.getElementById("body_mass_index_calculation");

        // get the values of the slides
        var weight = prq.getSlideValue("rgiq0oE");
        var height = prq.getSlideValue("0Mi2qLN");

        // instead of using prq.getSlideValue you could do the same with this code:
        /*
        var slide_weight = prq.quiz.attributes.slides.data.find(s => s.id === "rgiq0oE");
        var slide_height = prq.quiz.attributes.slides.data.find(s => s.id === "0Mi2qLN");

        var weight = slide_weight.attributes.values[0];
        var height = slide_height.attributes.values[0];
        */

        // calculate the Body Mass Index
        var bmi = weight / (height * height);

        // insert the calculation on the element in the result page
        element.innerHTML = bmi.toFixed(2); 
        ```

    You can also load jQuery [this way](https://stackoverflow.com/questions/10113366/load-jquery-with-javascript-and-use-jquery).

=== "BigCommerce"

    You can display the information you have gathered throughout the quiz and mash it up however you want. For example, you could create a BMI (body mass index) calculator the following way.

    !!! example "Create a BMI calculator"

        ```html
        <!-- In Result page in a HTML block -->
        <!-- add an HTML element such as -->
        <div id="body_mass_index_calculation"></div>
        ```

        ```javascript
        /* In the Custom Javascript section */
        // get the element
        var element = document.getElementById("body_mass_index_calculation");

        // get the values of the slides
        var weight = prq.getSlideValue("rgiq0oE");
        var height = prq.getSlideValue("0Mi2qLN");

        // instead of using prq.getSlideValue you could do the same with this code:
        /*
        var slide_weight = prq.quiz.attributes.slides.data.find(s => s.id === "rgiq0oE");
        var slide_height = prq.quiz.attributes.slides.data.find(s => s.id === "0Mi2qLN");

        var weight = slide_weight.attributes.values[0];
        var height = slide_height.attributes.values[0];
        */

        // calculate the Body Mass Index
        var bmi = weight / (height * height);

        // insert the calculation on the element in the result page
        element.innerHTML = bmi.toFixed(2); 
        ```

    You can also load jQuery [this way](https://stackoverflow.com/questions/10113366/load-jquery-with-javascript-and-use-jquery).

=== "Standalone"


    You can display the information you have gathered throughout the quiz and mash it up however you want. For example, you could create a BMI (body mass index) calculator the following way.

    !!! example "Create a BMI calculator"

        ```html
        <!-- In Result page in a HTML block -->
        <!-- add an HTML element such as -->
        <div id="body_mass_index_calculation"></div>
        ```

        ```javascript
        /* In the Custom Javascript section */
        // get the element
        var element = document.getElementById("body_mass_index_calculation");

        // get the values of the slides
        var weight = prq.getSlideValue("rgiq0oE");
        var height = prq.getSlideValue("0Mi2qLN");

        // instead of using prq.getSlideValue you could do the same with this code:
        /*
        var slide_weight = prq.quiz.attributes.slides.data.find(s => s.id === "rgiq0oE");
        var slide_height = prq.quiz.attributes.slides.data.find(s => s.id === "0Mi2qLN");

        var weight = slide_weight.attributes.values[0];
        var height = slide_height.attributes.values[0];
        */

        // calculate the Body Mass Index
        var bmi = weight / (height * height);

        // insert the calculation on the element in the result page
        element.innerHTML = bmi.toFixed(2); 
        ```

    You can also load jQuery [this way](https://stackoverflow.com/questions/10113366/load-jquery-with-javascript-and-use-jquery).


### Example 3: Multiple-choice questions: select all, select none

=== "Shopify"

    You can make question choice become select all / selectnone via the [Multiple-Choice settings](/reference/quiz-builder/questions/#multiple-choice). 


=== "Shopify (Legacy)"

    It is possible to make the quiz multiple choice questions select all preceding answers and none of the answers with custom JavaScript code. You will be able to use it as long as there is only one choice that contains the word "All" and one that contains the word "None".  It doesn't matter the order or the question number.

    ??? example "Select all, select none"

        This code may require adjustments by a developer.  Use it as an example only.

        ```javascript
        // Initializes an object to hold the current slide's state, ensuring it doesn't overwrite if already exists.
        var prq = prq || {
          currentSlide: {
            values: [], // An array to store the values (identifiers) of selected choices.
          },
        };

        // Selects all elements with class `.lq-choice` as the choices available on the current slide/view.
        const choices = document.querySelectorAll(".lq-choice");

        // Retrieves the currently selected choice values from the global state.
        var values = prq.currentSlide.values;

        // Iterates over each choice and attaches a click event listener to handle selection/deselection.
        choices.forEach((selector) => {
          selector.addEventListener("click", function () {
            refresh(this.id); // Calls the refresh function on click, passing the clicked choice's ID.
          });
        });

        // Defines the logic to update choice selections based on user interaction.
        function refresh(id) {
          var choice = document.getElementById(id); // Retrieves the DOM element for the clicked choice.
          
          // Logic to deselect a choice if it's already selected.
          if (valuesIncludes(values, choice)) {
            values = removeChoice(values, choice);
          } 
          // Logic to select all choices except "none" when "all" is clicked.
          else if (isAll(choice)) {
            const cs = [...choices].filter((c) => !isNone(c));
            values = cs.map((c) => choiceId(c));
          } 
          // Logic to handle "none" selection, deselecting all other choices or selecting none only.
          else if (isNone(choice)) {
            if (valuesIncludes(values, choice)) {
              values = [];
            } else {
              const cs = [...choices].filter((c) => !isNone(c));
              values = [choiceId(choice)];
            }
          } 
          // General logic for ticking a choice and unticking "none".
          else {
            addChoice(values, choice);
            values = removeChoice(values, choiceNone(choices));
          }

          // Updates the UI to reflect the current selection state.
          choices.forEach((c) =>
            values.includes(choiceId(c))
              ? c.classList.add("lq-selected")
              : c.classList.remove("lq-selected")
          );
        }

        // Helper function to add a choice's ID to the selection.
        function addChoice(values, choice) {
          values.push(choiceId(choice));
        }

        // Helper function to remove a choice's ID from the selection.
        function removeChoice(values, choice) {
          return values.filter((v) => v !== choiceId(choice));
        }

        // Returns the "none" choice element.
        function choiceNone(choices) {
          return [...choices].find((c) => isNone(c));
        }

        // Unused in the given code but presumably intended to return the "all" choice element.
        function choiceAll(choices) {
          return [...choices].find((c) => isAll(c));
        }

        // Extracts and returns the ID part of a choice's DOM ID.
        function choiceId(choice) {
          return choice.id.split("-")[1];
        }

        // Determines if a choice is meant to select all options.
        function isAll(c) {
          return c.innerHTML.toLowerCase().includes("all");
        }

        // Determines if a choice represents a "none" selection.
        function isNone(c) {
          return c.innerHTML.toLowerCase().includes("none");
        }

        // Checks if the current selection includes a specific choice's ID.
        function valuesIncludes(values, c) {
          return values.includes(choiceId(c));
        }
        ```

=== "WooCommerce"

    It is possible to make the quiz multiple choice questions select all preceding answers and none of the answers with custom JavaScript code. You will be able to use it as long as there is only one choice that contains the word "All" and one that contains the word "None".  It doesn't matter the order or the question number.

    ??? example "Select all, select none"

        This code may require adjustments by a developer.  Use it as an example only.

        ```javascript
        // Initializes an object to hold the current slide's state, ensuring it doesn't overwrite if already exists.
        var prq = prq || {
          currentSlide: {
            values: [], // An array to store the values (identifiers) of selected choices.
          },
        };

        // Selects all elements with class `.lq-choice` as the choices available on the current slide/view.
        const choices = document.querySelectorAll(".lq-choice");

        // Retrieves the currently selected choice values from the global state.
        var values = prq.currentSlide.values;

        // Iterates over each choice and attaches a click event listener to handle selection/deselection.
        choices.forEach((selector) => {
          selector.addEventListener("click", function () {
            refresh(this.id); // Calls the refresh function on click, passing the clicked choice's ID.
          });
        });

        // Defines the logic to update choice selections based on user interaction.
        function refresh(id) {
          var choice = document.getElementById(id); // Retrieves the DOM element for the clicked choice.
          
          // Logic to deselect a choice if it's already selected.
          if (valuesIncludes(values, choice)) {
            values = removeChoice(values, choice);
          } 
          // Logic to select all choices except "none" when "all" is clicked.
          else if (isAll(choice)) {
            const cs = [...choices].filter((c) => !isNone(c));
            values = cs.map((c) => choiceId(c));
          } 
          // Logic to handle "none" selection, deselecting all other choices or selecting none only.
          else if (isNone(choice)) {
            if (valuesIncludes(values, choice)) {
              values = [];
            } else {
              const cs = [...choices].filter((c) => !isNone(c));
              values = [choiceId(choice)];
            }
          } 
          // General logic for ticking a choice and unticking "none".
          else {
            addChoice(values, choice);
            values = removeChoice(values, choiceNone(choices));
          }

          // Updates the UI to reflect the current selection state.
          choices.forEach((c) =>
            values.includes(choiceId(c))
              ? c.classList.add("lq-selected")
              : c.classList.remove("lq-selected")
          );
        }

        // Helper function to add a choice's ID to the selection.
        function addChoice(values, choice) {
          values.push(choiceId(choice));
        }

        // Helper function to remove a choice's ID from the selection.
        function removeChoice(values, choice) {
          return values.filter((v) => v !== choiceId(choice));
        }

        // Returns the "none" choice element.
        function choiceNone(choices) {
          return [...choices].find((c) => isNone(c));
        }

        // Unused in the given code but presumably intended to return the "all" choice element.
        function choiceAll(choices) {
          return [...choices].find((c) => isAll(c));
        }

        // Extracts and returns the ID part of a choice's DOM ID.
        function choiceId(choice) {
          return choice.id.split("-")[1];
        }

        // Determines if a choice is meant to select all options.
        function isAll(c) {
          return c.innerHTML.toLowerCase().includes("all");
        }

        // Determines if a choice represents a "none" selection.
        function isNone(c) {
          return c.innerHTML.toLowerCase().includes("none");
        }

        // Checks if the current selection includes a specific choice's ID.
        function valuesIncludes(values, c) {
          return values.includes(choiceId(c));
        }
        ```

=== "Magento"

    It is possible to make the quiz multiple choice questions select all preceding answers and none of the answers with custom JavaScript code. You will be able to use it as long as there is only one choice that contains the word "All" and one that contains the word "None".  It doesn't matter the order or the question number.

    ??? example "Select all, select none"

        This code may require adjustments by a developer.  Use it as an example only.

        ```javascript
        // Initializes an object to hold the current slide's state, ensuring it doesn't overwrite if already exists.
        var prq = prq || {
          currentSlide: {
            values: [], // An array to store the values (identifiers) of selected choices.
          },
        };

        // Selects all elements with class `.lq-choice` as the choices available on the current slide/view.
        const choices = document.querySelectorAll(".lq-choice");

        // Retrieves the currently selected choice values from the global state.
        var values = prq.currentSlide.values;

        // Iterates over each choice and attaches a click event listener to handle selection/deselection.
        choices.forEach((selector) => {
          selector.addEventListener("click", function () {
            refresh(this.id); // Calls the refresh function on click, passing the clicked choice's ID.
          });
        });

        // Defines the logic to update choice selections based on user interaction.
        function refresh(id) {
          var choice = document.getElementById(id); // Retrieves the DOM element for the clicked choice.
          
          // Logic to deselect a choice if it's already selected.
          if (valuesIncludes(values, choice)) {
            values = removeChoice(values, choice);
          } 
          // Logic to select all choices except "none" when "all" is clicked.
          else if (isAll(choice)) {
            const cs = [...choices].filter((c) => !isNone(c));
            values = cs.map((c) => choiceId(c));
          } 
          // Logic to handle "none" selection, deselecting all other choices or selecting none only.
          else if (isNone(choice)) {
            if (valuesIncludes(values, choice)) {
              values = [];
            } else {
              const cs = [...choices].filter((c) => !isNone(c));
              values = [choiceId(choice)];
            }
          } 
          // General logic for ticking a choice and unticking "none".
          else {
            addChoice(values, choice);
            values = removeChoice(values, choiceNone(choices));
          }

          // Updates the UI to reflect the current selection state.
          choices.forEach((c) =>
            values.includes(choiceId(c))
              ? c.classList.add("lq-selected")
              : c.classList.remove("lq-selected")
          );
        }

        // Helper function to add a choice's ID to the selection.
        function addChoice(values, choice) {
          values.push(choiceId(choice));
        }

        // Helper function to remove a choice's ID from the selection.
        function removeChoice(values, choice) {
          return values.filter((v) => v !== choiceId(choice));
        }

        // Returns the "none" choice element.
        function choiceNone(choices) {
          return [...choices].find((c) => isNone(c));
        }

        // Unused in the given code but presumably intended to return the "all" choice element.
        function choiceAll(choices) {
          return [...choices].find((c) => isAll(c));
        }

        // Extracts and returns the ID part of a choice's DOM ID.
        function choiceId(choice) {
          return choice.id.split("-")[1];
        }

        // Determines if a choice is meant to select all options.
        function isAll(c) {
          return c.innerHTML.toLowerCase().includes("all");
        }

        // Determines if a choice represents a "none" selection.
        function isNone(c) {
          return c.innerHTML.toLowerCase().includes("none");
        }

        // Checks if the current selection includes a specific choice's ID.
        function valuesIncludes(values, c) {
          return values.includes(choiceId(c));
        }
        ```

=== "BigCommerce"

    It is possible to make the quiz multiple choice questions select all preceding answers and none of the answers with custom JavaScript code. You will be able to use it as long as there is only one choice that contains the word "All" and one that contains the word "None".  It doesn't matter the order or the question number.

    ??? example "Select all, select none"

        This code may require adjustments by a developer.  Use it as an example only.

        ```javascript
        // Initializes an object to hold the current slide's state, ensuring it doesn't overwrite if already exists.
        var prq = prq || {
          currentSlide: {
            values: [], // An array to store the values (identifiers) of selected choices.
          },
        };

        // Selects all elements with class `.lq-choice` as the choices available on the current slide/view.
        const choices = document.querySelectorAll(".lq-choice");

        // Retrieves the currently selected choice values from the global state.
        var values = prq.currentSlide.values;

        // Iterates over each choice and attaches a click event listener to handle selection/deselection.
        choices.forEach((selector) => {
          selector.addEventListener("click", function () {
            refresh(this.id); // Calls the refresh function on click, passing the clicked choice's ID.
          });
        });

        // Defines the logic to update choice selections based on user interaction.
        function refresh(id) {
          var choice = document.getElementById(id); // Retrieves the DOM element for the clicked choice.
          
          // Logic to deselect a choice if it's already selected.
          if (valuesIncludes(values, choice)) {
            values = removeChoice(values, choice);
          } 
          // Logic to select all choices except "none" when "all" is clicked.
          else if (isAll(choice)) {
            const cs = [...choices].filter((c) => !isNone(c));
            values = cs.map((c) => choiceId(c));
          } 
          // Logic to handle "none" selection, deselecting all other choices or selecting none only.
          else if (isNone(choice)) {
            if (valuesIncludes(values, choice)) {
              values = [];
            } else {
              const cs = [...choices].filter((c) => !isNone(c));
              values = [choiceId(choice)];
            }
          } 
          // General logic for ticking a choice and unticking "none".
          else {
            addChoice(values, choice);
            values = removeChoice(values, choiceNone(choices));
          }

          // Updates the UI to reflect the current selection state.
          choices.forEach((c) =>
            values.includes(choiceId(c))
              ? c.classList.add("lq-selected")
              : c.classList.remove("lq-selected")
          );
        }

        // Helper function to add a choice's ID to the selection.
        function addChoice(values, choice) {
          values.push(choiceId(choice));
        }

        // Helper function to remove a choice's ID from the selection.
        function removeChoice(values, choice) {
          return values.filter((v) => v !== choiceId(choice));
        }

        // Returns the "none" choice element.
        function choiceNone(choices) {
          return [...choices].find((c) => isNone(c));
        }

        // Unused in the given code but presumably intended to return the "all" choice element.
        function choiceAll(choices) {
          return [...choices].find((c) => isAll(c));
        }

        // Extracts and returns the ID part of a choice's DOM ID.
        function choiceId(choice) {
          return choice.id.split("-")[1];
        }

        // Determines if a choice is meant to select all options.
        function isAll(c) {
          return c.innerHTML.toLowerCase().includes("all");
        }

        // Determines if a choice represents a "none" selection.
        function isNone(c) {
          return c.innerHTML.toLowerCase().includes("none");
        }

        // Checks if the current selection includes a specific choice's ID.
        function valuesIncludes(values, c) {
          return values.includes(choiceId(c));
        }
        ```

=== "Standalone"

    It is possible to make the quiz multiple choice questions select all preceding answers and none of the answers with custom JavaScript code. You will be able to use it as long as there is only one choice that contains the word "All" and one that contains the word "None".  It doesn't matter the order or the question number.

    ??? example "Select all, select none"

        This code may require adjustments by a developer.  Use it as an example only.

        ```javascript
        // Initializes an object to hold the current slide's state, ensuring it doesn't overwrite if already exists.
        var prq = prq || {
          currentSlide: {
            values: [], // An array to store the values (identifiers) of selected choices.
          },
        };

        // Selects all elements with class `.lq-choice` as the choices available on the current slide/view.
        const choices = document.querySelectorAll(".lq-choice");

        // Retrieves the currently selected choice values from the global state.
        var values = prq.currentSlide.values;

        // Iterates over each choice and attaches a click event listener to handle selection/deselection.
        choices.forEach((selector) => {
          selector.addEventListener("click", function () {
            refresh(this.id); // Calls the refresh function on click, passing the clicked choice's ID.
          });
        });

        // Defines the logic to update choice selections based on user interaction.
        function refresh(id) {
          var choice = document.getElementById(id); // Retrieves the DOM element for the clicked choice.
          
          // Logic to deselect a choice if it's already selected.
          if (valuesIncludes(values, choice)) {
            values = removeChoice(values, choice);
          } 
          // Logic to select all choices except "none" when "all" is clicked.
          else if (isAll(choice)) {
            const cs = [...choices].filter((c) => !isNone(c));
            values = cs.map((c) => choiceId(c));
          } 
          // Logic to handle "none" selection, deselecting all other choices or selecting none only.
          else if (isNone(choice)) {
            if (valuesIncludes(values, choice)) {
              values = [];
            } else {
              const cs = [...choices].filter((c) => !isNone(c));
              values = [choiceId(choice)];
            }
          } 
          // General logic for ticking a choice and unticking "none".
          else {
            addChoice(values, choice);
            values = removeChoice(values, choiceNone(choices));
          }

          // Updates the UI to reflect the current selection state.
          choices.forEach((c) =>
            values.includes(choiceId(c))
              ? c.classList.add("lq-selected")
              : c.classList.remove("lq-selected")
          );
        }

        // Helper function to add a choice's ID to the selection.
        function addChoice(values, choice) {
          values.push(choiceId(choice));
        }

        // Helper function to remove a choice's ID from the selection.
        function removeChoice(values, choice) {
          return values.filter((v) => v !== choiceId(choice));
        }

        // Returns the "none" choice element.
        function choiceNone(choices) {
          return [...choices].find((c) => isNone(c));
        }

        // Unused in the given code but presumably intended to return the "all" choice element.
        function choiceAll(choices) {
          return [...choices].find((c) => isAll(c));
        }

        // Extracts and returns the ID part of a choice's DOM ID.
        function choiceId(choice) {
          return choice.id.split("-")[1];
        }

        // Determines if a choice is meant to select all options.
        function isAll(c) {
          return c.innerHTML.toLowerCase().includes("all");
        }

        // Determines if a choice represents a "none" selection.
        function isNone(c) {
          return c.innerHTML.toLowerCase().includes("none");
        }

        // Checks if the current selection includes a specific choice's ID.
        function valuesIncludes(values, c) {
          return values.includes(choiceId(c));
        }
        ```

### Example 4: Redirect to Translated Product URL

=== "Shopify"

    In this version of the Revenuehunt app you can direct users to different markets via the [App Settings > Shopify Markets tab](/reference/app-settings/#shopify-markets) and the product will be already shown in the right language and currency. 


=== "Shopify (Legacy)"

    Our application syncs only the base products from your store. Products translated into other languages won't have unique IDs for sync. Although you can change the quiz language, product names and descriptions will display in the original language. 

    A workaround for this could be creating quizzes in different languages and redirecting users to the translated product pages with JavaScript. We explain this approach in [this article](/how-to-guides/change-quiz-language/#step-3-redirect-to-translated-product-url).

=== "WooCommerce"

    Our application syncs only the base products from your store. Products translated into other languages won't have unique IDs for sync. Although you can change the quiz language, product names and descriptions will display in the original language. 

    A workaround for this could be creating quizzes in different languages and redirecting users to the translated product pages with JavaScript. We explain this approach in [this article](/how-to-guides/change-quiz-language/#step-3-redirect-to-translated-product-url).

=== "Magento"

    Our application syncs only the base products from your store. Products translated into other languages won't have unique IDs for sync. Although you can change the quiz language, product names and descriptions will display in the original language. 

    A workaround for this could be creating quizzes in different languages and redirecting users to the translated product pages with JavaScript. We explain this approach in [this article](/how-to-guides/change-quiz-language/#step-3-redirect-to-translated-product-url).

=== "BigCommerce"

    Our application syncs only the base products from your store. Products translated into other languages won't have unique IDs for sync. Although you can change the quiz language, product names and descriptions will display in the original language. 

    A workaround for this could be creating quizzes in different languages and redirecting users to the translated product pages with JavaScript. We explain this approach in [this article](/how-to-guides/change-quiz-language/#step-3-redirect-to-translated-product-url).

=== "Standalone"

    Our application syncs only the base products from your store. Products translated into other languages won't have unique IDs for sync. Although you can change the quiz language, product names and descriptions will display in the original language. 

    A workaround for this could be creating quizzes in different languages and redirecting users to the translated product pages with JavaScript. We explain this approach in [this article](/how-to-guides/change-quiz-language/#step-3-redirect-to-translated-product-url).

### Other Examples

=== "Shopify"

    **Questions**

    ??? example "Skip a question automatically if a score is high"

        ```javascript
        if ((quiz.variables.scores.skinSensitivity ?? 0) > 80) {
          actions.next();
        }
        ```

    ??? example "Auto-go back if a user picks a certain answer"

        ```javascript
        if (quiz.answers.byBlock['q1']?.value === 'No') {
          actions.previous();
        }
        ```

    ??? example "Style the next button"

        ```javascript
        const btn = window.quiz.querySelector('.quiz-next-button');
        if (btn) btn.style.backgroundColor = '#ff6600';
        ```

    ??? example "Change question text dynamically"

        ```javascript
        const q = window.quiz.getElementById('question-title');
        if (q) q.textContent = 'Tell us more about your skin type';
        ```

    ??? example "Show a hidden element based on answers"

          ```javascript
          const banner = window.quiz.getElementById('promo-banner');
          if (quiz.answers.byBlock['q2']?.value === 'Dry') {
          banner.style.display = 'block';
          }
          ```


      
    **Results Page**


    ??? example "Automatically add all recommended products to cart"

          ```javascript
          (async () => {
          await actions.addAllToCart();
          })();
          ```


    ??? example "Apply discount code if sensitivity is high"

          ```javascript
          (async () => {
          if ((quiz.variables.scores.skinSensitivity ?? 0) > 70) {
          await actions.applyDiscountCode();
          }
          })();
          ```


    ??? example "Change product title styling"

        ```javascript
        const slot = window.quiz.querySelector('.slot-product__title');
        if (slot) slot.style.fontWeight = 'bold';
        ```

    ??? example "Replace a product image"

        ```javascript
        const img = window.quiz.getElementById('slot-product-1-img');
        if (img) img.src = 'https://example.com/new-image.jpg';
        ```


    ??? example "Highlight recommended products"

        ```javascript
        Object.values(quiz.resultContext.slotItems || {}).forEach(item => {
        console.log('Recommended product:', item.title, item.priceRange?.minVariantPrice?.amount);
        });
        ```

    ??? example "Display a message based on result"

        ```javascript
        if (quiz.currentResult.ref === 'sensitive-skin') {
        const msg = window.quiz.querySelector('.custom-message');
        if (msg) msg.textContent = 'We picked extra-gentle products for you!';
        }
        ```

    **Analytics & Tracking**

    ??? example "Track quiz completion with Google Analytics 4"

        ```javascript
        // Results Page Custom JavaScript
        // Send quiz completion event to GA4
        if (typeof gtag !== 'undefined') {
          gtag('event', 'quiz_completed', {
            'event_category': 'Quiz',
            'event_label': quiz.currentResult.ref,
            'quiz_id': quiz.id,
            'response_id': quiz.metadata.responseId,
            'highest_score': quiz.variables.highest,
            'total_questions': quiz.progress?.totalQuestions || 0
          });
        }
        ```

    ??? example "Track quiz start with Google Analytics 4"

        ```javascript
        // First Question Custom JavaScript
        // Send quiz start event to GA4
        if (typeof gtag !== 'undefined' && quiz.progress?.index === 0) {
          gtag('event', 'quiz_started', {
            'event_category': 'Quiz',
            'quiz_id': quiz.id
          });
        }
        ```

    ??? example "Track specific question with Meta Pixel"

        ```javascript
        // Question Custom JavaScript
        // Track when user reaches a specific question
        if (typeof fbq !== 'undefined') {
          fbq('trackCustom', 'QuizQuestion', {
            question_ref: quiz.currentQuestion?.ref,
            question_index: quiz.progress?.index,
            quiz_id: quiz.id
          });
        }
        ```

    ??? example "Track quiz completion with Meta Pixel"

        ```javascript
        // Results Page Custom JavaScript
        // Send quiz completion event to Meta Pixel
        if (typeof fbq !== 'undefined') {
          fbq('trackCustom', 'QuizCompleted', {
            content_name: quiz.currentResult.ref,
            quiz_id: quiz.id,
            highest_variable: quiz.variables.highest,
            num_recommendations: Object.keys(quiz.resultContext.slotItems || {}).length
          });
        }
        ```


=== "Shopify (Legacy)"

=== "WooCommerce"

=== "Magento"

=== "BigCommerce"

=== "Standalone"

---
This guide outlines the foundational steps and examples for integrating custom JavaScript into your RevneuHunt Product Recommendation Quiz. 