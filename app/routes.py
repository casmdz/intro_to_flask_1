from app import app
from flask import render_template

@app.route('/')
def homePage():
    people = ['shoha', 'brandt', 'aubrey', 'and me']
    text = 'SENDING THIS FROM PYTHON'
    favorite_txt = 'Be sure to check out my top 5 artists'
    return render_template('index.html', people = people, my_text = text, favorite_txt = favorite_txt) 

#doesnt have to be "index" #sending the variable "people" 
# #you can access the KEY "TEXT" in index, people = people, my_test = text

# @app.route('/favorite_5')
# def favorite_5():
#     favorites = ['Tyler the Creator', 'Men I Trust', 'Porcupine Tree', 'The Garden', 'TOKYOPILL']
#     return render_template('favorite_5.html', favorites = favorites) 


@app.route('/contact')
def contactPage():
    okay = 'placeholder'
    return render_template('contact.html', okay_text = okay)
