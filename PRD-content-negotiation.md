# PRD: Content Negotiation for Documentation Site

## Overview

Implement content negotiation for `docs.revenuehunt.com` so that a single URL can serve different content formats (HTML or Markdown) based on who is requesting it.

## Problem Statement

Currently, the documentation site serves the same content at two separate URLs:

- `https://docs.revenuehunt.com/how-to-guides/send-leads-to-hubspot` → HTML (for humans)
- `https://docs.revenuehunt.com/how-to-guides/send-leads-to-hubspot.md` → Markdown (for AI agents)

This creates:
1. **Duplicate content** - Two URLs with identical information dilutes SEO signals
2. **Maintenance overhead** - Conceptually two versions to keep in sync
3. **Non-standard discovery** - AI agents must guess or be told to append `.md`
4. **Poor AI optimization** - Does not follow emerging standards (llmstxt.org, agentstxt.dev)

## Desired Behavior

A single canonical URL should serve different formats based on the request:

| Request | Response |
|---------|----------|
| Default browser request | HTML page with full styling/navigation |
| `Accept: text/markdown` header | Raw markdown source |
| `Accept: text/plain` header | Raw markdown source |
| `?format=md` query parameter | Raw markdown source |

### Example

```bash
# Returns HTML (default)
curl https://docs.revenuehunt.com/how-to-guides/send-leads-to-hubspot

# Returns Markdown
curl -H "Accept: text/markdown" https://docs.revenuehunt.com/how-to-guides/send-leads-to-hubspot

# Returns Markdown (query param fallback)
curl "https://docs.revenuehunt.com/how-to-guides/send-leads-to-hubspot?format=md"
```

## Technical Requirements

### 1. Content Negotiation Logic

The system must detect markdown requests via:

1. **Accept header** - `text/markdown` or `text/plain` with higher priority than `text/html`
2. **Query parameter** - `?format=md` as a fallback for testing/debugging
3. **Optional: User-Agent detection** - Known AI crawlers (GPTBot, ClaudeBot, PerplexityBot) could be auto-served markdown

### 2. Response Headers

**When serving Markdown:**
```
Content-Type: text/markdown; charset=utf-8
Link: <canonical-html-url>; rel="canonical"
X-Content-Format: markdown
Cache-Control: public, max-age=3600
```

**When serving HTML:**
```
Link: <markdown-url>; rel="alternate"; type="text/markdown"
X-Content-Negotiation: available
```

### 3. URL Handling

- Do NOT apply content negotiation to static assets (`.js`, `.css`, `.png`, `.jpg`, `.svg`, `.ico`, `.woff`, `.woff2`)
- Do NOT apply to discovery files (`/llms.txt`, `/agents.txt`, `/robots.txt`, `/sitemap.xml`)
- Do NOT apply to URLs already ending in `.md`
- Apply to all documentation pages under `/how-to-guides/`, `/tutorials/`, `/reference/`, `/customer-success/`

### 4. Markdown Source Availability

The raw `.md` files must be available on the server. Currently handled by `copy_markdown_plugin.py` which copies all `.md` files to the built site directory.

## Current Infrastructure

| Component | Details |
|-----------|---------|
| Static site generator | MkDocs with Material theme |
| Hosting | GitHub Pages |
| Domain | `docs.revenuehunt.com` (via CNAME) |
| CI/CD | GitHub Actions (`mkdocs gh-deploy`) |
| Markdown copying | Custom plugin `copy_markdown_plugin.py` |

## Implementation Options

### Option A: Cloudflare Workers

Add Cloudflare in front of GitHub Pages and use a Worker for content negotiation.

**Pros:**
- No migration required
- Edge-based (fast)
- Free tier sufficient

**Cons:**
- Requires Cloudflare account setup
- Additional infrastructure to maintain

**Implementation:**
1. Add domain to Cloudflare (if not already)
2. Create Worker with content negotiation logic
3. Route `docs.revenuehunt.com/*` through Worker

### Option B: Migrate to Vercel

Use Vercel's Edge Middleware.

**Pros:**
- Native middleware support
- Good DX with preview deployments
- Free tier available

**Cons:**
- Requires migration from GitHub Pages
- Different deployment workflow

**Implementation:**
1. Create `vercel.json` with build config
2. Create `middleware.ts` with content negotiation logic
3. Connect repo to Vercel

### Option C: Migrate to Netlify

Use Netlify's Edge Functions.

**Pros:**
- Native edge function support
- Good GitHub integration
- Free tier available

**Cons:**
- Requires migration from GitHub Pages
- Different deployment workflow

**Implementation:**
1. Create `netlify.toml` with build config
2. Create edge function with content negotiation logic
3. Connect repo to Netlify

## Acceptance Criteria

1. **Single URL serves both formats**
   - `curl https://docs.revenuehunt.com/how-to-guides/send-leads-to-hubspot` returns HTML
   - `curl -H "Accept: text/markdown" https://docs.revenuehunt.com/how-to-guides/send-leads-to-hubspot` returns raw markdown

2. **Proper headers**
   - HTML responses include `Link` header pointing to markdown alternate
   - Markdown responses include `Content-Type: text/markdown`

3. **Discovery files accessible**
   - `/llms.txt` returns the LLM discovery file
   - `/agents.txt` returns the agent discovery file
   - `/robots.txt` allows AI crawlers

4. **No regression**
   - All existing HTML pages continue to work
   - Search engine indexing unaffected
   - Site performance maintained

5. **Caching**
   - Both formats should be cacheable
   - Cache headers appropriate for CDN caching

## Discovery Files (Already Created)

The following files have been added to `docs/`:

| File | Purpose |
|------|---------|
| `llms.txt` | Site overview for LLM answer engines, documents content negotiation support |
| `agents.txt` | Structured discovery for autonomous AI agents |
| `robots.txt` | Explicitly allows AI crawlers (GPTBot, ClaudeBot, PerplexityBot, etc.) |

## Out of Scope

- API endpoints (none exist)
- Authentication/authorization
- Rate limiting
- Analytics tracking of format requests
- Auto-detection of AI crawlers (optional enhancement)

## Success Metrics

1. Single canonical URL in search results (no duplicate `.md` URLs indexed)
2. AI agents successfully retrieve markdown via `Accept` header
3. No increase in page load time for human visitors

## References

- [llmstxt.org](https://llmstxt.org/) - LLM discovery file specification
- [agentstxt.dev](https://agentstxt.dev/) - Agent discovery specification
- [HTTP Content Negotiation (MDN)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Content_negotiation)
- [RFC 9110 - HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110#name-content-negotiation)
