# How to Send Leads to Omnisend

Apart from giving your customers a personalized product recommendation, you can connect Product Recommendation Quiz to your Omnisend account so that the quiz results are sent automatically to your mailing list. This way you can segment them based on their responses and follow up with targeted campaigns.

<div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/763403d8f6e74461875845e68fe39e12?sid=2103a65c-be3d-4efd-80d8-a01173a4a30b" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

## Link Quiz to Omnisend

1. **Generate Omnisend API Key**: First, you'll have to [generate a new API Key in Omnisend](https://app.omnisend.com/integrations/api-keys). To do that,visit the `API section` in your Omnisend account and select the option `This API key will only allow adding new subscribers`. Copy the API Key.

    ![how to send leads to omnisend api key generate](/images/how_to_send_leads_to_omnisend_api_key_generate.png)

    !!! tip

        It's advisable to label your API key with a recognizable name like `revenuehunt` or `shopquiz` for easy identification later. 

2. Access the [Quiz Builder](/reference/quiz-builder/) and navigate to the [Connect/Integrations](/reference/quiz-builder/connect-integrations/) tab.
2. Scroll to the Omnisend section and click on the `Connect` button to initiate the connection process.
3. In the popup/field that appears, you'll need to enter your `Omnisend API Key` into the input field, then click `save`.
4. Update the preview/live quiz with the top-right `Publish/Save` button to save the connection. 

Following these steps ensures that every time a customer completes your quiz, their contact details, quiz responses, and product recommendations are automatically sent to your Omnisend account. 

We send all the responses to the quiz and the recommended products along with the contact information to the customer’s Omnisend profile. This information will appear in the customer’s profile as `custom properties`.

=== "Shopify"

    ![how to omnisend custom properties](/images/how_to_omnisend_custom_properties.gif)

=== "Shopify V2"

    ![how to omnisend custom properties](/images/how_to_shopifyv2_omnisend_custom_properties.gif)

=== "WooCommerce"

    ![how to omnisend custom properties](/images/how_to_omnisend_custom_properties.gif)

=== "Magento"

    ![how to omnisend custom properties](/images/how_to_omnisend_custom_properties.gif)

=== "BigCommerce"

    ![how to omnisend custom properties](/images/how_to_omnisend_custom_properties.gif)

=== "Standalone"

    ![how to omnisend custom properties](/images/how_to_omnisend_custom_properties.gif)

If you need to add any additional information to the email template, your developer can do so by pulling the appropriate custom properties from the user profile.
 
## Send Follow-up Emails with Omnisend

It’s possible to send the product recommendations via Omnisend, although this is not something that’s a one-click install. It should be built by someone with technical knowledge and experience in Omnisend. Below you’ll find some basic instructions that can be forwarded to a developer.

!!! note

    Once the quiz is connected to Omnisend (and the data is sent there), it’s out of our app’s scope, and any particular questions on how to set up the flows and how to build the email templates should be directed to Omnisend.

