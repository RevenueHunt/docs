---
description: "Learn how to A/B test your RevenueHunt quiz to optimize conversions and find the best-performing quiz version."
icon: material/ab-testing
---

# How to A/B Test Your Product Recommendation Quiz

A/B testing, also called split testing, lets you compare two versions of a quiz to see which performs better.

This article sets up an A/B test by hand, using the create, duplicate and edit features of the RevenueHunt app.

Ensure you have:

- Access to the RevenueHunt app where you can create and edit quizzes.
- Basic understanding of [how to publish quizzes](/how-to-guides/publish-quiz/) on your website.
- Access to your website backend, or a platform that lets you edit HTML and JavaScript for traffic distribution. This is optional, and only for advanced routing.
- An analytics tool such as [Google Analytics](/how-to-guides/integrate-google-analytics/) or [Meta Pixel](/how-to-guides/integrate-meta-pixel/), to measure quiz performance.

## Step 1: create two versions of your quiz

- **Design Your Original Quiz**: Create your quiz, Version A, in the RevenueHunt app. Use the content and design you expect to perform best.
- **Duplicate and Modify for Version B**: Use the duplicate feature on the dashboard to copy Version A. Change one element, such as the title, the color scheme or the question order. Keep every other element the same, so the test measures that one change. Publish with the top-right `Publish` button.

## Step 2: publish both versions on your website

There are two ways to put both versions on your website. Which one suits you depends on whether you can edit your site code, and on how precise the test needs to be.

### No coding solution: basic A/B testing

The simplest A/B test publishes each version on its own page in your store. This needs no code:

- **Inline Quiz on a New Page**: Create a new page for each version of the quiz (Version A and Version B). Follow the [Inline Quiz on a New Page](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page) publishing instructions to embed each quiz into its respective page.

You can then link to each version from anywhere on your website, or from an external marketing channel.

### Coding solution: advanced A/B testing

To randomize which version each customer sees, you need some code:

- **Link Popup**: Create one entry point, such as a button or a link, that sends the customer to either Version A or Version B. A developer has to write the logic that picks the link for each customer. For the setup steps, see [How to Set Up a Quiz Link Popup on Your Store](/how-to-guides/publish-quiz-link/).

## Step 3: evenly distribute traffic between quizzes

To manually distribute traffic:

- For Basic Routing: Give each version its own URL, and send customers to one or the other from your website links and promotions.
- For Advanced Routing: Add a JavaScript snippet or server-side logic to your landing page. It serves Version A or Version B at random to each new customer.

## Step 4: track and analyze results

- **Set Up Analytics**: Give each version its own tracking. The [Metrics](/reference/quiz-builder/metrics/) panel already records quiz starts, completions, conversion rate and drop-off. For more, connect each quiz to [Google Analytics](/how-to-guides/integrate-google-analytics/) or [Meta Pixel](/how-to-guides/integrate-meta-pixel/).
- **Analyze Performance**: Once enough traffic has reached both versions, compare the data against the goal you set, such as a higher completion rate.

## Step 5: implement improvements

Decide which version performs better. Put the winning elements into your main quiz, and pick a new variable for the next test.

## Tips for effective A/B testing

- Test one variable at a time to understand its impact clearly.
- Collect a large enough sample before you draw a conclusion.


---
This article explains how to A/B test a quiz in the RevenueHunt app. It covers creating two versions, publishing both, splitting traffic between them and comparing the results.
