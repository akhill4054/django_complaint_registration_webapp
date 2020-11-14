from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
from django.contrib.staticfiles.storage import staticfiles_storage


def register(request):
    json_file = staticfiles_storage.open('files/categories.json')
    categories = json.load(json_file)
    json_file.close()

    template = loader.get_template('register/complaint_form.html')
    return HttpResponse(template.render({'categories': categories}, request))