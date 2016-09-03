import os

SECRET_KEY = '\x0c\xd8\xd8\xa9S\x9d\x93\xac5\xca\x15RX\xb1\t\x07\x0c\xd1E\x0b\xbf\x1c\x98\x18'
DEBUG = True

# Database configuration
DB_USERNAME = 'austin'
DB_PASSWORD = 'AH!4SMG'
BLOG_DATABASE_NAME = 'flask_blog'
DB_HOST = 'localhost'
DB_URI = 'mysql+pymysql://%s:%s@%s/%s' % (DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME)

# SQL ALCHEMY SETTINGS
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Flask uploads
UPLOADED_IMAGES_DEST = '/home/austin/compsci/flask_intro/flask_blog/static/images'
UPLOADED_IMAGES_URL  = '/static/images/'
