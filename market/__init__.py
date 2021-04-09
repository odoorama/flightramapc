from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '770b4c1042e02a50e52b88c1'
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from market import routes




