from django.shortcuts import render, redirect
from .models import Config, About

# Create your views here.

def folio(request) :
    config = Config.objects.first()
    about = About.objects.first()
    return render(
        request,
        'folio/folio.html',
        {
            'config' : config,
            'about' : about,
        }
    )

def home(request) :
    return redirect("https://john-lion.netlify.app/")