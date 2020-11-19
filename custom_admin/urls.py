from django.urls import path
from . import views


urlpatterns = [
    path('/', views.admin, name='admin'),
    path('/delete/', views.delete_complaint, name='delete'),
    path('/delete_all/', views.delete_all, name='delete_all'),
    path('/fix_count/', views.fix_count, name='fix_count'),
]