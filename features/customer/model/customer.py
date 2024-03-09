from datetime import datetime

from sqlalchemy import DateTime
from werkzeug.security import generate_password_hash

from features.repo import db


class CustomerModel(db.Model):
    __tablename__ = "customers"

    customer_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    dob = db.Column(DateTime, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    aadhar_number = db.Column(db.String(12), nullable=False)
    registration_date = db.Column(DateTime)
    mobile_no = db.Column(db.String(10), nullable=False)

    @property
    def json(self):
        return {
            'name': self.name,
            'dob': self.dob.strftime("%d-%m-%Y"),
            'email': self.email,
            'aadhar_number': self.aadhar_number,
            'registration_date': self.registration_date.strftime("%d-%m-%Y"),
            'mobile_no': self.mobile_no,
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def create(cls, args):
        return cls(username=args["username"],
                   password=(generate_password_hash(
                       args["password"], method="pbkdf2:sha256"
                   )),
                   name=args["name"],
                   dob=datetime.strptime(args["dob"], "%d-%m-%Y"),
                   email=args["email"],
                   aadhar_number=args["aadhar_number"],
                   registration_date=datetime.strptime(args["registration_date"], "%d-%m-%Y") if args.get(
                       "registration_date", None) else datetime.now(),
                   mobile_no=args["mobile_no"])
