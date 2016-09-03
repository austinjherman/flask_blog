from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate
from flask.ext.markdown import Markdown
from flask_uploads import UploadSet, configure_uploads, IMAGES


app = Flask(__name__.split('.')[0])
app.config.from_object('settings')

db = SQLAlchemy(app)

migrate = Migrate(app, db)

Markdown(app)

uploaded_images = UploadSet('images', IMAGES)
configure_uploads(app, uploaded_images)

from blog import views
from author import views




