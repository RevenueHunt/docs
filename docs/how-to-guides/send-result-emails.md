# Setting Up Email Notifications for Product Recommendation Quizzes

Email results notifications enhance customer engagement by following up with participants of your Shop Quiz. This guide covers setting up email results for both quiz respondents and administartors and well as sending resutls emails via an external CRM.

## Email Quiz Results via Shop Quiz app

Result emails will be sent directly from the Shop Quiz app to the email provided by the customer. Follow the step by step instructions below to active and edit the result emails send via the app.

1. **Add Email Question**: Before you set up your result emails, you need to make sure that the quiz has an email question. To add an email question go to the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/#quiz-builder_1).
2. **Activate Respondent Emails**: Go to `Notifications > TO RESPONDENT` and toggle the button to activate the emails.
3. **Edit REPLY-TO**: Choose what email the customers will be able to reply to once they recieve the resutls. Note: If you want to edit the FROM email you will have to connect your own SMTP sever to the quiz following [these instructions](https://docs.revenuehunt.com/how-to-guides/how-to-send-result-emails-from-custom-server/).
4. **Email TO**: If you have more than one email question in your quiz, choose an answer to which email question should be used to send the result emails. If you have only one email question, it will be selected by default.
5. **Email Subject**: Edit the title of the email that customers will receive. You can use `@` to recall information such as the customer name or the quiz name in the title field.
5. **Edit Email Content**: Configure the email your customers will receive. You can choose between a Basic (text) email format or Advanced (HTML) email format. You can switch between the two by clicking `switch to advanced HTML message` or `switch to basic text message` in the `Email Text Message` field.
    - **Basic text** email template is easy to use. Type the text that you want the customer to see in the `Email Text Message` field. You can personalize the email subject and content. You can add dynamic elements with `@`. Use `@` (Information Recalls) to recall quiz information in the email body. You can recall data such as customer name, email, phone number, quiz name, question responses, recommended products and more. Basic email template does not allow the display of images or color customization but offers maximum deliverability.
    - **Advanced HTML** email template requires the knowledge of HTML and [Handlebars helpers](https://github.com/helpers/handlebars-helpers) to be edited. Note that HTML emails are not rendered the same in different email clients and that you should add styles inline, not as classes. Also, note that you can’t add JavaScript code since it won’t be executed by email clients. Incorporate quiz response metadata like `{{first_name}}` to personalize emails. You can use Handlebars to loop through and display recommended products or customize content based on quiz outcomes. Read more about styling Advanced HTML Email temapltes [here](#advanced-html-email-templates).
6. **Publish the changes**: Remember to publish the changes with the top-right `Publish` button.

## Sending Result Emails with Your CRM

You can automate the process of sending quiz result emails using your own CRM platform. Connect your quiz to one of our [available integrations](https://revenuehunt.com/integrations/), and the quiz data will be transmitted to your CRM as soon as the customer completes the quiz and reaches the results page. This allows you to set up your own email sequences directly within your CRM. For guidance on connecting the quiz to our integrations, refer to the documentation provided for each integration.

## Activate Email Notifications To Admin

You can receive an email notification every time someone completes the quiz or proceeds to checkout. This allows the quiz admin/responsible to stay up to date with quiz engagments. 

1. **Open Notifications**: Navigate to `Notifications > TO SELF` in your quiz dashboard. 
2. **Activate Notifications**: Toggle the button to activate the emails. Here, you can opt to receive an email for each quiz completion and/or when someone proceeds to the cart or checkout.
3. **Publish the changes**: Remember to publish the changes with the top-right `Publish` button.


## Advanced HTML Email Templates

**Using Metadata**

Each quiz response has metadata which can be used in your emails to personalize them. You can see the metadata from the quiz response here:

The metadata from a quiz response can include various details that are useful for personalizing email communications.

For example:

- **Show Customer Name**: If you wish to display the respondent’s name, you can use the `{{first_name}}` handlebar in your code.
    ```html
    <p>Hello {{first_name}},</p>
    ```

    It should render as:

    ```
    Hello Alex,
    ```
    
- **Recommended Products in Metadata**: The most recommended products are listed within the metadata JSON under the `products` property.

**Usign Handlebars**

For more detailed guidance on using handlebars in your HTML email templates, refer to the following resources:

- Handlebars Builtin Helpers: [Handlebars Built-in Helpers](https://handlebarsjs.com/guide/builtin-helpers.html)
- GitHub Handlebars Helpers: [Handlebars Helpers on GitHub](https://github.com/helpers/handlebars-helpers)

The format for helpers in Notifications might slightly differ from those on GitHub. For instance, to truncate a product name to 7 characters, you should write:

```handlebars
{{truncate product.name 7}}
```

If you want to present specific metadata you should use a special property `{{#eq}} ... {{/eq}}`

- To target all slot blocks:

```handlebars
{{#eq block.type "SlotsBlock"}} ... {{/eq}}
```

- To target a specific block, for example, a block with the ID `A4TeY9`:

```handlebars
{{#eq block.id "A4TeY9"}} … {{/eq}}
```

Specific use cases:

- **List the Recommended Products**: If you want to loop through the most recommended products, you can do so like this:
    ```html
        {{#each products as | product |}}
    <div style="overflow:hidden; margin-bottom: 10px;">
    <img src="{{product.image_url}}" alt="{{product.name}}" width="48" height="48" style="float:left; margin-right: 10px;"/>
    <span style="height:48px;float:left">
    <a href="{{product.url}}" target="_blank">{{product.name}}</a>
    <br>{{product.price}} USD</span>
    </div>
    {{/each}}
    ```

- **List recommended products with Slot Titles**: If you want to list the most recommended product with Slot titles, you can do so like this:
    ```html
    {{#each blocks as |block|}}
    {{#eq block.type "SlotsBlock"}}
    {{#each block.slots as |slot|}}
    <b>{{slot.title}}</b><br>
    {{#each products as |product|}}
    <div style="overflow:hidden; margin-bottom: 10px;">
    <img src="{{product.image_url}}" alt="{{product.name}}" width="48" height="48" style="float:left; margin-right: 10px;"/>
    <span style="height:48px;float:left">
    <a href="{{product.url}}" target="_blank">{{product.name}}</a>
    <br>{{product.price}} USD</span>
    </div>
    {{/each}}
    {{/each}}
    {{/eq}}
    {{#eq block.type "ProductsBlock"}}
    {{#each block.products as |product|}}
    <div style="overflow:hidden; margin-bottom: 10px;">
    <img src="{{product.image_url}}" alt="{{product.name}}" width="48" height="48" style="float:left; margin-right: 10px;"/>
    <span style="height:48px;float:left">
    <a href="{{product.url}}" target="_blank">{{product.name}}</a>
    <br>{{product.price}} USD</span>
    </div>
    {{/each}}
    {{/eq}}
    {{/each}}
    ```

- **List recommended products separated by Slot Blocks**: If you want to recommend a Morning and Night slot routine separately you can use the following code. Make sure to change the block IDs (“A4TeY9” and “PPT2PG”) to the ones in your quiz.
    ```html
    <h3>Let’s start with your morning routine</h3>
    {{#each blocks as |block|}}
    {{#eq block.id "A4TeY9"}}
    {{#each block.slots as |slot|}}
    <b>{{slot.title}}</b><br>
    {{#each products as |product|}}
    <div style="overflow:hidden; margin-bottom: 10px;">
    <img src="{{product.image_url}}" alt="{{product.name}}" width="48" height="48" style="float:left; margin-right: 10px;"/>
    <span style="height:48px;float:left">
    <a href="{{product.url}}" target="_blank">{{product.name}}</a>
    <br>{{product.price}} USD</span>
    </div>
    {{/each}} 
    {{/each}}
    {{/eq}}
    {{/each}}
    <br>
    <h3>Finish the day with your night routine</h3>
    {{#each blocks as |block|}}
    {{#eq block.id "PPT2PG"}}
    {{#each block.slots as |slot|}}
    <b>{{slot.title}}</b><br>
    {{#each products as |product|}}
    <div style="overflow:hidden; margin-bottom: 10px;">
    <img src="{{product.image_url}}" alt="{{product.name}}" width="48" height="48" style="float:left; margin-right: 10px;"/>
    <span style="height:48px;float:left">
    <a href="{{product.url}}" target="_blank">{{product.name}}</a>
    <br>{{product.price}} USD</span>
    </div>
    {{/each}} 
    {{/each}}
    {{/eq}}
    {{/each}}
    ```