# How to Add JavaScript to the Quiz

Unlock the full potential of your Shop Quiz by integrating custom JavaScript. This guide will walk you through adding personalized behavior, displaying bespoke product recommendations, navigating to specific pages, and more, using JavaScript. Follow these steps to inject custom code that interacts seamlessly with your quiz's results page and beyond.

Before adding your custom JavaScript, ensure you're familiar with the basics of JavaScript and the Vue.js framework, as our quiz leverages Vue.js for dynamic content rendering. This guide is meant for developers and Shopify partners. Do not attempt JavaScript manipulation unless you are one.

## Accessing the Custom JavaScript Section

### Results Page

1. Navigate to the **Results Page Settings** in your quiz dashboard.
2. Select **Advanced Settings**.
3. Scroll down to find the **Custom JavaScript** section and click `add`.
4. This is your canvas for crafting and deploying custom scripts that can modify the quiz's behavior based on user interactions and results.

## Quiz Questions

1. Navigate to the Quiz Builder.
2. Open question settings.
3. Scroll down to find the **Custom JavaScript** section and click `add`.
4. This is your canvas for crafting and deploying custom scripts that can modify the quiz's behavior based on user interactions and results. Note: JavaScript addded to the first slide in the quiz builder will be applied to all slides.


### Basic Example

To begin, let's log the quiz response object to the console:

```javascript
console.log(prq);
```

This line of code will display the available Vue.js functions and properties within the prq scope in your browser's console, allowing you to inspect the quiz data in real-time.

## Custom JavaScript Capabilities

The `prq` object is your gateway to customizing the quiz experience. Here's how you can use it:

### Quiz Data Manipulation
- **Accessing Quiz Slides and Responses**: Use `prq.quizSlides()` to retrieve all quiz slides/questions, including user responses.
- **Fetching Specific Slide Values**: Obtain the value of a particular slide by using `prq.getSlideValue(slideId)`.

### Participant Information Retrieval
- **Lead Details**: Easily fetch the quiz participant's email, phone number, and name using `prq.leadEmail()`, `prq.leadPhone()`, and `prq.leadName()`, respectively.

### Results Page Customization
- **Manipulating Results Page Content**: Access and modify the contents of the results page, including blocks and products, using `prq.resultsPage()`.
- **Product Recommendations**: Leverage `prq.recommendedProducts()` and `prq.mostVotedProduct()` to customize product suggestions.

### Enhancing User Interaction
- **Automatic Actions**: Automatically add products to the cart or proceed to checkout using `prq.addAllToCart()` and `prq.checkout()`.
- **Discount Codes**: Apply specific discount codes with `prq.setDiscountCode('10-OFF')`.

### Navigation and Engagement
- **Quiz Navigation**: Offer options to retake the quiz, close it, or open it in a popup through `prq.retakeQuiz()`, `prq.closeQuiz()`, and `window.openQuizPopup('quizID')`.

### Advanced Interactions
- **Creating Interactive Elements**: Dynamically create HTML elements that interact with the quiz. For instance, to allow users to retake the quiz from the results page, you can add an element like an anchor tag and associate it with the `prq.retakeQuiz()` function.

```html
<!-- HTML element in the results page -->
<a id="retake_quiz_button">Retake Quiz</a>
```

```javascript
// Custom JavaScript to add onclick functionality
document.getElementById("retake_quiz_button").onclick = function() {
  prq.retakeQuiz();
};
```

### Custom Calculations and More

- **Perform Calculations**: Use the quiz data to perform custom calculations, such as calculating and displaying a body mass index (BMI) based on quiz responses.

```html
<div id="bmi_calculation"></div>
```

```javascript
var weight = prq.getSlideValue("weightSlideId");
var height = prq.getSlideValue("heightSlideId");
var bmi = weight / (height * height);
document.getElementById("bmi_calculation").innerHTML = bmi.toFixed(2);
```

- **Enhancing Choice Selection**: Customize the behavior of multiple-choice questions, enabling "Select All" or "Select None" functionality with custom JavaScript.

### Additional Customizations

Beyond manipulating quiz data and enhancing user interactions, your custom JavaScript can include:

- **Privacy and Marketing Opt-Ins**: Add checkboxes for privacy policies and marketing consent.
- **Custom Redirects**: Redirect users to specific pages based on quiz outcomes or language preferences.
- **Styling Adjustments**: Use custom CSS in conjunction with JavaScript to tailor the look and feel of the quiz and results page.

This guide outlines the foundational steps and examples for integrating custom JavaScript into your Shop Quiz. 