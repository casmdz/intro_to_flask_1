from app import app
from flask import render_template, request, redirect, url_for
from .forms import UserCreationForm
from .models import User
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

@app.route('/signup', methods=["GET", "POST"])
def signUpPage():
    form = UserCreationForm()
    print(request.method)
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            
            print(email, username, password)
            
            #add user to database
            user = User(username, email, password)
            print(user)
            user.saveToDB()
            
            return redirect(url_for('contactPage'))     #contactPage = give the name of the function
    
    return render_template('signup.html', form = form)