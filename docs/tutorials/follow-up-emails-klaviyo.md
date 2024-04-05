---
icon: material/numeric-4
---


# Sending Follow-up Emails with Klaviyo

In this tutorial, you’ll learn how to add Shop Quiz leads to [Klaviyo](https://docs.revenuehunt.com/how-to-guides/send-leads-to-klaviyo/) and how to build a post-quiz email flow in Klaviyo.

**You’ll learn:**

- how to add an email question to your quiz
- how to ask for marketing consent in your quiz
- how to connect your quiz to Klaviyo
- how to send quiz leads to Klaviyo Profiles
- how to send quiz leads to Klaviyo Lists
- how to segment customers coming from the quiz in Klaviyo
- how to create a result email flow in Klaviyo
- how to use our built-in Klaviyo email templates

<div class="videoWrapper">
<iframe src="https://www.youtube.com/embed/2NK7PTfNpJg" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Intro

In this tutorial, you’ll learn how to connect your quiz to [Klaviyo](https://docs.revenuehunt.com/how-to-guides/send-leads-to-klaviyo/) and set up a post-quiz email flow.

Connecting the quiz to Klaviyo can significantly increase your sales. 

RevenueHunt allows you to send all quiz information directly to Klaviyo. This includes the quiz taker’s email and name but also all the quiz questions, answers and recommended products.

Sending a follow-up email with Klaviyo is very easy. Let’s get started.

## Add Email Question

To send contacts to Klaviyo your quiz needs to have an `email question`. 

1. You can add it to the quiz from the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/) tab.
2. You can [ask for marketing consent](https://docs.revenuehunt.com/how-to-guides/ask-for-marketing-consent/) directly in the quiz. For example:
    - You can inform the customer in the [question description](https://docs.revenuehunt.com/how-to-guides/ask-for-marketing-consent#option-1-question-description) that by providing the email address they agree to receive marketing information.
    - Or you can add a [marketing checkmark](https://docs.revenuehunt.com/how-to-guides/ask-for-marketing-consent#option-2-marketing-checkmark) by joining two slides together. 

## Connect Quiz to Klaviyo

To connect the quiz to Klaviyo you’ll have to provide your Klaviyo **Public API Key**. 

Public API Key is essential because it allows us to send information to Klaviyo Profiles.

1. To find your Public Key login to your Klaviyo account.
2. In account `Settings` open the `API Keys` tab and copy the public API Key.
3. Navigate back to the Shop Quiz app. 
4. In the [`Quiz > Connect`](https://docs.revenuehunt.com/reference/quiz-builder/#connect) tab, scroll to Klaviyo and `edit` the connection.
5. Paste your Public API Key and `save`.
6. Publish the changes with the top-right `Publish` button.
7. Test quiz all the way to the results. Make sure to provide a sample email that doesn’t already exist in your Kalviyo account.
8. To verify the test, open `Kalviyo > Profiles` section.
9. If a new profile was added the integration was successful.

From now on all the contacts coming from the quiz will be added to your Klaviyo account.

## Create Segment for Quiz Takers

All quiz contacts can be grouped into a **segment** in Klaviyo. 

1. To create a new segment in Klaviyo go to  `Audience > List & Segements` and click `create a new Segment`.
2. Name the segment and set up the definition.
3. The `Permalink-QuizID` property is unique for profiles coming from the quiz.
4. If you don’t see the permalink property in the dropdown menu, you may need to take a test quiz and try again.
5. Click `Create a segment`.

Now all the contacts coming from the quiz will also be added to this specific segment.

## Set Up Email Flow

### Add a Triger

1. To create an email flow that includes only quiz takers open the `Flows` tab. 
2. Choose to create from scratch and come up with a name.
3. Next, you’ll be asked to set up a flow trigger.
4. Choose a segment created in the previous step. This way whenever someone enters the segment they will trigger the email flow.
5. Confirm with `DONE`.

### Edit the Email

1. Grab the `EMAIL` action and drop it below the flow trigger.
2. Click on the `...` three dots and `edit the email`.
3. Edit the `name/subject/email` to your liking and select the `HTML email template`.
4. From the [`Connect >  Klaviyo`](https://docs.revenuehunt.com/reference/quiz-builder/#connect) tab you can **download a ready-to-use email template**.
5. Copy the code and go back to Klaviyo.
6. Open the `HTML email template` and remove the existing code.
7. Paste the new template code.
8. You can then `preview` the email as one of your segment subscribers.
9. Make sure to `Save` the changes and click `Done`.
10. Return to your flow and turn your email `LIVE`.

From that moment on, all the quiz takers, who leave their email, will be automatically added to your Kalviyo Segment and will be sent a follow-up email. 

Remember to deactivate the [email Notifications](https://docs.revenuehunt.com/how-to-guides/send-result-emails/) from the Quiz Builder once the Klaviyo flow is set up. 

## Add Contacts to List

Shop Quiz allows you to add contacts from the quiz directly to a **list** in Klaviyo. To do that you’ll need to provide a **Private API Key**.

1. To create a new Private Key for the Shop Quiz app login to your Klaviyo account.
2. In account `Settings` open the `API Keys` tab and create a `new Private API Key`.
3. Allow `Full access`.
4. Copy the private key.
5. In the Quiz [Connect](https://docs.revenuehunt.com/reference/quiz-builder/#connect) tab scroll to Klaviyo and edit the connection.
6. Paste your Private API Key.
7. Choose to `mark all profiles as true` and select a list that contacts should be added to.
8. Keep in mind that contacts from the quiz can be added only to a [**Single Opt-in**](https://help.klaviyo.com/hc/en-us/articles/115005251108) List in Klaviyo.
9. Save the changes and publish them with the top-right `Publish` button.
10. Remember to test the connection with a sample email via the `Preview` button.

Congratulations!

You’ve learned how to create a quiz email flow in Klaviyo.

Check out our [documentation](https://docs.revenuehunt.com/) for more resources on getting started with recommendation quizzes.
