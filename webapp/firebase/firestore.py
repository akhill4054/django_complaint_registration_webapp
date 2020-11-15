import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from os import getcwd, path
from home.models import Complaint, Applicant
from django.contrib.staticfiles.storage import staticfiles_storage
import json


# Initializing firestore
PATH_TO_SERVICE_ACCOUNT_JSON = path.join(getcwd(
), 'webapp/firebase', 'complaint-registration-c8304-firebase-adminsdk-ro5vg-c316961538.json')

cred = credentials.Certificate(PATH_TO_SERVICE_ACCOUNT_JSON)

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()


def total_complaints():
    doc_ref = db.collection(u'meta-data').document('meta-inf')
    doc = doc_ref.get()

    if doc.exists:
        return doc.to_dict()['total_complaints']
    else:
        json_file = staticfiles_storage.open('files/categories.json')
        categories = json.load(json_file)
        json_file.close()

        dict = {'total_complaints': 0}

        for cat in categories:
            dict[cat] = 0
        doc_ref.set(dict)

        return 0

def total_complaints_meta_inf():
    doc_ref = db.collection(u'meta-data').document('meta-inf')
    return doc_ref.get().to_dict()

# Use this to increment or decrement total number of complaints
def __incr_dcr_complaint_count(incr, category):
    doc_ref = db.collection(u'meta-data').document('meta-inf')

    updated_dict = doc_ref.get().to_dict()

    if incr:
        updated_dict[category] = updated_dict[category] + 1
        updated_dict['total_complaints'] = updated_dict['total_complaints'] + 1
    else:
        updated_dict[category] = updated_dict[category] - 1
        updated_dict['total_complaints'] = updated_dict['total_complaints'] - 1

    doc_ref.set(updated_dict)


def post_complaint(complaint):
    doc_ref = db.collection(u'complaints').document()
    # Setting document id
    complaint.id = doc_ref.id
    dict = complaint.asdict()
    doc_ref.set(dict)
    # Incrementing total complaints count
    __incr_dcr_complaint_count(True, dict['cat'])


def get_complaint(id):
    docs = db.collection(u'complaints').where('id', '==', id).stream()
    for doc in docs:
        return doc.to_dict()
    return None


def delete_complaint(id):
    doc_ref = db.collection(u'complaints').document(id)
    # Decrementing total complaints count
    __incr_dcr_complaint_count(False, doc_ref.get().to_dict()['cat'])
    # Deleting doc
    doc_ref.delete()


# Admin
def delete_all():
    docs = db.collection(u'complaints').stream()
    deleted = 0

    # Getting meta-inf doc
    meta_doc_ref = db.collection(u'meta-data').document('meta-inf')
    updated_meta_dict = meta_doc_ref.get().to_dict()

    # Deleting all docs
    for doc in docs:
        cat = doc.to_dict()['cat']
        updated_meta_dict[cat] = updated_meta_dict[cat] - 1
        doc.reference.delete()
        deleted += 1

    # Updating total complaints count
    updated_meta_dict['total_complaints'] = updated_meta_dict['total_complaints'] - deleted
    meta_doc_ref.set(updated_meta_dict)

def fix_counts():
    docs = db.collection(u'complaints').stream()

    # Getting meta-inf doc
    meta_doc_ref = db.collection(u'meta-data').document('meta-inf')
    updated_meta_dict = meta_doc_ref.get().to_dict()
    # Resetting meta-inf
    for k, v in updated_meta_dict.items():
        updated_meta_dict[k] = 0

    count = 0
    for doc in docs:
        cat = doc.to_dict()['cat']
        updated_meta_dict[cat] = updated_meta_dict[cat] + 1
        count += 1
    
    updated_meta_dict['total_complaints'] = count

    meta_doc_ref.set(updated_meta_dict)

# Test methods
def __generate_complaint(category):
    return Complaint(
        category,
        'CBI',
        '11/12/13',
        'Were ere reererer rere re woumbaba we',
        Applicant(
            name_prefix='Mrs.',
            name='Pheobe Buffay',
            email='asdasdbhsa@sd.com',
            contact=None,
            city='London',
            pin='12345678'
        )
    )

from random import randrange

def __populate(count):
    json_file = staticfiles_storage.open('files/categories.json')
    categories = json.load(json_file)
    json_file.close()

    for i in range(count):
        category = categories[randrange(0, len(categories))]
        post_complaint(__generate_complaint(category))

# __populate(30)