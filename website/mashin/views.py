from django.shortcuts import render

# Create your views here.


def index2(request):
    return render(request, 'mashin/index2.html')


def toyota(request):
    return render(request, 'mashin/toyota.html')


def honda(request):
    return render(request, 'mashin/honda.html')


def renault(request):
    return render(request, 'mashin/renault.html')