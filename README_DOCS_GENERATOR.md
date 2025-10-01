# Documentation Generator for ChatGPT Training

This project includes a Python script that generates platform-specific documentation files for training ChatGPT agents for customer support.

## Generated Files

The script creates three text files containing all documentation content:

- **shopify.txt** (1.1MB) - Documentation for Shopify platform
- **shopify-legacy.txt** (833KB) - Documentation for Shopify Legacy platform
- **woocommerce.txt** (2.3MB) - Documentation for WooCommerce platform

## What the Script Does

The `generate_platform_docs.py` script:

1. Scans all `.md` files in the `docs/` directory
2. Extracts generic (platform-agnostic) content
3. Extracts platform-specific content for each supported platform
4. Combines generic + platform-specific content for each platform
5. Generates three separate `.txt` files with proper source URLs
6. Excludes Magento, BigCommerce, and Standalone platforms

## File Format

Each section in the generated files follows this format:

```
================================================================================
SOURCE: https://docs.revenuehunt.com/path/to/article/
================================================================================

[Generic content that applies to all platforms]

--- Platform Name Specific Content ---

[Platform-specific content]
```

This format makes it easy to:
- Identify the source of each content chunk
- Link customers to the full documentation
- Train ChatGPT to reference specific articles

## Usage

To regenerate the documentation files:

```bash
python3 generate_platform_docs.py
```

The script will:
- Process all 132+ markdown files
- Generate the three platform-specific files
- Display progress and file sizes

## When to Regenerate

Regenerate the files whenever:
- Documentation content is updated
- New articles are added
- Platform-specific information changes
- You need fresh training data for ChatGPT

## Platform-Specific Content Detection

The script recognizes Material for MkDocs tabbed content format:

```markdown
=== "Shopify"
    Content specific to Shopify

=== "WooCommerce"
    Content specific to WooCommerce
```

Content not under any platform tab is treated as generic and included in all three output files.

## Technical Details

- **Language**: Python 3
- **Dependencies**: Standard library only (os, re, pathlib, typing)
- **Input**: All `.md` files in `docs/` directory
- **Output**: Three `.txt` files in the project root
- **Base URL**: https://docs.revenuehunt.com

## File Structure

The generated files include:
- Header with platform name
- Table of contents implicit through SOURCE sections
- Generic documentation content
- Platform-specific sections clearly marked
- Proper source attribution for each section

## Use Cases

These files can be used to:
- Train ChatGPT for customer support
- Draft customer emails with proper documentation links
- Create support agent knowledge base
- Generate automated responses with accurate links
- Build FAQ systems
- Train new support team members
