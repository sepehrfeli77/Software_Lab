from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.sql import func

db = SQLAlchemy()


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        vals = vars(self)
        return {attr: vals[attr] for attr in vals if 'instance_state' not in attr}

    def __repr__(self):
        return self.name


class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    national_id = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    prescriptions = db.relationship('Prescription', backref='doctor')
    create_time = db.Column(db.DateTime(timezone=True), default=func.now())

    def to_dict(self):
        vals = vars(self)
        return {attr: vals[attr] for attr in vals if 'instance_state' not in attr}

    def __repr__(self):
        return self.name

    
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    national_id =  db.Column(db.String(10), unique = True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    prescriptions = db.relationship('Prescription', backref='patient')
    create_time = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)

    def to_dict(self):
        vals = vars(self)
        return {attr: vals[attr] for attr in vals if 'instance_state' not in attr}

    def __repr__(self):
        return self.name


class Prescription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    drugs = db.Column(db.String(100), nullable=False)
    comment = db.Column(db.String(50), nullable=True)
    create_time = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)

    def to_dict(self):
        vals = vars(self)
        return {attr: vals[attr] for attr in vals if 'instance_state' not in attr}

    def __repr__(self):
        return f"{self.doctor_id} -> {self.patient_id}"
