from django.shortcuts import render
# Create your views here.
from datetime import date
from datetime import datetime


def index3(request):
    today = datetime.now()
    wd = date.weekday(today)
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    datte = days[wd]
    return render(request, 'day/index3.html', {'datte': datte})







