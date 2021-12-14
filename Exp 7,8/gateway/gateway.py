import requests
from flask import Flask, request
from flask.json import jsonify
from requests.models import Response

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




@app.route('/doctor/sign_up/', methods=['POST'])
def doctor_signup():
    json = request.json
    response = requests.post(f"{account_service.url}/create_doctor", json=json)
    return response.content, response.status_code, response.headers.items()

@app.route('/patient/sign_up/', methods=['POST'])
def patient_signup():
    json = request.json
    response = requests.post(f"{account_service.url}/create_patient", json=json)
    return response.content, response.status_code, response.headers.items()

@app.route('/admin/sign_up/', methods=['POST'])
def admin_signup():
    json = request.json
    response = requests.post(f"{account_service.url}/create_admin", json=json)
    return response.content, response.status_code, response.headers.items()

@app.route('/doctor/sign_in', methods=['POST'])
def doctor_login():
    json = request.json
    response = requests.post(f"{account_service.url}/login/doctor/{json.get('national_id')}", json=json)
    return response.content, response.status_code, response.headers.items()

@app.route('/patient/sign_in', methods=['POST'])
def patient_login():
    json = request.json
    response = requests.post(f"{account_service.url}/login_patient", json=json)
    return response.content, response.status_code, response.headers.items()

@app.route('/admin/sign_in', methods=['POST'])
def admin_login():
    json = request.json
    response = requests.post(f"{account_service.url}/login_admin", json=json)
    return response.content, response.status_code, response.headers.items()

if __name__ == '__main__':
    app.run(debug=True, port=8001)