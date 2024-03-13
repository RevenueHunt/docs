# Setting Up Email Notifications for Product Recommendation Quizzes

Email notifications enhance customer engagement by following up with participants of your Product Recommendation Quiz. This guide covers setting up notifications for both quiz administrators and respondents.

## Prerequisites
- Access to the quiz dashboard.
- An active quiz with an email question to collect respondent details.

## Configuring Notifications

### To Quiz Administrators (Self)

1. **Activate Notifications**: Navigate to `Notifications > TO SELF` in your quiz dashboard. Here, you can opt to receive an email for each quiz completion and/or when someone proceeds to the cart or checkout.

### To Respondents

1. **Setting Up Respondent Emails**: Go to `Notifications > TO RESPONDENT` to configure the email your customers will receive. This feature is crucial for engaging customers who haven't completed their purchase.

2. **Customizing Emails**: You can personalize the email subject and content. Use `@` to include quiz responses dynamically and offer discounts or coupon codes to encourage checkout.

## Advanced Email Customization

### Custom HTML Emails

1. **Enable HTML Messages**: In `Notifications > To Respondent`, switch to the advanced HTML message mode to access a code editor for your email template.

2. **HTML Email Tips**: Remember to use inline styles and that JavaScript won't be executed by email clients.

### Utilizing Handlebars for Personalization

- **Metadata Use**: Incorporate quiz response metadata like `{{first_name}}` to personalize emails.
  
- **Listing Recommended Products**: Use Handlebars to loop through and display recommended products or customize content based on quiz outcomes.

3. Examples and Templates

- **Morning and Night Routine**: Separate recommendations for morning and night routines using specific block IDs.

- **Email Templates**: Access ready-made templates for advanced slots or product lists by navigating to the Notifications section and selecting the appropriate template for your needs.

### Integrating SMTP for Personalized Emails

SMTP (Simple Mail Transfer Protocol) integration ensures emails are sent from your domain, enhancing trust and deliverability.

1. **SMTP Configuration**: In your quiz dashboard, navigate to `Settings` and select the `SMTP` tab. Enter your SMTP server details and test the connection.

2. **Testing SMTP Settings**: Use tools like [smtper.net](https://www.smtper.net/) or [GMass SMTP Test](https://www.gmass.co/smtp-test) to ensure settings are correct. If issues arise, consult your developer or SMTP provider.

**Special Considerations**

- **Office 365 Users**: If using Office 365's SMTP, you may need to whitelist our server IP `3.14.55.225` in your Office 365 settings.
  
- **Google Workspace Users**: For Gmail-based SMTP, enable 2-Step Verification and generate an app-specific password for SMTP authentication.

## Integrating Quiz Results with Your CRM for Email Automation

You can automate the process of sending quiz result emails using your own CRM platform. Connect your quiz to one of our available integrations, and the quiz data will be transmitted to your CRM as soon as the customer completes the quiz and reaches the results page. This allows you to set up your own email sequences directly within your CRM. For guidance on connecting the quiz to our integrations, refer to the documentation provided for each integration.

Properly set up email notifications not only keep you informed about quiz participation but also significantly enhance the post-quiz engagement with respondents. By leveraging SMTP integration and advanced customization options, you can create a seamless and personalized follow-up experience for your customers.
