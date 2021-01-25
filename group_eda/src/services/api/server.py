from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from test1 import give_json
import os

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "C": generate_password_hash("76"),
    "B": generate_password_hash("edades")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/')
@auth.login_required
def index():
    return "Your token id is : {token:C98453658}, you can log in http://apiprojectdata.ddns.net:5000/token:C98453658 to download de API endpoint"

@app.route("/token:C98453658")
def return_json():
    return give_json(countries=['Spain', 'Iran', 'Brazil', 'Mexico', 'Netherlands'])


if __name__ == '__main__':
    """Configuraciones de inicio del servidor"""
    port = int(os.environ.get('PORT', 5000))
    if port == 5000:
        app.debug = True
    app.run(host='82.223.204.128', port=port) 
    """Aqui estamos situando el host de la aplicacion como "localhost" """