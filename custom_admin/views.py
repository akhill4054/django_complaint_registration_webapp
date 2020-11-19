from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import webapp.firebase.firestore as db


# Create your views here.
def admin(request):
    template = loader.get_template('admin/admin_page.html')
    return HttpResponse(template.render({}, request))

def delete_complaint(request):
    if request.method == 'POST':
        complaint_id = request.POST['complaint_id']
        if complaint_id != None and complaint_id != "":
            db.delete_complaint(complaint_id)
    return HttpResponseRedirect('/admin//')

def delete_all(request):
    if request.method == 'POST':
        admin_code = request.POST['admin_code']
        if admin_code == "asdf1212345":
            db.delete_all(complaint_id)
    return HttpResponseRedirect('/admin//')

def fix_count(request):
    db.fix_counts()
    return HttpResponseRedirect('/admin//')