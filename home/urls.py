from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^$|^home$', views.home, name='home'),
    path('browse', views.browse, name='home'),
    path('about', views.about, name='home'),
]