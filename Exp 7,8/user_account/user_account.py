from flask import Flask, request, g
from flask_sqlalchemy import SQLAlchemy
from models import *
from flask.json import jsonify
from sqlalchemy.exc import IntegrityError
from http import HTTPStatus

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinic.sqlite3'

@app.before_first_request
def setup_db():
    db.init_app(app)
    db.create_all()

@app.route('/create_doctor', methods=['POST'])
def create_user():
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


if __name__ == "__main__":
    app.run(debug=True, port=8003)