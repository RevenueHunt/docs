---
icon: material/numeric-4
---


# Sending follow-up emails with Klaviyo

In this tutorial, you’ll learn how to add Shop Quiz leads to Klaviyo and how to build a post-quiz email flow in Klaviyo.

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

In this tutorial, you’ll learn how to connect your quiz to Klaviyo and set up a post-quiz email flow.

Connecting the quiz to Klaviyo can significantly increase your sales. 

RevenueHunt allows you to send all quiz information directly to Klaviyo.

This includes the quiz taker’s email and name but also all the quiz questions, answers and recommended products.

Sending a follow up email with Klaviyo is very easy. 

Let’s get started.



To send contacts to Klaviyo your quiz needs to have an email question. 

You can add it to the quiz from the Quiz Builder tab.


You can ask for marketing consent directly in the quiz.

For example:

You can inform the customer in the question description that by providing the email address they agree to receive marketing information.

Or you can add a marketing checkmark by joining two slides together. 


To connect the quiz to Klaviyo you’ll have to provide your Klaviyo Public API Key.

Public API Key is essential because it allows us to send information to Klaviyo Profiles.

To find your Public Key login to your Klaviyo account.

In account Settings open the API Keys tab and copy the public API Key.

Navigate back to the Shop Quiz app. 

In the Quiz > Connect tab, scroll to Klaviyo and edit the connection.

Paste your Public API Key and save.

Publish the changes with the top-right Publish button.



Test quiz all the way to the results. 

Make sure to provide a sample email that doesn’t already exist in your Kalviyo account.

To verify the test, open Kalviyo > Profiles section.

If a new profile was added the integration was successful.

From now on all the contacts coming from the quiz will be added to your Klaviyo account.


All quiz contacts can be grouped into a segment. 

To create a new segment in Klaviyo go to  Audience > List & Segements and click create a new Segment.

Name the segment and set up the definition.

The Permalink property is unique for profiles coming from the quiz.

If you don’t see the permalink property in the dropdown menu, you may need to take a test quiz and try again.

Click "Create a segment".

Now all the contacts coming from the quiz will also be added to this specific segment.



To create an email flow that inclvudes only quiz takers open the Flows tab. 

Choose to create from scratch and come up with a name.

Next, you’ll be asked to set up a flow trigger.

Choose a segment created in the previous step.

This way whenever someone enters the segment they will trigger the email flow.


Confirm with DONE.



Grab the EMAIL action and drop it below the flow  trigger.

Click on the three dots and edit the email.

Edit the name/subject/email to your liking and select the HTML email template.

From the Connect >  Klaviyo tab you can download a ready to use email template.

Copy the code and go back to Klaviyo.

Open the HTML email template and remove the existing code.

Paste the new template code.

You can then preview the email as one of your segment subscribers.

Make sure to Save the changes and click Done.


Return to your flow and turn your email LIVE.

From that moment on, all the quiz takers, who leave their email, will be automatically added to your Kalviyo Segment and will be sent a follow-up email. 

Remember to deactivate the email Notifications from the Quiz Builder once the Klaviyo flow is set up. 



Shop Quiz allows you to add contacts from the quiz directly to a list in Klaviyo. 

To do that you’ll need to provide a Private API Key.

To create a new Private Key for the Shop Quiz app login to your Klaviyo account.

In account Settings open the API Keys tab and create a new Private API Key.

Allow Full access.

Copy the private key.

In the Quiz Connect tab scroll to Klaviyo and edit the connection.

Paste your Private API Key.

Choose to mark all profiles as true and select a list that contacts should be added to.

Keep in mind that contacts from the quiz can be added only to a Single Opt-in List in Klaviyo.

Save the changes and Publish them with the top-right Publish button.

Remember to test the connection with a sample email.



Congratulations!

You’ve learned how to create a quiz email flow in Klaviyo.

Check out our FAQ section for more resources on getting started with recommendation quizzes.
