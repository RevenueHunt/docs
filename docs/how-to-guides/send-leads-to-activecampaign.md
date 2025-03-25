# How to Send Leads to ActiveCampaign

Integrating your RevenueHunt Product Recommendation Quiz with ActiveCampaign allows for a seamless transition of valuable customer data directly into your email marketing campaigns and CRM management. 

This guide will navigate you through the steps to link your quiz with ActiveCampaign, enabling you to use quiz data for targeted follow-ups and enhanced customer engagement.

Before you begin, ensure you have:

- An active ActiveCampaign account.
- A quiz built on the RevenueHunt platform.

!!! note

    The integration process mainly involves transferring raw data from the quiz to ActiveCampaign. Setting up detailed flows or custom events based on this data is managed within ActiveCampaign itself.

## Link Quiz to ActiveCampaign

To integrate your quiz with ActiveCampaign:

1. Open the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/).
2. Click on the [Connect](https://docs.revenuehunt.com/reference/quiz-builder/#connect) tab located at the top of the screen to access the integration settings.
3. In the integration options, locate ActiveCampaign and copy the `API Token`. You'll need it later.
    ![how to send leads to activecampaign](/images/how_to_send_leads_to_activecampaign.png)
4. Click the `Connect` button within the ActiveCampaign section.
4. Once clicked, you'll be redirected to a configuration page in your ActiveCampaign account. Click on `Add an account`.
    ![how to send leads to activecampaign step1](/images/how_to_send_leads_to_activecampaign_step1.png)

5. Enter your `API Token` when prompted.
    ![how to send leads to activecampaign step2](/images/how_to_send_leads_to_activecampaign_step2.png)

5. Select the specific quiz you wish to integrate and proceed by clicking `Continue`.
    ![how to send leads to activecampaign step3](/images/how_to_send_leads_to_activecampaign_step3.png)

6. Map your quiz responses to the corresponding fields in ActiveCampaign to ensure data is correctly synchronized. This may involve adding new field mappings if necessary.
    ![how to activecampaign connect](/images/how_to_activecampaign_connect.png)

Once configured, your quiz will be connected, and you can modify settings or update the integration directly from this interface.

![how to send leads to activecampaign step final](/images/how_to_send_leads_to_activecampaign_step_final.png)

Alternatively, you can initiate the connection from within ActiveCampaign:

1. Go to the Apps menu in ActiveCampaign and search for `Product Recommendation Quiz`.

    !!! warning

        If you're unable to see the Apps page in your account, it is likely because ActiveCampaign branding is turned off for your account. Please try toggling the ActiveCampaign branding setting off and then back on in your account settings. Once you've done that, check if the Apps page appears

2. Select the quiz icon and follow the provided setup instructions. During the setup process, you will be prompted to enter your `ActiveCampaign API Token`. This token is essential for linking the quiz data with your ActiveCampaign account and can be found in the [`Connect`](https://docs.revenuehunt.com/reference/quiz-builder/#connect) > ActiveCampaign section of the app.

!!! note

    Note that the Quiz is only responsible for sending the raw data, you will have to configure a flow or any other custom event you wish to make with the data within ActiveCampaign in itself, and any questions regarding this process should be asked to ActiveCampaign’s support team directly.

## Adding custom information to the Contact profile

With the quiz integrated, you might want to enhance contact profiles with additional custom information derived from quiz results.

Here’s a list of additional custom information that can be added to your contact profile:

- Email
- First Name
- Full Name
- Quiz ID
- Quiz Name
- Response ID
- Tags
- Permalink
- Permalink Hash
- Recommended Product IDs

To add these fields to a new profile:

1. Navigate to `Lists -> Manage fields` within ActiveCampaign and click `Add Field` to create new fields for the extra quiz data.
    ![how to send leads to activecampaign new field1](/images/how_to_send_leads_to_activecampaign_new_field1.png)
2. Name each field appropriately. These fields will be categorized under `General Details`.
    ![how to send leads to activecampaign new field2](/images/how_to_send_leads_to_activecampaign_new_field2.png)
3. These fields will be categorized under `General Details`.
    ![how to send leads to activecampaign new field3](/images/how_to_send_leads_to_activecampaign_new_field3.png)
3. Return to the Product Recommendation Quiz app in ActiveCampaign to map these new fields, ensuring future contacts from the quiz are enriched with this custom information.
    ![how to activecampaign mapping](/images/how_to_activecampaign_mapping.png)

After that, all the new contacts from the quiz will receive more custom information.

![how to activecampaign profile](/images/how_to_activecampaign_profile.png)

## Sending Follow-up Emails with ActiveCampaign

To send automatic follow-up emails to quiz takers, you can set up an automation in ActiveCampaign.

To automate email communications based on quiz participation:

1. Within ActiveCampaign, go to the `Automations` menu and create a new automation.
2. Set a trigger related to the Product Recommendation Quiz by selecting the appropriate quiz under `Apps`.
    ![how to activecampaign automation](/images/how_to_activecampaign_automation.gif)
3. Following the trigger setup, design your email template. Incorporate personalization by adding `custom properties`, such as direct links to quiz responses, to your text blocks.
    ![how to activecampaign add custom properties](/images/how_to_activecampaign_add_custom_properties.gif)

### Adding Recommended Products to Emails

Unfortunately, for now, the only information about the recommended products we’re able to send to Activecampaign is the Recommended Product IDs. This is not enough information to display the whole list of recommended products.

To show any products in an ActiveCampaign you may need to connect your ActiveCampaign to Shopify first. Then by adding a product block, you should be able to display products from specific collections. It could be possible to add multiple product blocks and have them shown or hidden based on the recommended product ID, however, this option has not been yet tested thoroughly.

---
By following this article, you can set up your post-quiz email flow with ActiveCampaign.



 



