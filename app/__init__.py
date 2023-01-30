#init file... creating a module 

from flask import Flask
from config import Config 
from flask import render_template
from .models import db
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config) #from this set all my settings

db.init_app(app)
migrate = Migrate(app,db)

from . import routes
from . import models  