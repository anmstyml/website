from django.urls import path
from . import views

urlpatterns = [
    path('', views.index1),
    path('fr/', views.fr),
    path('de/', views.de),
    path('es/', views.es),
]