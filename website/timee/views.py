from django.shortcuts import render

# Create your views here.
from datetime import time
from datetime import datetime


def index(request):
    now = datetime.now()
    ti = now.time()
    tiMe = ti.hour
    data = {'tiMe': tiMe}
    return render(request, 'timee/index.html', data)
print(index(3))