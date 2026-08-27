---
icon: material/server
description: "Learn how to send RevenueHunt result emails from your own SMTP server instead of defaults."
---

# How to Send Result Emails from Your Server Using SMTP

SMTP, or Simple Mail Transfer Protocol, is the protocol that carries email across the internet. Connect your quiz to your own SMTP server and the result emails leave from your address rather than RevenueHunt, so they carry your branding.

!!! tip "Which emails this affects"

    Connecting an SMTP server changes where both kinds of quiz email come from:

    - The result email your customer receives.
    - The notification you receive on each quiz completion.

## Setting up SMTP server connection

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/i5eUNaSdET4?si=0WMwUXM-CTzcqHkU" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open the app settings**: go to your quiz dashboard and open [App settings](/reference/app-settings/).
    2. **Open the SMTP tab**: select the [SMTP tab](/reference/app-settings/#smtp).
    3. **Enter your SMTP details**: fill in your SMTP server details.

        SMTP credentials differ by email provider. To find yours:

        - Search your email provider's documentation for `SMTP`.
        - See [Specific SMTP configurations](#specific-smtp-configurations) for the common email providers.
        - Contact your email provider's support team for assistance.

        Fill in the following fields:

        ![how to set up smtp](/images/manual_shopifyV2_appsettings_smtp.png)

        - **SMTP From**: enter your sender name, such as your store name, and the email address your provider gave you.
        - **SMTP Server**: copy the server address from your provider's configuration. It usually looks like `smtp.something`.
        - **SMTP Username**: the email address your provider gave you.
        - **SMTP Password**: the password your provider gave you.
        - **SMTP Port**: the port number from your provider's configuration.
        - **SMTP Authentication**: select `Plain`.
        - **Security Settings**: adjust these to your provider's requirements. Uncheck anything it does not need.

        !!! note

            If you are unsure what to enter, search your email provider's documentation for `SMTP`, or ask their support team.

    4. **Test and activate**: click `Save` to test the connection.

        If the connection fails, check every credential again, the SMTP port first.

        !!! tip
            If there are errors, please check the [troubleshooting guidelines](#troubleshooting-common-smtp-connection-issues).

        From then on, emails leave your own server rather than the RevenueHunt one.

        ![how to set up smtp success](/images/how_to_shopifyv2_smtp_success.png)




=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4887d06413b84d0098f2c08c49f8ead9?sid=6eac3370-9976-4ea2-81c3-85a0691669a5" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open the app settings**: go to your quiz dashboard and open [App Settings](/reference/app-settings/).
    2. **Open the SMTP tab**: select the [SMTP tab](/reference/app-settings/#smtp).

        ![how to set up smtp](/images/manual_appsettings_smtp.png)

    3. **Enter your SMTP details**: fill in your SMTP server details.

        Fill in the following fields:

        ![how to set up smtp filled in](/images/how_to_smtp_filledin.png)

        - **SMTP From Field**: Enter your email address in the format `name@revenuehunt.com`.
        - **SMTP Server**: Copy the host value from your email provider's configuration (usually in the format `smtp.something`).
        - **Username**: Use the username provided, usually your email address.
        - **SMTP Password**: Enter the password provided by your email provider. Note that some providers may require a special password for SMTP settings.
        - **SMTP Port**: Enter the port number (e.g., `587`) as specified by your email provider's configuration.

        SMTP settings vary by email provider. To find your settings:

        - Search your email provider's documentation for `SMTP`.
        - Visit [Specific SMTP Configurations](#specific-smtp-configurations) for common email provider instructions.
        - Contact your email provider's support team for assistance.

        !!! note

            If you are unsure what to enter, search your email provider's documentation for `SMTP`, or ask their support team.

    4. **Test and activate**: click `test connection & activate`. If the test passes, your emails leave from your own server from then on.

        If there are errors, please check the [troubleshooting guidelines](#troubleshooting-common-smtp-connection-issues).

=== "WooCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4887d06413b84d0098f2c08c49f8ead9?sid=6eac3370-9976-4ea2-81c3-85a0691669a5" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open the app settings**: go to your quiz dashboard and open [App Settings](/reference/app-settings/).
    2. **Open the SMTP tab**: select the [SMTP tab](/reference/app-settings/#smtp).

        ![how to set up smtp](/images/manual_appsettings_smtp.png)

    3. **Enter your SMTP details**: fill in your SMTP server details.

        Fill in the following fields:

        ![how to set up smtp filled in](/images/how_to_smtp_filledin.png)

        - **SMTP From Field**: Enter your email address in the format `name@revenuehunt.com`.
        - **SMTP Server**: Copy the host value from your email provider's configuration (usually in the format `smtp.something`).
        - **Username**: Use the username provided, usually your email address.
        - **SMTP Password**: Enter the password provided by your email provider. Note that some providers may require a special password for SMTP settings.
        - **SMTP Port**: Enter the port number (e.g., `587`) as specified by your email provider's configuration.

        SMTP settings vary by email provider. To find your settings:

        - Search your email provider's documentation for `SMTP`.
        - Visit [Specific SMTP Configurations](#specific-smtp-configurations) for common email provider instructions.
        - Contact your email provider's support team for assistance.

        !!! note

            If you are unsure what to enter, search your email provider's documentation for `SMTP`, or ask their support team.

    4. **Test and activate**: click `test connection & activate`. If the test passes, your emails leave from your own server from then on.

        If there are errors, please check the [troubleshooting guidelines](#troubleshooting-common-smtp-connection-issues).

=== "Magento"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4887d06413b84d0098f2c08c49f8ead9?sid=6eac3370-9976-4ea2-81c3-85a0691669a5" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open the app settings**: go to your quiz dashboard and open [App Settings](/reference/app-settings/).
    2. **Open the SMTP tab**: select the [SMTP tab](/reference/app-settings/#smtp).

        ![how to set up smtp](/images/manual_appsettings_smtp.png)

    3. **Enter your SMTP details**: fill in your SMTP server details.

        Fill in the following fields:

        ![how to set up smtp filled in](/images/how_to_smtp_filledin.png)

        - **SMTP From Field**: Enter your email address in the format `name@revenuehunt.com`.
        - **SMTP Server**: Copy the host value from your email provider's configuration (usually in the format `smtp.something`).
        - **Username**: Use the username provided, usually your email address.
        - **SMTP Password**: Enter the password provided by your email provider. Note that some providers may require a special password for SMTP settings.
        - **SMTP Port**: Enter the port number (e.g., `587`) as specified by your email provider's configuration.

        SMTP settings vary by email provider. To find your settings:

        - Search your email provider's documentation for `SMTP`.
        - Visit [Specific SMTP Configurations](#specific-smtp-configurations) for common email provider instructions.
        - Contact your email provider's support team for assistance.

        !!! note

            If you are unsure what to enter, search your email provider's documentation for `SMTP`, or ask their support team.

    4. **Test and activate**: click `test connection & activate`. If the test passes, your emails leave from your own server from then on.

        If there are errors, please check the [troubleshooting guidelines](#troubleshooting-common-smtp-connection-issues).

=== "BigCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4887d06413b84d0098f2c08c49f8ead9?sid=6eac3370-9976-4ea2-81c3-85a0691669a5" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open the app settings**: go to your quiz dashboard and open [App Settings](/reference/app-settings/).
    2. **Open the SMTP tab**: select the [SMTP tab](/reference/app-settings/#smtp).

        ![how to set up smtp](/images/manual_appsettings_smtp.png)

    3. **Enter your SMTP details**: fill in your SMTP server details.

        Fill in the following fields:

        ![how to set up smtp filled in](/images/how_to_smtp_filledin.png)

        - **SMTP From Field**: Enter your email address in the format `name@revenuehunt.com`.
        - **SMTP Server**: Copy the host value from your email provider's configuration (usually in the format `smtp.something`).
        - **Username**: Use the username provided, usually your email address.
        - **SMTP Password**: Enter the password provided by your email provider. Note that some providers may require a special password for SMTP settings.
        - **SMTP Port**: Enter the port number (e.g., `587`) as specified by your email provider's configuration.

        SMTP settings vary by email provider. To find your settings:

        - Search your email provider's documentation for `SMTP`.
        - Visit [Specific SMTP Configurations](#specific-smtp-configurations) for common email provider instructions.
        - Contact your email provider's support team for assistance.

        !!! note

            If you are unsure what to enter, search your email provider's documentation for `SMTP`, or ask their support team.

    4. **Test and activate**: click `test connection & activate`. If the test passes, your emails leave from your own server from then on.

        If there are errors, please check the [troubleshooting guidelines](#troubleshooting-common-smtp-connection-issues).


=== "Standalone"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4887d06413b84d0098f2c08c49f8ead9?sid=6eac3370-9976-4ea2-81c3-85a0691669a5" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open the app settings**: go to your quiz dashboard and open [App Settings](/reference/app-settings/).
    2. **Open the SMTP tab**: select the [SMTP tab](/reference/app-settings/#smtp).

        ![how to set up smtp](/images/manual_appsettings_smtp.png)

    3. **Enter your SMTP details**: fill in your SMTP server details.

        Fill in the following fields:

        ![how to set up smtp filled in](/images/how_to_smtp_filledin.png)

        - **SMTP From Field**: Enter your email address in the format `name@revenuehunt.com`.
        - **SMTP Server**: Copy the host value from your email provider's configuration (usually in the format `smtp.something`).
        - **Username**: Use the username provided, usually your email address.
        - **SMTP Password**: Enter the password provided by your email provider. Note that some providers may require a special password for SMTP settings.
        - **SMTP Port**: Enter the port number (e.g., `587`) as specified by your email provider's configuration.

        SMTP settings vary by email provider. To find your settings:

        - Search your email provider's documentation for `SMTP`.
        - Visit [Specific SMTP Configurations](#specific-smtp-configurations) for common email provider instructions.
        - Contact your email provider's support team for assistance.

        !!! note

            If you are unsure what to enter, search your email provider's documentation for `SMTP`, or ask their support team.

    4. **Test and activate**: click `test connection & activate`. If the test passes, your emails leave from your own server from then on.

        If there are errors, please check the [troubleshooting guidelines](#troubleshooting-common-smtp-connection-issues).




## Specific SMTP configurations

### Outlook office 365 users

To find credentials to fill in please check [this Microsoft documentation](https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/how-to-set-up-a-multifunction-device-or-application-to-send-email-using-microsoft-365-or-office-365).

For Office 365 SMTP, whitelist IP `3.14.55.225` to allow email sending.

- **Whitelisting Steps**:
    - Sign into Office 365, select `Admin`, then `Exchange` under `Admin Centers`.
    - In `Protection`, choose `Connection Filter` and edit with the pencil icon.
    - Add IP `3.14.55.225` to the `IP Allow List` and enable the `Enable Safe List`.

### Google workspace users


For the credentials to enter, see [this Google documentation](https://support.google.com/a/answer/176600?hl=en).

![how to set up smtp google](/images/how_to_smtp_googleworkspaceinstructions.png)

- **Enable 2-Step Verification** (2FA): Required for SMTP connections.
    - [Enable 2FA](https://support.google.com/accounts/answer/185839)
- **Generate App Password** for SMTP:
    - Navigate to [App Passwords](https://myaccount.google.com/apppasswords).
    - Select `Mail` and `Other`, then generate a password to use in the SMTP settings.

## Troubleshooting: common SMTP connection issues

- **Test your credentials with a third-party tool**: check your SMTP settings with a tool such as [GMass SMTP Test](https://www.gmass.co/smtp-test). Credentials that work there work in the RevenueHunt app too. If they fail, ask your developer or your SMTP provider.
- **SMTP settings not working**: check them with a third-party tool. If they still fail, confirm them with your SMTP provider.
- **Office 365 is blocking the email**: ask support to allow the IP `3.14.55.225`.
- **Google Workspace SMTP fails**: check that 2FA is on and that you used the app password. Port 587 or 465 should work. If neither does, try again or check Google's support pages.


---
This article explains how to add your email provider's SMTP server to your quiz, so result emails leave from your own server. For anything else about SMTP, see your provider's documentation or ask their support team.
