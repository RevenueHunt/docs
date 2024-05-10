---
icon: material/image-off
---

# How to Fix Product Images Not Showing

Our quiz is served through an iFrame on your website but it’s hosted on our server. Your developer will have to disable hotlinking protection on your website for the product images (which are pulled from your store) to appear on the results page.
 

Hotlinking means displaying an image on a website by linking to the website hosting the image:
[https://simple.wikipedia.org/wiki/Hotlinking](https://simple.wikipedia.org/wiki/Hotlinking)

## Enable hotlinking in WordPress

Hotlinking in WordPress is usually enabled by default. WordPress allows you to use direct image URLs in your content, which can be hotlinked by other websites.

If you want to allow our app to hotlink your images, you can whitelist our server `admin.revenuehunt.com` and our server’s IP address `3.14.55.225`.

[This article](https://betterstudio.com/blog/how-to-disable-hotlinking-in-wordpress/#:~:text=If%20you%20want%20to%20allow,the%20%E2%80%9C%20Allow%20direct%20requests%E2%80%9D) can guide you on how to enable hotlinking on your WordPress site by disabling hotlinking protection.
