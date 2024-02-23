
## Results Page

![quiz builder results page](/images/manual_quizbuilder_resultspage.png)

In the Results Page section, you can add content to the results page shown at the end of the quiz. You can adjust the results page settings and see the preview of how the results page looks like.

### Block Types

**+** / **add block** - Opens a menu of content blocks that you can add to your resutls page. You can drag an drop the blocks to change the order.

![quiz builder results page add block menu](/images/manual_quizbuilder_resultspage_addblockmenu.png)

- **Heading Block** - Adds a new heading to your page, ideal for titles or section breaks.

- **Content Block** - Adds a new content block to your page, ideal for adding and formatting text, lists, and links.

- **HTML Block** - Adds a block where you can input custom HTML code for advanced content and styling.

- **Image Block** - Adds an embedded image block into your page. You can upload your own image. The image should be max 1000px x 1000px and max 2MB.

- **Products Block** - Adds a block specifically designed for displaying a list of recommended products.

- **Slots Block** - Adds a block specifically designed for displaying the recommended products sorted into slots. Slots allow you to group recommended products into different categories (e.g. cleanser, toner, serum, moisturizer...). Slots show the most voted products from a collection that's linked to the slot.

![quiz builder results page block menu](/images/manual_quizbuilder_resultspage_blockmenu.png)

### Block Logic

**conditional logic** / **tree icon** - Opens the [Block Logic]() menu.

![quiz builder resutls page block logic](/images/manual_quizbuilder_resultspage_blockmenu_blocklogic.png)

With Block Logic you can make blocks visible or hidden based on customer's responses.

**Add Block Logic** - Adds a new block logic rule.

![quiz builder resutls page block logic example](/images/manual_quizbuilder_resultspage_blockmenu_blocklogic_example.png)

All the Block Logic rules follow the same format

**IF response to** pick the question from a dropdown list

**is**/ **is not** pick a choice from the dropdown list

**THEN block is** pick either **Visible** or **Hidden**

**IN ALL OTHER CASES this block is** pick pick either **Visible** or **Hidden**

*In the example, if a user chooses a choice "A gift" in Question 1 "Who are you shopping for?" then this content block with text "This is content text." will be visible. If they give a different answer in Question 1 this content block will be hidden.*

- **+** - Adds another Block Logic rule. Adds a new OR logical rule.

- **bin** - Delete the current Block Logic rule.

- **+ add concurrent logic** - Adds a new AND logical statement to the same rule. AND conditional statements can be tricky, as both statements have to be true for the rule to take effect. For most quizzes, using the OR rule is enough.

**...** - Opens the more options menu.

![quiz builder resutls page block menu more options](/images/manual_quizbuilder_resultspage_blockmenu_moreoptions.png)

- **+ add block below** - Opens the **+** / **add block** menu.

- **bin** / **delete block** - Deletes the current block from the resutls page.

### Block Settings

🔧 / **wrench icon** - Opens the block settings menu.

**Product Block Settings**

![quiz builder results page product block settings](/images/manual_quizbuilder_resultspage_blockmenu_productblocksettings.png)

- **Title** - Type a title to be displayed above the recommended products.

- **Description** - Add a description to be displayed above the recommended products.

- **Max. recommended products** - Select how many products should be recommended in this Product Block. Max 15 products can be displayed per block. If you want to show more products, add another Product Block to your results page and make sure that the "Allow duplicated recommendations" settings is off in your Results page settings.

- **Hide block when no products are recommended** - Activate this setting if you want to hide the product block if there are no recommendations. By default, with no recommendations a "Based on your answers, we need a little more time to give you our recommendations. Please get in touch with us." text will be displayed instead. This text can be edited in the Quiz Settings> Messages section.

**Slot Block Settings** 

![quiz builder resutls page slot block settings](/images/manual_quizbuilder_resultspage_blockmenu_slotblocksettings.png)

- **Add a slot** - Adds a new slot to the slot block. You can have multiple slots in a slot block.

![quiz builder results page slot block settings add slot](/images/manual_quizbuilder_resultspage_blockmenu_slotblocksettings_addslot.png)

- **Title** - Type a title to be displayed above the slot.

- **Description** - Add a description to be displayed above the slot.

- **Max. recommended products** - Select how many products should be recommended in this Slot. Max 15 products can be displayed per slot.

- **Included collections** - Select from which collections (or tags) from your store the slot should display the products. Slots show the most voted products from a collection that's linked to the slot.

- **Excluded collections** - Select from which collections (or tags) from your store the slot should never display the products. Slots show the most voted products from a collection that's linked to the slot. If a producrt recevied votes in the quiz but is part of the excluded collection, the slot will not show that product.

**Slot ID** - Displays the current slot ID.

### Results Page Settings

⚙️ / **gear icon** - Opens the results page settings.

![quiz builder results page results page settings](/images/manual_quizbuilder_resultspage_settings.png)

### Results Page Settings: BASIC

**Checkout Settings**

![quiz builder resutls page resutls page settings basic checkout](/images/manual_quizbuilder_resultspage_settings_basic_checkout.png)

- **Add product to cart** - Allows the user to add the recommended products to the cart directly from the results page.

    - **Proceed to cart** - After the products are added to the cart, the customer will proceed to the cart page.

    - **proceed to checkout** - After the products are added to the cart, the customer will proceed to the checkout page.

- **Link to product** - Displays a "view product" button that takes the customer to the product page. This option disables the "add to cart" feature.

**Individual Product Settings**

![quiz builder resutls page resutls page settings basic individual product settings](/images/manual_quizbuilder_resultspage_settings_basic_individualproductsettings.png)

