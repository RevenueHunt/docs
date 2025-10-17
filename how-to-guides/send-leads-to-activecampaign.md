# How to Send Leads to ActiveCampaign

=== "Shopify"


    While the new Built for Shopiify version of the RevenueHunt app **does not** yet integrate directly with ActiveCampaign, it is still possible to send quiz leads to ActiveCampaign.

    One option includes using our [Webhooks](/how-to-guides/send-leads-to-webhooks/) integration to send quiz leads to ActiveCampaign. Another, includes manually adding the quiz leads to ActiveCampaign by uploading a CSV file generated from the quiz.

    This guide explain how you can send quiz data to ActiveCampaign with a workaround.



=== "Shopify (Legacy)"

    Integrating your RevenueHunt Product Recommendation Quiz with ActiveCampaign allows for a seamless transition of valuable customer data directly into your email marketing campaigns and CRM management. 

    This guide will navigate you through the steps to link your quiz with ActiveCampaign, enabling you to use quiz data for targeted follow-ups and improved customer engagement.

    Before you begin, ensure you have:

    - An active ActiveCampaign account.
    - A quiz built on the RevenueHunt platform.

    !!! note

        The integration process mainly involves transferring raw data from the quiz to ActiveCampaign. Setting up detailed flows or custom events based on this data is managed within ActiveCampaign itself.


=== "WooCommerce"


    Integrating your RevenueHunt Product Recommendation Quiz with ActiveCampaign allows for a seamless transition of valuable customer data directly into your email marketing campaigns and CRM management. 

    This guide will navigate you through the steps to link your quiz with ActiveCampaign, enabling you to use quiz data for targeted follow-ups and improved customer engagement.

    Before you begin, ensure you have:

    - An active ActiveCampaign account.
    - A quiz built on the RevenueHunt platform.

    !!! note

        The integration process mainly involves transferring raw data from the quiz to ActiveCampaign. Setting up detailed flows or custom events based on this data is managed within ActiveCampaign itself.


=== "Magento"


    Integrating your RevenueHunt Product Recommendation Quiz with ActiveCampaign allows for a seamless transition of valuable customer data directly into your email marketing campaigns and CRM management. 

    This guide will navigate you through the steps to link your quiz with ActiveCampaign, enabling you to use quiz data for targeted follow-ups and improved customer engagement.

    Before you begin, ensure you have:

    - An active ActiveCampaign account.
    - A quiz built on the RevenueHunt platform.

    !!! note

        The integration process mainly involves transferring raw data from the quiz to ActiveCampaign. Setting up detailed flows or custom events based on this data is managed within ActiveCampaign itself.


=== "BigCommerce"


    Integrating your RevenueHunt Product Recommendation Quiz with ActiveCampaign allows for a seamless transition of valuable customer data directly into your email marketing campaigns and CRM management. 

    This guide will navigate you through the steps to link your quiz with ActiveCampaign, enabling you to use quiz data for targeted follow-ups and improved customer engagement.

    Before you begin, ensure you have:

    - An active ActiveCampaign account.
    - A quiz built on the RevenueHunt platform.

    !!! note

        The integration process mainly involves transferring raw data from the quiz to ActiveCampaign. Setting up detailed flows or custom events based on this data is managed within ActiveCampaign itself.


=== "Standalone"


    Integrating your RevenueHunt Product Recommendation Quiz with ActiveCampaign allows for a seamless transition of valuable customer data directly into your email marketing campaigns and CRM management. 

    This guide will navigate you through the steps to link your quiz with ActiveCampaign, enabling you to use quiz data for targeted follow-ups and improved customer engagement.

    Before you begin, ensure you have:

    - An active ActiveCampaign account.
    - A quiz built on the RevenueHunt platform.

    !!! note

        The integration process mainly involves transferring raw data from the quiz to ActiveCampaign. Setting up detailed flows or custom events based on this data is managed within ActiveCampaign itself.


## Link Quiz to ActiveCampaign

