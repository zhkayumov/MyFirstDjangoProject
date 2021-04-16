from django.http import HttpResponse
from django.http import HttpRequest
from django.http import HttpResponseForbidden
from django.conf import settings


# Create your views here.

def show_settings(request: HttpRequest) -> HttpResponse:
    if settings.DEBUG is True:
        output = f"Current settings: DEBUG = {settings.DEBUG}, ALLOWED_HOSTS = {settings.ALLOWED_HOSTS}, INSTALLED_APPS = {settings.INSTALLED_APPS}, MIDDLEWARE = {settings.MIDDLEWARE}, ROOT_URLCONF = {settings.ROOT_URLCONF}, TEMPLATES = {settings.TEMPLATES}"
        return HttpResponse(output)
    else:
        return HttpResponseForbidden()
