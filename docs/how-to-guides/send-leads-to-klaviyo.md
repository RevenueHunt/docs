# Integrating Quizzes with Klaviyo

Businesses have the capability to enhance customer engagement by integrating personalized product recommendation quizzes with Klaviyo. This integration allows for the automatic transfer of quiz results to a Klaviyo mailing list or segments, enabling segmentation based on participant responses and the initiation of targeted follow-up campaigns.

## How to Link Your Quiz to Klaviyo

1. To establish this connection, access your quiz and select the [Connect](https://docs.revenuehunt.com/reference/quiz-builder/#connect) tab at the screen's top. This action reveals options for linking with various third-party services. 
2. Proceed by choosing `Connect` within the Klaviyo section, which prompts a popup window. 
3. You're required to enter your Klaviyo **Public API Key** and, optionally, a Private API Key for adding contacts to specific lists within Klaviyo.
4. Coose whether you want the profiles from the quiz to be automatically marked as profiles that consented to receive marketing materials or not. 
5. Click the top-right `Publish` button to update the preview/live quiz.

Following these steps ensures that every quiz participant's contact information, alongside their responses and product recommendations, are forwarded to your Klaviyo account, registering as `custom properties` within Klaviyo customer profiles. These properties are instrumental in personalizing Klaviyo email templates.

**Considerations** 

- **Processing Time**: Klaviyo may delay in displaying new leads.
- **Character Limitations**: Special characters (e.g., è, é, ê) may impede data transmission.

### API Keys

- **Public API Key**: Obtainable from Klaviyo's designated webpage. You can get your Klaviyo Public API Key [here](https://www.klaviyo.com/account#api-keys-tab).
- **Private API Key (optional)**: For list-specific contact additions, you can get your Klaviyo Private API Key [here](https://www.klaviyo.com/account#api-keys-tab). Make sure to allow "Full access".

## Sending follow-up emails via Klaviyo

This section requires developer intervention for crafting product recommendation follow-ups via Klaviyo. The setup encompasses connecting the quiz, segment creation exclusive to quiz participants, initiating a segment-triggered email flow, and custom email template development. These steps necessitate technical proficiency in Klaviyo's operation and customization.



## Adding quiz contacts to a Klaviyo list

While direct list addition is possible, opting for dynamic segmentation based on quiz responses offers a more refined approach, significantly boosting campaign revenue potential. Klaviyo facilitates segment creation and email flow assignment, enriching the targeting precision of campaigns.

Automated addition to a specified list necessitates a Private API Key, enabling list selection. However, given Klaviyo's potential issues with double opt-in lists not sending opt-in emails, a single opt-in configuration with explicit consent is advisable.

## Include custom properties in Klaviyo email templates

For developers, Klaviyo permits the inclusion of custom properties within email templates, leveraging HTML, CSS, and Django templating. This flexibility enables tailored content display based on quiz outcomes, enhancing personalization.

## Pull product information directly from Shopify

There’s a feature in Klaviyo that allows you to pull the product information directly from Shopify by providing the id.

This way you don’t need to use the “description” or “image_url” that is provided by revenuehunt, but can pull it directly from Shopify by providing the origin_id of the product.

More information about this function can be found [here](https://help.klaviyo.com/hc/en-us/articles/360004785571-Overview-of-the-Catalog-Lookup-Tag).

This comprehensive integration strategy between quizzes and Klaviyo not only streamlines data capture and segmentation but also opens avenues for highly personalized and effective marketing campaigns, leveraging nuanced customer insights gleaned from quiz interactions.
