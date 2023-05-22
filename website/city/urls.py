from django.urls import path
from . import views

urlpatterns = [
    path('city', views.home),
    path('news/', views.news),
    path('management/', views.management),
    path('fact/', views.fact),
    path('phones/', views.phones),
    path('histori/', views.histori),
    path('histori/people/', views.people),
    path('histori/photos/', views.photos),
]