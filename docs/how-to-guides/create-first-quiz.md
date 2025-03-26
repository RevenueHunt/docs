---
icon: material/pencil
---


# How to Create and Publish Your First Product Recommendation Quiz

Follow these steps to create your first quiz with the RevenueHunt app. You can also follow our [introduction video tutorial](/tutorials/getting-started/).

<div class="videoWrapper">
<iframe src="https://www.youtube.com/embed/UMCpGlbjrUA?si=ftq73J4rFKtW_yGr" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Step 1: Create a New Quiz

1. **Add new quiz**: Go to the app’s [dashboard](/reference/dashboard/) and click [`+ new quiz`](/reference/dashboard/#new-quiz).
2. **Choose a template**: Choose a pre-defined template or start from scratch.
3. **Name your quiz**: The name can be edited later.
4. **Redirect to Quiz Builder**: After that, you'll be redirected to the [Quiz Builder](/reference/quiz-builder/).

## Step 2: Manage Questions

In [Quiz Builder](/reference/quiz-builder/) you'll be able to add questions to your quiz.

1. **Add slides**: To add a question, click the `+` button or hover over an existing question and click the `+ new question` button. Select a [question type](/reference/quiz-builder/questions/#question-types) from the dropdown.
2. **Delete slides**: To delete a question, click the `.../more options` button (three dots) and select **Delete/Remove**.

## Step 3: Link Products and Collections to Choices

Once you have your questions, you'll have to link products to choices to show recommendations to the customer.

1. **Go to Link Products/Collections/Choice Settings tab**: In the Quiz Builder, select a choice and go to [Link Products](/reference/quiz-builder/link-products/)/ [Link Collections](/reference/quiz-builder/link-collections/) / [Choice Settings](/reference/quiz-builder/questions/#choice-settings) tab.
2. **Upvote Products**: Link product variants or collections to each choice. This determines the product recommendations based on customer responses. In the end, the Results Page will display the products sorted by the number of votes.
3. **Edit the Results Page**: Go to the [Results Page](/reference/quiz-builder/results-page/) tab and edit the content. You can change the number of recommended products in the [Product Block settings](/reference/quiz-builder/questions/#block-settings).

??? question "How do I get the right recommendations?"

    Our product recommendation algorithm works like a voting system:

    - Products are linked to each choice
    - When a customer picks a choice, all linked products receive one vote
    - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
    - If no products have been linked or all the products have been excluded, the results page will appear empty
    - If there's a draw in the number of votes, the app will randomize the order of products.

    If you want to make the results ultra-precise, you can also:

    - Limit the recommendations to only show products that received X votes or more in the [Results Page settings](/how-to-guides/only-recommend-products-with-minimum-votes/).
    - Use [Exclusions](/how-to-guides/recommend-products/#understanding-inclusion-and-exclusion) to make sure that unwanted products are not shown (even if they were upvoted in another choice earlier).

Read more about how the recommendations work [here](/how-to-guides/recommend-products/).

## Step 4: Publish & Preview the Quiz

To test the quiz, you'll have to save the changes and preview it.

1. **Publish the changes**: Click [`Publish` / `Save`](/reference/quiz-builder/questions/) on the top-right menu. Don't worry, clicking `Publish / Save` will not automatically add the quiz to your website. It will simply save the changes and allow you to preview the quiz.
2. **Preview the quiz**: Click [`Preview`](/reference/quiz-builder/questions/) to test the quiz you've created. 

    !!! tip    
        You can test the quiz as much as you like as long as you always open a new preview window. These test responses done as admin are automatically removed after 1 hour to not add to your usage quota.

## Step 5: Publish the Quiz on Your website

Once you're satisfied with your quiz, you can put it on your website. 

1. **Publish the quiz**: Follow this guide on [How to Publish the Quiz on Your Website](/how-to-guides/publish-quiz/) to learn about different ways the quiz can be added.

## After Publishing

If changes are made post-publishing, click `Publish / Save` again to update the live quiz.

---
This guide outlines the steps to create and launch a Product Recommendation Quiz for your store.