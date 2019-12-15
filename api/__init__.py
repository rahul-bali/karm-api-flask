from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

# Init api
app = Flask(__name__)

app.config.from_pyfile('config.py')

# Database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://testadmin:root@localhost/flask-db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db & Init ma
db = SQLAlchemy(app)
ma = Marshmallow(app)

from api import routes
