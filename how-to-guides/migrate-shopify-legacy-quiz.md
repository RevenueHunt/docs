---
icon: material/transfer
---

# How to Migrate a Legacy Quiz to the 💎Built for Shopify App

If you have quizzes built in the original RevenueHunt app (Legacy), you can now import them directly into the `💎Built for Shopify` version of RevenueHunt app instead of rebuilding them from scratch. The migration tool copies your questions, results pages, logic, and design settings in one click.

!!! info "Shopify only"

    The **Migrate from Legacy App** option is currently available for Shopify stores only. Merchants on WooCommerce, Magento, BigCommerce, or Standalone can use the [Import Quiz](/how-to-guides/copy-the-quiz-from-one-store-to-another/) feature instead.

---

## Before You Begin

- You must have the `💎Built for Shopify` version of RevenueHunt app installed and active. If you haven't switched yet, follow the [Install App](/how-to-guides/install-app/) guide.
- Your legacy quizzes remain untouched — the migration creates a **copy** in the `💎Built for Shopify` app. Nothing is deleted from the legacy version.

---

## Step 1: Open the New Quiz Menu

1. Open the **RevenueHunt** app in your Shopify dashboard.
2. From the Dashboard, click the **Create new quiz** button.
3. In the dropdown menu that appears, select **Migrate from Legacy App**.

    ![Create new quiz dropdown showing Migrate from Legacy App option](/images/manual_shopifyV2_dashboard_createquiz_migratefromlegacyapp_menu.png)

---

## Step 2: Select the Quiz to Import

A dialog will appear listing all quizzes from your legacy account. Each quiz shows:

- **Name** and basic stats (number of questions, results pages, last updated date)
- **What will migrate** — a green checkmark confirms that questions, results, logic, and design are included
- **Warnings** — yellow notices flag anything that cannot be migrated automatically

    ![Migrate from Legacy App dialog showing quiz list with status indicators](/images/manual_shopifyV2_dashboard_createquiz_migratefromlegacyapp_dialog.png)

Click **Import Now** next to the quiz you want to migrate.

---

## Step 3: Review the Imported Quiz

Once the import completes, the quiz opens in the Quiz Builder. Its name will include the suffix **(Imported from V1)** so you can easily identify it.

![Imported quiz open in the Built for Shopify Quiz Builder](/images/manual_shopifyV2_dashboard_createquiz_migratefromlegacyapp_imported.png)

Review your questions, results pages, and logic to make sure everything looks correct before publishing.

---

## What Gets Migrated — and What Doesn't

| What migrates | Status |
|---|---|
| Questions and answer choices | ✅ Fully migrated |
| Results pages and content | ✅ Fully migrated |
| Conditional / branching logic | ✅ Fully migrated |
| Quiz design and styling | ✅ Fully migrated |
| Custom CSS | ⚠️ Not adapted automatically — see below |
| Custom JavaScript | ⚠️ Will not migrate — see below |
| Special third-party integrations | ⚠️ Needs review after import |
| Product mappings | ⚠️ May need re-linking — see below |

---

## What to Watch For After Import

Most quizzes migrate cleanly, but some advanced configurations require a manual follow-up.

### Custom CSS

If your legacy quiz used custom CSS, the styles are carried over as-is, but the **`💎Built for Shopify` app uses a different HTML structure** than the legacy app. CSS rules that targeted legacy elements may not apply correctly.

!!! warning "Review your design after import"

    Check the quiz preview after importing. If something looks off — wrong colors, broken layouts, missing fonts — you will need to update the CSS selectors to match the new structure, or rebuild the style using the [Design editor](/how-to-guides/customize-quiz-design/).

### Custom JavaScript

Custom JavaScript **will not be migrated**. The `💎Built for Shopify` app has a different JavaScript API, so legacy scripts cannot be transferred automatically.

!!! warning "Rebuild JS customizations manually"

    If your legacy quiz relied on custom JavaScript (e.g., custom events, DOM manipulation, or callback functions), you will need to rewrite those using the [JavaScript API](/how-to-guides/add-javascript/).

### Product Mappings

Questions, answer choices, and result pages migrate — but product links are tied to Shopify product IDs, which are the same across both app versions on the same store. **Product mappings should transfer correctly** for stores where the legacy app and the `💎Built for Shopify` app are installed on the same Shopify account.

!!! tip

    After importing, go to your results page and verify that the expected products are still linked. If any products appear missing or unlinked, re-add them using the [Results Page editor](/reference/quiz-builder/results-page/).

### Special Integrations

Connections to third-party tools (Klaviyo, Mailchimp, webhooks, etc.) are not automatically re-established after migration. Reconnect any integrations you need through [Quiz Settings](/reference/quiz-builder/quiz-settings/).

---

## After the Import

Once you've reviewed the quiz and fixed any warnings:

1. **Test the quiz end-to-end** using the Preview button before publishing.
2. **Reconnect integrations** (email platforms, CRMs, pixels) in Quiz Settings.
3. **Publish the quiz** using your preferred [publishing method](/how-to-guides/publish-quiz/).
4. When you're happy with the result, you can safely archive or delete the legacy version.

---

!!! success "The base quiz is always importable"

    Even if your legacy quiz has custom CSS, JavaScript, or unusual configurations, the core content — questions, logic, and results — will always import successfully. The warnings only indicate which advanced features need a manual finishing touch, not that the import will fail.

---

**Related articles:**

- [How to Install the App](/how-to-guides/install-app/)
- [How to Copy a Quiz from One Store to Another](/how-to-guides/copy-the-quiz-from-one-store-to-another/)
- [How to Customize Your Quiz Design](/how-to-guides/customize-quiz-design/)
- [How to Add JavaScript](/how-to-guides/add-javascript/)
- [Contact Customer Support](/how-to-guides/contact-customer-support/)
