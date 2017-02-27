from app import db
from flask_table import Table, Col
from sqlalchemy import func

class VisiteeTable(Table):
    last_name = Col('Last Name', td_html_attrs=())
    first_name = Col('First Name')
    email = Col('Email')
    phone_number = Col('Phone Number')
    location = Col('Location')
    address = Col('Address')
    last_visit_date = Col('LastVisitDate')

class VisiteeModel(db.Model):

    __tablename__ = 'visitees'
    id = db.Column(db.Integer, primary_key = True)
    last_name = db.Column(db.String(64))
    first_name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    phone_number = db.Column(db.String(16))
    location = db.Column(db.String(64))
    address = db.Column(db.String(128))
    last_visit_date = db.Column(db.Date)

    def __init__(self, last_name, first_name, email, phone_number, location, address, last_visit_date):

        self.last_name = last_name
        self.first_name = first_name
        self.email = email
        self.phone_number = phone_number
        self.location = location    # the place, for example "Christopher House"
        self.address = address
        self.last_visit_date = last_visit_date

    def json(self):
        return {'visitee last name': self.last_name,
                'visitee first name': self.first_name,
                'email': self.email,
                'phone number': self.phone_number,
                'location': self.location,
                'address': self.address,
                'last visit date': self.last_visit_date
                }

    @classmethod
    def find_all_visitees(cls):
        return cls.query.all()

    @classmethod
    def find_longest_waiting_visitee(cls):
        return cls.query(func.min(VisiteeModel.last_visit_date))

    def add_visitee(self):
        # write json to file
        pass

    def remove_visitee(self):
        # remove visitor from json file
        pass

    def list_visitees_by_location(self):
        # if many visitees are in the same place (hospital, nursing home, etc.), list them
        pass

    def find_visitee_by_last_name(self):
        pass

