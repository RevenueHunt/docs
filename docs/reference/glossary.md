---
description: "Canonical RevenueHunt terminology for quizzes, questions, blocks, choices, responses, upvotes and conditional logic, per platform."
---

# Glossary

The words this documentation uses, and what each one means.

## People

| Term | What it means |
|---|---|
| **you** | The person building the quiz. |
| **merchant** | A store owner using RevenueHunt. |
| **customer** | The person taking your quiz, and the person who buys as a result. |
| **lead** | A customer who has given you an email address or phone number through the quiz. Leads are what sync to Klaviyo, Mailchimp and your other integrations. |

## Responses

| Term | What it means |
|---|---|
| **answer** | What a customer picked or typed for one question. |
| **quiz response** | A complete submission: every answer from one customer, plus metadata such as the date and the products recommended. |
| **response** | Short for quiz response, as in *this quiz has 1,049 responses*. |

## The app

=== "Shopify"

    | Term | What it means |
    |---|---|
    | **Quiz builder** | Where you build a quiz: its questions, conditional logic, quiz design, results page and settings. |
    | **Dashboard** | The list of your quizzes. Duplicate, rename, delete and set a default quiz from here. |
    | **Analytics** | Where your quiz performance data lives: completion rate, drop-off per question, and which products get recommended. |
    | **Preview** | Opens the quiz as a customer would see it, without publishing. Responses from a preview are test data. |
    | **Quiz ID** | The short code that identifies one quiz. You need it when embedding a quiz or troubleshooting. |
    | **default quiz** | The quiz shown where a page does not name a specific one. Set it from the Dashboard. |
    | **Success checklist** | The setup steps shown on the Dashboard for getting a quiz live. |
    | **Quiz Copilot** | The assistant that helps you build, edit and translate a quiz. Built for Shopify only. |
    | **Content Dynamic Source** | Pulls an answer a customer already gave into text shown later in the quiz or on the results page, so the wording adapts to them. Called Information Recall in the other versions. |

=== "Shopify (Legacy)"

    | Term | What it means |
    |---|---|
    | **Quiz Builder** | Where you build a quiz: its questions, Conditional Logic, Quiz Design, Results Page and settings. |
    | **Dashboard** | The list of your quizzes. Duplicate, rename, delete and set a default quiz from here. |
    | **Metrics** | Where your quiz performance data lives: completion rate, drop-off per question, and which products get recommended. |
    | **Preview** | Opens the quiz as a customer would see it, without publishing. Responses from a preview are test data. |
    | **Quiz ID** | The short code that identifies one quiz. You need it when embedding a quiz or troubleshooting. |
    | **default quiz** | The quiz shown where a page does not name a specific one. Set it from the Dashboard. |
    | **Success Checklist** | The setup steps shown on the Dashboard for getting a quiz live. |
    | **Information Recall** | Pulls an answer a customer already gave into text shown later in the quiz or on the Results Page, so the wording adapts to them. |

=== "WooCommerce"

    | Term | What it means |
    |---|---|
    | **Quiz Builder** | Where you build a quiz: its questions, Conditional Logic, Quiz Design, Results Page and settings. |
    | **Dashboard** | The list of your quizzes. Duplicate, rename, delete and set a default quiz from here. |
    | **Metrics** | Where your quiz performance data lives: completion rate, drop-off per question, and which products get recommended. |
    | **Preview** | Opens the quiz as a customer would see it, without publishing. Responses from a preview are test data. |
    | **Quiz ID** | The short code that identifies one quiz. You need it when embedding a quiz or troubleshooting. |
    | **default quiz** | The quiz shown where a page does not name a specific one. Set it from the Dashboard. |
    | **Success Checklist** | The setup steps shown on the Dashboard for getting a quiz live. |
    | **Information Recall** | Pulls an answer a customer already gave into text shown later in the quiz or on the Results Page, so the wording adapts to them. |

