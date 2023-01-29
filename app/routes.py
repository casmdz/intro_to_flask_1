from app import app
from flask import render_template

@app.route('/')
def homePage():
    people = ['shoha', 'brandt', 'aubrey', 'and me']
    text = 'SENDING THIS FROM PYTHON'
    return render_template('index.html', people = people, my_text = text) 

#doesnt have to be "index" #sending the variable "people" 
# #you can access the KEY "TEXT" in index, people = people, my_test = text

@app.route('/contact')
def contactPage():
    return render_template('contact.html')