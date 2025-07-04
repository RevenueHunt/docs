---
icon: material/server
---

# How to Send Result Emails from Your Server Using SMTP

SMTP (Simple Mail Transfer Protocol) is a protocol used for sending emails across the internet. By connecting your Product Recommendation Quiz to an SMTP server, emails are sent from your account instead of revenuehunt, enhancing brand consistency and trust.

## Setting Up SMTP Server Connection

=== "Shopify"

    ![how to set up smtp](/images/manual_appsettings_smtp.png)

    1. **Access Settings**: Navigate to your quiz dashboard and open the [App Settings](/reference/app-settings/).
    2. **Locate SMTP Settings**: Select the [SMTP tab](/reference/app-settings/#smtp).
    3. **Enter SMTP Details**: Fill in your SMTP server details. 

        !!! note

            If you're not sure how to fill it in, try contacting your email service provider or check their documentation (search for "SMTP" on the documentation page).

    4. **Test and Activate**: Click on `test connection & activate`. If the test is succsefull, from now on all the emails will be sent from your server. If there are errors, please check the [troubleshooting guidelines](#troubleshooting-common-smtp-connection-issues)

=== "Shopify V2"

    ![how to set up smtp](/images/manual_appsettings_smtp.png)

    1. **Access Settings**: Navigate to your quiz dashboard and open the [App Settings](/reference/app-settings/).
    2. **Locate SMTP Settings**: Select the [SMTP tab](/reference/app-settings/#smtp).
    3. **Enter SMTP Details**: Fill in your SMTP server details. 

        !!! note

            If you're not sure how to fill it in, try contacting your email service provider or check their documentation (search for "SMTP" on the documentation page).

    4. **Test and Activate**: Click on `test connection & activate`. If the test is succsefull, from now on all the emails will be sent from your server. If there are errors, please check the [troubleshooting guidelines](#troubleshooting-common-smtp-connection-issues)

=== "WooCommerce"

    ![how to set up smtp](/images/manual_appsettings_smtp.png)

    1. **Access Settings**: Navigate to your quiz dashboard and open the [App Settings](/reference/app-settings/).
    2. **Locate SMTP Settings**: Select the [SMTP tab](/reference/app-settings/#smtp).
    3. **Enter SMTP Details**: Fill in your SMTP server details. 

        !!! note

            If you're not sure how to fill it in, try contacting your email service provider or check their documentation (search for "SMTP" on the documentation page).

    4. **Test and Activate**: Click on `test connection & activate`. If the test is succsefull, from now on all the emails will be sent from your server. If there are errors, please check the [troubleshooting guidelines](#troubleshooting-common-smtp-connection-issues)

=== "Magento"

    ![how to set up smtp](/images/manual_appsettings_smtp.png)

    1. **Access Settings**: Navigate to your quiz dashboard and open the [App Settings](/reference/app-settings/).
    2. **Locate SMTP Settings**: Select the [SMTP tab](/reference/app-settings/#smtp).
    3. **Enter SMTP Details**: Fill in your SMTP server details. 

        !!! note

            If you're not sure how to fill it in, try contacting your email service provider or check their documentation (search for "SMTP" on the documentation page).

    4. **Test and Activate**: Click on `test connection & activate`. If the test is succsefull, from now on all the emails will be sent from your server. If there are errors, please check the [troubleshooting guidelines](#troubleshooting-common-smtp-connection-issues)

=== "BigCommerce"

    ![how to set up smtp](/images/manual_appsettings_smtp.png)

    1. **Access Settings**: Navigate to your quiz dashboard and open the [App Settings](/reference/app-settings/).
    2. **Locate SMTP Settings**: Select the [SMTP tab](/reference/app-settings/#smtp).
    3. **Enter SMTP Details**: Fill in your SMTP server details. 

        !!! note

            If you're not sure how to fill it in, try contacting your email service provider or check their documentation (search for "SMTP" on the documentation page).

    4. **Test and Activate**: Click on `test connection & activate`. If the test is succsefull, from now on all the emails will be sent from your server. If there are errors, please check the [troubleshooting guidelines](#troubleshooting-common-smtp-connection-issues)

=== "Standalone"

    ![how to set up smtp](/images/manual_appsettings_smtp.png)

    1. **Access Settings**: Navigate to your quiz dashboard and open the [App Settings](/reference/app-settings/).
    2. **Locate SMTP Settings**: Select the [SMTP tab](/reference/app-settings/#smtp).
    3. **Enter SMTP Details**: Fill in your SMTP server details. 

        !!! note

            If you're not sure how to fill it in, try contacting your email service provider or check their documentation (search for "SMTP" on the documentation page).

    4. **Test and Activate**: Click on `test connection & activate`. If the test is succsefull, from now on all the emails will be sent from your server. If there are errors, please check the [troubleshooting guidelines](#troubleshooting-common-smtp-connection-issues)

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
For further assistance with SMTP, consult the documentation of your email service provider or contact their support team.
