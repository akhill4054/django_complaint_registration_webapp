from django.urls import path
from . import views


urlpatterns = [
    path('register', views.register, name='register'),
    path('submit', views.submit, name='submit'),
    path('submitted/doc_id=<str:complaint_id>', views.form_submitted, name='submitted'),
    path('form_submission_failed', views.form_submission_failed, name='submission_failed'),
]