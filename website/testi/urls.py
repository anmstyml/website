from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('form.html/', views.form),
    path('form.html/save', views.save),
    path('demo.html', views.demo),
    path('archives.html', views.archives),
    path('blog.html', views.blog),
    path('page.html', views.page),
    path('single.html', views.single),
    path('index.html', views.index),
]