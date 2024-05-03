---
icon: material/language-javascript
---

# How to Add JavaScript to the Quiz

Unlock the full potential of your Shop Quiz: Product Recommendation Quiz by integrating custom JavaScript. We made it very easy for developers to tap into the quiz response and get all the information they need: individual answers to questions, triggered tags and recommended products.

With custom JavaScript, you can:

- add custom behavior, images, texts or logic
- display custom product recommendations
- forward to any particular page on your store
- add tracking codes to specific questions (Google Analytics, Facebook Pixel)

This guide will walk you through adding JavaScript to quiz questions and the results page. 

!!! warning
    This guide is meant for developers and Shopify Partners. If you're not familiar with the basics of JavaScript and the Vue.js framework, it is advised to ask for help from a professional to implement this. You can find/hire a developer [here](https://experts.shopify.com/).


## Access the Custom JavaScript Console

You can add custom JavaScirpt to the quiz results page and the quiz questions.

### Results Page

1. Navigate to the [Results Page Settings](https://docs.revenuehunt.com/reference/quiz-builder/#results-page-settings) in the Quiz Builder.
2. Select [**Advanced Settings**](https://docs.revenuehunt.com/reference/quiz-builder/#advanced-settings).
3. Scroll down to find the **Custom JavaScript** section and click `add`.
4. This is your canvas for crafting and deploying custom scripts that can modify the quiz's behavior based on user interactions and results.
5. Remember to click the `Publish` button to update the preview/live quiz.

### Quiz Questions

1. Navigate to the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/).
2. Open [question settings](https://docs.revenuehunt.com/reference/quiz-builder/#question-settings).
3. Scroll down to find the **Custom JavaScript** section and click `add`.
4. This is your canvas for crafting and deploying custom scripts that can modify the quiz's behavior based on user interactions and results.
5. Remember to click the `Publish` button to update the preview/live quiz.

!!! tip

    JavaScript added to the first Welcome slide in the quiz builder will be applied to all slides.



## Console.log(prq) Function

To begin, let's log the quiz response object to the console:

```javascript
console.log(prq);
```

This line of code will display the available Vue.js functions and properties within the prq scope in your browser's console, allowing you to inspect the quiz data in real-time.

![how to add javascript consolelog](/images/how to add javascript consolelog.png)

## Custom JavaScript Capabilities

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

### Example 1: Trigger the prq functions from an element in the results page

You can do it two ways: 

1. Create an element in the result page and add the `onclick` functionality later via the Custom Javascript.

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

You can display the information you have gathered throughout the quiz and mash it up however you want. For example, you could create a BMI (body mass index) calculator the following way.

```html
<!-- In Result page in a HTML block -->
<!-- add an HTML element such as -->
<div id="body_mass_index_calculation"></div>
```

```html

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

It is possible to make the quiz multiple choice questions select all preceding answers and none of the answers with custom JavaScript code. You will be able to use it as long as there is only one choice that contains the word “All” and one that contains the word “None”.  It doesn’t matter the order or the question number.

!!! note

    This code may require adjustments by a developer.  Use it as an example only.

```html
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

Our application syncs only the base products from your store. Products translated into other languages won't have unique IDs for sync. Although you can change the quiz language, product names and descriptions will display in the original language. 

A workaround for this could be creating quizzes in different languages and redirecting users to the translated product pages with JavaScript. We explain this approach in [this article](https://docs.revenuehunt.com/how-to-guides/change-quiz-language/#step-3-redirect-to-translated-product-url).

---
This guide outlines the foundational steps and examples for integrating custom JavaScript into your Shop Quiz: Product Recommendation Quiz. 