=== "Shopify"

    It is **not yet possible** to link your Product Recommendation Quiz created in the new Built for Shopify version of the RevenueHunt app to ActiveCampaign.

    Check [Alternative Ways to Send Quiz Leads to ActiveCampaign](#alternative-ways-to-send-quiz-leads-to-activecampaign) to learn how you can send quiz leads to ActiveCampaign anyway.



=== "Shopify (Legacy)"

    To integrate your quiz with ActiveCampaign:

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Click on the [Connect](/reference/quiz-builder/connect-integrations/) tab located at the top of the screen to access the integration settings.
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

    2. Select the quiz icon and follow the provided setup instructions. During the setup process, you will be prompted to enter your `ActiveCampaign API Token`. This token is essential for linking the quiz data with your ActiveCampaign account and can be found in the [`Connect`](/reference/quiz-builder/connect-integrations/) > ActiveCampaign section of the app.

    !!! note

        Note that the Quiz is only responsible for sending the raw data, you will have to configure a flow or any other custom event you wish to make with the data within ActiveCampaign in itself, and any questions regarding this process should be asked to ActiveCampaign’s support team directly.

=== "WooCommerce"


    To integrate your quiz with ActiveCampaign:

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Click on the [Connect](/reference/quiz-builder/connect-integrations/) tab located at the top of the screen to access the integration settings.
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

    2. Select the quiz icon and follow the provided setup instructions. During the setup process, you will be prompted to enter your `ActiveCampaign API Token`. This token is essential for linking the quiz data with your ActiveCampaign account and can be found in the [`Connect`](/reference/quiz-builder/connect-integrations/) > ActiveCampaign section of the app.

    !!! note

        Note that the Quiz is only responsible for sending the raw data, you will have to configure a flow or any other custom event you wish to make with the data within ActiveCampaign in itself, and any questions regarding this process should be asked to ActiveCampaign’s support team directly.




=== "Magento"


    To integrate your quiz with ActiveCampaign:

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Click on the [Connect](/reference/quiz-builder/connect-integrations/) tab located at the top of the screen to access the integration settings.
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

    2. Select the quiz icon and follow the provided setup instructions. During the setup process, you will be prompted to enter your `ActiveCampaign API Token`. This token is essential for linking the quiz data with your ActiveCampaign account and can be found in the [`Connect`](/reference/quiz-builder/connect-integrations/) > ActiveCampaign section of the app.

    !!! note

        Note that the Quiz is only responsible for sending the raw data, you will have to configure a flow or any other custom event you wish to make with the data within ActiveCampaign in itself, and any questions regarding this process should be asked to ActiveCampaign’s support team directly.

=== "BigCommerce"


    To integrate your quiz with ActiveCampaign:

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Click on the [Connect](/reference/quiz-builder/connect-integrations/) tab located at the top of the screen to access the integration settings.
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

    2. Select the quiz icon and follow the provided setup instructions. During the setup process, you will be prompted to enter your `ActiveCampaign API Token`. This token is essential for linking the quiz data with your ActiveCampaign account and can be found in the [`Connect`](/reference/quiz-builder/connect-integrations/) > ActiveCampaign section of the app.

    !!! note

        Note that the Quiz is only responsible for sending the raw data, you will have to configure a flow or any other custom event you wish to make with the data within ActiveCampaign in itself, and any questions regarding this process should be asked to ActiveCampaign’s support team directly.

=== "Standalone"


    To integrate your quiz with ActiveCampaign:

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Click on the [Connect](/reference/quiz-builder/connect-integrations/) tab located at the top of the screen to access the integration settings.
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

    2. Select the quiz icon and follow the provided setup instructions. During the setup process, you will be prompted to enter your `ActiveCampaign API Token`. This token is essential for linking the quiz data with your ActiveCampaign account and can be found in the [`Connect`](/reference/quiz-builder/connect-integrations/) > ActiveCampaign section of the app.

    !!! note

        Note that the Quiz is only responsible for sending the raw data, you will have to configure a flow or any other custom event you wish to make with the data within ActiveCampaign in itself, and any questions regarding this process should be asked to ActiveCampaign’s support team directly.



## Alternative Ways to Send Quiz Leads to ActiveCampaign

=== "Shopify"

    Sometimes, you would like a bit more control over the data that is sent to ActiveCampaign. In that case there are a few alternatives you can use to send quiz leads to ActiveCampaign.

    - **Using Webhooks**: You can use our Webhooks integration to send quiz leads to ActiveCampaign. Just connect your quiz to Webhooks following [this guide](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks set up a redirection of selected data to ActiveCampaign.
    - **Manually adding the quiz leads to ActiveCampaign**: You can manually add the quiz leads to ActiveCampaign by uploading a CSV file generated from the quiz [responses](/reference/quiz-builder/metrics/#responses) section.



=== "Shopify (Legacy)"

    Sometimes, you would like a bit more control over the data that is sent to ActiveCampaign. In that case there are a few alternatives you can use to send quiz leads to ActiveCampaign.

    - **Using Zapier**: You can use out native Zapier integration to send quiz leads to ActiveCampaign. Just connect your quiz to Zapier following [this guide](/how-to-guides/send-leads-to-zapier/). Then, in Zapier set up a redirection of selected data to ActiveCampaign.
    - **Using Webhooks**: You can use our Webhooks integration to send quiz leads to ActiveCampaign. Just connect your quiz to Webhooks following [this guide](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks set up a redirection of selected data to ActiveCampaign.
    - **Manually adding the quiz leads to ActiveCampaign**: You can manually add the quiz leads to ActiveCampaign by uploading a CSV file generated from the quiz [metrics > responses](/reference/quiz-builder/metrics/#responses) section.
    
=== "WooCommerce"

    Sometimes, you would like a bit more control over the data that is sent to ActiveCampaign. In that case there are a few alternatives you can use to send quiz leads to ActiveCampaign.

    - **Using Zapier**: You can use out native Zapier integration to send quiz leads to ActiveCampaign. Just connect your quiz to Zapier following [this guide](/how-to-guides/send-leads-to-zapier/). Then, in Zapier set up a redirection of selected data to ActiveCampaign.
    - **Using Webhooks**: You can use our Webhooks integration to send quiz leads to ActiveCampaign. Just connect your quiz to Webhooks following [this guide](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks set up a redirection of selected data to ActiveCampaign.
    - **Manually adding the quiz leads to ActiveCampaign**: You can manually add the quiz leads to ActiveCampaign by uploading a CSV file generated from the quiz [metrics > responses](/reference/quiz-builder/metrics/#responses) section.


=== "Magento"


    Sometimes, you would like a bit more control over the data that is sent to ActiveCampaign. In that case there are a few alternatives you can use to send quiz leads to ActiveCampaign.

    - **Using Zapier**: You can use out native Zapier integration to send quiz leads to ActiveCampaign. Just connect your quiz to Zapier following [this guide](/how-to-guides/send-leads-to-zapier/). Then, in Zapier set up a redirection of selected data to ActiveCampaign.
    - **Using Webhooks**: You can use our Webhooks integration to send quiz leads to ActiveCampaign. Just connect your quiz to Webhooks following [this guide](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks set up a redirection of selected data to ActiveCampaign.
    - **Manually adding the quiz leads to ActiveCampaign**: You can manually add the quiz leads to ActiveCampaign by uploading a CSV file generated from the quiz [metrics > responses](/reference/quiz-builder/metrics/#responses) section.

=== "BigCommerce"


    Sometimes, you would like a bit more control over the data that is sent to ActiveCampaign. In that case there are a few alternatives you can use to send quiz leads to ActiveCampaign.

    - **Using Zapier**: You can use out native Zapier integration to send quiz leads to ActiveCampaign. Just connect your quiz to Zapier following [this guide](/how-to-guides/send-leads-to-zapier/). Then, in Zapier set up a redirection of selected data to ActiveCampaign.
    - **Using Webhooks**: You can use our Webhooks integration to send quiz leads to ActiveCampaign. Just connect your quiz to Webhooks following [this guide](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks set up a redirection of selected data to ActiveCampaign.
    - **Manually adding the quiz leads to ActiveCampaign**: You can manually add the quiz leads to ActiveCampaign by uploading a CSV file generated from the quiz [metrics > responses](/reference/quiz-builder/metrics/#responses) section.

=== "Standalone"


    Sometimes, you would like a bit more control over the data that is sent to ActiveCampaign. In that case there are a few alternatives you can use to send quiz leads to ActiveCampaign.

    - **Using Zapier**: You can use out native Zapier integration to send quiz leads to ActiveCampaign. Just connect your quiz to Zapier following [this guide](/how-to-guides/send-leads-to-zapier/). Then, in Zapier set up a redirection of selected data to ActiveCampaign.
    - **Using Webhooks**: You can use our Webhooks integration to send quiz leads to ActiveCampaign. Just connect your quiz to Webhooks following [this guide](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks set up a redirection of selected data to ActiveCampaign.
    - **Manually adding the quiz leads to ActiveCampaign**: You can manually add the quiz leads to ActiveCampaign by uploading a CSV file generated from the quiz [metrics > responses](/reference/quiz-builder/metrics/#responses) section.


## Adding custom information to the Contact profile

=== "Shopify"


    With the quiz integrated via [one of our alternative methods](/how-to-guides/send-leads-to-activecampaign/#alternative-ways-to-send-quiz-leads-to-activecampaign), you should be able to tag contact profiles with additional custom information derived from quiz results.

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

    !!! warning

        Since you are using one of our alternative methods to connect to ActiveCampaign, you will have full control over the data that is sent to ActiveCampaign. The data provided above are only a list of the most common fields that are sent to ActiveCampaign.

        For more information about using data in customer profile for ActiveCampaign, please refer to [ActiveCampaign documentation](https://help.activecampaign.com/hc/en-us/articles/115001374664-How-to-manage-custom-contact-fields).

    To set up a redirection of selected data to ActiveCampaign, you can use our Webhooks integration. Just connect your quiz to Webhooks following [this guide](/how-to-guides/send-leads-to-webhooks/). Then, check [ActiveCampaign's webhooks documentation](https://developers.activecampaign.com/page/webhooks) for more information on how to set up a redirection of selected data to ActiveCampaign.



=== "Shopify (Legacy)"

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


=== "WooCommerce"


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





=== "Magento"


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





=== "BigCommerce"


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





=== "Standalone"


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

=== "Shopify"


    To send automatic follow-up emails to quiz takers, you can set up an automation in ActiveCampaign.

    To automate email communications based on quiz participation:

    1. Within ActiveCampaign, go to the `Automations` menu and create a new automation.
    2. Set a trigger related to the custom properties you added to the contact profile via Webhooks.
    3. Following the trigger setup, design your email template. Incorporate personalization by adding `custom properties`, such as direct links to quiz responses, to your text blocks.
        ![how to activecampaign add custom properties](/images/how_to_activecampaign_add_custom_properties.gif)


=== "Shopify (Legacy)"

    To send automatic follow-up emails to quiz takers, you can set up an automation in ActiveCampaign.

    To automate email communications based on quiz participation:

    1. Within ActiveCampaign, go to the `Automations` menu and create a new automation.
    2. Set a trigger related to the Product Recommendation Quiz by selecting the appropriate quiz under `Apps`.
        ![how to activecampaign automation](/images/how_to_activecampaign_automation.gif)
    3. Following the trigger setup, design your email template. Incorporate personalization by adding `custom properties`, such as direct links to quiz responses, to your text blocks.
        ![how to activecampaign add custom properties](/images/how_to_activecampaign_add_custom_properties.gif)

=== "WooCommerce"


    To send automatic follow-up emails to quiz takers, you can set up an automation in ActiveCampaign.

    To automate email communications based on quiz participation:

    1. Within ActiveCampaign, go to the `Automations` menu and create a new automation.
    2. Set a trigger related to the Product Recommendation Quiz by selecting the appropriate quiz under `Apps`.
        ![how to activecampaign automation](/images/how_to_activecampaign_automation.gif)
    3. Following the trigger setup, design your email template. Incorporate personalization by adding `custom properties`, such as direct links to quiz responses, to your text blocks.
        ![how to activecampaign add custom properties](/images/how_to_activecampaign_add_custom_properties.gif)

=== "Magento"


    To send automatic follow-up emails to quiz takers, you can set up an automation in ActiveCampaign.

    To automate email communications based on quiz participation:

    1. Within ActiveCampaign, go to the `Automations` menu and create a new automation.
    2. Set a trigger related to the Product Recommendation Quiz by selecting the appropriate quiz under `Apps`.
        ![how to activecampaign automation](/images/how_to_activecampaign_automation.gif)
    3. Following the trigger setup, design your email template. Incorporate personalization by adding `custom properties`, such as direct links to quiz responses, to your text blocks.
        ![how to activecampaign add custom properties](/images/how_to_activecampaign_add_custom_properties.gif)

=== "BigCommerce"


    To send automatic follow-up emails to quiz takers, you can set up an automation in ActiveCampaign.

    To automate email communications based on quiz participation:

    1. Within ActiveCampaign, go to the `Automations` menu and create a new automation.
    2. Set a trigger related to the Product Recommendation Quiz by selecting the appropriate quiz under `Apps`.
        ![how to activecampaign automation](/images/how_to_activecampaign_automation.gif)
    3. Following the trigger setup, design your email template. Incorporate personalization by adding `custom properties`, such as direct links to quiz responses, to your text blocks.
        ![how to activecampaign add custom properties](/images/how_to_activecampaign_add_custom_properties.gif)

=== "Standalone"


    To send automatic follow-up emails to quiz takers, you can set up an automation in ActiveCampaign.

    To automate email communications based on quiz participation:

    1. Within ActiveCampaign, go to the `Automations` menu and create a new automation.
    2. Set a trigger related to the Product Recommendation Quiz by selecting the appropriate quiz under `Apps`.
        ![how to activecampaign automation](/images/how_to_activecampaign_automation.gif)
    3. Following the trigger setup, design your email template. Incorporate personalization by adding `custom properties`, such as direct links to quiz responses, to your text blocks.
        ![how to activecampaign add custom properties](/images/how_to_activecampaign_add_custom_properties.gif)

### Adding Recommended Products to Emails

=== "Shopify"


    Unfortunately, for now, the only information about the recommended products we were able to send to Activecampaign is the Recommended Product IDs. This is not enough information to display the whole list of recommended products.

    To show any products in an ActiveCampaign you may need to connect your ActiveCampaign to Shopify first. Then by adding a product block, you should be able to display products from specific collections. It could be possible to add multiple product blocks and have them shown or hidden based on the recommended product ID, however, this option has not been yet tested thoroughly.


=== "Shopify (Legacy)" 


    Unfortunately, for now, the only information about the recommended products we’re able to send to Activecampaign is the Recommended Product IDs. This is not enough information to display the whole list of recommended products.

    To show any products in an ActiveCampaign you may need to connect your ActiveCampaign to Shopify first. Then by adding a product block, you should be able to display products from specific collections. It could be possible to add multiple product blocks and have them shown or hidden based on the recommended product ID, however, this option has not been yet tested thoroughly.

=== "WooCommerce"



    Unfortunately, for now, the only information about the recommended products we’re able to send to Activecampaign is the Recommended Product IDs. This is not enough information to display the whole list of recommended products.

    To show any products in an ActiveCampaign you may need to connect your ActiveCampaign to WooCommerce first. Then by adding a product block, you should be able to display products from specific collections. It could be possible to add multiple product blocks and have them shown or hidden based on the recommended product ID, however, this option has not been yet tested thoroughly.

=== "Magento"



    Unfortunately, for now, the only information about the recommended products we’re able to send to Activecampaign is the Recommended Product IDs. This is not enough information to display the whole list of recommended products.

    To show any products in an ActiveCampaign you may need to connect your ActiveCampaign to Magento first. Then by adding a product block, you should be able to display products from specific collections. It could be possible to add multiple product blocks and have them shown or hidden based on the recommended product ID, however, this option has not been yet tested thoroughly.

=== "BigCommerce"



    Unfortunately, for now, the only information about the recommended products we’re able to send to Activecampaign is the Recommended Product IDs. This is not enough information to display the whole list of recommended products.

    To show any products in an ActiveCampaign you may need to connect your ActiveCampaign to BigCommerce first. Then by adding a product block, you should be able to display products from specific collections. It could be possible to add multiple product blocks and have them shown or hidden based on the recommended product ID, however, this option has not been yet tested thoroughly.

=== "Standalone"



    Unfortunately, for now, the only information about the recommended products we’re able to send to Activecampaign is the Recommended Product IDs. This is not enough information to display the whole list of recommended products.

    To show any products in an ActiveCampaign you may need to connect your ActiveCampaign to your Google Product Catalog first.


---
This article explaina how to connect the quiz to ActiveCampaign, send leads to ActiveCampaign and send follow-up emails with ActiveCampaign.



 



