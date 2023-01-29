#init file... creating a module 

from flask import Flask
from config import Config 
from flask import render_template

app = Flask(__name__)
app.config.from_object(Config) #from this set all my settings

from . import routes