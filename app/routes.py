from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'user_name': 'Deepak'}
    dummy_details = [
    {
        'author': {'user_name':'Ankita'},
        'post_name':'Flask is awesome'
    },
    {
        'author': {'user_name':'Deepak'},
        'post_name':'I am thinking to take some project ideas from Freelancer'
    }
    ]
    return render_template('index.html',title='Home Page - Calm Crow',user=user,dummy_details=dummy_details)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title='Sign in', form=form)