- **Show main product image** - Click to always show the main product image, even when a variant is recommended.

- **Show variant image** - Click to always show the variant image, instead of the main product image.

- **Show price** - Toggle to display the product price on the results page.

- **Show vendors** - Toggle to display the product vendor under the product on the results page.

- **Show CTA button** - Toggle to display the "add to cart" or "view product" button under the products on the results page.

- **Show "more info" link** - Toggle to display a "more info" link below the product name or description on the resutls page. The link takes you to the product page.

- **Show description** - Toggle to display the product description below the product name on the results page. Additional option is displayed.

    **Truncate description** - Toggle to shorten the product description on the results page and display a "read more" link which will enlarge it while clicked.

- **Show reviews** - Toggle to show product rating below the product name on the resutls page. After activation make sure to run a [Catalog Sync]() to sync all the product reviews with the app.

- **Show metafields** - Toggle to allow showing of custom product metafields on the resutls page. To show product metafields follow the instructions in [How to show product metafieleds in the quiz]().

**Style Settings**

![quiz builder resutls page resutls page settings basic style](/images/manual_quizbuilder_resultspage_settings_basic_stylesettings.png)

**Background image** - Click "Add" to upload a background image to the resutls page. Image should be max 1000px x 1000px and 2MB. An extra menu appears once activated. 

- **Image Opacity** - A slider that allows you to adjust the opacity of the uploaded background image.


### Results Page Settings: ADVANCED

![quiz builder resutls page resutls page settings advanced](/images/manual_quizbuilder_resultspage_settings_advanced.png)

**Recommendation Settings**

**If no results, no products** - If there are no products that can be recommended a "Based on your answers, we need a little more time to give you our recommendations. Please get in touch with us." text will be displayed instead. This text can be edited in the Quiz Settings > Messages section.

**If no results, random products** - If there are no products that can be recommended the app will show random products that received any votes.

**Group product variants** - Groups product variants as a dropdown under the main product name. Toggle to activate. Variants are displayed in the order of votes they received at the end of the quiz. If varaints receive the same number of votes, the order in which they are displayed on the resutls page will be random.

**Show unavailable products** - Allows products that are unavailable (out of stock) in the store to be recommended via the quiz. Toggle to activate.

**Allow duplicated recommendations** - Allows products to show multiple times on the results page (for example in two different product blocks or slot blocks). Toggle to activate.

**Minimum number of votes** - Adds an extra setting to each product or slot block which allows you to limit the products recommended in this block only to those that received X votes or more. Toggle to activate.

![quiz builder results page results page settings min votes setting](/images/manual_quizbuilder_resultspage_settings_advanced_minvotes.png)

**Custom JS Code**

**Custom JavaScript** - Click "Add" to open the JavaScript console.

**Multiple Results Pages**

**Activate multiple results pages** - Click "activate" to open the MULTIPLE RESULTS PAGES menu.

### Results Page Settings: MULTIPLE RESULTS PAGES

![quiz builder resutls page results page settings multiple results pages](/images/manual_quizbuilder_resultspage_settings_multipleresultspages.png)

**Results Page 1** 

- **Edit this page** - Click "edit" to switch to this results page and edit its content.

- **This is currently the default Results Page** - Indicates which page is the default one. Customer will be taken to the default results page unless you redirect them with [Jump Logic](#conditional-logic) to another page.

**Results Page 2**

- **You're editing this Results Page settings & blocks** - Indicates which results page you are currently editing.

- **Set as default** - Click "set" to select this resutls page as default. Customer will be taken to the default results page unless you redirect them with [Jump Logic](#conditional-logic) to another page.

**Create new Results Page** - add a new resutls page to your quiz.

### Results Page Settings: DISCOUNTS

![quiz builder resutls page discount](/images/manual_quizbuilder_resultspage_settings_discount.png)

**Discount Code Settings** - Allows to add a static discount to your resutls page. Click "Add" to open the discount menu.

![quiz builder results page discount discount code](/images/manual_quizbuilder_resultspage_settings_discount_discountcode.png)

- **Visible discount** - Select the discount % from the dropdown. The percentage discount will be visible in the results page products. The discount code will be automatically redeemed at checkout.

- **Code** - Type a discount code that corresponds to this discount. You have to set up this discount code in your store > Shopify Discounts first. Follow this guide to learn [How to add a discount to the quiz]().

**Dynamic Discounts** - Allows to add a dynamic discount to your results page with a minimal cart value. Click "activate" to open the discount menu.

![quiz builder results page discount discount code](/images/manual_quizbuilder_resultspage_settings_discount_dynamicdiscounts.png)

**Dynamic Discounts Settings**

- **Enable notifications** - A toast notification will appear when a customer qualifies for a discount. Toggle to enable/disable.

- **Encourage discounts** - The notification will also include a message telling the customer how close they are to receiving the next highest discount. Toggle to enable/disable.

**Discount [A]** 

- **Discount code** - Type a discount code that corresponds to this discount. You have to set up this discount code in your store > Shopify Discounts first. Follow this guide to learn [How to add a discount to the quiz]().

- **Discount percentage** - Type the discount %. The percentage discount will be visible in the results page products. The discount code will be automatically redeemed at checkout.

- **Min. value in cart** - Type the value of products added to the cart on the results page above which the discount will be applied.

- **+** / **add another discount** - adds a new dynamic discount (Discount [B]).

- **bin** / **delete this discount** - deletes this dynamic discount.

**add a discount** - Adds a new dynamic discount below (Discount [B]).

**deactivate** - Deactivates dynamic discounts.