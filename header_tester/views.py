from django.http import HttpResponse

def index(request):
    response = HttpResponse("Security Headers Test Page")
    # Way to add to view directly
    # response['X-Content-Type-Options'] = 'nosniff'
    # response['X-Frame-Options'] = 'DENY'
    # response['Strict-Transport-Security'] = 'max-age=63072000; includeSubDomains'
    return response
