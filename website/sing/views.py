from django.shortcuts import render

# Create your views here.

def index1(request):
    return render(request, 'sing/index1.html')


def fr(request):
    return render(request, 'sing/fr.html')


def de(request):
    return render(request, 'sing/de.html')


def es(request):
    return render(request, 'sing/es.html')