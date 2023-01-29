from app import app
from flask import render_template
import os

@app.route('/')
def homePage():
    people = ['shoha', 'brandt', 'aubrey', 'and me']
    text = 'SENDING THIS FROM PYTHON'
    return render_template('index.html', people = people, my_text = text) 

@app.route('/contact')
def contactPage():
    return render_template('contact.html')

@app.route('/about')
def aboutPage():
    return render_template('about.html')