=== "Magento"

    | Term | What it means |
    |---|---|
    | **Quiz Builder** | Where you build a quiz: its questions, Conditional Logic, Quiz Design, Results Page and settings. |
    | **Dashboard** | The list of your quizzes. Duplicate, rename, delete and set a default quiz from here. |
    | **Metrics** | Where your quiz performance data lives: completion rate, drop-off per question, and which products get recommended. |
    | **Preview** | Opens the quiz as a customer would see it, without publishing. Responses from a preview are test data. |
    | **Quiz ID** | The short code that identifies one quiz. You need it when embedding a quiz or troubleshooting. |
    | **default quiz** | The quiz shown where a page does not name a specific one. Set it from the Dashboard. |
    | **Success Checklist** | The setup steps shown on the Dashboard for getting a quiz live. |
    | **Information Recall** | Pulls an answer a customer already gave into text shown later in the quiz or on the Results Page, so the wording adapts to them. |

=== "BigCommerce"

    | Term | What it means |
    |---|---|
    | **Quiz Builder** | Where you build a quiz: its questions, Conditional Logic, Quiz Design, Results Page and settings. |
    | **Dashboard** | The list of your quizzes. Duplicate, rename, delete and set a default quiz from here. |
    | **Metrics** | Where your quiz performance data lives: completion rate, drop-off per question, and which products get recommended. |
    | **Preview** | Opens the quiz as a customer would see it, without publishing. Responses from a preview are test data. |
    | **Quiz ID** | The short code that identifies one quiz. You need it when embedding a quiz or troubleshooting. |
    | **default quiz** | The quiz shown where a page does not name a specific one. Set it from the Dashboard. |
    | **Success Checklist** | The setup steps shown on the Dashboard for getting a quiz live. |
    | **Information Recall** | Pulls an answer a customer already gave into text shown later in the quiz or on the Results Page, so the wording adapts to them. |

=== "Standalone"

    | Term | What it means |
    |---|---|
    | **Quiz Builder** | Where you build a quiz: its questions, Conditional Logic, Quiz Design, Results Page and settings. |
    | **Dashboard** | The list of your quizzes. Duplicate, rename, delete and set a default quiz from here. |
    | **Metrics** | Where your quiz performance data lives: completion rate, drop-off per question, and which products get recommended. |
    | **Preview** | Opens the quiz as a customer would see it, without publishing. Responses from a preview are test data. |
    | **Quiz ID** | The short code that identifies one quiz. You need it when embedding a quiz or troubleshooting. |
    | **default quiz** | The quiz shown where a page does not name a specific one. Set it from the Dashboard. |
    | **Success Checklist** | The setup steps shown on the Dashboard for getting a quiz live. |
    | **Information Recall** | Pulls an answer a customer already gave into text shown later in the quiz or on the Results Page, so the wording adapts to them. |

## Quiz structure

=== "Shopify"

    A quiz is a sequence of questions, ending in a results page. Questions are modular: each one holds one or more blocks.

    ```
    quiz
    └── question          one screen of the quiz
        └── block         a component on that screen
            └── choice    an alternative inside a choices block
    ```

    | Term | What it means |
    |---|---|
    | **quiz** | The whole thing: a sequence of questions ending in a results page. |
    | **question** | One screen of the quiz. Adding a question type creates a question with the matching block already inside it. |
    | **question type** | What the add menu offers. Choosing **Email Address** creates a question containing an email address input block. You can then add an image block above it. |
    | **block** | A component inside a question. There are content blocks, choices blocks, input blocks and chart blocks. |
    | **choice** | One of the alternatives a customer can pick inside a choices block. |
    | **slide** | The name for a question in the API and in merge tags such as `{{slide:ZMiXjj}}`. |

=== "Shopify (Legacy)"

    A quiz is a sequence of questions, ending in a Results Page. A question holds its choices directly.

    ```
    quiz
    └── question          one screen of the quiz
        └── choice        an alternative the customer can pick
    ```

    | Term | What it means |
    |---|---|
    | **quiz** | The whole thing: a sequence of questions ending in a Results Page. |
    | **question** | One screen of the quiz. The question type determines what the customer sees and does. |
    | **question type** | Multiple Choice, Pictures Choice, Dropdown, Yes/No, Short-text, Multi-line Text, Date, File Upload, Number, Name, Email Address, Phone Number, Legal Terms/GDPR, and the Welcome, Thank You and Statement messages. |
    | **choice** | One of the alternatives a customer can pick. |
    | **slide** | Another word for a question, used in the API and in merge tags. |

    !!! note "Blocks are a Built for Shopify feature"

        Questions in this version are not modular. Blocks exist on the Results Page, but not inside questions.

