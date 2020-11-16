from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime
from webapp.firebase import firestore
from .models import Complaint
from django.contrib.staticfiles.storage import staticfiles_storage
import json
from datetime import datetime


def home(request):
    template = loader.get_template('home/home.html')

    total_complaints = firestore.total_complaints()

    return HttpResponse(template.render({'total_complaints': total_complaints}, request))


def browse(request):
    json_file = staticfiles_storage.open('files/categories.json')
    categories = json.load(json_file)
    json_file.close()

    complaints_meta_inf = firestore.total_complaints_meta_inf()

    template = loader.get_template('browse/browse.html')

    return HttpResponse(template.render({
        'categories': categories,
        'meta': complaints_meta_inf,
    }, request))


def about(request):
    template = loader.get_template('about/about.html')
    return HttpResponse(template.render({}, request))


def invalid(request):
    template = loader.get_template('home/invalid.html')
    return HttpResponse(template.render({}, request))


# Quries
def query_complaint(request, complaint_id):
    # Fetching queried complaint
    complaint = firestore.get_complaint(complaint_id)

    template = loader.get_template('query/complaint.html')
    return HttpResponse(template.render({
        'complaint_id': complaint_id,
        'reg_date_time': complaint.reg_date_time if complaint else None,
        'complaint': complaint,
    }, request))


def query_complaints(request, category):
    template = loader.get_template('query/complaints.html')
    return HttpResponse(template.render({
        'complaints': None,
        'category': category.lower,
    }, request))
