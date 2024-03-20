# How to Ask for Marketing/Data Processing Consent

Asking for consent to use customer data for marketing purposes is not just a best practice; it's a legal requirement in many jurisdictions. This guide will walk you through incorporating consent requests into your quizzes effectively, ensuring compliance while maintaining a smooth user experience.

Directly asking for marketing consent or acceptance of data processing in your quiz can be a straightforward and efficient way to ensure compliance with regulations like GDPR. This article outlines several methods to integrate consent requests seamlessly into your quizzes.

## Add a Link to Your Privacy Policy

A fundamental step in asking for consent is to make your Privacy Policy easily accessible. You can link to your Privacy Policy within any text element of the quiz using Markdown Language. For instance:

```markdown
By providing your email address you agree to our [privacy policy](https://www.linktoyourprivacypolicy.com).
```

## How to Ask for Marketing/Data Processing Consent

Asking for marketing or data processing consent within your quizzes is crucial for legal compliance and builds trust with your audience. This document outlines how to integrate consent requests effectively into your quizzes.

### Option 1: Question Description

Incorporating consent information directly into the description of a question is a straightforward method to ensure users are informed.

**Adding a Question Description**

1. In the quiz builder, select a question and click on the question settings (wrench icon).
2. Enable the question description feature.

**Incorporating Consent Text**

- A text field will appear where you can add your consent text.
- Include a link to your privacy policy using Markdown, e.g., `[privacy policy](https://www.linktoyourprivacypolicy.com)`.
- Publish your changes using the "Publish" button located at the top-right corner.

### Option 2: Marketing Checkmark

Creating a marketing consent checkbox by combining quiz slides can ensure users actively consent before proceeding.

**Create a Multiple Choice Question**

- Place a Multiple Choice question right after the email/phone question slide.
- Add a single choice with your consent text.

**Join Questions**

- Return to the email/phone question, access its settings (wrench icon), and enable the “join next question” option.
- This connects the two questions, requiring users to select the marketing consent option to proceed.

### Option 3: GDPR Question

Asking a direct GDPR-related question can effectively gauge user consent.

**Incorporating a GDPR Question**

- Pose a question asking if users consent to the processing of their data for marketing purposes.

**Using Jump Logic**

- Depending on the response (yes or no), use jump logic to direct users to different sections of the quiz for immediate segmentation based on consent.


Clearly communicating consent options and making your privacy policy accessible are key practices for respecting user preferences and ensuring transparency in your data collection. Utilize the methods outlined above to effectively integrate consent requests into your quizzes.
