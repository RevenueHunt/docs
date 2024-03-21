# How to Edit Your Shop Quiz Results Page

You can customize your quiz design as well as the look of your quiz's [Results Page](https://docs.revenuehunt.com/reference/quiz-builder/#results-page). This guide will walk you through adding elements to your results page using a variety of content blocks and creating of dynamic results page with Block logic.

## Build Your Resutls Page

1. **Plan Your Page Layout**: Decide on a mix of static and dynamic blocks to provide both consistent and personalized content.
2. **Add Blocks**: Insert Heading, Content, HTML, Image, Products List, and Products Slots Blocks as needed.
3. **Configure Each Block**: For dynamic elements, use the `@` symbol for information recalls and set Block Logic for conditional visibility.
4. **Adjust Page Settings**: Tailor the checkout process, product reviews visibility, and manage out-of-stock and duplicate product recommendations under Basic Settings. Use Advanced Settings for further customization with JavaScript and metafields.
5. **Review and Test**: Ensure the Results Page reflects your quiz's purpose and functions as intended, providing a seamless and personalized user experience.

### Adding Content

A **Static Results Page** shows the same content each time customer re-takes the quiz. The only thing that changes are the product recommendations in the Product Block or Slot Block.

A **Dynamic Results Page** not only changes the product recommendations but also adapts content based on customer quiz responses.

You'll want to start by adding content to your results page. Below is a list of availbale elements you can use to build your page.

Available Block Types:

1. **Heading Block**: Use for adding titles or headings.
2. **Content Block**: Ideal for adding text explanations about product matches.
3. **HTML Block**: Allows for the addition of custom HTML, including CSS for styling.
4. **Image Block**: Adds visual elements to your results page.
5. **Products List Block**: Shows a list of matching products, with the ability to set a maximum number.
6. **Products Slots Block**: Recommends bundles of complementary products across different categories.

Dynamic elements of the resutls apge:

- **Information Recalls**: Information Recalls allow you to recall any answer the customer provided in the quiz and used in any Content Block or a Heading Block on the resutls page. To add an information recall type `@` on your keeboard. A dropdown will appear with the list of informaiton to be raclled. Select the data poitn you're interested in and it will be added to the block.
- **Block Logic**: With Block Logic you can make blocks visible or hidden based on customer's responses. Block logic can be applied to any block on the resutls page, includign the product blocks and the slot blocks.

### Adjusting Results Page Settings

Next, you can adjust the [results page settings](https://docs.revenuehunt.com/reference/quiz-builder/#results-page-settings). 

Basic Settings worth checking:

- **Checkout Settings**: Control how customers interact with recommended products, allowing for direct cart addition or linking to product details.
- **Show Product Reviews**: Display product reviews to add credibility and influence decisions. We currently support these Reviews Apps for Shopify: Product Reviews by Shopify, Stamped Product Reviews & UGC, Judge.me Product Reviews, Rivyo Product Reviews.
- **Exclude Out-of-Stock Products**: Ensure unavailable items are not recommended.
- **Avoid Duplicate Recommendations**: Prevent the same product from being recommended in multiple blocks.

Advanced Settings worth checking:

- **Custom JavaScript**: Add custom scripts for unique behaviors or logic. Check [How to Customize Quiz Design]() for instructions on how to add custom JavaScript to your Results Page.
- **Product Metafields**: Use metafields or attributes to display specific product details, enhancing information on the results page. Check [How to Add Product Metafields](https://docs.revenuehunt.com/how-to-guides/how-to-add-product-metafields/) for detailed instructions on showing product metafields on the resutls page.
- **Multiple Results Pages**: Offer diverse results pages based on customer responses for enhanced personalization.


By following this guide, you can significantly enhance your shop's quiz results page, creating a dynamic, engaging, and personalized shopping experience for your customers.
