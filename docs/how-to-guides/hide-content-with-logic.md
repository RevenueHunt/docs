# How to Show or Hide Content Based on Quiz Answers

In this article, you’ll discover how to use IF-THEN conditional logic to display customized text to quiz takers. This includes adding custom text within your quiz using [Jump Logic](), displaying custom text on the Results page with [Block Logic](), and achieving similar effects with [Skip Logic]().

Using a skincare routine quiz as an example, we show how custom text is displayed based on the customer’s skin type.

## Jump Logic: How to Show Custom Text in the Quiz

![how to hide content with logic jump logic](/images/how to hide content with logic jump logic.png)

1. **Create Quiz**: Open the [Quiz Builder]() and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. *Tip:* Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:
    - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
    - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
    - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
    - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

3. **Add Jump Logic**: If we don’t add jump logic to the quiz, our statement questions will just appear one after the other, regardless of the choice we made. To add jump logic, you should go back to the skin type question and select [conditional logic](). Set up IF-THEN statements with `OR` logic to direct the customer to the correct text based on their skin type. 

    ![how to hide content with logic jump logic statement](/images/how to hide content with logic jump logic statement.png)

4. **Add "Always Jump to..." Logic**: Once all the statements are linked with logic to the skin type question, you should point each statement to the next question in the quiz. This is done by going to the [jump logic]() tab and scrolling towards the `Always jump to...` section. Point each statement to the next question.

4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

## Block Logic: How to Show Custom Text on the Results Page

1. **Create Quiz**: Open the [Quiz Builder]() and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. *Tip:* Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

2. **Add Content Blocks to Results Page**: Go to the Results Page and add a new `content block`. To add a content block click the `+` sign and select `Content Block` from the list. Add multiple content blocks describing the specific skin type and its challenges. For example:
    - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
    - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
    - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
    - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.
    - *Tip*: Make the heading stand out with [markdown language](). Use the`#` sign before a sentence can make it bold.

3. **Add Block Logic**: If we don’t add Block Logic to the quiz, our blocks will just appear one after the other on the Results Page, regardless of the choice we made. To add Block Logic, select a content block and click on `block logic`. Next, click `add block logic`. Set up IF-THEN statements to control when each content block should be visible or hidden based on the customer's choices.

    ![how to hide content with logic block logic statement](/images/how to hide content with logic block logic statement.png)

4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

## Skip Logic: How to Show Custom Text in the Quiz

![how to hide content with logic skip logic](/images/how to hide content with logic skip logic.png)

1. **Create Quiz**: Open the [Quiz Builder]() and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. *Tip:* Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:
    - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
    - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
    - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
    - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.


3. **Add Skip Logic**: If we don’t add skip logic to the quiz, our statement questions will just appear one after the other, regardless of the choice we made. To add skip logic, you should go back to the skin type question and select `conditional logic`. Next, you should navigate to the `Skip Logic` section and add a skip logic rule to each statement. Use skip logic to ensure that only relevant statement questions appear based on the customer's skin type selection.

    ![how to hide content with logic skip logic statement](/images/how to hide content with logic skip logic statement.png)

4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

For more detailed instructions on using Jump Logic, Block Logic, and Skip Logic, consider checking the respective articles linked throughout this guide.
