from flask import Flask, request, jsonify, make_response, request, render_template, session, flash
import jwt
from datetime import datetime, timedelta
from functools import wraps
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from models import *
from flask.json import jsonify
from sqlalchemy.exc import IntegrityError
from http import HTTPStatus

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinic.sqlite3'
app.config['SECRET_KEY'] = 'Private_Key'

def token_required(func):
    # decorator factory which invoks update_wrapper() method and passes decorated function as an argument
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

@app.route('/login/doctor/<national_id>', methods=['POST'])
def doctor_login(national_id):
    doctor = Doctor.query.filter_by(national_id=national_id).first()
    if doctor is None:
        return {'message': 'Error: No doctor found'}, HTTPStatus.NOT_FOUND
    if request.json['password'] == doctor.password:
        session['logged_in'] = True

        token = jwt.encode({
            'doctor': national_id,
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

@app.route('/doctor/show_profile/<national_id>', methods=['GET'])
@token_required
def show_doctor_profile(national_id):
    token = request.headers.get('token')
    data = jwt.decode(token, app.config['SECRET_KEY'])
    if data["doctor"] == national_id:
        doctor = Doctor.query.filter_by(national_id=national_id).first()
        return jsonify(doctor.to_dict())
    else:
        return jsonify({"message":"Invalid access"})

@app.route('/admin/show_doctors', methods=['GET'])
@token_required
def show_doctors():
    token = request.headers.get('token')
    data = jwt.decode(token, app.config['SECRET_KEY'])
    admin = Admin.query.all()[0]
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
    if data["admin"] == admin.name:
        return jsonify([u.to_dict() for u in Patient.query.all()])
    else:
        return jsonify({"message":"Invalid access"})


if __name__ == "__main__":
    app.run(debug=True, port=8003)