from django.shortcuts import render, redirect
from .models import *

def about(request):
    object = About.objects.get(id=1)
    context = {
        'object': object
    }
    return render(request, 'about/about.html', context)


def contact(request):
    return render(request, 'about/contact.html')


def privacy(request):
    return render(request, 'about/privacy.html')


def agreement(request):
    return render(request, 'about/agreement.html')
