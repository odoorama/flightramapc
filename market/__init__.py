from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '770b4c1042e02a50e52b88c1'

from market import routes




