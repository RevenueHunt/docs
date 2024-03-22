# How to Use Skip Logic

Skip Logic is a feature designed to streamline the experience of quiz or survey participants by tailoring the sequence of questions they encounter. This customization is achieved through conditional statements that govern whether a question is presented or skipped, based on the respondent's answers to preceding questions. Here's a simplified overview on how to implement and use Skip Logic, along with examples of its application.

## Implementing Skip Logic

**Adding Skip Logic to a Question**

You can introduce Skip Logic into your quiz by accessing the [Conditional Logic settings](https://docs.revenuehunt.com/reference/quiz-builder/#conditional-logic) of a question and navigating to the [Skip Logic](https://docs.revenuehunt.com/reference/quiz-builder/#skip-logic) tab. From here, you can create a new Skip Logic statement specifying the conditions under which the current question should be bypassed.

**Creating Skip Logic Statements**

These statements follow a simple format: 

- IF the answer to question X IS EQUAL TO choice Y, THEN skip this question. 

An icon will appear next to questions with Skip Logic applied, indicating the presence of these conditional statements. Multiple Skip Logic rules can be added to any question if needed.

## Examples of Skip Logic

### Filtering Email Collection Based on Interest

**Scenario**

You want to collect emails from interested customers without deterring others.

**Implementation**

- Start with a Yes/No question asking if the customer is willing to leave their email.
- Follow up with an email input question.
- Apply Skip Logic to the email question: if the customer opts out in the previous step, they are directed straight to the results page, bypassing the email question.

### Customizing Content Based on Skin Type

**Scenario**

You want to provide personalized advice based on the customer's skin type.

**Implementation**

- Add a multiple-choice question about skin type (Dry, Normal, Oily, or Combination).
- Create separate statement questions for each skin type, detailing specific advice or information.
- Apply Skip Logic to ensure respondents see only the statement relevant to their skin type, creating a customized experience.

## Skip Logic vs. Jump Logic

The new app interface gives the option to use Jump Logic and Skip Logic. You shouldn’t combine both types of logic in the same quiz.

- **Jump Logic** creates diverging paths within a quiz based on respondent answers, allowing for a branched experience.
- **Skip Logic**, in contrast, customizes the path by omitting certain questions based on previous answers, keeping the overall sequence intact but personalized.

