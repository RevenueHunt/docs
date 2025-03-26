# BigCommerce: Use Custom Fields as tags

You can create a Custom Field called “tags” within your BigCommerce store and use it to automaticaly group products within the Product Recommendation Quiz. These Custom Fields/tags can be then used to link products in bulk to choices or slots in the quiz.

Here’s how it works:

1. Navigate to your product page in BigCommerce and add open the `Custom Fields` menu.
    ![Use_Custom_Fields_as_tags_image1.jpg](/images/Use_Custom_Fields_as_tags_image1.jpg)
2. Next, select `+ Add custom fields` to create a new entry.
    ![Use_Custom_Fields_as_tags_image2.jpg](/images/Use_Custom_Fields_as_tags_image2.jpg)
3. In the Custom Field Name type “tags” and under Custom Field Value add the tags separated by a coma.
    ![Use_Custom_Fields_as_tags_image3.jpg](/images/Use_Custom_Fields_as_tags_image3.jpg)
4. Make sure to save the changes. You can tag many products in your store this way. 
5. Once you’re done tagging the products with the custom field called “tags”, simply run a [manual sync](/how-to-guides/sync-catalog/) of the app to make sure the Product Recommendation Quiz catalog is up to date. Products with the same tags will be automatically grouped together within the app and you’ll be able to link them to choices in the quiz within the [Link Categories/Tags](/reference/quiz-builder/link-collections/-link-categories) section.