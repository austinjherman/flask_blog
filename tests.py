# Set the path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import sqlalchemy
from flask.ext.sqlalchemy import SQLAlchemy

from flask_blog import app, db
from author.models import *
from blog.models import *

##############################################################################################

## Constants for testing

##############################################################################################

# Blog

BLOG_NAME     = 'Test Blog'
USER_FULLNAME = 'Test User'
USER_EMAIL    = 'test@gmail.com'
USERNAME      = 'test_user'
PASSWORD      = 'test'


##############################################################################################

## Setup class for testing

##############################################################################################

class UserTest(unittest.TestCase):
    def setUp(self):
        db_username = app.config['DB_USERNAME']
        db_password = app.config['DB_PASSWORD']
        db_host     = app.config['DB_HOST']
        self.db_uri = 'mysql+pymysql://%s:%s@%s/' % (db_username, db_password, db_host)
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['BLOG_DATABASE_NAME'] = 'test_blog'
        app.config['SQLALCHEMY_DATABASE_URI'] = self.db_uri + app.config['BLOG_DATABASE_NAME']
        engine = sqlalchemy.create_engine(self.db_uri)
        conn = engine.connect()
        conn.execute('commit')
        conn.execute('CREATE DATABASE ' + app.config['BLOG_DATABASE_NAME'])
        db.create_all()
        conn.close()
        self.app = app.test_client()

    def tearDown(self):
        db.session.remove()
        engine = sqlalchemy.create_engine(self.db_uri)
        conn = engine.connect()
        conn.execute('commit')
        conn.execute('DROP DATABASE ' + app.config['BLOG_DATABASE_NAME'])
        conn.close()

        
##############################################################################################

## Helper functions

##############################################################################################

    def create_blog(self):
        return self.app.post('/setup', data=dict(
            name     = BLOG_NAME,
            fullname = USER_FULLNAME,
            email    = USER_EMAIL,
            username = USERNAME,
            password = PASSWORD,
            confirm  = PASSWORD
            ), follow_redirects=True)

    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username = username,
            password = password
            ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def create_post(self):
        return self.app.post('/post', data=dict(
            title        = 'Post Title',
            body         = 'Post body.',
            new_category = 'New Category',
            ), follow_redirects=True)

    def delete_post(self, post):
        return self.app.get('/delete/' + str(post.id), follow_redirects=True)

    def edit_post(self, post):
        return self.app.post('/edit/' + str(post.id), data=dict(
            title        = 'Edited Post Title',
            body         = 'Edited post body',
            new_category = 'Edited post category'
            ), follow_redirects=True)
    
    def create_comment(self, post):
        return self.app.post('/article/' + post.slug, data=dict(
            body = 'This is a comment'
            ), follow_redirects=True)

    def delete_comment(self, comment):
        return self.app.get('/delete-comment/' + str(comment.id), follow_redirects=True)


#############################################################################################

## Testing functions

#############################################################################################

    def test_create_blog(self):
        rv = self.create_blog()
        assert 'Blog created' in str(rv.data)

    def test_login_logout(self):
        self.create_blog()
        rv = self.login(USERNAME, PASSWORD)
        assert 'User ' + USERNAME + ' logged in' in str(rv.data)
        rv = self.logout()
        assert 'User logged out' in str(rv.data)
        rv = self.login(USERNAME, 'wrong password')
        assert 'Incorrect username and password' in str(rv.data)

    def test_create_delete_post(self):
        self.create_blog()
        self.login(USERNAME, PASSWORD)
        rv = self.create_post()
        post = Post.query.first()
        assert 'Posted by' in str(rv.data)
        rv = self.delete_post(post)
        assert 'Article deleted' in str(rv.data)

    def test_edit_post(self):
        self.create_blog()
        self.login(USERNAME, PASSWORD)
        self.create_post()
        post = Post.query.first()
        rv = self.edit_post(post)
        assert 'Posted by' in str(rv.data) and 'Edited Post' in str(rv.data)

    def test_create_delete_comment(self):
        self.create_blog()
        self.login(USERNAME, PASSWORD)
        self.create_post()
        post = Post.query.first()
        rv = self.create_comment(post)
        assert 'This is a comment' in str(rv.data)
        comment = Comment.query.first()
        rv = self.delete_comment(comment)
        assert 'Comment deleted'
        
        

        
if __name__ == '__main__':
    unittest.main()
        
