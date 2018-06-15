from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ba Nyar Naing'}
    posts = [
            {
                'author': {'username': 'Ba Nyar'},
                'body': 'Beautiful day in Myanmar'
            },
            {
                'author': {'username': 'Shwe Wah'},
                'body': 'The Catvengers movie was so cool!'
            }
        ]
    return render_template('index.html', title='Home', user=user, posts=posts)
