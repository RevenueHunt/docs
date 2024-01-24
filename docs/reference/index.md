# App Manual

Discover all the app's functions

This is an app manual. You'll find here an explanation on all buttons and functions of the app as well as the version history.

## Dashboard

On the dahsbaord you'll find all the quizzes that you create.

![dashboard](/images/manual_dashboard.png)

Shopify Side Menu

![dashboard side menu](/images/manual_sidemenu.png)

**Plans & Pricing** - Opens the [Plans & Pricing tab](#plans--pricing) (in-app URL (https://admin.revenuehunt.com/plans))

**App Settings** - Opens the [App Settings](#app-settings) menu.

![dashboard top menu](/images/manual_dashboard_topmenu.png)

**Help** - Opens the [Success Checklist](#success-checklist).

**New quiz** - Opens the [New quiz](#new-quiz) setup menu.


### Notifications

![dashboard notifications bar](/images/manual_notifications.png)

**view all** - Opens a list of archived notifications.

**"x"** - Archives a notification.

### MY QUIZZES

![dashboard tutorial quiz](/images/manual_tutorial_quiz.png)

**Tutorial Quiz (copy)** - A deafault quiz that explains how to use various app functions.

**0 leads** - Indicates the total number of quiz responses the quiz recieved.

**...** - Opens quiz managment options.

![dashboard quiz menu](/images/manual_dots_menu.png)

- **Edit** - Opens the [Quiz Builder]().

- **Connect** - Opens the [Connect tab]() within the Quiz Builder.

- **Share** - Opens the [Share tab]() within the Quiz Builder.

- **Metrics** - Opens the [Metrics tab]() within the Quiz Builder.

- **Preview** - Opens the Quiz Preview.

- **Publish** - Publish quiz changes to the Preview/Live Quiz. (If you have not yet added the quiz to your website as a link or an embed, clicking "Publish" will simply update the preview.)

- **Make a copy** - Create a copy of this quiz on the dashboard.

- **Export Responses as CSV** - Generate a CSV file with quiz responses from the last three months. Once clicked a link will appear on your dashbaord to download the CSV report. The link is valid for two hours.

- **Version History** - Open the [Version History tab]() in Quiz Builder > Quiz Settings.

- **Copy quiz ID: xxx** - Copy the quiz ID of the current quiz.

- **Set as Default Quiz** - Set as a default quiz to be displayed in the Shop App.

- **Delete** - Delete the quiz.

![dashboard quiz performance](/images/manual_dashboard_performance_overview.png)

**Quiz Performance Overview** - Highlights your quizzes performance during in the last 30 days 

**show overview** - Shows an overview of the quizzes metrics in the last 30 days.

**show breakdown** - Shows a detailed breakdown of the quizzes metrics in the last 30 days.

### Tips & Tricks

Displays useful tips and tricks for building a better quiz.

![dashboard tips](/images/manual_dashboard_tips.png)

**view all** - Opens archived tips.

### Success Checklist

To open the Success Checklist click on the any of the ❓❗✅ 🔄 icons.

![dashboard success checklist](/images/manual_succes_checklist.png)

❓ - Opens the Getting Started section of the Success Checklist.

❗ - Opens the To Do section of the Success Checklist. The number indicasted number of tasks to be completed.

✅ - Opens the To Do section of the Success Checklist. The number indicasted number of tasks completed.

🔄 - Opens the Sync section of the Success Checklist. 

![dashbaord success checklist sync app](/images/manual_success_checklist_sync.png)

**run manual sync** - Starts a full sync of your product catalog. The sync takes about 30 - 60 minutes to complete. If your store has more than 3,000 product variants, the sync can take longer. Please note that a full syunc of your catalog is done every 24 hours.

## New Quiz

![new quiz page](/images/manual_newquiz.png)

**start with an empty quiz** - Chose this is you want to start with an empty quiz. Once clicked, a popup will show asking you to name the quiz (the name can be changed later in [Quiz Settings]()).

![new quiz empty add name](/images/manual_addname.png)

**import quiz from another store** - Allows you to import a quiz from another store by inserting a copy quiz code. Check [How to Copy the Quiz from one store to another]() for detailed instructions.

**Select from one of our Quiz Templates**  - allows you to use one of pre-designed templates.

![new quiz add quiz from a template](/images/manual_newquiz_template.png)

**live preview** - Opens a live preview of the quiz templates.

**use this template** - Adds the template to your dahsbaord. 

## Quiz Builder

### Quiz Builder

### Link Collections

### Link Products

### Quiz Design

### Customer Tags

### Results Page

### Notifications

### Quiz Settings

### Preview

### Share

### Connect

### Publish

## Plans & Pricing

![plans & pricing page](/images/manual_plans_pricing.png)

**Your quizzes received *1,049* responses during the past 30 days** Indicates your quiz engagment in the last 30 days.

**view larger plans** - Opens a list of larger plans offered in the app.

**Pricing FAQs** - Opens the [Plans & Pricing FAQ]() page.

**check out this FAQs article** - Opens the [Plans & Pricing FAQ]() page.

**Get Basic/Pro** - Click to upgrade your plan to Basic/Pro. After clicking you'll be taken to the Shopify payment page to approve the subscription.

## App Settings

### General

![app settings general](/images/manual_appsettings_general.png)

**Your Profile**

**Shop email** - Your main store contact email. We automaticaly update this email each time we sync your store. You can change this email in your store settings (not the app).

**Your best email** -  Provide your best email (not your store email) for communication in case of issues.

**Send notifications to email** - Toggle the button to activate the notification emails to your best email. Once active we will send the notifications that appear on the dashaboard to your best email. For example, in case you go over your plan's limits, CSV export completions or connection issues.

**Data & GDPR**

**Anonymize quiz respones after 30 days** - Some jurisdictions require merchants to delete any Personal Identifiable Information (PII) they hold from customers upon request. To comply with GDPR legislation, you can choose to anonymize all of your quiz responses by automatically deleting any Personal Identifiable Information from the responses 30 days after being collected. To activate this setting toggle the icon.

### Catalogue

![app settings catalogue](/images/manual_appsettings_catalogue.png)

**Metafields Namespaces** - We will import the metafields information for the following namespaces. You will then be able to display this information in the products result page. In this section we'll display a list of metafield categories found in your store. You can toggle the button to activate the metrafielss and follow this article to show them in the quiz: [How to Add Product Metafileds]().

### SMTP

![app settings smtp](/images/manual_appsettings_smtp.png)

**SMTP Settings** 

SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol which enables third-party apps (e.g. Shop Quiz) to send emails through your email server.

When you connect the Shop Quiz app to your SMTP Server, the follow-up emails with the quiz results that are sent to your customers won’t be sent from our no-reply@prq.email email account, they’ll be sent from your email account. 

Check [How to Send Reuslt Emails from your own server]() for detailed instructions on how to set this up.

**Name to display(From):** - Set what name and email the customer will see when they recieve the email.

**SMTP Server** - Set your server URL.

**SMTP Username** - Set your SMTP Username.

**SMTP Password**  - Provide the paswsword associated with the username.

**SMTP Port** - Set the SMTP port (25, 465, 587 or 2525)
    
**test connection & activate** - Once you've provided all your credentials you can test if the connection to your SMTP server is succesful. If you see an error check your SMTP settings with the help of a third party tool such as[Gmass](https://www.gmass.co/smtp-test) or any other SMTP test site. If your settings work as intended there, they should work on our end, too. If you’re having issues, please get in touch with your developer / SMTP provider.

### Shop App (Beta)

![app settings shop app](/images/manual_appsettings_shopapp.png)

**Entry Point Settings**

**Activate Entry Point** - Toggle to activate a quiz in the Shop App.

**Quiz Dropdown** - Select from a list of quizzes which one should be featured in the Shop App.

**TITLE** - Type a title for your Shop App quiz.

**DESCRIPTION** - Provide a short description of the quiz.

**CTA TEXT** - Type what will be written on the button that opens the quiz.

**Quiz Image URL** - Provide a URL of an image you'd like to see featured on the Shop App quiz page.

**Entry Point Preview** - Shows a preview of how the quiz entry point will look like in your store's page in the Shop App.

![app settings shop app preview](/images/manual_appsettings_shopapp_preview.png)


## Version History 