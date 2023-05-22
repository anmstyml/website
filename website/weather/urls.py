from django.urls import path
from . import views

urlpatterns = [
    path('monday', views.monday),
    path('thursday', views.thursday),
    path('wensday', views.wensday),
]
