# EPSA website verification report — 2026-10-29
Repository: Mitesh575/EVEREST-PERIODICALS-WEBSITE
Branch: audit/seo-accessibility-privacy-2026-10

This is a source-code remediation branch and NOT a completed production security, performance, or accessibility certification.

| Check | Source outcome | Not yet independently verified |
|---|---|---|
| Published metrics | Conflicting 250+/300+ and 150+ marketing statistics removed rather than substituting unverified counts | Real catalogue/customer records and approved metrics |
| UGC-CARE/indexing | Unqualified UGC-CARE and Scopus marketing removed from homepage | Individual journals and publisher/indexing records |
| SEO | Existing canonical tags and sitemap inspected; privacy page and Open Graph added | Google Search Console data and deployed responses |
| PageSpeed | HTML structure reviewed, reduced-motion support added | Mobile and desktop Lighthouse/CrUX scores |
| Enquiry form | Browser EmailJS integration and fallback feedback inspected | Authorized successful/failed end-to-end delivery |
| Security | Existing CSP meta tag, public EmailJS client integration reviewed | HTTP response headers, host settings, abuse controls, TLS scan |
| Accessibility | Semantic FAQ buttons, menu state, visible focus, skip link and status live region added | axe, keyboard, screen reader, contrast and zoom acceptance |
| Privacy | Added limited enquiry information page | Data-retention schedule, recipients, processor and legal review |
| Language/theme/mobile | Tamil introduction now in Tamil script; button clearly signals intro only | Full translation, device testing and contrast |
| Catalogue/quotation | Existing category-only catalogue confirmed | Publisher-approved ISSNs/title data and transactional quotation workflow |

Follow-up before merging: validate all institutional/business assertions, obtain owner approval for privacy content, run browser tests, verify EmailJS authorized origin/rate limiting, and test preview deployment. Then record production evidence before closing checklist items.
