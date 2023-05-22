from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import datetime


def monday(request):
    return HttpResponse('''
    <h1> Погода будет супер ! 20+  Зонтик не бери !</h1>
    <ul>
      <li> <a href="http://127.0.0.1:8000/weather/thursday"> thursday</a> </li>       
      <li> <a href="http://127.0.0.1:8000/weather/wensday"> wensday</a> </li>     
    </ul>              
  ''' + f"<h2> {datetime.date.today()} </h2>")


def thursday(request):
    return HttpResponse('''
    <h1> Будет жарко! 30+ </h1>
    <ul>
    <li> <a href = "http://127.0.0.1:8000/weather/monday" > monday </a > </li>
    <li> <a href = "http://127.0.0.1:8000/weather/wensday" > wensday </a> </li>
    </ul>
  ''' + f"<h2> {datetime.date.today()} </h2>")


def wensday(request):
    return HttpResponse('''
    <h1> Погода будет не очень! 10+ Сиди дома </h1>
    <ul>
    <li> <a href = "http://127.0.0.1:8000/weather/monday" > monday </a> </li>
    <li> <a href="http://127.0.0.1:8000/weather/thursday" > thursday</a> </li>
    </ul>
  ''' + f"<h2> {datetime.date.today()} </h2>")
