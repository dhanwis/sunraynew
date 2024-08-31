# sunray/middleware.py

from django.http import HttpResponseRedirect
from django.conf import settings
from django.urls import reverse

class AdminLoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if user is accessing admin-related URLs and is not authenticated
        if request.path.startswith('/admin/') and not request.user.is_authenticated:
            return HttpResponseRedirect(settings.LOGIN_URL + '?next=' + request.path)
        
        response = self.get_response(request)
        return response
