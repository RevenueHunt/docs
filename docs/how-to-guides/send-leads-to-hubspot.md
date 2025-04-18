# How to Send Leads to HubSpot

Integrating your RevenueHunt Product Recommendation Quiz with HubSpot can significantly enhance your marketing efforts. 

By automatically sending quiz results to your HubSpot account, you can segment your contacts based on their responses and engage them with personalized campaigns. 

This guide will walk you through the steps to link your quiz to HubSpot, ensuring that every interaction is captured for targeted follow-ups.

Before starting, make sure you have:

- Access to your RevenueHunt Product Recommendation Quiz.
- An active HubSpot account.

## Link Quiz to HubSpot

1. Go to the [Quiz Builder](/reference/quiz-builder/) and click on the [Connect](/reference/quiz-builder/connect-integrations/) tab on the top of the screen.
2. Within the integration options, find the section dedicated to HubSpot and click on the `Connect` button.
3. A new browser tab will open, prompting you to authorize the connection between your quiz platform and your HubSpot account.
4. Select your HubSpot account from the list provided.
    ![how to send leads to hubspot connect](/images/how_to_send_leads_to_hubspot_connect.png)
    
5. You'll be directed to a confirmation page indicating that the connection has been successfully established.
    ![how to send leads to hubspot connect succesfull](/images/how_to_send_leads_to_hubspot_connect_succesfull.png)

Once connected, the quiz results will automatically flow into your HubSpot account. 

## Quiz Data in HubSpot

Every time your customers take the quiz, their contact details along with all of their responses and product recommendations will be sent to your HubSpot account.

1. To view the imported data, navigate to the `contacts` section within HubSpot.
2. Select any contact that has taken the quiz, and click on `view all properties` to examine the details.
    ![how to hubspot properties1](/images/how_to_hubspot_image1.png)
3. You will find a section labeled `Product Recommendation Quiz` or similarly, depending on your quiz setup. This section houses all quiz-related data, including answers and product recommendations.
    ![how to hubspot properties2](/images/how_to_hubspot_image2.png)

## Sending Follow-up Emails with HubSpot

You can now use these properties to create **segmented lists** based your customers responses to the quiz so you can follow up with hyper-segmented campaigns.

Check [this HubSpot article](https://knowledge.hubspot.com/lists/create-active-or-static-lists) to learn how to create lists.

### Using Custom Quiz Properties in Email Templates

To personalize your follow-up emails based on quiz data, you’ll need to pull custom properties into the email templates.

- In HubSpot, navigate to `Marketing > Email > Create email`.
- In the email editor, use the **Personalization Token** feature.
- Click on `Insert`, then select Personalization Token from the dropdown.
    ![how to hubspot image5](/images/how_to_hubspot_image5.png)
- Choose the custom quiz properties that were captured with your Product Recommendation Quiz. HubSpot will automatically replace these tokens with each contact's respective data during the email send.
- Use the `Preview` feature to ensure that the custom properties are appearing correctly in your email.

    ![how to hubspot image6](/images/how_to_hubspot_image6.png)


!!! info

    Please be aware that while HubSpot efficiently handles text-based quiz data, its interface currently **does not support embedding images** directly into email templates as custom properties. Plan your quiz content accordingly to ensure seamless integration and utilization within HubSpot.

---
By folliwng this article, you can set up your post-quiz email flow with HubSpot.
