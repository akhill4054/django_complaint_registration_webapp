from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime
from webapp.firebase import firestore
from django.contrib.staticfiles.storage import staticfiles_storage
import json


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
