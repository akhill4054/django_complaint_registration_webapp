from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime
from . import firestore


def home(request):
    template = loader.get_template('home/home.html')
    return HttpResponse(template.render({'time': datetime.datetime.now()}, request))

def invalid(request):
    template = loader.get_template('home/invalid.html')
    return HttpResponse(template.render({}, request))