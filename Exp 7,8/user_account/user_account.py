from flask import Flask, request, jsonify, make_response, request, render_template, session, flash
import jwt
from datetime import datetime, timedelta
from functools import wraps
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from models import *
#from user_account.models import *

from flask.json import jsonify
from sqlalchemy.exc import IntegrityError
from http import HTTPStatus

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinic.db'
app.config['SECRET_KEY'] = 'Private_Key'


def token_required(func):
    # decorator factory which invokes update_wrapper() method and passes decorated function as an argument
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.headers.get('token')
        if not token:
            return jsonify({'Alert!': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'Message': 'Invalid token'}), 403
        return func(*args, **kwargs)
    return decorated


@app.before_first_request
def setup_db():
    db.init_app(app)
    db.create_all()


@app.route('/create_doctor', methods=['POST'])
def create_doctor():
    data = request.json

    doctor = Doctor(name=data.get('name'),
                password=data.get('password'),
                national_id=data.get('national_id'))

    try:
        db.session.add(doctor)
        db.session.commit()
        return {'message': 'Success'}, HTTPStatus.CREATED

    except IntegrityError as e:
        if 'UNIQUE' in str(e):
            return {'message': 'Error: national id already exists'}, HTTPStatus.CONFLICT
        else:
            return {'message': 'Error: bad request error'}, HTTPStatus.BAD_REQUEST


@app.route('/create_patient', methods=['POST'])
def create_patient():
    data = request.json

    patient = Patient(name=data.get('name'),
                password=data.get('password'),
                national_id=data.get('national_id'))

    try:
        db.session.add(patient)
        db.session.commit()
        return {'message': 'Success'}, HTTPStatus.CREATED

    except IntegrityError as e:
        if 'UNIQUE' in str(e):
            return {'message': 'Error: national id already exists'}, HTTPStatus.CONFLICT
        else:
            return {'message': 'Error: bad request error'}, HTTPStatus.BAD_REQUEST


@app.route('/create_admin', methods=['POST'])
def create_admin():
    data = request.json

    admin = Admin(name=data.get('name'),
                password=data.get('password'))

    if len(Admin.query.all()) == 0:
        try:
            db.session.add(admin)
            db.session.commit()
            return {'message': 'Success'}, HTTPStatus.CREATED
        except:
            return {'message': 'Error: bad request error'}, HTTPStatus.BAD_REQUEST
    else:
        return {'message': 'System already has an admin'}, HTTPStatus.FORBIDDEN


@app.route('/login/doctor', methods=['POST'])
def doctor_login():
    data = request.json
    national_id = data.get('national_id')
    password = data.get('password')

    doctor = Doctor.query.filter_by(national_id=national_id).first()
    if doctor is None:
        return {'message': 'Error: No doctor found'}, HTTPStatus.NOT_FOUND
    if password == doctor.password:
        session['logged_in'] = True

        token = jwt.encode({
            'doctor': national_id,
            'expiration': str(datetime.utcnow() + timedelta(seconds=1200))
        },
            app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('utf-8')})
    else:
        return {'message': 'Password is wrong'}, HTTPStatus.FORBIDDEN

@app.route('/login/patient', methods=['POST'])
def patient_login():
    data = request.json
    national_id = data.get('national_id')
    password = data.get('password')

    patient = Patient.query.filter_by(national_id=national_id).first()
    if patient is None:
        return {'message': 'Error: No patient found'}, HTTPStatus.NOT_FOUND
    if password == patient.password:
        session['logged_in'] = True

        token = jwt.encode({
            'patient': national_id,
            'expiration': str(datetime.utcnow() + timedelta(seconds=1200))
        },
            app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('utf-8')})
    else:
        return {'message': 'Password is wrong'}, HTTPStatus.FORBIDDEN

@app.route('/login/admin', methods=['POST'])
def admin_login():
    admin = Admin.query.all()[0]
    if admin is None:
        return {'message': 'Error: No admin register in the system'}, HTTPStatus.NOT_FOUND
    if request.json["name"] == admin.name and request.json['password'] == admin.password:
        session['logged_in'] = True

        token = jwt.encode({
            'admin': admin.name,
            'expiration': str(datetime.utcnow() + timedelta(seconds=1200))
        },
            app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('utf-8')})
    else:
        return {'message': 'Password is wrong'}, HTTPStatus.FORBIDDEN


@app.route('/doctor/show_profile', methods=['GET'])
@token_required
def show_doctor_profile():
    token = request.headers.get('token')
    data = jwt.decode(token, app.config['SECRET_KEY'])
    national_id = data['doctor']
    doctor = Doctor.query.filter_by(national_id=national_id).first()
    if doctor is not None:
        return jsonify(doctor.to_dict())
    else:
        return jsonify({"message":"Invalid access"})

@app.route('/patient/show_profile', methods=['GET'])
@token_required
def show_patient_profile():
    token = request.headers.get('token')
    data = jwt.decode(token, app.config['SECRET_KEY'])
    national_id = data['patient']
    patient = Patient.query.filter_by(national_id=national_id).first()
    if patient is not None:
        return jsonify(patient.to_dict())
    else:
        return jsonify({"message":"Invalid access"})


@app.route('/admin/show_doctors', methods=['GET'])
@token_required
def show_doctors():
    token = request.headers.get('token')
    data = jwt.decode(token, app.config['SECRET_KEY'])
    admin = Admin.query.all()[0]
    if data.get("admin") is None:
        return jsonify({"message":"You are not admin"})
    if data["admin"] == admin.name:
        return jsonify([u.to_dict() for u in Doctor.query.all()])
    else:
        return jsonify({"message":"Invalid access"})


