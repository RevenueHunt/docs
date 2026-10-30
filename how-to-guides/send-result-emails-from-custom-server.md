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

    1. **Open [App settings](/reference/app-settings/) from the side menu.**
    2. **Open [`SMTP settings`](/reference/app-settings/#smtp).**
    3. **Fill in your SMTP details.**

        ![The SMTP settings in App settings](/images/manual_shopifyV2_appsettings_smtp.png)

        - `SMTP From`: the name and address the customer sees. Use the format `"Full Name" <name@company.com>`.
        - `SMTP Server`: the server address from your provider, such as `smtp.example.com`.
        - `SMTP Username`: usually the email address your provider gave you.
        - `SMTP Password`: the password for that username. Some providers issue a separate password for SMTP.
        - `SMTP Port`: the port your provider specifies, usually `25`, `465`, `587` or `2525`.
        - `SMTP Authentication`: pick your provider's method from the dropdown, usually `plain`.
        - `Encryption`: choose `STARTTLS` or `SSL/TLS`, whichever your provider asks for. STARTTLS usually runs on port 587, and SSL/TLS on port 465.

        Credentials differ by provider. Search your provider's documentation for `SMTP`, read [Specific SMTP configurations](#specific-smtp-configurations) below, or ask their support team.

    4. **Click `Test connection`.** The app sends a test email and reports `SMTP connection successful`, with the subject, the recipient and the timestamp.

        ![A successful SMTP connection test](/images/how_to_shopifyv2_smtp_success.png)

        If the test fails, check every credential again, the port first. See [Troubleshooting](#troubleshooting-common-smtp-connection-issues).

    5. **Tick `Enable sending emails using your own SMTP server`.** The checkbox stays greyed out until a test passes. From then on, both quiz emails leave your own server.




=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4887d06413b84d0098f2c08c49f8ead9?sid=6eac3370-9976-4ea2-81c3-85a0691669a5" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open the app settings**: go to your quiz dashboard and open [App Settings](/reference/app-settings/).
    2. **Open the SMTP tab**: select the [SMTP tab](/reference/app-settings/#smtp).

        ![how to set up smtp](/images/manual_appsettings_smtp.png)

    3. **Enter your SMTP details**: fill in your SMTP server details.

        Fill in the following fields:

        ![how to set up smtp filled in](/images/how_to_smtp_filledin.png)

        - `SMTP From`: the name and address the customer sees. Use the format `"Full Name" <name@company.com>`.
        - `SMTP Server`: the server address from your provider, such as `smtp.example.com`.
        - `SMTP Username`: usually the email address your provider gave you.
        - `SMTP Password`: the password for that username. Some providers issue a separate password for SMTP.
        - `SMTP Port`: the port your provider specifies, usually `25`, `465`, `587` or `2525`.

        Credentials differ by provider. Search your provider's documentation for `SMTP`, read [Specific SMTP configurations](#specific-smtp-configurations) below, or ask their support team.

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

        - `SMTP From`: the name and address the customer sees. Use the format `"Full Name" <name@company.com>`.
        - `SMTP Server`: the server address from your provider, such as `smtp.example.com`.
        - `SMTP Username`: usually the email address your provider gave you.
        - `SMTP Password`: the password for that username. Some providers issue a separate password for SMTP.
        - `SMTP Port`: the port your provider specifies, usually `25`, `465`, `587` or `2525`.

        Credentials differ by provider. Search your provider's documentation for `SMTP`, read [Specific SMTP configurations](#specific-smtp-configurations) below, or ask their support team.

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

        - `SMTP From`: the name and address the customer sees. Use the format `"Full Name" <name@company.com>`.
        - `SMTP Server`: the server address from your provider, such as `smtp.example.com`.
        - `SMTP Username`: usually the email address your provider gave you.
        - `SMTP Password`: the password for that username. Some providers issue a separate password for SMTP.
        - `SMTP Port`: the port your provider specifies, usually `25`, `465`, `587` or `2525`.

        Credentials differ by provider. Search your provider's documentation for `SMTP`, read [Specific SMTP configurations](#specific-smtp-configurations) below, or ask their support team.

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

        - `SMTP From`: the name and address the customer sees. Use the format `"Full Name" <name@company.com>`.
        - `SMTP Server`: the server address from your provider, such as `smtp.example.com`.
        - `SMTP Username`: usually the email address your provider gave you.
        - `SMTP Password`: the password for that username. Some providers issue a separate password for SMTP.
        - `SMTP Port`: the port your provider specifies, usually `25`, `465`, `587` or `2525`.

        Credentials differ by provider. Search your provider's documentation for `SMTP`, read [Specific SMTP configurations](#specific-smtp-configurations) below, or ask their support team.

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

        - `SMTP From`: the name and address the customer sees. Use the format `"Full Name" <name@company.com>`.
        - `SMTP Server`: the server address from your provider, such as `smtp.example.com`.
        - `SMTP Username`: usually the email address your provider gave you.
        - `SMTP Password`: the password for that username. Some providers issue a separate password for SMTP.
        - `SMTP Port`: the port your provider specifies, usually `25`, `465`, `587` or `2525`.

        Credentials differ by provider. Search your provider's documentation for `SMTP`, read [Specific SMTP configurations](#specific-smtp-configurations) below, or ask their support team.

    4. **Test and activate**: click `test connection & activate`. If the test passes, your emails leave from your own server from then on.

        If there are errors, please check the [troubleshooting guidelines](#troubleshooting-common-smtp-connection-issues).




## Specific SMTP configurations

### Outlook and Office 365

To find credentials to fill in please check [this Microsoft documentation](https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/how-to-set-up-a-multifunction-device-or-application-to-send-email-using-microsoft-365-or-office-365).

Office 365 blocks the app until you allow its IP address, `3.14.55.225`.

1. **Sign in to Office 365, select `Admin`, then `Exchange` under `Admin Centers`.**
2. **Open `Protection`, choose `Connection Filter`, and click the pencil icon to edit it.**
3. **Add `3.14.55.225` to the `IP Allow List`, then turn on `Enable Safe List`.**

### Google Workspace


For the credentials to enter, see [this Google documentation](https://support.google.com/a/answer/176600?hl=en).

![how to set up smtp google](/images/how_to_smtp_googleworkspaceinstructions.png)

1. **[Turn on 2-Step Verification](https://support.google.com/accounts/answer/185839).** Google requires it before it will issue an app password.
2. **Open [App Passwords](https://myaccount.google.com/apppasswords), select `Mail` and `Other`, and generate a password.**
3. **Use that password as your `SMTP Password`**, not your normal Google password.

## Troubleshooting: common SMTP connection issues

- **Test your credentials with a third-party tool**: check your SMTP settings with a tool such as [GMass SMTP Test](https://www.gmass.co/smtp-test). Credentials that work there work in the RevenueHunt app too. If they fail there, ask your developer or your SMTP provider.
- **Office 365 is blocking the email**: add `3.14.55.225` to the `IP Allow List`. See [Outlook and Office 365](#outlook-and-office-365).
- **Google Workspace SMTP fails**: check that 2FA is on and that you used the app password. Port 587 or 465 should work. If neither does, try again or check Google's support pages.


---
This article explains how to add your email provider's SMTP server to your quiz, so result emails leave from your own server. For anything else about SMTP, see your provider's documentation or ask their support team.
