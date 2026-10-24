# AGENTS.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Writing documentation

Before writing or editing anything in `docs/`, read `STYLE.md` and
`docs/reference/glossary.md`. Both are binding. They supersede the
Content Standards section further down this file.

After changing anything in `docs/`, do all five:

1. Check the pages you changed:
   `python tools/style_check.py docs/path/to/page.md`
2. Spellcheck the same pages:
   `python tools/spell_check.py docs/path/to/page.md`
   The style checker has no dictionary, so a clean style score says nothing
   about spelling. A correct word the dictionary lacks goes in
   `tools/spell_allow.txt`, never silence a real typo that way. Anything in
   backticks is skipped, because an app label is quoted verbatim.
3. If you added a page, add it to the `nav` in `mkdocs.yml`. A page that is
   not in the nav still renders at its URL but is reachable only by search.
4. Regenerate the support-bot files and put them in the same commit as the
   page changes, never a follow-up commit:
   `python generate_platform_docs.py`
   On Windows prefix it with `PYTHONIOENCODING=utf-8`, or the script dies
   partway through and leaves two of the three files stale.
5. Confirm the site builds: `python -m mkdocs build --strict`

Commit messages must be plain text. Never use a double quote, backtick,
dollar sign or backslash in them, or the Discord notification workflow fails.

## Planning

PRDs and planning docs for this repo live in `../devbot/planning/docs/` (centralized 2026-05-19).

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

Paths, repos, and release pipelines for the two WordPress plugin wrappers live in the `wp-plugin-release` skill (`.claude/skills/wp-plugin-release/SKILL.md`).
