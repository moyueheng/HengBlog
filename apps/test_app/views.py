from http.client import HTTPResponse
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse

# Create your views here.


def home(request):
    # Translators: This message appears on the home page only
    output = _("Welcome to mysite.com")
    return HttpResponse(output)