=== "WooCommerce"

    A quiz is a sequence of questions, ending in a Results Page. A question holds its choices directly.

    ```
    quiz
    └── question          one screen of the quiz
        └── choice        an alternative the customer can pick
    ```

    | Term | What it means |
    |---|---|
    | **quiz** | The whole thing: a sequence of questions ending in a Results Page. |
    | **question** | One screen of the quiz. The question type determines what the customer sees and does. |
    | **question type** | Multiple Choice, Pictures Choice, Dropdown, Yes/No, Short-text, Multi-line Text, Date, File Upload, Number, Name, Email Address, Phone Number, Legal Terms/GDPR, and the Welcome, Thank You and Statement messages. |
    | **choice** | One of the alternatives a customer can pick. |
    | **slide** | Another word for a question, used in the API and in merge tags. |

    !!! note "Blocks are a Built for Shopify feature"

        Questions in this version are not modular. Blocks exist on the Results Page, but not inside questions.

=== "Magento"

    A quiz is a sequence of questions, ending in a Results Page. A question holds its choices directly.

    ```
    quiz
    └── question          one screen of the quiz
        └── choice        an alternative the customer can pick
    ```

    | Term | What it means |
    |---|---|
    | **quiz** | The whole thing: a sequence of questions ending in a Results Page. |
    | **question** | One screen of the quiz. The question type determines what the customer sees and does. |
    | **question type** | Multiple Choice, Pictures Choice, Dropdown, Yes/No, Short-text, Multi-line Text, Date, File Upload, Number, Name, Email Address, Phone Number, Legal Terms/GDPR, and the Welcome, Thank You and Statement messages. |
    | **choice** | One of the alternatives a customer can pick. |
    | **slide** | Another word for a question, used in the API and in merge tags. |

    !!! note "Blocks are a Built for Shopify feature"

        Questions in this version are not modular. Blocks exist on the Results Page, but not inside questions.

=== "BigCommerce"

    A quiz is a sequence of questions, ending in a Results Page. A question holds its choices directly.

    ```
    quiz
    └── question          one screen of the quiz
        └── choice        an alternative the customer can pick
    ```

    | Term | What it means |
    |---|---|
    | **quiz** | The whole thing: a sequence of questions ending in a Results Page. |
    | **question** | One screen of the quiz. The question type determines what the customer sees and does. |
    | **question type** | Multiple Choice, Pictures Choice, Dropdown, Yes/No, Short-text, Multi-line Text, Date, File Upload, Number, Name, Email Address, Phone Number, Legal Terms/GDPR, and the Welcome, Thank You and Statement messages. |
    | **choice** | One of the alternatives a customer can pick. |
    | **slide** | Another word for a question, used in the API and in merge tags. |

    !!! note "Blocks are a Built for Shopify feature"

        Questions in this version are not modular. Blocks exist on the Results Page, but not inside questions.

=== "Standalone"

    A quiz is a sequence of questions, ending in a Results Page. A question holds its choices directly.

    ```
    quiz
    └── question          one screen of the quiz
        └── choice        an alternative the customer can pick
    ```

    | Term | What it means |
    |---|---|
    | **quiz** | The whole thing: a sequence of questions ending in a Results Page. |
    | **question** | One screen of the quiz. The question type determines what the customer sees and does. |
    | **question type** | Multiple Choice, Pictures Choice, Dropdown, Yes/No, Short-text, Multi-line Text, Date, File Upload, Number, Name, Email Address, Phone Number, Legal Terms/GDPR, and the Welcome, Thank You and Statement messages. |
    | **choice** | One of the alternatives a customer can pick. |
    | **slide** | Another word for a question, used in the API and in merge tags. |

    !!! note "Blocks are a Built for Shopify feature"

        Questions in this version are not modular. Blocks exist on the Results Page, but not inside questions.

