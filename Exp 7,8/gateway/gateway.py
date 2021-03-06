import requests
from flask import Flask, request
from flask.json import jsonify
from requests.models import Response
from flask_swagger_ui import get_swaggerui_blueprint


class Service:
    total_services = 0

    def __init__(self, name, address, port):
        self.name = name
        self.url = f"http://{address}:{port}"
        Service.total_services += 1
        self.id = Service.total_services


app = Flask(__name__)
account_service = Service("Account Service", "127.0.0.1", 8003)
app.config['SECRET_KEY'] = 'Private_Key'

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
  SWAGGER_URL,
  API_URL,
  config={
    'app_name':'API Document for EXP 7,8'
  }
)
app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)


@app.route('/doctor/sign_up', methods=['POST'])
def doctor_signup():
    json = request.json
    response = requests.post(f"{account_service.url}/create_doctor", json=json)
    return response.content, response.status_code, response.headers.items()


@app.route('/patient/sign_up', methods=['POST'])
def patient_signup():
    json = request.json
    response = requests.post(f"{account_service.url}/create_patient", json=json)
    return response.content, response.status_code, response.headers.items()


@app.route('/admin/sign_up', methods=['POST'])
def admin_signup():
    json = request.json
    response = requests.post(f"{account_service.url}/create_admin", json=json)
    return response.content, response.status_code, response.headers.items()


@app.route('/doctor/sign_in', methods=['POST'])
def doctor_login():
    json = request.json
    response = requests.post(f"{account_service.url}/login/doctor", json=json)
    return response.content, response.status_code, response.headers.items()


@app.route('/patient/sign_in', methods=['POST'])
def patient_login():
    json = request.json
    response = requests.post(f"{account_service.url}/login/patient", json=json)
    return response.content, response.status_code, response.headers.items()


@app.route('/admin/sign_in', methods=['POST'])
def admin_login():
    json = request.json
    response = requests.post(f"{account_service.url}/login/admin", json=json)
    return response.content, response.status_code, response.headers.items()


@app.route('/doctor/show_profile', methods=['GET'])
def doctor_show_profile():
    json = request.json
    response = requests.get(f"{account_service.url}/doctor/show_profile", json=json, headers=request.headers)
    return response.content, response.status_code, response.headers.items()

@app.route('/patient/show_profile', methods=['GET'])
def patient_show_profile():
    json = request.json
    response = requests.get(f"{account_service.url}/patient/show_profile", json=json, headers=request.headers)
    return response.content, response.status_code, response.headers.items()


@app.route('/doctors', methods=['GET'])
def show_doctors():
    json = request.json
    response = requests.get(f"{account_service.url}/admin/show_doctors", json=json, headers=request.headers)
    return response.content, response.status_code, response.headers.items()


@app.route('/patients', methods=['GET'])
def show_patients():
    json = request.json
    response = requests.get(f"{account_service.url}/admin/show_patients", json=json, headers=request.headers)
    return response.content, response.status_code, response.headers.items()

@app.route('/prescriptions', methods=['GET'])
def show_prescriptions():
    json = request.json
    response = requests.get(f"{account_service.url}/admin/show_prescriptions", json=json, headers=request.headers)
    return response.content, response.status_code, response.headers.items()


@app.route('/doctor/prescription/indicate', methods=['POST'])
def indicate_prescription():
    json = request.json
    response = requests.post(f"{account_service.url}/doctor/indication", json=json, headers=request.headers)
    return response.content, response.status_code, response.headers.items()


@app.route('/doctor/prescription/list', methods=['GET'])
def doctor_prescriptions():
    json = request.json
    response = requests.get(f"{account_service.url}/doctor/prescriptions", json=json, headers=request.headers)
    return response.content, response.status_code, response.headers.items()


@app.route('/patient/prescription/list', methods=['GET'])
def patient_prescriptions():
    json = request.json
    response = requests.get(f"{account_service.url}/patient/prescriptions", json=json, headers=request.headers)
    return response.content, response.status_code, response.headers.items()


@app.route('/admin/prescription/list', methods=['GET'])
def admin_prescriptions():
    json = request.json
    response = requests.get(f"{account_service.url}/admin/prescriptions", json=json, headers=request.headers)
    return response.content, response.status_code, response.headers.items()

@app.route('/admin/stat', methods=['GET'])
def admin_stat():
    json = request.json
    response = requests.get(f"{account_service.url}/admin/statistics/daily", json=json, headers=request.headers)
    return response.content, response.status_code, response.headers.items()


if __name__ == '__main__':
    app.run(debug=True, port=8001)
