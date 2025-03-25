# How to Send Leads to Mailchimp

Automating the transfer of quiz results to your Mailchimp account streamlines the process of segmenting your audience and enables targeted follow-up campaigns based on personalized product recommendations. 

!!! warning "Important Considerations"

    - **Limited Data Transfer**: Mailchimp integration only supports email, name, and customer tags to be send from the quiz. For more complex emailing/data needs, including direct product recommendations, consider using a different service.
    - **Alternative Services**: For functionality beyond basic data transfer, platforms like [Klaviyo](https://docs.revenuehunt.com/how-to-guides/send-leads-to-klaviyo/), [HubSpot](https://docs.revenuehunt.com/how-to-guides/send-leads-to-hubspot/) or [Omnisend]() are recommended. These services offer more robust integration options for personalized follow-ups.

Before you begin, ensure you have:

- An active Mailchimp account.
- A RevenueHunt Product Recommendation Quiz that you wish to connect with Mailchimp.

## Link Quiz to Mailchimp

Connecting your quiz to Mailchimp allows for the seamless transfer of leads:

1. Locate your quiz and click on the [Connect](https://docs.revenuehunt.com/reference/quiz-builder/#connect) tab at the top of the interface.
2. Find the Mailchimp section and click on the `Connect` button. This action will redirect you to a Mailchimp login page in a new tab.
    ![how to send leads to mailchimp authorize1](/images/how_to_send_leads_to_mailchimp_authorize1.png)

3. Log into your Mailchimp account and authorize the app by clicking on `Allow`.
    ![how to send leads to mailchimp authorize2](/images/how_to_send_leads_to_mailchimp_authorize2.png)

4. If the connection was successful, you'll see a `Mailchimp got connected, please close this windows to go back to the dashboard.` message.
4. After authorization, your quiz is connected to Mailchimp, and you can proceed to link it to a specific mailing list.
    ![how to send leads to mailchimp settings](/images/how_to_send_leads_to_mailchimp_settings.png)

5. Return to the [Connect](https://docs.revenuehunt.com/reference/quiz-builder/#connect) tab in your quiz platform. You may need to refresh the page to update the connection status.
6. Follow the prompts to select the Mailchimp list you wish to send your quiz results to from the dropdown.

## Use Customer Tags for Segmentation in Mailchimp

With [customer tags](https://docs.revenuehunt.com/reference/quiz-builder/#customer-tags), you can segment your audience within Mailchimp based on their quiz responses:

1. Make sure the quiz is connected to Mailchimp. 
2. Create [customer tags](https://docs.revenuehunt.com/reference/quiz-builder/#customer-tags) in the RevenueHunt app and link them to choices.
3. Once done, click the `Publish` button to update the preview/live quiz with new changes.
4. Navigate to the `Audience` section in your Mailchimp account.
5. Use the customer tags to create segmented lists or groups, allowing for targeted campaign efforts based on the quiz outcomes.

## Hack: Send Quiz Answers to MailChimp

To override Mailchimp's limitation on pushing detailed quiz data, you can use `customer tags` to represent customer responses.

1. For each possible quiz answer, create a corresponding [customer tag](https://docs.revenuehunt.com/reference/quiz-builder/#customer-tags) within your quiz setup. This requires planning to ensure each tag accurately represents the quiz responses.
    ![how to send leads to mailchimp tags](/images/how_to_send_leads_to_mailchimp_tags.png)

2. Upon completion of the quiz by a participant, Mailchimp will receive all the tags that the customer picked based on their choices.

---
By following this article, you can set up your post-quiz email flow with MailChimp.
