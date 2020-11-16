from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^$|^home$', views.home, name='home'),
    path('browse', views.browse, name='home'),
    path('browse/complaint/<str:complaint_id>', views.query_complaint, name='query_complaint'),
    path('browse/category/<str:category>', views.query_complaints, name='query_complaints'),
    path('about', views.about, name='home'),
]