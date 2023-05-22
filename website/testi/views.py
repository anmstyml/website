from django.shortcuts import render

# Create your views here.
import random


def getRandom():
    return random.randint(1, 10)


def index(request):
    title = 'my Blog'
    mylist = [10, 20, 30]
    mydict = {'ds1': 'ton', 'ds2': 'go', 'ds3': 'sew'}
    mytuple = (1, 2, 3, 4)
    data = {'title': title, 'mylist': mylist, 'mydict': mydict, 'mytuple': mytuple, 'random': getRandom()}
    return render(request, 'testi/index.html', data)


def form(request):
    return render(request, 'testi/form.html')


def save(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    return render(request, 'testi/save.html', {'title': title, 'description': description})


def demo(request):
    return render(request, 'testi/demo.html')


def archives(request):
    return render(request, 'testi/archives.html')


def blog(request):
    return render(request, 'testi/blog.html')


def page(request):
    return render(request, 'testi/page.html')


def single(request):
    return render(request, 'testi/single.html')







