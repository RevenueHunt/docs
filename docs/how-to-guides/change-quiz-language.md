# How to Change the Language of Your Quiz

## Change Quiz Language in Settings

1. **Open Quiz Settings**: To change the quiz language navigate to [Quiz Settings](https://docs.revenuehunt.com/reference/quiz-builder/#quiz-settings) or Quiz Settings -> [Messages](https://docs.revenuehunt.com/reference/quiz-builder/#messages).
2. **Language**: Choose a language from a dropdown list to change the text on the quiz buttons and placeholders into that language.
3. **Add your own translations**: If the desired language is not available or you prefer a different translation you can modify individual instances (such as buttons and placeholders) directly within the [Messages](https://docs.revenuehunt.com/reference/quiz-builder/#messages) tab.
4. **Override the translations**: Should any buttons revert to their original English translations, overriding your selected quiz language you can manually adjust the button text in Quiz Builder -> [Question settings](https://docs.revenuehunt.com/reference/quiz-builder/#question-settings).


## Set Up Multilingual Quizzes

This guide provides instructions for changing the language of quizzes in environments that do not support multi-language plugins. While our application currently lacks native multi-language support, there are effective workarounds to present quizzes in multiple languages.

In short:

- For now, it is possible to create multiple quizzes, each one in a different language. 
- Then, each of these quizzes will have a unique quiz ID. 
- You can embed each of these quizzes on a separate page on your store (eg quiz-en, quiz-de, quiz-fr…) or have your developer create a script that displays the correct quiz popup depending on the browser language.
- However, the main problem is that our app can only sync the base products from your store (in the main language), as products translated automatically to other languages don't have unique product IDs that we could sync. So you can change the quiz language but the product names and descriptions will be shown in the original language. There are some [workarounds](#step-3-handling-product-sync-in-multilingual-stores) mentioned in the article that you can try.

### Step 1: Create Quizzes in Different Languages

- **Manual Translation**: Begin by manually translating your quizzes into the desired languages. Each translated quiz will have a unique ID.
- **Quiz Settings Adjustment**: Navigate to the [Quiz Settings](https://docs.revenuehunt.com/reference/quiz-builder/#quiz-settings) to modify the language of interactive elements like buttons. However, note that questions and choices need manual translation.

### Step 2: Display the Correct Quiz Based on Browser Language

Utilize JavaScript to show the appropriate quiz to users based on their browser's language setting. The script should:

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

Note: make sure that you don’t publish two quizzes on the same page, as this may lead to unwanted behavior.

### Step 3: Redirect to Translated Product URL

Our application syncs only the base products from your store. Products translated into other languages won't have unique IDs for sync. Although you can change the quiz language, product names and descriptions will display in the original language. A workaroudn for this could be creating quizzes in different languages and redirecting users to the translated product pages with JavaScript.

- Instead of adding a product to cart, you can change the [checkout settings](https://docs.revenuehunt.com/how-to-guides/change-checkout-settings/) to `link to product` and point customers to the translated product page.
- By default, the customer will be redirected to the original product URL, but you can force an automatic URL change via JavaScript. 
- For example, you can tell the Results Page to automatically change all the links from this `https://www.example.com/products/productA` to this `https://www.example.com/en/products/productA` This way your customers will be automatically redirected to the translated product page.
- To redirect to an English translation of a product, one can use:
        ```javascript
        let shopURL = "https://www.example.com";

        var links = document.querySelectorAll(".lq-product a");

        for (let i = 0; i < links.length; i++) {
        var href = links[i].href;
        links[i].href = href.replace(shopURL,shopURL+"/en");
        }
        ```

- Make sure to replace the `https://www.example.com` with your store URL and change the `shopURL+"/en"` to the languge code you have set up in your store (for example, `shopURL+"/fr"` for French).


While awaiting native multi-language plugin support, these steps allow for a versatile approach to presenting and managing quizzes in multiple languages, ensuring a tailored experience for your international audience.