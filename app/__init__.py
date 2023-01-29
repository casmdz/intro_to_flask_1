#init file... creating a module 

from flask import Flask
from config import Config #lowkey we could've put the code in this file, but shoha likes less clutter
from flask import render_template

app = Flask(__name__)
app.config.from_object(Config) #from this set all my settings

from . import routes


@app.route('/favorite_5')
def favorite_5():
    favorites = ['Tyler the Creator', 'Men I Trust', 'Porcupine Tree', 'The Garden', 'TOKYOPILL']
    return render_template('favorite_5.html', favorites = favorites) 