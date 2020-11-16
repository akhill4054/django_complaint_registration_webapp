from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import json
from django.contrib.staticfiles.storage import staticfiles_storage
from webapp.firebase import firestore
from home.models import Complaint, Applicant


def register(request):
    json_file = staticfiles_storage.open('files/categories.json')
    categories = json.load(json_file)
    json_file.close()

    template = loader.get_template('register/complaint_form.html')
    return HttpResponse(template.render({'categories': categories}, request))

def submit(request):
    if request.method == 'POST':
        try:
            # Form details
            category = request.POST['category']
            service = request.POST['service']
            date = request.POST['date']
            desc = request.POST['desc']
            # Sender/applicant details
            gender = request.POST['gender']
            name = request.POST['name']
            phone = request.POST['phone']
            email = request.POST['email']
            city = request.POST['city']
            pin = request.POST['pin']

            # Validating form data
            req_params = [category, service, date, desc, gender, name, email, city, pin]

            for param in req_params:
                if req_params == '': return HttpResponseRedirect('form_submission_failed')

            # Posting form
            applicant = Applicant(
                    gender, 
                    name, 
                    email, 
                    phone if phone != '' else None, 
                    city,
                    pin
                )

            complaint = Complaint(category, service, date, desc, applicant)

            complaint_id = firestore.post_complaint(complaint)
            
            return HttpResponseRedirect('submitted/doc_id={}'.format(complaint_id))
        except:
            return HttpResponseRedirect('form_submission_failed')
    else:
        return HttpResponseRedirect('form_submission_failed')

def form_submitted(request, complaint_id):
    template = loader.get_template('submitted/submitted.html')
    return HttpResponse(template.render({'complaint_id': complaint_id}, request))

def form_submission_failed(request):
    template = loader.get_template('submission_failed/submission_failed.html')
    return HttpResponse(template.render({}, request))