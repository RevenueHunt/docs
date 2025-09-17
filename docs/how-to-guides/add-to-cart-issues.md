---
icon: material/cart-off
---


# Why Products Aren't Added to the Cart?

If your products are not added to the cart, here are the most probable causes:

## Your quiz is not published on a live website

The quiz needs to be published on live website (not hidden by a “coming soon” plugin or password). 

!!! tip

    Check [this article](/how-to-guides/publish-quiz/) to learn how to publish your quiz.

## You’re using a cart drawer

Our RevenueHunt app does not integrate with drawer carts at the moment. So after the quiz is over, the quiz is adding products to the “regular” cart instead of the drawer cart in your theme.

!!! warning "Cart Drawer"

    Check this article: [How to Update Your Shopify Cart Drawer Products After the Quiz](/how-to-guides/update-shopify-cart-drawer/) 

    This guide explains:

    - How RevenueHunt quiz app adds products to the Shopify cart

    - Why the cart drawer may not update

    - What your theme editor or developer can do to fix it

Unfortunately, drawer carts are an added functionality by specific store themes, not a core Shopify feature. Because of that, we cannot integrate with all the different themes that have drawer carts at the moment. However, there are a few ways this can be solved. Check the [How to Update Your Shopify Cart Drawer Products After the Quiz article](/how-to-guides/update-shopify-cart-drawer/) for more information.

**Option 1: Configure your Shopify theme to handle cart updates**

If you configure your Shopify theme to handle cart updates, it may be possible to integrate with drawer carts directly from the quiz.
    
!!! tip

    Check [this article](/how-to-guides/update-shopify-cart-drawer/) to learn how quiz adds products to the cart and how to configure your Shopify theme to handle cart updates.

**Option 2: Send the customer to the product page**

You could, instead of adding the product to the cart, send the customer to the product page by changing the checkout settings. They will be able to add the product to the drawer cart from there.

!!! tip

    Check [this article](/how-to-guides/change-checkout-settings/) to learn how to change your checkout settings.


## Your product is a subscription product

RevenueHunt app is able to sync and recommend subscription products created with ReCharge Subscriptions for Shopify. Check [here](/how-to-guides/recommend-subscription-products/) for instructions on how to enable it.

For other subscription apps, there's a [workaround](/how-to-guides/recommend-subscription-products/#other-subscriptions) that allows you to still guide your customers towards subscription options via the RevenueHunt app. 


---
This article helps with troubleshooting add-to-cart issues in RevenueHunt app.