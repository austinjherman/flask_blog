from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate

app = Flask(__name__.split('.')[0])
app.config.from_object('settings')

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from blog import views
from author import views




