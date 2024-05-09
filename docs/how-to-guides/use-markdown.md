---
icon: material/format-header-pound
---


# How to Use Markdown Language

Markdown is an incredibly versatile language that allows you to format text on the web. It's used widely for creating readable and convertible text to HTML, enabling the styling of documents through simple syntax. 

This guide will walk you through the basics of Markdown Language, using the syntax supported by RevenueHunt’s Shop Quiz: Product Recommendation Quiz, to help you incorporate various styling elements into your content efficiently.

??? question "What is Markdown Language?"

    Markdown allows you to format words as bold or italic, add images, create lists, and much more, using just regular text with a few non-alphabetic characters, such as `#` or `*`. It's designed to be as straightforward as possible, making it accessible for anyone to learn and use.

## Markdown in Shop Quiz: Product Recommendation Quiz

Shop Quiz utilizes its own version of Markdown syntax, supporting a curated set of elements to enhance your questions, choices, and results pages.

![how to use markdown languge example](/images/how to use markdown languge example.png)

### Headings

Headings are essential for structuring your content, making it easier to read and navigate. In Markdown, you create headings by prefixing your text with one or more hash (`#`) symbols. The number of hashes before your text determines the level of the heading:

```markdown
# H1
## H2
### H3
```

### Text Styling

To emphasize text, you can make it italic or bold. Markdown uses asterisks (*) or underscores (_) to create italic or bold text. Here's how you can style your text:

```markdown
*italic text*
**bold text**
***italic & bold text***
```

### Links

Adding links to your content can provide readers with additional resources. To insert a link in Markdown, you use square brackets to enclose the anchor text and parentheses to enclose the URL:

```markdown
[link title](https://www.example.com)
```

### Images

Images can enhance your content visually, making it more engaging. To add an image, you use an exclamation mark followed by square brackets for the alt text and parentheses for the image URL:

```markdown
![alt text](https://www.example.com/path/to/image.jpg)
```

### Videos

Including videos can make your content even more interactive and informative. Videos hosted on YouTube or Vimeo can be embedded using the standard Markdown image syntax, with the video URL in the parentheses:

```markdown
![](https://youtu.be/0_tO8HgJiLQ)
![](https://www.youtube.com/watch?v=0_tO8HgJiLQ)
![](https://vimeo.com/142172484)
![](https://player.vimeo.com/video/142172484)
```

Videos are displayed responsively at 100% of their container’s width, with the height automatically determined based on a 16:9 aspect ratio. You can customize the aspect ratio or specify a fixed width and height using additional attributes in the Markdown:

```markdown
![](https://youtu.be/zNzZ1PfUDNk){ratio="16:9"}
![](https://youtu.be/0_tO8HgJiLQ){width="560" height="315"}
```

---
Markdown is a simple yet powerful language for formatting text on the web. By mastering the basic syntax elements supported by Shop Quiz: Product Recommendation Quiz, you can effectively enhance your quizzes and content, making them more attractive and engaging for users.