import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from os import getcwd, path
from . models import Complaint, Applicant


# Initializing firestore
PATH_TO_SERVICE_ACCOUNT_JSON = path.join(getcwd(), 'complaint-registration-c8304-firebase-adminsdk-ro5vg-c316961538.json')

cred = credentials.Certificate(PATH_TO_SERVICE_ACCOUNT_JSON)

if not firebase_admin._apps: 
    firebase_admin.initialize_app(cred)

db = firestore.client()

def post_complaint(complaint):
    doc_ref = db.collection(u'complaints').document()
    # Setting document id
    complaint.id = doc_ref.id
    doc_ref.set(complaint.asdict())

def get_complaint(id):
    docs = db.collection(u'complaints').where('id', '==', id).stream()
    
    for doc in docs: return doc.to_dict()

    return None

def delete_document(id):
    db.collection(u'complaints').document(id).delete()

# Test methods
def generate_complaint():
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

def populate():
    post_complaint(generate_complaint())

def test_query():
    hardcoded_id = "OEwhPhOGnaro0KZ5cAkw"
    print(f'**${get_complaint(hardcoded_id)}')