## Results page structure

=== "Shopify"

    The results page is built from sections, and each section holds blocks.

    ```
    results page
    └── section          a band, shown or hidden by display logic
        └── block        a component in that section
            └── slot     one recommendation position in a products block
    ```

    | Term | What it means |
    |---|---|
    | **results page** | The screen a customer sees after the last question. A quiz can have several. |
    | **section** | A band of the results page. Display logic shows and hides whole sections. |
    | **block** | A component inside a section: text, image, video, custom HTML, a products block or a slot block. |
    | **slot** | One recommendation position inside a products block. Use slots when you want a fixed structure, such as a cleanser, then a serum, then a moisturizer. |

=== "Shopify (Legacy)"

    The Results Page is built from blocks. There are no sections.

    ```
    Results Page
    └── block            a component on the page
        └── slot         one recommendation position in a Product Block
    ```

    | Term | What it means |
    |---|---|
    | **Results Page** | The screen a customer sees after the last question. A quiz can have several. |
    | **block** | A component on the Results Page: text, image, video, custom HTML, a Product Block or a Slot Block. Display Logic shows and hides individual blocks. |
    | **slot** | One recommendation position inside a Product Block. Use slots when you want a fixed structure, such as a cleanser, then a serum, then a moisturizer. |

=== "WooCommerce"

    The Results Page is built from blocks. There are no sections.

    ```
    Results Page
    └── block            a component on the page
        └── slot         one recommendation position in a Product Block
    ```

    | Term | What it means |
    |---|---|
    | **Results Page** | The screen a customer sees after the last question. A quiz can have several. |
    | **block** | A component on the Results Page: text, image, video, custom HTML, a Product Block or a Slot Block. Display Logic shows and hides individual blocks. |
    | **slot** | One recommendation position inside a Product Block. Use slots when you want a fixed structure, such as a cleanser, then a serum, then a moisturizer. |

=== "Magento"

    The Results Page is built from blocks. There are no sections.

    ```
    Results Page
    └── block            a component on the page
        └── slot         one recommendation position in a Product Block
    ```

    | Term | What it means |
    |---|---|
    | **Results Page** | The screen a customer sees after the last question. A quiz can have several. |
    | **block** | A component on the Results Page: text, image, video, custom HTML, a Product Block or a Slot Block. Display Logic shows and hides individual blocks. |
    | **slot** | One recommendation position inside a Product Block. Use slots when you want a fixed structure, such as a cleanser, then a serum, then a moisturizer. |

=== "BigCommerce"

    The Results Page is built from blocks. There are no sections.

    ```
    Results Page
    └── block            a component on the page
        └── slot         one recommendation position in a Product Block
    ```

    | Term | What it means |
    |---|---|
    | **Results Page** | The screen a customer sees after the last question. A quiz can have several. |
    | **block** | A component on the Results Page: text, image, video, custom HTML, a Product Block or a Slot Block. Display Logic shows and hides individual blocks. |
    | **slot** | One recommendation position inside a Product Block. Use slots when you want a fixed structure, such as a cleanser, then a serum, then a moisturizer. |

=== "Standalone"

    The Results Page is built from blocks. There are no sections.

    ```
    Results Page
    └── block            a component on the page
        └── slot         one recommendation position in a Product Block
    ```

    | Term | What it means |
    |---|---|
    | **Results Page** | The screen a customer sees after the last question. A quiz can have several. |
    | **block** | A component on the Results Page: text, image, video, custom HTML, a Product Block or a Slot Block. Display Logic shows and hides individual blocks. |
    | **slot** | One recommendation position inside a Product Block. Use slots when you want a fixed structure, such as a cleanser, then a serum, then a moisturizer. |

## Recommendation system

