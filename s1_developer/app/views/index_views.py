from django.conf import settings
from django.shortcuts import render

# Create your views here.


def index(request):
    data = {
        "version": settings.VERSION
    }
    return render(request, 'index.html', data)
