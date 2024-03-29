# How to Send Leads to ActiveCampaign

Integrating your Shop Quiz with ActiveCampaign allows for a seamless transition of valuable customer data directly into your email marketing campaigns and CRM management. This guide will navigate you through the steps to link your quiz with ActiveCampaign, enabling you to leverage quiz data for targeted follow-ups and enhanced customer engagement.

Before you begin, ensure you have:

- An active ActiveCampaign account.
- A quiz built on the Shop Quiz platform.

*Note: The integration process mainly involves transferring raw data from the quiz to ActiveCampaign. Setting up detailed flows or custom events based on this data is managed within ActiveCampaign itself.*

## Link Quiz to ActiveCampaign

To integrate your quiz with ActiveCampaign:

1. Navigate to your quiz platform and select the quiz you wish to connect.
2. Click on the [Connect]() tab located at the top of the screen to access the integration settings.
3. In the integration options, locate and click the `Connect` button within the ActiveCampaign section.
4. Once clicked, you'll be redirected to a configuration page in your ActiveCampaign account. Click on `Add an account` and enter your `API Token` when prompted.
5. Select the specific quiz you wish to integrate and proceed by clicking `Continue`.
6. Map your quiz responses to the corresponding fields in ActiveCampaign to ensure data is correctly synchronized. This may involve adding new field mappings if necessary.
    ![how to activecampaign connect](/images/how to activecampaign connect.png)

Once configured, your quiz will be connected, and you can modify settings or update the integration directly from this interface.

Alternatively, you can initiate the connection from within ActiveCampaign:

1. Go to the Apps menu in ActiveCampaign and search for `Product Recommendation Quiz`.
2. Select the quiz icon and follow the provided setup instructions. During the setup process, you will be prompted to enter your ActiveCampaign API Token. This token is essential for linking the quiz data with your ActiveCampaign account.


If you have any questions about the process, don’t hesitate to reach out to our support team. Note that the Quiz is only responsible for sending the raw data, you will have to configure a flow or any other custom event you wish to make with the data within ActiveCampaign in itself, and any questions regarding this process should be asked to ActiveCampaign’s support team directly.

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
2. Name each field appropriately. These fields will be categorized under `General Details`.
3. Return to the Product Recommendation Quiz app in ActiveCampaign to map these new fields, ensuring future contacts from the quiz are enriched with this custom information.
    ![how to activecampaign mapping](/images/how to activecampaign mapping.png)

After that, all the new contacts from the quiz will receive more custom information.

![how to activecampaign profile](/images/how to activecampaign profile.png)

## Sending Follow-up Emails with ActiveCampaign

To send automatic follow-up emails to quiz takers, you can set up an automation in ActiveCampaign.

To automate email communications based on quiz participation:

1. Within ActiveCampaign, go to the `Automations` menu and create a new automation.
2. Set a trigger related to the Product Recommendation Quiz by selecting the appropriate quiz under `Apps`.
    ![how to activecampaign automation](/images/how to activecampaign automation.gif)
3. Following the trigger setup, design your email template. Incorporate personalization by adding `custom properties`, such as direct links to quiz responses, to your text blocks.
    ![how to activecampaign add custom properties](/images/how to activecampaign add custom properties.gif)

### Adding Recommended Products to Emails

Unfortunately, for now, the only information about the recommended products we’re able to send to Activecampaign is the Recommended Product IDs. This is not enough information to display the whole list of recommended products.

To show any products in an ActiveCampaign you may need to connect your ActiveCampaign to Shopify first. Then by adding a product block, you should be able to display products from specific collections. It could be possible to add multiple product blocks and have them shown or hidden based on the recommended product ID, however, this option has not been yet tested thoroughly.



 