1. **Connect Your Quiz to Omnisend**: Refer to the instructions provided [here](#link-quiz-to-omnisend) to ensure your quiz is correctly connected to Omnisend.
2. **Create a Segment for Quiz Participants**: In Omnisend, create a segment specifically for users who have completed the quiz. This can be done by filtering for a `custom property` that only quiz participants will have, such as `permalink_quiz_id`.
    ![how to omnisend segment](/images/how_to_omnisend_segment.gif)
3. **Set Up an Automated Workflow**: Develop an automation workflow in Omnisend that triggers when someone is added to the newly created segment of quiz participants. This step involves configuring Omnisend to automatically start the email campaign sequence for users in this segment.
    ![how to omnisend flow](/images/how_to_omnisend_flow.gif)
4. **Customize the Email Template**: Customizing the email template to include quiz results and product recommendations requires HTML, CSS, and [Django templating](https://docs.djangoproject.com/en/1.8/ref/templates/builtins/) knowledge. Use Omnisend’s existing email templates as a base and modify them to incorporate the quiz data as custom properties. Ensure the template aligns with your brand’s style guide.

=== "Shopify"

    Here are some email templates that you can use as a reference:

    - [Basic Slots Template (4-Step Skincare Routine)](https://docs.google.com/document/d/1wy-_nb0nGyU0_NsWB6YZMiXbXiA2sMyrGu6ks7TqzjQ/edit?usp=sharing)
    - [Advanced Slots Template (Morning & Night Routine)](https://docs.google.com/document/d/1RIXL2zF0ErGbUX5IwCRXjnr8bNV3wXuZQuuy3NmbL_I/edit?usp=sharing)
    - [Products List Template (Coffee Recommendations)](https://docs.google.com/document/d/175YmJpZ_iTahGFip46MGb6fcn5cupNsCEuZFxMnFCAg/edit?usp=sharing)

    Bear in mind that the templates won’t work by just copy/pasting. These templates were created for our demo quiz. Your developer will have to modify the `custom properties` in these templates to match the ones that are passed from the quiz to your Omnisend account. The `quiz ID` is different, so are other property names. After the changes are made, your developer can insert the code as a `custom HTML block` on the Omnisend email template.

=== "Shopify V2"

    In the [Integrations](/reference/quiz-builder/connect-integrations/) section, under `Omnisend`, you can find the `omnisend template`. 
    
    ![how to shopifyv2 omnisend template](/images/how_to_shopifyv2_omnisend_template.png)
    
    Click on the button to receive and copy an HTML email template specifically tailored for the quiz.
    
    ![how to shopifyv2 omnisend template copy](/images/how_to_shopifyv2_omnisend_template_copy.png)

    You can use this template as a reference to create your own.

=== "WooCommerce"

    Here are some email templates that you can use as a reference:

    - [Basic Slots Template (4-Step Skincare Routine)](https://docs.google.com/document/d/1wy-_nb0nGyU0_NsWB6YZMiXbXiA2sMyrGu6ks7TqzjQ/edit?usp=sharing)
    - [Advanced Slots Template (Morning & Night Routine)](https://docs.google.com/document/d/1RIXL2zF0ErGbUX5IwCRXjnr8bNV3wXuZQuuy3NmbL_I/edit?usp=sharing)
    - [Products List Template (Coffee Recommendations)](https://docs.google.com/document/d/175YmJpZ_iTahGFip46MGb6fcn5cupNsCEuZFxMnFCAg/edit?usp=sharing)

    Bear in mind that the templates won’t work by just copy/pasting. These templates were created for our demo quiz. Your developer will have to modify the `custom properties` in these templates to match the ones that are passed from the quiz to your Omnisend account. The `quiz ID` is different, so are other property names. After the changes are made, your developer can insert the code as a `custom HTML block` on the Omnisend email template.

=== "Magento"

    Here are some email templates that you can use as a reference:

    - [Basic Slots Template (4-Step Skincare Routine)](https://docs.google.com/document/d/1wy-_nb0nGyU0_NsWB6YZMiXbXiA2sMyrGu6ks7TqzjQ/edit?usp=sharing)
    - [Advanced Slots Template (Morning & Night Routine)](https://docs.google.com/document/d/1RIXL2zF0ErGbUX5IwCRXjnr8bNV3wXuZQuuy3NmbL_I/edit?usp=sharing)
    - [Products List Template (Coffee Recommendations)](https://docs.google.com/document/d/175YmJpZ_iTahGFip46MGb6fcn5cupNsCEuZFxMnFCAg/edit?usp=sharing)

    Bear in mind that the templates won’t work by just copy/pasting. These templates were created for our demo quiz. Your developer will have to modify the `custom properties` in these templates to match the ones that are passed from the quiz to your Omnisend account. The `quiz ID` is different, so are other property names. After the changes are made, your developer can insert the code as a `custom HTML block` on the Omnisend email template.     


=== "BigCommerce"

    Here are some email templates that you can use as a reference:

    - [Basic Slots Template (4-Step Skincare Routine)](https://docs.google.com/document/d/1wy-_nb0nGyU0_NsWB6YZMiXbXiA2sMyrGu6ks7TqzjQ/edit?usp=sharing)
    - [Advanced Slots Template (Morning & Night Routine)](https://docs.google.com/document/d/1RIXL2zF0ErGbUX5IwCRXjnr8bNV3wXuZQuuy3NmbL_I/edit?usp=sharing)
    - [Products List Template (Coffee Recommendations)](https://docs.google.com/document/d/175YmJpZ_iTahGFip46MGb6fcn5cupNsCEuZFxMnFCAg/edit?usp=sharing)

    Bear in mind that the templates won’t work by just copy/pasting. These templates were created for our demo quiz. Your developer will have to modify the `custom properties` in these templates to match the ones that are passed from the quiz to your Omnisend account. The `quiz ID` is different, so are other property names. After the changes are made, your developer can insert the code as a `custom HTML block` on the Omnisend email template.

=== "Standalone"

    Here are some email templates that you can use as a reference:

    - [Basic Slots Template (4-Step Skincare Routine)](https://docs.google.com/document/d/1wy-_nb0nGyU0_NsWB6YZMiXbXiA2sMyrGu6ks7TqzjQ/edit?usp=sharing)
    - [Advanced Slots Template (Morning & Night Routine)](https://docs.google.com/document/d/1RIXL2zF0ErGbUX5IwCRXjnr8bNV3wXuZQuuy3NmbL_I/edit?usp=sharing)
    - [Products List Template (Coffee Recommendations)](https://docs.google.com/document/d/175YmJpZ_iTahGFip46MGb6fcn5cupNsCEuZFxMnFCAg/edit?usp=sharing)

    Bear in mind that the templates won’t work by just copy/pasting. These templates were created for our demo quiz. Your developer will have to modify the `custom properties` in these templates to match the ones that are passed from the quiz to your Omnisend account. The `quiz ID` is different, so are other property names. After the changes are made, your developer can insert the code as a `custom HTML block` on the Omnisend email template.

## Use Quiz Data In Omnisend Email Templates

You can use the quiz data in your Omnisend email templates by using the `custom properties` that are passed from the quiz to your Omnisend account.

=== "Shopify"

    ![how to omnisend custom properties](/images/how_to_omnisend_custom_properties.gif)

=== "Shopify V2"

    ![how to omnisend custom properties](/images/how_to_shopifyv2_omnisend_custom_properties.gif)

=== "WooCommerce"

    ![how to omnisend custom properties](/images/how_to_omnisend_custom_properties.gif)

=== "Magento"

    ![how to omnisend custom properties](/images/how_to_omnisend_custom_properties.gif)

=== "BigCommerce"

    ![how to omnisend custom properties](/images/how_to_omnisend_custom_properties.gif)

=== "Standalone"

    ![how to omnisend custom properties](/images/how_to_omnisend_custom_properties.gif)

If you need to add any additional information to the email template, your developer can do so by pulling the appropriate custom properties from the user profile.

### Display a Link to the Quiz Results in an email


=== "Shopify"

    Use the `permalink_koHP8VA` in your email template. This property already contains a full url to the quiz results page.

    !!! example

        `<a href="{{ contact.custom.permalink_koHP8VA }}">View your quiz results</a>`


=== "Shopify V2"

    Use the `quiz_QUIZID_response_id` to create a link to the quiz results page. Just add `#response-{{ person|lookup:'quiz_QUIZID_response_id' }}` to the end of your results page href attribute in any link or URL. 


    !!! example

        `<a href="https://yourwebsite.com/#response-{{ contact.custom.quiz_lBJ9bk_response_id }}">View your quiz results</a>

        where `lBJ9bk` is the quiz ID and

        - `{{ contact.custom.quiz_lBJ9bk_response_id }}` fetches the dynamic response ID (e.g., eVgV0Y).

=== "WooCommerce"

    Use the `permalink_koHP8VA` in your email template. This property already contains a full url to the quiz results page.

    !!! example

        `<a href="{{ contact.custom.permalink_koHP8VA }}">View your quiz results</a>`

=== "Magento"

    Use the `permalink_koHP8VA` in your email template. This property already contains a full url to the quiz results page.

    !!! example

        `<a href="{{ contact.custom.permalink_koHP8VA }}">View your quiz results</a>`

=== "BigCommerce"   

    Use the `permalink_koHP8VA` in your email template. This property already contains a full url to the quiz results page.

    !!! example

        `<a href="{{ contact.custom.permalink_koHP8VA }}">View your quiz results</a>`

=== "Standalone"

    Use the `permalink_koHP8VA` in your email template. This property already contains a full url to the quiz results page.

    !!! example

        `<a href="{{ contact.custom.permalink_koHP8VA }}">View your quiz results</a>`




## Customer Tags in Omnisend

Note that while customer profiles are updated with new quiz takes—including answers and product recommendations—Omnisend does not automatically remove unselected tags from previous sessions. A `tags_quizID` property is used to track the latest customer tags, which can be utilized to create segmented audiences for targeted marketing efforts.

---
By following this article, you can set up your post-quiz email flow with Omnisend.
