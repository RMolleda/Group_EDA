from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from test1 import give_json
import os

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "F": generate_password_hash("2001"),
    "C": generate_password_hash("2000")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/')
@auth.login_required
def index():
    return give_json('Spain', 'Iran', 'Brazil', 'Mexico', 'Netherlands')


if __name__ == '__main__':
    """Configuraciones de inicio del servidor"""
    port = int(os.environ.get('PORT', 6060))
    if port == 6060:
        app.debug = True
    app.run(host='0.0.0.0', port=port) 
    """Aqui estamos situando el host de la aplicacion como "localhost" """
app.run()
