from django.urls import path
from . import views

urlpatterns = [
    path('', views.index2),
    path('toyota/', views.toyota),
    path('honda/', views.honda),
    path('renault/', views.renault),
]