=== "Shopify"

    Two separate systems, deciding different things.

    | System | Attaches to | Decides |
    |---|---|---|
    | **upvotes** | a product, variant or collection | which products are recommended, and their order |
    | **variables and scores** | a named variable | which results page or section a customer sees |

    | Term | What it means |
    |---|---|
    | **upvote** | The signal a choice gives a product, variant or collection. The products block sorts by upvote count, most upvoted first. |
    | **variable** | A named bucket you create, such as `dry_skin`, that collects scores as a customer answers. |
    | **score** | The number a choice adds to a variable. The variable with the highest total is the **winning variable**, which display logic and jump logic use to decide what to show. |

=== "Shopify (Legacy)"

    One system. Choices give upvotes to products, and the Results Page shows the most upvoted first.

    | Term | What it means |
    |---|---|
    | **upvote** | The signal a choice gives a product, variant or collection. The Product Block sorts by upvote count, most upvoted first. |
    | **Minimum number of votes** | A setting that hides products which did not receive enough upvotes. |

    !!! note "Variables and scores are a Built for Shopify feature"

        To show different content to different customers in this version, use Display Logic and Jump Logic based on their answers.

=== "WooCommerce"

    One system. Choices give upvotes to products, and the Results Page shows the most upvoted first.

    | Term | What it means |
    |---|---|
    | **upvote** | The signal a choice gives a product, variant or category. The Product Block sorts by upvote count, most upvoted first. |
    | **Minimum number of votes** | A setting that hides products which did not receive enough upvotes. |

    !!! note "Variables and scores are a Built for Shopify feature"

        To show different content to different customers in this version, use Display Logic and Jump Logic based on their answers.

=== "Magento"

    One system. Choices give upvotes to products, and the Results Page shows the most upvoted first.

    | Term | What it means |
    |---|---|
    | **upvote** | The signal a choice gives a product, variant or category. The Product Block sorts by upvote count, most upvoted first. |
    | **Minimum number of votes** | A setting that hides products which did not receive enough upvotes. |

    !!! note "Variables and scores are a Built for Shopify feature"

        To show different content to different customers in this version, use Display Logic and Jump Logic based on their answers.

=== "BigCommerce"

    One system. Choices give upvotes to products, and the Results Page shows the most upvoted first.

    | Term | What it means |
    |---|---|
    | **upvote** | The signal a choice gives a product, variant or category. The Product Block sorts by upvote count, most upvoted first. |
    | **Minimum number of votes** | A setting that hides products which did not receive enough upvotes. |

    !!! note "Variables and scores are a Built for Shopify feature"

        To show different content to different customers in this version, use Display Logic and Jump Logic based on their answers.

=== "Standalone"

    One system. Choices give upvotes to products, and the Results Page shows the most upvoted first.

    | Term | What it means |
    |---|---|
    | **upvote** | The signal a choice gives a product, variant or collection. The Product Block sorts by upvote count, most upvoted first. |
    | **Minimum number of votes** | A setting that hides products which did not receive enough upvotes. |

    !!! note "Variables and scores are a Built for Shopify feature"

        To show different content to different customers in this version, use Display Logic and Jump Logic based on their answers.

## Conditional logic

Conditional logic is the tab holding **jump logic** and **skip logic**. Display logic is not part of it: you set display logic on the results page itself.

```
conditional logic
├── jump logic    sends the customer to   a question, a results page, or an external URL
└── skip logic    skips                   a question

display logic     shows or hides          part of the results page
```

| Term | What it means |
|---|---|
| **conditional logic** | The tab holding jump logic and skip logic. |
| **jump logic** | Sends a customer to a different question, to a particular results page, or to an external URL. Use it to build a quiz with more than one results page. |
| **skip logic** | Skips a question when it is not relevant to a particular customer. |
| **display logic** | Shows or hides parts of the results page. Set on the results page itself. |

=== "Shopify"

    Jump logic and skip logic are triggered by an **IF** condition based on an answer, a variable or a score. Display logic acts on sections.

=== "Shopify (Legacy)"

    Jump Logic and Skip Logic are triggered by an **IF** condition based on an answer. Display Logic acts on individual blocks.

=== "WooCommerce"

    Jump Logic and Skip Logic are triggered by an **IF** condition based on an answer. Display Logic acts on individual blocks.

=== "Magento"

    Jump Logic and Skip Logic are triggered by an **IF** condition based on an answer. Display Logic acts on individual blocks.

