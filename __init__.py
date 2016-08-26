from flask import Flask

app = Flask(__name__.split('.')[0])
app.config.from_object('settings')

from home import views




