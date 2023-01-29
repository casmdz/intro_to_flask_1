#init file... creating a module 

from flask import Flask
from config import Config #lowkey we could've put the code in this file, but shoha likes less clutter


app = Flask(__name__)
app.config.from_object(Config) #from this set all my settings

from . import routes