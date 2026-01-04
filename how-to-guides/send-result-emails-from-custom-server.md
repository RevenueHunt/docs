---
icon: material/server
---

# How to Send Result Emails from Your Server Using SMTP

SMTP (Simple Mail Transfer Protocol) is a protocol used for sending emails across the internet. By connecting your Product Recommendation Quiz created with Revenuehunt app to an SMTP server, emails are sent from your account instead of revenuehunt, enhancing brand consistency and trust.

!!! tip "Connect your SMTP server to your quiz if:"
    - You're sending result emails to quiz respondents.
    - You're sending emails to a specific email address with notifications about each new quiz completion.

    Connecting your SMTP server to your quiz will allow you to send emails from your own email servers instead of Revenuehunt email servers and is a recommended practice.

## Setting Up SMTP Server Connection

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/i5eUNaSdET4?si=0WMwUXM-CTzcqHkU" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Access Settings**: Navigate to your quiz dashboard and open the [App Settings](/reference/app-settings/).
    2. **Locate SMTP Settings**: Select the [SMTP tab](/reference/app-settings/#smtp).
    3. **Enter SMTP Details**: Fill in your SMTP server details. 

        SMTP credentials vary by email provider. To find yours: 

        - Check your email provider's documentation by searching for 'SMTP'.
        - Refer to the Revenue Hunt documentation for links to common email providers.
        - Contact your email provider's support team for assistance.

        Fill in the following fields:

        ![how to set up smtp](/images/manual_shopifyV2_appsettings_smtp.png)

        - **SMTP From**: Enter the name (e.g., 'Revenue Hunt') and the provided email address.
        - **SMTP Server**: Copy the SMTP server address from your email provider's configuration (usually in the format `smtp.something`).
        - **SMTP Username**: Use the email address provided by your email provider.
        - **SMTP Password**: Copy the password provided by your email provider.
        - **SMTP Port**: Enter the correct SMTP port number from your email provider's configuration.
        - **SMTP Authentication**: Select 'Plain' for authentication method.
        - **Security Settings**: Adjust as necessary based on your service's requirements (e.g., uncheck options that are not needed).

        !!! note

            If you're not sure how to fill it in, try contacting your email service provider or check their documentation (search for "SMTP" on the documentation page).

    4. **Test and Activate**: After filling out the SMTP settings, click `Save` to test the connection. 
   
        If the connection fails, double-check all credentials, especially the SMTP port. 

        !!! tip
            If there are errors, please check the [troubleshooting guidelines](#troubleshooting-common-smtp-connection-issues).       
        
        Once successful, emails will be sent from your email server instead of Revenue Hunt's server.
    
        ![how to set up smtp success](/images/how_to_shopifyv2_smtp_success.png)




=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4887d06413b84d0098f2c08c49f8ead9?sid=6eac3370-9976-4ea2-81c3-85a0691669a5" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Access Settings**: Navigate to your quiz dashboard and open the [App Settings](/reference/app-settings/).
    2. **Locate SMTP Settings**: Select the [SMTP tab](/reference/app-settings/#smtp).

        ![how to set up smtp](/images/manual_appsettings_smtp.png)

    3. **Enter SMTP Details**: Fill in your SMTP server details. 

        Fill in the following fields:

        ![how to set up smtp filled in](/images/how_to_smtp_filledin.png)

        - **SMTP From Field**: Enter your email address in the format `name@revenuehunt.com`.
        - **SMTP Server**: Copy the host value from your email provider's configuration (usually in the format `smtp.something`).
        - **Username**: Use the username provided, usually your email address.
        - **SMTP Password**: Enter the password provided by your email provider. Note that some providers may require a special password for SMTP settings.
        - **SMTP Port**: Enter the port number (e.g., `587`) as specified by your email provider's configuration.

        SMTP settings vary by email provider. To find your settings:
        
        - Search your email provider's documentation for 'SMTP'.
        - Visit [Specific SMTP Configurations](#specific-smtp-configurations) for common email provider instructions.
        - Contact your email provider's support team for assistance.

        !!! note

            If you're not sure how to fill it in, try contacting your email service provider or check their documentation (search for "SMTP" on the documentation page).

    4. **Test and Activate**: Click on `test connection & activate`. If the test is succsefull, from now on all the emails will be sent from your server. 
    
        If there are errors, please check the [troubleshooting guidelines](#troubleshooting-common-smtp-connection-issues).

=== "WooCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4887d06413b84d0098f2c08c49f8ead9?sid=6eac3370-9976-4ea2-81c3-85a0691669a5" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Access Settings**: Navigate to your quiz dashboard and open the [App Settings](/reference/app-settings/).
    2. **Locate SMTP Settings**: Select the [SMTP tab](/reference/app-settings/#smtp).

        ![how to set up smtp](/images/manual_appsettings_smtp.png)

    3. **Enter SMTP Details**: Fill in your SMTP server details. 

        Fill in the following fields:

        ![how to set up smtp filled in](/images/how_to_smtp_filledin.png)

        - **SMTP From Field**: Enter your email address in the format `name@revenuehunt.com`.
        - **SMTP Server**: Copy the host value from your email provider's configuration (usually in the format `smtp.something`).
        - **Username**: Use the username provided, usually your email address.
        - **SMTP Password**: Enter the password provided by your email provider. Note that some providers may require a special password for SMTP settings.
        - **SMTP Port**: Enter the port number (e.g., `587`) as specified by your email provider's configuration.

        SMTP settings vary by email provider. To find your settings:
        
        - Search your email provider's documentation for 'SMTP'.
        - Visit [Specific SMTP Configurations](#specific-smtp-configurations) for common email provider instructions.
        - Contact your email provider's support team for assistance.

        !!! note

            If you're not sure how to fill it in, try contacting your email service provider or check their documentation (search for "SMTP" on the documentation page).

    4. **Test and Activate**: Click on `test connection & activate`. If the test is succsefull, from now on all the emails will be sent from your server. 
    
        If there are errors, please check the [troubleshooting guidelines](#troubleshooting-common-smtp-connection-issues).

=== "Magento"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4887d06413b84d0098f2c08c49f8ead9?sid=6eac3370-9976-4ea2-81c3-85a0691669a5" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Access Settings**: Navigate to your quiz dashboard and open the [App Settings](/reference/app-settings/).
    2. **Locate SMTP Settings**: Select the [SMTP tab](/reference/app-settings/#smtp).

        ![how to set up smtp](/images/manual_appsettings_smtp.png)

    3. **Enter SMTP Details**: Fill in your SMTP server details. 

        Fill in the following fields:

        ![how to set up smtp filled in](/images/how_to_smtp_filledin.png)

        - **SMTP From Field**: Enter your email address in the format `name@revenuehunt.com`.
        - **SMTP Server**: Copy the host value from your email provider's configuration (usually in the format `smtp.something`).
        - **Username**: Use the username provided, usually your email address.
        - **SMTP Password**: Enter the password provided by your email provider. Note that some providers may require a special password for SMTP settings.
        - **SMTP Port**: Enter the port number (e.g., `587`) as specified by your email provider's configuration.

        SMTP settings vary by email provider. To find your settings:
        
        - Search your email provider's documentation for 'SMTP'.
        - Visit [Specific SMTP Configurations](#specific-smtp-configurations) for common email provider instructions.
        - Contact your email provider's support team for assistance.

        !!! note

            If you're not sure how to fill it in, try contacting your email service provider or check their documentation (search for "SMTP" on the documentation page).

    4. **Test and Activate**: Click on `test connection & activate`. If the test is succsefull, from now on all the emails will be sent from your server. 
    
        If there are errors, please check the [troubleshooting guidelines](#troubleshooting-common-smtp-connection-issues).

=== "BigCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4887d06413b84d0098f2c08c49f8ead9?sid=6eac3370-9976-4ea2-81c3-85a0691669a5" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Access Settings**: Navigate to your quiz dashboard and open the [App Settings](/reference/app-settings/).
    2. **Locate SMTP Settings**: Select the [SMTP tab](/reference/app-settings/#smtp).

        ![how to set up smtp](/images/manual_appsettings_smtp.png)

    3. **Enter SMTP Details**: Fill in your SMTP server details. 

        Fill in the following fields:

        ![how to set up smtp filled in](/images/how_to_smtp_filledin.png)

        - **SMTP From Field**: Enter your email address in the format `name@revenuehunt.com`.
        - **SMTP Server**: Copy the host value from your email provider's configuration (usually in the format `smtp.something`).
        - **Username**: Use the username provided, usually your email address.
        - **SMTP Password**: Enter the password provided by your email provider. Note that some providers may require a special password for SMTP settings.
        - **SMTP Port**: Enter the port number (e.g., `587`) as specified by your email provider's configuration.

        SMTP settings vary by email provider. To find your settings:
        
        - Search your email provider's documentation for 'SMTP'.
        - Visit [Specific SMTP Configurations](#specific-smtp-configurations) for common email provider instructions.
        - Contact your email provider's support team for assistance.

        !!! note

            If you're not sure how to fill it in, try contacting your email service provider or check their documentation (search for "SMTP" on the documentation page).

    4. **Test and Activate**: Click on `test connection & activate`. If the test is succsefull, from now on all the emails will be sent from your server. 
    
        If there are errors, please check the [troubleshooting guidelines](#troubleshooting-common-smtp-connection-issues).


=== "Standalone"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4887d06413b84d0098f2c08c49f8ead9?sid=6eac3370-9976-4ea2-81c3-85a0691669a5" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Access Settings**: Navigate to your quiz dashboard and open the [App Settings](/reference/app-settings/).
    2. **Locate SMTP Settings**: Select the [SMTP tab](/reference/app-settings/#smtp).

        ![how to set up smtp](/images/manual_appsettings_smtp.png)

    3. **Enter SMTP Details**: Fill in your SMTP server details. 

        Fill in the following fields:

        ![how to set up smtp filled in](/images/how_to_smtp_filledin.png)

        - **SMTP From Field**: Enter your email address in the format `name@revenuehunt.com`.
        - **SMTP Server**: Copy the host value from your email provider's configuration (usually in the format `smtp.something`).
        - **Username**: Use the username provided, usually your email address.
        - **SMTP Password**: Enter the password provided by your email provider. Note that some providers may require a special password for SMTP settings.
        - **SMTP Port**: Enter the port number (e.g., `587`) as specified by your email provider's configuration.

        SMTP settings vary by email provider. To find your settings:
        
        - Search your email provider's documentation for 'SMTP'.
        - Visit [Specific SMTP Configurations](#specific-smtp-configurations) for common email provider instructions.
        - Contact your email provider's support team for assistance.

        !!! note

            If you're not sure how to fill it in, try contacting your email service provider or check their documentation (search for "SMTP" on the documentation page).

    4. **Test and Activate**: Click on `test connection & activate`. If the test is succsefull, from now on all the emails will be sent from your server. 
    
        If there are errors, please check the [troubleshooting guidelines](#troubleshooting-common-smtp-connection-issues).




## Specific SMTP Configurations

### Outlook Office 365 Users

To find credentials to fill in please check [this Microsoft documentation](https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/how-to-set-up-a-multifunction-device-or-application-to-send-email-using-microsoft-365-or-office-365).

For Office 365 SMTP, whitelist IP `3.14.55.225` to allow email sending.

- **Whitelisting Steps**:
    - Sign into Office 365, select `Admin`, then `Exchange` under `Admin Centers`.
    - In `Protection`, choose `Connection Filter` and edit with the pencil icon.
    - Add IP `3.14.55.225` to the `IP Allow List` and enable the `Enable Safe List`.

### Google Workspace Users


To find credentials to fill in please check [this Google documentation](https://support.google.com/a/answer/176600?hl=en).

![how to set up smtp google](/images/how_to_smtp_googleworkspaceinstructions.png)

- **Enable 2-Step Verification** (2FA): Required for SMTP connections.
    - [Enable 2FA](https://support.google.com/accounts/answer/185839)
- **Generate App Password** for SMTP:
    - Navigate to [App Passwords](https://myaccount.google.com/apppasswords).
    - Select `Mail` and `Other`, generate a password for use in SMTP settings.

## Troubleshooting: Common SMTP Connection Issues

- **Test Credentails with Thrid Party Tool**: Utilize third-party tools like [GMass SMTP Test](https://www.gmass.co/smtp-test) for SMTP settings verification. If the credentials work there, they will also work in our app. Should you encounter issues, consult with your developer or SMTP service provider.
- **SMTP Settings Not Working**: Ensure correctness with third-party tools. If issues persist, verify with your SMTP provider.
- **Office 365 Email Blocking**: Contact support to whitelist IP `3.14.55.225` if emails are not sending.
- **Google Workspace SMTP Failure**: Check if 2FA is enabled and correct app password is used. SMTP port 587 or 465 should work; if not, retry or check Google's support for updates.


---
This article explains how to add your email provider's SMTP server to your quiz and send result emails from your server. For further assistance with SMTP, consult the documentation of your email service provider or contact their support team.
