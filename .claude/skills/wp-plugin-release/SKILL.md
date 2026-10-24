---
name: wp-plugin-release
description: Reference for the RevenueHunt WordPress.org and WooCommerce Marketplace plugins — local paths, git remotes, how they load embed.js from the monolith, version files, and the SVN / ZIP release pipelines.
---

# WordPress / WooCommerce plugins

The monolith serves `embed.js` from `public/embed.js` (accessed at `https://admin.revenuehunt.com/embed.js`). Two separate WordPress plugin projects act as thin wrappers that load this script into merchant storefronts. They share a Local by Flywheel dev environment but have **different codebases, Git repos, and deployment pipelines**.

## Project Locations

| Project | Local Path | Purpose |
|---------|-----------|---------|
| **WP Plugin** (eCommerce) | `~/Local Sites/productrecommendationquiz/app/public/wp-content/plugins/product-recommendation-quiz-for-ecommerce` | WordPress.org free plugin (supports WooCommerce, Magento, BigCommerce, Standalone) |
| **WooCommerce Extension** | `~/Local Sites/productrecommendationquiz/app/public/wp-content/plugins/product-recommendation-quiz-for-woocommerce` | Free WooCommerce Marketplace extension (WooCommerce-only) |

## How They Connect to the Monolith

Both plugins enqueue `embed.js` from the monolith on the merchant's frontend:

```
Merchant storefront → plugin enqueues <script async src="https://admin.revenuehunt.com/embed.js?shop=...">
                                                          ↑
                                              monolith/public/embed.js
```

The plugins also handle OAuth token exchange with the monolith via REST API endpoints (`wc/v3/prq_set_token`, `prq/v1/settoken`), calling `https://api.revenuehunt.com`.

## Git Repositories

| Project | Remote | Branch |
|---------|--------|--------|
| WP Plugin (eCommerce) | `git@github.com:RevenueHunt/product-recommendation-quiz-for-woocommerce.git` | `master` |
| WooCommerce Extension | `keybase://team/revenuehunt.admin/woocommerce` | `master` |

> **Note**: The eCommerce plugin's GitHub repo is confusingly named `product-recommendation-quiz-for-woocommerce` even though the plugin slug is `product-recommendation-quiz-for-ecommerce`.

## Deployment Pipelines

The two plugins have completely different deployment methods:

### WP Plugin (eCommerce) → WordPress.org SVN

Deployed to the public WordPress.org plugin repository via SVN.

- **SVN repo**: `https://plugins.svn.wordpress.org/product-recommendation-quiz-for-ecommerce/`
- **Plugin page**: https://wordpress.org/plugins/product-recommendation-quiz-for-ecommerce/
- **Credentials**: SVN username and password stored in KeePassXC
- **Process**: Update versions → Git push → Copy files to SVN trunk (excluding `.claude/`, `.project/`, `CLAUDE.md`, `.git/`) → `svn ci` → `svn copy trunk tags/X.X.X` → `svn ci`
- **Propagation**: 5–15 minutes after SVN tag commit
- **Full SOP**: `.project/sops/SOP_Update-WordPress-Plugin.md` in the plugin directory
- **Deployment skill**: `.claude/skills/deploy-wordpress-plugin.md`
- **Deploy command**: `.claude/commands/deploy.md`

### WooCommerce Extension → WooCommerce Partners Dashboard (ZIP upload)

Deployed as a free extension via the WooCommerce Marketplace vendor dashboard.

- **Dashboard**: https://woocommerce.com/wp-admin/
- **Product page**: https://woocommerce.com/wp-admin/edit.php?post_type=product&page=view-product&post=6046806
- **Credentials**: WordPress.com credentials stored in KeePassXC
- **Process**: Update versions → Git push to Keybase → Copy folder to Desktop → Remove dev files (`.git/`, `.claude/`, `.project/`, `CLAUDE.md`) → ZIP → Upload via Dashboard Version > Add Version
- **Full SOP**: `.project/sops/SOP_Update-WooCommerce-Extension.md` in the plugin directory
- **Deployment skill**: `.claude/skills/deploy-woocommerce-extension.md`
- **Deploy command**: `.claude/commands/deploy.md`

## Version Files to Update (Both Plugins)

When releasing either plugin, these files need version bumps:

| File | What to update |
|------|---------------|
| `product-recommendation-quiz-for-*.php` | `Version:` header + `PRQ_PLUGIN_VERSION` constant |
| `readme.txt` / `README.txt` | `Stable tag:`, `Tested up to:`, `WC tested up to:` (woo only) |
| `changelog.txt` | New entry at TOP (never remove old entries) |

## Key Differences Between the Two Plugins

| Aspect | WP Plugin (eCommerce) | WooCommerce Extension |
|--------|----------------------|----------------------|
| Slug | `product-recommendation-quiz-for-ecommerce` | `product-recommendation-quiz-for-woocommerce` |
| Distribution | WordPress.org (free) | WooCommerce Marketplace (free) |
| `channel` value in JS | `wordpress` | `woocommerce` |
| Platforms supported | WooCommerce + others | WooCommerce only |
| Git hosting | GitHub | Keybase |
| Deploy method | SVN to WordPress.org | ZIP upload to WooCommerce Dashboard |
| Has CLAUDE.md | Yes (detailed) | No |
| Has .claude/rules/ | Yes (6 files) | No |