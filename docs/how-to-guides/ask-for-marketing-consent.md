---
icon: material/account-check-outline
---

# How to Ask for Marketing/Data Processing Consent

Directly asking for marketing consent or acceptance of data processing in your quiz can be a straightforward and efficient way to ensure compliance with regulations like GDPR.

This article outlines several methods to integrate consent requests seamlessly into your quizzes.

## Add a Link to Your Privacy Policy

A fundamental step in asking for consent is to make your Privacy Policy easily accessible. You can link to your Privacy Policy within any text element of the quiz using [Markdown Language](https://docs.revenuehunt.com/how-to-guides/use-markdown/). 

For example, like this:

```markdown
By providing your email address you agree to our [privacy policy](https://www.linktoyourprivacypolicy.com).
```

## How to Ask for Marketing/Data Processing Consent

### Option 1: Question Description

You can inform the customer in the question description that by providing the email address they agree to receive marketing information.

1. To show question description go to the [quiz builder](https://docs.revenuehunt.com/reference/quiz-builder/#quiz-builder_1) select a question and open the [question settings](https://docs.revenuehunt.com/reference/quiz-builder/#question-settings).
2. Enable the `question description` feature.
3. A text field will appear where you can add your consent text.
4. Include a link to your privacy policy using [Markdown Language](https://docs.revenuehunt.com/how-to-guides/use-markdown/), e.g., `[privacy policy](https://www.linktoyourprivacypolicy.com)`
5. Publish your changes using the `Publish` button located at the top-right corner.

### Option 2: Marketing Checkmark

Create a marketing consent checkbox by combining quiz slides can ensure users actively consent before proceeding.

1. Go to the [quiz builder](https://docs.revenuehunt.com/reference/quiz-builder/#quiz-builder_1) and place a `Multiple Choice` question right after the `email/phone` question slide.
2. Add a single choice with your consent text, e.g., `I consent to process my data for marketing purposes.`
3. Return to the `email/phone` question , access [question settings](https://docs.revenuehunt.com/reference/quiz-builder/#question-settings), and enable the `join next question` option.
4. This connects the two questions, requiring users to select the marketing consent option to proceed with the quiz.
    ![how to ask for marketing consent join questions](/images/how to ask for marketing consent join questions.png)

### Option 3: GDPR Question

You can ask directly a `Legal Tererms/GDPR` question in your quiz, where you ask the customer to accept the processing of their data or receive marketing information.

1. Go to the [quiz builder](https://docs.revenuehunt.com/reference/quiz-builder/#quiz-builder_1), click the `+` button and add a [Legal Term/GDPR slide](https://docs.revenuehunt.com/reference/quiz-builder/#question-types).
2. In the question text ask if users consent to the processing of their data for marketing purposes.
3. Depending on the response (yes or no), use [jump logic](https://docs.revenuehunt.com/how-to-guides/use-jump-logic/) to direct users to different sections of the quiz for immediate segmentation based on consent.

---
Clearly communicating consent options and making your privacy policy accessible are key practices for respecting user preferences and ensuring transparency in your data collection. Utilize the methods outlined above to effectively integrate consent requests into your quizzes.
