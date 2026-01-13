from django.shortcuts import render
from .models import Config
# Create your views here.

def folio(request) :
    config = Config.objects.first()
    return render(
        request,
        'folio/folio.html',
        {
            'config' : config,
        }
    )