# Security Headers Testing App
Django app to test how different security header configurations impact browser behavior and overall security posture

## Common Security Headers
### Content Security Policy (CSP):
Controls the resources a browser is allowed to load for a page, preventing XSS attacks by restricting the sources of scripts, images, and other content.
### Strict-Transport-Security (HSTS):
Forces browsers to use HTTPS for all future connections to the site, preventing man-in-the-middle attacks and enforcing secure communication.
### X-Frame-Options:
Protects against clickjacking attacks by restricting the ways a page can be embedded in an iframe, preventing malicious websites from overlaying your site and tricking users.
### X-Content-Type-Options:
Prevents browsers from performing MIME-sniffing, which can be exploited in XSS attacks by forcing them to respect the declared MIME type of resources.
### X-XSS-Protection:
Enables the browser's built-in XSS filter, which can help mitigate reflected XSS attacks.
### Referrer-Policy:
Controls how much referrer information is sent with requests, helping to protect user privacy.
### Permissions-Policy (formerly Feature-Policy):
Allows web developers to selectively enable or disable browser features, enhancing control over how the browser interacts with the page.
### Cache-Control:
Controls how the browser caches resources, which can be important for performance and security.
### Access-Control-Allow-Origin:
While not strictly a security header in the same vein as the others, it is crucial for controlling cross-origin resource sharing (CORS) and preventing unauthorized access to resources from other domains.
