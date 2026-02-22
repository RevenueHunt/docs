# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a documentation site for the RevenueHunt app - a product recommendation and video quiz application for e-commerce platforms (Shopify, WooCommerce, Magento, BigCommerce, and Standalone). The documentation is built using MkDocs with the Material theme.

## Key Commands

### Development and Build
```bash
# Install dependencies
pip install -r requirements.txt

# Serve documentation locally with hot reload
mkdocs serve

# Build static site
mkdocs build

# Deploy to GitHub Pages (if configured)
mkdocs gh-deploy
```

### Content Management
```bash
# Rename image files with spaces (removes spaces)
ruby rename_images.rb

# Build the custom plugin for copying markdown files
python setup.py develop
```

## Architecture

### Documentation Structure
- **docs/**: Main documentation content organized by content type:
  - `tutorials/`: Step-by-step learning guides
  - `how-to-guides/`: Task-oriented instructions  
  - `reference/`: Technical reference and app manual
  - `customer-success/`: Business guidance and best practices
  - `images/`: All documentation images and screenshots

### Technical Components

#### MkDocs Configuration (`mkdocs.yml`)
- **Theme**: Material Design with dark/light mode toggle
- **Navigation**: Multi-level navigation with tabs and sections
- **Plugins**: Search and custom copy_markdown_plugin
- **Extensions**: Full PyMdown Extensions suite for advanced markdown

#### Custom Plugin (`plugins/copy_markdown_plugin.py`)
- Copies all .md files to the built site directory
- Preserves directory structure for direct markdown access

#### Content Processing (`rename_images.rb`)
- Ruby utility to rename image files (removes spaces)
- Updates all markdown file references automatically
- Essential for web compatibility of image assets

### Content Organization Philosophy
- **Tutorials**: Learning-oriented (how to learn)
- **How-to Guides**: Problem-oriented (how to solve)
- **Reference**: Information-oriented (technical specs)
- **Customer Success**: Understanding-oriented (business context)

## Development Guidelines

### Working with Documentation
- All content uses Material theme conventions
- Images should be optimized and follow naming conventions (no spaces)
- Use tabs syntax for platform-specific instructions (Shopify, WooCommerce, etc.)
- Admonitions (info, warning, etc.) are heavily used for callouts

### Navigation Updates
- Main navigation is defined in `mkdocs.yml` nav section
- External links to blog posts are included in Customer Success
- Update navigation when adding new content sections

### Image Management
- Store all images in `docs/images/`
- Run `ruby rename_images.rb` after adding images with spaces
- Reference images using relative paths from the markdown file location

### Build and Testing
- Always test locally with `mkdocs serve` before deploying
- Site builds to `site/` directory
- Custom plugin ensures markdown files are available in built site

### Content Standards
- Use consistent heading hierarchy
- Include cross-references between related topics
- Maintain platform-specific tabs for multi-platform features
- Follow the established content taxonomy (tutorials vs how-to vs reference)

---

## Related Projects: WordPress / WooCommerce Plugins

The monolith serves `embed.js` from `public/embed.js` (accessed at `https://admin.revenuehunt.com/embed.js`). Two separate WordPress plugin projects act as thin wrappers that load this script into merchant storefronts. They share a Local by Flywheel dev environment but have **different codebases, Git repos, and deployment pipelines**.

### Project Locations

| Project | Local Path | Purpose |
|---------|-----------|---------|
| **WP Plugin** (eCommerce) | `~/Local Sites/productrecommendationquiz/app/public/wp-content/plugins/product-recommendation-quiz-for-ecommerce` | WordPress.org free plugin (supports WooCommerce, Magento, BigCommerce, Standalone) |
| **WooCommerce Extension** | `~/Local Sites/productrecommendationquiz/app/public/wp-content/plugins/product-recommendation-quiz-for-woocommerce` | Paid WooCommerce Marketplace extension (WooCommerce-only) |

### How They Connect to the Monolith

Both plugins enqueue `embed.js` from the monolith on the merchant's frontend:

```
Merchant storefront → plugin enqueues <script async src="https://admin.revenuehunt.com/embed.js?shop=...">
                                                          ↑
                                              monolith/public/embed.js
```

The plugins also handle OAuth token exchange with the monolith via REST API endpoints (`wc/v3/prq_set_token`, `prq/v1/settoken`), calling `https://api.revenuehunt.com`.

### Git Repositories

| Project | Remote | Branch |
|---------|--------|--------|
| WP Plugin (eCommerce) | `git@github.com:RevenueHunt/product-recommendation-quiz-for-woocommerce.git` | `master` |
| WooCommerce Extension | `keybase://team/revenuehunt.admin/woocommerce` | `master` |

> **Note**: The eCommerce plugin's GitHub repo is confusingly named `product-recommendation-quiz-for-woocommerce` even though the plugin slug is `product-recommendation-quiz-for-ecommerce`.

### Deployment Pipelines

The two plugins have completely different deployment methods:

#### WP Plugin (eCommerce) → WordPress.org SVN

Deployed to the public WordPress.org plugin repository via SVN.

- **SVN repo**: `https://plugins.svn.wordpress.org/product-recommendation-quiz-for-ecommerce/`
- **Plugin page**: https://wordpress.org/plugins/product-recommendation-quiz-for-ecommerce/
- **Credentials**: SVN username and password stored in KeePassXC
- **Process**: Update versions → Git push → Copy files to SVN trunk (excluding `.claude/`, `.project/`, `CLAUDE.md`, `.git/`) → `svn ci` → `svn copy trunk tags/X.X.X` → `svn ci`
- **Propagation**: 5–15 minutes after SVN tag commit
- **Full SOP**: `.project/sops/SOP_Update-WordPress-Plugin.md` in the plugin directory
- **Deployment skill**: `.claude/skills/deploy-wordpress-plugin.md`
- **Deploy command**: `.claude/commands/deploy.md`

#### WooCommerce Extension → WooCommerce Partners Dashboard (ZIP upload)

Deployed as a paid extension via the WooCommerce Marketplace vendor dashboard.

- **Dashboard**: https://woocommerce.com/wp-admin/
- **Product page**: https://woocommerce.com/wp-admin/edit.php?post_type=product&page=view-product&post=6046806
- **Credentials**: WordPress.com credentials stored in KeePassXC
- **Process**: Update versions → Git push to Keybase → Copy folder to Desktop → Remove dev files (`.git/`, `.claude/`, `.project/`, `CLAUDE.md`) → ZIP → Upload via Dashboard Version > Add Version
- **Full SOP**: `.project/sops/SOP_Update-WooCommerce-Extension.md` in the plugin directory
- **Deployment skill**: `.claude/skills/deploy-woocommerce-extension.md`
- **Deploy command**: `.claude/commands/deploy.md`

### Version Files to Update (Both Plugins)

When releasing either plugin, these files need version bumps:

| File | What to update |
|------|---------------|
| `product-recommendation-quiz-for-*.php` | `Version:` header + `PRQ_PLUGIN_VERSION` constant |
| `readme.txt` / `README.txt` | `Stable tag:`, `Tested up to:`, `WC tested up to:` (woo only) |
| `changelog.txt` | New entry at TOP (never remove old entries) |

### Key Differences Between the Two Plugins

| Aspect | WP Plugin (eCommerce) | WooCommerce Extension |
|--------|----------------------|----------------------|
| Slug | `product-recommendation-quiz-for-ecommerce` | `product-recommendation-quiz-for-woocommerce` |
| Distribution | WordPress.org (free) | WooCommerce Marketplace (paid) |
| `channel` value in JS | `wordpress` | `woocommerce` |
| Platforms supported | WooCommerce + others | WooCommerce only |
| Git hosting | GitHub | Keybase |
| Deploy method | SVN to WordPress.org | ZIP upload to WooCommerce Dashboard |
| Has CLAUDE.md | Yes (detailed) | No |
| Has .claude/rules/ | Yes (6 files) | No |