from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__.split('.')[0])
app.config.from_object('settings')

db = SQLAlchemy(app)

from blog import views
from author import views




