# middleware.py
from django.conf import settings
from django.shortcuts import render
from django.urls import reverse

class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            maintenance_url = reverse('maintenance')
        except:
            maintenance_url = '/maintenance/'  # Fallback in case reverse fails
        if settings.MAINTENANCE_MODE and not request.path.startswith(maintenance_url):
            return render(request, 'website/maintenance.html')
        response = self.get_response(request)
        return response