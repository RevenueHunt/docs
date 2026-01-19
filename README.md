# RevenueHunt Documentation

[![MkDocs](https://img.shields.io/badge/Built%20with-MkDocs-blue)](https://www.mkdocs.org/)
[![Material for MkDocs](https://img.shields.io/badge/Theme-Material-purple)](https://squidfunk.github.io/mkdocs-material/)
[![License](https://img.shields.io/badge/License-Proprietary-red)](https://revenuehunt.com)

Official documentation for the **RevenueHunt Product Recommendation Quiz** app — a powerful e-commerce solution for creating interactive product quizzes, collecting zero-party data, and delivering personalized product recommendations.

**Live Documentation:** [https://docs.revenuehunt.com](https://docs.revenuehunt.com)

## What is RevenueHunt?

RevenueHunt is a product recommendation quiz app for e-commerce platforms that helps online stores:

- **Increase conversions** with personalized product recommendations
- **Collect zero-party data** through interactive quizzes
- **Segment customers** based on quiz responses
- **Integrate with marketing tools** like Klaviyo, HubSpot, Mailchimp, and more
- **Support multiple platforms**: Shopify, WooCommerce, Magento, BigCommerce, and Standalone

## Documentation Structure

This documentation follows the [Diátaxis framework](https://diataxis.fr/):

| Section | Purpose | Example Topics |
|---------|---------|----------------|
| **[Tutorials](https://docs.revenuehunt.com/tutorials/)** | Learning-oriented guides | Making your first quiz, Quiz design basics |
| **[How-to Guides](https://docs.revenuehunt.com/how-to-guides/)** | Task-oriented instructions | Add discounts, Integrate analytics, Publish quiz |
| **[App Manual](https://docs.revenuehunt.com/reference/)** | Technical reference | Quiz Builder, Dashboard, API settings |
| **[Customer Success](https://docs.revenuehunt.com/customer-success/)** | Business guidance | Conversion optimization, Best practices |

## Key Topics Covered

- **Quiz Creation**: Building product recommendation quizzes with conditional logic
- **Product Recommendations**: Linking products, collections, and recommendation algorithms
- **Quiz Design**: Customizing appearance, branding, and user experience
- **Integrations**: Klaviyo, HubSpot, Mailchimp, Omnisend, Zapier, Google Analytics, Meta Pixel
- **Publishing**: Embedding quizzes inline, popup, chat widget, or external links
- **Analytics**: Tracking quiz performance, revenue attribution, and conversion metrics
- **Multi-language & Multi-currency**: Supporting international stores and Shopify Markets

## Local Development

### Prerequisites

- Python 3.8+
- pip

### Setup

```bash
# Clone the repository
git clone https://github.com/RevenueHunt/docs.git
cd docs

# Install dependencies
pip install -r requirements.txt

# Serve locally with hot reload
mkdocs serve
```

The documentation will be available at `http://127.0.0.1:8000`.

### Build

```bash
# Build static site
mkdocs build
```

Output is generated in the `site/` directory.

## Project Structure

```
docs/
├── docs/                    # Documentation content
│   ├── tutorials/           # Step-by-step learning guides
│   ├── how-to-guides/       # Task-oriented instructions
│   ├── reference/           # Technical reference (App Manual)
│   ├── customer-success/    # Business guidance and best practices
│   └── images/              # Screenshots and diagrams
├── plugins/                 # Custom MkDocs plugins
├── mkdocs.yml               # MkDocs configuration
├── requirements.txt         # Python dependencies
└── rename_images.rb         # Utility for image file naming
```

## Tech Stack

- **Static Site Generator**: [MkDocs](https://www.mkdocs.org/)
- **Theme**: [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- **Markdown Extensions**: PyMdown Extensions (tabs, admonitions, code highlighting)
- **Search**: Built-in MkDocs search with suggestions and highlighting
- **Analytics**: Google Analytics 4

## LLM Training Data

This repository includes generated documentation files for training AI assistants:

- `shopify.txt` — Shopify-specific documentation
- `shopify-legacy.txt` — Shopify Legacy documentation
- `woocommerce.txt` — WooCommerce-specific documentation

See [README_DOCS_GENERATOR.md](README_DOCS_GENERATOR.md) for details on regenerating these files.

## Contributing

When contributing to this documentation:

1. Follow the established content taxonomy (tutorials vs how-to vs reference)
2. Use Material theme conventions for formatting
3. Store images in `docs/images/` without spaces in filenames
4. Test locally with `mkdocs serve` before submitting changes
5. Use platform-specific tabs for multi-platform instructions

## Links

- **Product Website**: [https://revenuehunt.com](https://revenuehunt.com)
- **Shopify App**: [Shopify App Store](https://apps.shopify.com/product-recommendation-quiz-revenuehunt)
- **WooCommerce Plugin**: [WordPress Plugin Directory](https://wordpress.org/plugins/product-recommendation-quiz-for-ecommerce/)
- **Support**: [Contact Support](https://docs.revenuehunt.com/how-to-guides/contact-customer-support/)

## License

This documentation is proprietary to RevenueHunt. All rights reserved.

---

*Built with [MkDocs](https://www.mkdocs.org/) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)*
