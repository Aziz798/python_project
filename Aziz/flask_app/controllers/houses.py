from flask_app import app
from flask import render_template ,redirect,request,flash,session
from flask_app.models.house import House


@app.route('/')
def home_page():
    return render_template('home_page.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard')





