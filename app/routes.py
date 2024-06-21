from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    user = {'user_name': 'Deepak'}
    dummy_details = [
    {
        'author': {'user_name':'Ankita'},
        'recipe_name':'Sabudana Khichdi'
    },
    {
        'author': {'user_name':'Deepak'},
        'recipe_name':'Poha'
    }
    ]
    return render_template('index.html',title='Recipe Khajana',user=user,dummy_details=dummy_details)