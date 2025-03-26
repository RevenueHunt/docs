---
icon: material/numeric-3
---

# Using Conditional Logic in your Product Recommendation Quiz

In this tutorial, you’ll learn how to use [Jump Logic](#jump-logic), [Skip Logic](#skip-logic), and [Block Logic](#block-logic) to show (or hide) questions/content in the quiz as well as the Results Page.

**You’ll learn:**

- how to add statement questions to your quiz
- how to use Jump Logic to show different skin advice in the quiz (statement)
- how to use Jump Logic to redirect the customer to an external URL from the quiz
- how to use Jump Logic to create branching in the quiz to show different questions
- how to use Jump Logic to create branching in the quiz to link different products to the same answers
- how to use Jump Logic to send customers to different Results Pages
- how to use Skip Logic to show different skin advice in the quiz (statement)
- how to use Skip Logic to show or hide a number of follow-up questions
- how to use Skip Logic to show or hide follow-up questions based on questions that allow multiple answers
- how to use Block Logic to show different personalized advice on the Results Page based on customer answers
- how to use Block Logic to show different image results based on customer answers
- how to use Block Logic to show product blocks with different numbers of recommended products
- how to add content blocks to your Results Page
- how to use markdown language

<div class="videoWrapper">
<iframe src="https://www.youtube.com/embed/xtMj6vYux9c?si=BiZzrohxwi78qzNE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Intro 

In this tutorial, you’ll learn how to use simple [conditional logic](/how-to-guides/use-conditional-logic/) to give personalized advice. 

A quiz can act as a professional shopping assistant. It can react to the answers given by the customer and provide valuable feedback. All it takes is a bit of logic. 

In this Skin Care Quiz, there are four blocks of text. Each describes in more detail what a skin type needs in terms of skincare.

With RevenueHunt app, you can show customers with dry skin certain questions (specifically targeted for them), while customers with oily skin would skip these questions. This can be done in many ways within the app.

**Objective**: In this video, we’ll teach you how to show these texts using [Jump Logic](#jump-logic), [Skip Logic](#skip-logic), or [Block Logic](#block-logic) on the results page.

## Jump Logic

Let’s start with Jump Logic.

1. To display text advice in the quiz, you’ll need a `Statement question`.
2. Make it longer by adding a description.
3. One statement will be needed for each type of skin advice.

Now, how can we make only one block appear, instead of all of them, one after the other? We can use [Jump Logic](/how-to-guides/use-jump-logic/).

1. Open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and select a question. 
2. Let’s add the first [Jump logic](/reference/quiz-builder/conditional-logic/#jump-logic) condition:
    - If the answer to `‘How does your skin feel on an average day?’` is `‘Dry and tight all over’` then *Dry skin* advice should appear. 
3. Click on the `+` plus sign to add another statement that can be true. This creates an additional `OR` conditional statement.
    - If the answer to `‘How does your skin feel on an average day?’` is `‘Oily all over’` then *Oily skin* advice should appear. 
4. The `OR` separator between conditions means that only one of these has to be true for the logic to work.
5. Let’s add conditions for the *Combination* and *Normal* skin.
6. To ensure the customer doesn’t see all four statements additional [Jump logic](/reference/quiz-builder/conditional-logic/#jump-logic) should be added to each of them. 
7. Click on a `statement` question.
8. In the `Always jump to…` section, indicate the question or a page that should preceed it.
9. Do the same for the other three statements.
10. Now that all is set, let’s update the preview/live quiz with the top-right `Publish` button and test it with `Preview`.
    - First, select `Dry skin`. 
    - Now let’s go back and select `Oily skin`.

It seems that everything works correctly, well done!

You’ve successfully added Jump Logic to your quiz. Your customers will now be able to see this personalized advice whenever they take the quiz.

[Jump Logic](/how-to-guides/use-jump-logic/) is a powerful tool. It can also be used to:

- redirect the customer to another, external URL directly from the quiz,
- create branching in the quiz to send the customer to different answering paths,
- create branching to link different products to the same choices,
- or send customers to different Result Pages.

## Skip Logic

For linear quizzes, using [Skip Logic](/how-to-guides/use-skip-logic/) instead is recommended.

To achieve the same effect you can set up your statements to be shown one after another.

1. Navigate to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab, select a question and open the [Skip Logic](/reference/quiz-builder/conditional-logic/#skip-logic) menu.
2. Then, add a Skip Logic rule to each statement. For example, when selecting a *Dry skin* statement, the rule states:
    - If the answer question `‘How does your skin feel on an average day?’` **IS NOT**  `Dry and tight all over`, then this question is skipped.
    - This implies that the *Dry skin* statement will **NOT** be skipped only if the answer to that question is `Dry and thigh all over`. In all other cases, the statement will **NOT** be shown.
3. Similar rules shall be applied to the statements about the *Oily*, *Combination*, and *Normal* skin.
4. Once all is set up, make sure to publish the changes with the top-right `Publish` button.
5. Let’s test the quiz with the `Preview` button.

It worked! The correct statement is shown and all the others are skipped based on the skin type the customer selected in the previous question.

[Skip logic](/how-to-guides/use-skip-logic/) can also be used to:

- show or hide a number of follow-up questions,
- show or hide follow-up content based on questions that allow multiple answers.

## Block Logic

Logic can also be applied to the contents of your [Results Page](/reference/quiz-builder/results-page/). 

With [Block logic](/how-to-guides/use-block-logic/), you can show or hide elements of your results page based on the customer's answers.

1. Let’s add four `Content blocks` with the skin type advice to your [Results Page](/reference/quiz-builder/results-page/).
2. You can edit the block text with [Markdown language](/how-to-guides/use-markdown/).
3. Now, how can we make only one block appear, instead of all of them? We can add [Block logic](/reference/quiz-builder/conditional-logic/#block-logic).
4. To do that, activate it in the lower right corner with the `...` button. 
5. Let’s add the first logic condition.
    - If the answer to `‘How does your skin feel on an average day?’` is `‘Dry and tight all over’` then this block (*Dry skin block*) will be **Visible**. 
    - In all other cases, it will be **Hidden**. 
6. Now, let’s add similar rules to other content blocks.
7. Let’s publish the changes with the top-right `Publish` button and test the quiz again with `Preview`.

You’ve now successfully used Block logic to show and hide content on the Results page.

[Block Logic](/how-to-guides/use-block-logic/) is a powerful tool that can also be used to:

- show different image results depending on customer answers
- or show product blocks with different numbers of recommendations. 


Congratulations! You’ve learned how to use simple logic to show personalized advice to your customers.

Check out our [documentation](/) for more resources on getting started with recommendation quizzes.

