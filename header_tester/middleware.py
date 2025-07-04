class SecurityHeadersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # --- Add or modify security headers here ---
        response['X-Frame-Options'] = 'DENY'
        response['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        response['Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline';"
        response['X-Content-Type-Options'] = 'nosniff'
        response['Referrer-Policy'] = 'no-referrer-when-downgrade'
        response['Permissions-Policy'] = 'geolocation=(), microphone=()'
        # --- End of header modifications ---

        return response
