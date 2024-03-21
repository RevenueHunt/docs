# How to Track Quiz Performance with Google Analytics

Google Analytics offers a powerful way to gain insights into user engagement with your quizzes. Linking your quiz with Google Analytics can provide valuable data on user interaction, pinpoint engagement issues, and help minimize abandonment rates.

## Connect Quiz to Google Analytics

You can add your Google Analytics Tracking Code to your quiz to understand how your customers are interacting with your quiz, identify bottlenecks, and reduce the drop-off rate.

1. Head to your quiz and click on the [Connect](https://docs.revenuehunt.com/reference/quiz-builder/#connect) tab.
2. Click on the `connect` button in the Google Analytics section and paste your Google Analytics Tracking Code (**G-xxxxx** for GA4).

### How to Find Your GA4 Tracking Code

Don't know how to find your GA tracking code? [Check this link](https://support.google.com/analytics/answer/1008080).

1. Open your GA4 account and navigate to `Settings > Data Streams`.
2. Select or set up a new data stream for your website.
3. Open the stream and copy the Measurement ID.
4. Copy the Measurement ID into the app’s `Connect > Google Analytics` section and publish the changes.

## Track Customer Behavior (Events)

You’ll be able to see quiz usage and customer behavior in your Google Analytics dashboard, under `Reports > Engagement > Events`.

![how to ga events](/images/how to ga events.png)

Events are triggered every time a customer starts a quiz, views a question, picks a choice, gets to the results page, adds a product to the cart, and proceeds to the cart/checkout. You can check more data about unique events by clicking on the specific Event name.

| Trigger                                                             | Event Action | Event Category    | Event Label    |
|---------------------------------------------------------------------|--------------|-------------------|----------------|
| User starts a quiz (clicks on the button of the first question or the welcome question) | view         | start             | quiz_name      |
| User views a question                                               | view         | question          | question_title |
| User clicks on a choice or selects an option from a dropdown        | click        | choice            | choice_text    |
| User responds to the email question                                 | submit       | email             | quiz_name      |
| User responds to the phone question                                 | submit       | phone             | quiz_name      |
| User gets to results page                                           | view         | results           | quiz_name      |
| A certain product is recommended in the results page                | recommendation | product          | product_name   |
| Customer clicks on product (view product button or image)           | view         | product           | product_name   |
| Customer adds a product to cart (via "add to cart" or "add all to cart" buttons) | click        | addCart           | product_name   |
| Customer proceeds to cart/checkout                                  | click        | checkoutButton    | quiz_name      |
| Customer retakes quiz                                               | click        | retakeQuiz        | quiz_name      |


## Track Quiz Revenue

You’ll see revenue attributed to the quiz in `Engagement > Conversions > Event name > purchase`. Click on the `purchase` event.

![how to ga revenue2](/images/how to ga revenue2.png)

Add a `Source` column next to the default channel grouping and look for the rows which include the `revenuehunt` source.

![how to ga events](/images/how to ga events.png)

### Quiz Exploration (BETA)

You can build your own exploration of quiz revenue in your Google Analytics 4 account.

![how to ga exploration](/images/how to ga exploration.png)

The exploration enables you to see how much revenue the quizzes have generated and attribute the original source/medium of the traffic.

**Guidelines:**

- Filter by the event name `recommendation`to isolate quiz-related data.
- `Session source/medium` shows where the traffic originated.
- `Sessions` count how many times the quiz was engaged with.
- `Total Revenue` displays earnings tied to the quiz.

**NOTE:** Some users have encountered issues with explorations not showing revenue data due to GA4 limitations.

## Exclude the Quiz as Source in Google Analytics

We strongly recommend not excluding your quiz as a traffic source, but here’s how to do it if you need to.

1. Exclude the `admin.revenuehunt.com` domain in Google Analytics. [More info on how to exclude referral traffic here](https://support.google.com/analytics/answer/2795830?hl=en).
2. Deactivate the `Set revenuehunt/quiz as UTM source/medium` toggle in the [Quiz Settings](https://docs.revenuehunt.com/reference/quiz-builder/#quiz-settings).

**Why Returning Users from Excluded Domains Still Appear in Your Reports?**

Old traffic might appear as coming from the excluded domain. This issue results from the default campaign timeout of 6 months. For more information, visit [Google Analytics support](https://support.google.com/analytics/answer/2795830?hl=en#zippy=).
