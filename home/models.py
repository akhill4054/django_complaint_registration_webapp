from django.db import models
import firestore_model
from datetime import datetime


class Complaint:
    id = None

    def __init__(self, cat, service, date, desc, applicant):
        self.cat = cat
        self.service = service
        self.date = date
        self.reg_date_time = datetime.utcnow().isoformat()
        self.desc = desc
        self.applicant = applicant

    @classmethod
    def from_dict(self, data):
        complaint = Complaint(
            data['cat'],
            data['service'],
            '-'.join(data['date'].split('-')[::-1]),
            data['desc'],
            Applicant.from_dict(data['applicant'])
        )

        complaint.id = data['id']
        complaint.reg_date_time = data['reg_date_time']

        return complaint

    def asdict(self):
        assert (self.id != None), "Complaint document id was null"

        return {
            'id': self.id,
            'cat': self.cat,
            'service': self.service,
            'date': self.date,
            'reg_date_time': self.reg_date_time,
            'desc': self.desc,
            'applicant': self.applicant.asdict()
        }


class Applicant:
    def __init__(self, name_prefix, name, email, contact, city, pin):
        self.name_prefix = name_prefix
        self.name = name
        self.email = email
        self.contact = contact
        self.city = city
        self.pin = pin

    @classmethod
    def from_dict(self, data):
        return Applicant(
            data['name_prefix'],
            data['name'],
            data['email'],
            data['contact'],
            data['city'],
            data['pin']
        )

    def asdict(self):
        return {
            'name_prefix': self.name_prefix,
            'name': self.name,
            'email': self.email,
            'contact': self.contact,
            'city': self.city,
            'pin': self.pin
        }