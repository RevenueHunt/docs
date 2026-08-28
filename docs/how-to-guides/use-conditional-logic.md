---
icon: material/diversify
description: "Master conditional logic in RevenueHunt to branch quizzes and customize content based on customer answers."
---

# How to Use Conditional Logic in Product Recommendation Quiz

[Conditional Logic](/reference/quiz-builder/conditional-logic/) is the tab holding **jump logic** and **skip logic**. Display logic is not part of it: you set that on the results page itself.

All three decide what a customer sees, from what they answered.

```
conditional logic
├── jump logic    sends the customer to   a question, a results page, or an external URL
└── skip logic    skips                   a question

display logic     shows or hides          part of the results page
```

## Show or hide content

`IF-THEN` rules put custom text in front of the right customer. Inside the quiz that is Jump Logic or Skip Logic, and on the results page it is Display Logic.

[How to Show or Hide Content Based on Quiz Answers](/how-to-guides/hide-content-with-logic/)

## Jump logic

Jump Logic sends each customer down a different path, from the answer they gave.

!!! info "Use Jump Logic to:"

    - Send the customer to a different follow-up question, from their answer.
    - Branch the quiz.
    - Send the customer to a different results page.
    - Send the customer to an external URL.

[How to Use Jump Logic](/how-to-guides/use-jump-logic/)

## Skip logic

Skip Logic changes which questions come next, so a customer only answers the ones that apply to them.

!!! info "Use Skip Logic to:"

    - Skip questions the customer's earlier answers have made irrelevant.
    - Show different follow-up questions after a multiple-choice question that allows several selections. A customer who picks two skin concerns then answers only the questions for those two.

[How to Use Skip Logic](/how-to-guides/use-skip-logic/)

## Display logic

Display Logic shows or hides individual elements on the results page.

=== "Shopify"

    !!! info "Use Display logic to:"

        - Show or hide content from the customer's answers.
        - Show or hide content from the score of a variable, for a scoring quiz or a personality-type quiz.
        - Show or hide content from the variable with the highest score, for a personality-type quiz.

=== "Shopify (Legacy)"

    !!! info "Use Display Logic to:"

        - Show or hide content on the Results Page, from the customer's answers.

=== "WooCommerce"

    !!! info "Use Display Logic to:"

        - Show or hide content on the Results Page, from the customer's answers.

=== "Magento"

    !!! info "Use Display Logic to:"

        - Show or hide content on the Results Page, from the customer's answers.

=== "BigCommerce"

    !!! info "Use Display Logic to:"

        - Show or hide content on the Results Page, from the customer's answers.

=== "Standalone"

    !!! info "Use Display Logic to:"

        - Show or hide content on the Results Page, from the customer's answers.

[How to Use Display Logic](/how-to-guides/use-display-logic/)

---

This article explains the kinds of conditional logic a quiz can use, and points to the guide for each one.