@app.route('/admin/show_patients', methods=['GET'])
@token_required
def show_patients():
    token = request.headers.get('token')
    data = jwt.decode(token, app.config['SECRET_KEY'])
    admin = Admin.query.all()[0]
    if data.get("admin") is None:
        return jsonify({"message":"You are not admin"})
    if data["admin"] == admin.name:
        return jsonify([u.to_dict() for u in Patient.query.all()])
    else:
        return jsonify({"message":"Invalid access"})

@app.route('/admin/show_prescriptions', methods=['GET'])
@token_required
def show_prescriptions():
    token = request.headers.get('token')
    data = jwt.decode(token, app.config['SECRET_KEY'])
    admin = Admin.query.all()[0]
    if data.get("admin") is None:
        return jsonify({"message":"You are not admin"})
    if data["admin"] == admin.name:
        return jsonify([u.to_dict() for u in Prescription.query.all()])
    else:
        return jsonify({"message":"Invalid access"})


@app.route('/doctor/indication', methods=['POST'])
@token_required
def indication():
    data = request.json

    doctor = Doctor.query.filter_by(national_id=data.get('doctor')).first().to_dict()
    if doctor is None:
        return {'message': 'Error: No such doctor'}, HTTPStatus.NOT_FOUND
    patient = Patient.query.filter_by(national_id=data.get('patient')).first().to_dict()
    if patient is None:
        return {'message': 'Error: No such patient'}, HTTPStatus.NOT_FOUND

    prescription = Prescription(
        doctor_id=doctor.get('id'),
        patient_id=patient.get('id'),
        drugs=data.get('drugs'),
        comment=data.get('comment'))

    try:
        db.session.add(prescription)
        db.session.commit()
        return {'message': 'Success'}, HTTPStatus.CREATED

    except IntegrityError as e:
        return {'message': 'Request Rejected'}


@app.route('/doctor/prescriptions', methods=['GET'])
@token_required
def dr_prescriptions():
    token = request.headers.get('token')
    data = jwt.decode(token, app.config['SECRET_KEY'])
    national_id = data['doctor']

    doctor = Doctor.query.filter_by(national_id=national_id).first().to_dict()
    if doctor is None:
        return {'message': 'Error: No such doctor'}, HTTPStatus.NOT_FOUND

    prescriptions = Prescription.query.filter_by(doctor_id=doctor['id']).all()
    if len(prescriptions) == 0:
        return {'message': 'No prescription'}, HTTPStatus.NOT_FOUND

    return jsonify([prescriptions[i].to_dict() for i in range(len(prescriptions))])


@app.route('/patient/prescriptions', methods=['GET'])
@token_required
def p_prescriptions():
    token = request.headers.get('token')
    data = jwt.decode(token, app.config['SECRET_KEY'])
    national_id = data['patient']

    patient = Patient.query.filter_by(national_id=national_id).first().to_dict()
    if patient is None:
        return {'message': 'Error: No such patient'}, HTTPStatus.NOT_FOUND

    prescriptions = Prescription.query.filter_by(patient_id=patient['id']).all()
    if len(prescriptions) == 0:
        return {'message': 'No prescription'}, HTTPStatus.NOT_FOUND

    return jsonify([prescriptions[i].to_dict() for i in range(len(prescriptions))])


@app.route('/admin/prescriptions', methods=['GET'])
@token_required
def a_prescriptions():
    token = request.headers.get('token')
    data = jwt.decode(token, app.config['SECRET_KEY'])
    admin = Admin.query.all()[0]
    if data.get("admin") is None:
        return jsonify({"message":"You are not admin"})

    if data["admin"] != admin.name:
        return jsonify({"message":"Invalid access"})
    prescriptions = Prescription.query.all()
    if len(prescriptions) == 0:
        return {'message': 'No prescription'}, HTTPStatus.NOT_FOUND

    return jsonify([prescriptions[i].to_dict() for i in range(len(prescriptions))])

@app.route('/admin/statistics/daily', methods=['GET'])
@token_required
def daily_stat():
    token = request.headers.get('token')
    data = jwt.decode(token, app.config['SECRET_KEY'])
    admin = Admin.query.all()[0]
    if data.get("admin") is None:
        return jsonify({"message":"You are not admin"})

    if data["admin"] != admin.name:
        return jsonify({"message":"Invalid access"})
    date = datetime.now()
    year = date.year
    day = date.day
    month = date.month

    begin_of_day = datetime(year, month, day, 0, 0 ,0)

    new_doctors = Doctor.query.filter(Doctor.create_time > begin_of_day).all()
    new_patients = Patient.query.filter(Patient.create_time > begin_of_day).all()
    new_prescriptions = Prescription.query.filter(Prescription.create_time > begin_of_day).all()
    new_doctors_size = len(new_doctors)
    new_patients_size = len(new_patients)
    new_prescriptions_size = len(new_prescriptions)
    result1 = new_doctors + new_patients + new_prescriptions + new_prescriptions
    result2 = [{
        "new_doctors_size":new_doctors_size,
        "new_patients_size":new_patients_size,
        "new_prescriptions_size":new_prescriptions_size
    }]
    result1 = [u.to_dict() for u in result1]
    print(result1)
    merged_dict = result1 + result2
    return jsonify(merged_dict)

if __name__ == "__main__":
    app.run(debug=True, port=8003)