=== "BigCommerce"

    Jump Logic and Skip Logic are triggered by an **IF** condition based on an answer. Display Logic acts on individual blocks.

=== "Standalone"

    Jump Logic and Skip Logic are triggered by an **IF** condition based on an answer. Display Logic acts on individual blocks.

## Products

=== "Shopify"

    | Term | What it means |
    |---|---|
    | **product** | An item in your Shopify catalog. |
    | **variant** | A version of a product, such as a size or color. |
    | **collection** | A group of products in Shopify. Link choices to collections to upvote every product inside. |
    | **product tag** | A label you put on a product in Shopify. RevenueHunt can include or exclude products by tag, the same way it does with collections, and you can build a smart collection from a tag. Not the same as a customer tag. |
    | **catalog** | The copy of your products that RevenueHunt syncs from your store. |

=== "Shopify (Legacy)"

    | Term | What it means |
    |---|---|
    | **product** | An item in your Shopify catalog. |
    | **variant** | A version of a product, such as a size or color. |
    | **collection** | A group of products in Shopify. Link choices to collections to upvote every product inside. |
    | **product tag** | A label you put on a product in Shopify. RevenueHunt can include or exclude products by tag, the same way it does with collections. Not the same as a customer tag. |
    | **catalog** | The copy of your products that RevenueHunt syncs from your store. |

=== "WooCommerce"

    | Term | What it means |
    |---|---|
    | **product** | An item in your WooCommerce store. |
    | **variant** | A version of a product, such as a size or color. |
    | **category** | A group of products in WooCommerce. Link choices to categories to upvote every product inside. |
    | **product tag** | A label you put on a product in WooCommerce. RevenueHunt can include or exclude products by tag, the same way it does with categories. Not the same as a customer tag. |
    | **catalog** | The copy of your products that RevenueHunt syncs from your store. |

    The setting that excludes groups is labelled `excluded collections` in the app, even on WooCommerce. It applies to your categories.

=== "Magento"

    | Term | What it means |
    |---|---|
    | **product** | An item in your Magento store. |
    | **variant** | A version of a product, such as a size or color. |
    | **category** | A group of products in Magento. Link choices to categories to upvote every product inside. |
    | **product tag** | A label you put on a product in Magento. RevenueHunt can include or exclude products by tag, the same way it does with categories. Not the same as a customer tag. |
    | **catalog** | The copy of your products that RevenueHunt syncs from your store. |

    The setting that excludes groups is labelled `excluded collections` in the app, even on Magento. It applies to your categories.

=== "BigCommerce"

    | Term | What it means |
    |---|---|
    | **product** | An item in your BigCommerce store. |
    | **variant** | A version of a product, such as a size or color. |
    | **category** | A group of products in BigCommerce. Link choices to categories to upvote every product inside. |
    | **product tag** | A label you put on a product in BigCommerce. RevenueHunt can include or exclude products by tag, the same way it does with categories. Not the same as a customer tag. |
    | **catalog** | The copy of your products that RevenueHunt syncs from your store. |

    The setting that excludes groups is labelled `excluded collections` in the app, even on BigCommerce. It applies to your categories.

=== "Standalone"

    | Term | What it means |
    |---|---|
    | **product** | An item you add to your Standalone catalog, or import through a Google Product Feed. |
    | **variant** | A version of a product, such as a size or color. |
    | **collection** | A group of products you create in your Standalone account. Link choices to collections to upvote every product inside. |
    | **product tag** | A label on a product in your feed. RevenueHunt can include or exclude products by tag, the same way it does with collections. Not the same as a customer tag. |
    | **catalog** | The products held in your Standalone account. |

## Publishing

| Term | What it means |
|---|---|
| **popup** | A quiz that opens over the page rather than sitting in it. Link Popup Quiz, Automatic Popup Quiz and Chat Popup Quiz are the published forms. |
| **inline quiz** | A quiz embedded directly in a page, as part of the content. |
| **customer tag** | A label a choice can apply to a customer, used to segment them in your store and in your email platform. Not the same as a product tag. |
