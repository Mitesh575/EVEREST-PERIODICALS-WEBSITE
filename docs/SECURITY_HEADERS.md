# EPSA security hosting verification
The homepage currently declares a Content-Security-Policy **meta** tag that allows inline scripts/styles. This is not proof of secure deployment or a substitute for real HTTP security headers.

Verify production response headers using curl -I, including HSTS, CSP with frame-ancestors, X-Content-Type-Options and Referrer-Policy. Configure them at the actual host/CDN after confirming resource compatibility. Do not turn on HSTS preload before confirming every subdomain and TLS certificate.

EmailJS browser public key/service/template IDs are client-visible configuration, not server secrets. Enable provider-side authorized domain restrictions, bot detection, abuse rate limiting and account notifications. Client-side timestamp-based throttling is bypassable. Do not live-submit test enquiries without an approved destination.

The privacy information page is intentionally narrowly scoped. Retention periods, deletion workflow, additional processing partners, and applicable legal obligations need agency review.
