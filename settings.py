import os

SECRET_KEY = 'so-secret'
DEBUG = True

# Database configuration goes here

# SQL ALCHEMY SETTINGS
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Flask uploads
UPLOADED_IMAGES_DEST = '/home/austin/compsci/flask_intro/flask_blog/static/images'
UPLOADED_IMAGES_URL  = '/static/images/'
