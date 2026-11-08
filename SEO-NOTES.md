# Trilok SEO and image handoff

Implemented: unique page titles and descriptions, index/follow directives, social sharing metadata, Organization/WebSite/WebPage/Service JSON-LD, one H1 per page, main landmarks, internal page links, descriptive image text, responsive local WebP images and crawl rules.

The production domain has not been supplied. No placeholder canonical or sitemap URLs were published. Once the actual domain is confirmed, run `python3 scripts/configure-seo.py --site-url https://YOUR-ACTUAL-DOMAIN` from this folder. This writes absolute canonical URLs, social image URLs, breadcrumbs, structured-data URLs and sitemap.xml, and updates robots.txt. It persists the origin in seo-config.json. Deploy all changed files to the same origin. Run the script again after changing SEO settings in it.

A physical business address has not been verified, so Organization and Service schema are used instead of inventing the required LocalBusiness address. No review ratings, opening hours, prices or endorsements have been fabricated. Domain-dependent social image resolution remains pending until the origin is set. Indexing requires public hosting and can be checked through the site's owner's Google Search Console; no indexing or ranking is promised.

References: https://developers.google.com/search/docs/appearance/structured-data/local-business and https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap

All 11 content visuals were generated with the built-in image_gen tool for this project; the existing Trilok logo is retained. Original PNGs, responsive WebPs, the prompt set and provenance are in assets/generated/. All visible content images use these files. Generated visuals are labeled as concepts rather than completed project photographs.
