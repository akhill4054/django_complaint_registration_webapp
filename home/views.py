from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime
from webapp.firebase import firestore


def home(request):
    template = loader.get_template('home/home.html')

    total_complaints = firestore.total_complaints()

    return HttpResponse(template.render({'total_complaints': total_complaints}, request))

def browse(request):
    template = loader.get_template('browse/browse.html')
    return HttpResponse(template.render({}, request))

def about(request):
    template = loader.get_template('about/about.html')
    return HttpResponse(template.render({}, request))

def invalid(request):
    template = loader.get_template('home/invalid.html')
    return HttpResponse(template.render({}, request))