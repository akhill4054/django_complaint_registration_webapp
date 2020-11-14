import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from os import getcwd, path
from home.models import Complaint, Applicant


# Initializing firestore
PATH_TO_SERVICE_ACCOUNT_JSON = path.join(getcwd(), 'webapp/firebase', 'complaint-registration-c8304-firebase-adminsdk-ro5vg-c316961538.json')

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
        doc_ref.set({'total_complaints': 0})
        return 0

# Use this to increment or decrement total number of complaints
def __incr_dcr_complaint_count(incr = True):
    doc_ref = db.collection(u'meta-data').document('meta-inf')
    
    updated_dict = doc_ref.get().to_dict()

    if incr: updated_dict['total_complaints'] = updated_dict['total_complaints'] + 1
    else: updated_dict['total_complaints'] = updated_dict['total_complaints'] - 1

    doc_ref.set(updated_dict)

def post_complaint(complaint):
    doc_ref = db.collection(u'complaints').document()
    # Setting document id
    complaint.id = doc_ref.id
    doc_ref.set(complaint.asdict())
    # Incrementing total complaints count
    __incr_dcr_complaint_count()

def get_complaint(id):
    docs = db.collection(u'complaints').where('id', '==', id).stream()
    
    for doc in docs: return doc.to_dict()

    return None

def delete_complaint(id):
    db.collection(u'complaints').document(id).delete()
    # Decrementing total complaints count
    __incr_dcr_complaint_count(False)


# Admin
def delete_all():
    docs = db.collection(u'complaints').stream()
    deleted = 0
    # Deleting all docs
    for doc in docs:
        doc.reference.delete()
        deleted += 1
    
    # Uodating total complaints count
    doc_ref = db.collection(u'meta-data').document('meta-inf')
    
    updated_dict = doc_ref.get().to_dict()
    updated_dict['total_complaints'] = updated_dict['total_complaints'] - deleted

    doc_ref.set(updated_dict)


# Test methods
def __generate_complaint():
    return Complaint(
        'Texes',
        'CBI',
        '11/12/13',
        'Were ere reererer rere re woumbaba we',
        Applicant(
            name_prefix = 'Mr.',
            name = 'Joseph',
            email = 'asdasdbhsa@sd.com',
            contact = None,
            city = 'London',
            pin = '12345678'
        )
    )

def __populate():
    post_complaint(__generate_complaint())

def __test_query():
    hardcoded_id = "OEwhPhOGnaro0KZ5cAkw"
    print(f'**${get_complaint(hardcoded_id)}')