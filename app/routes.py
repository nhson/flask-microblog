from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Hoang Son'}
    posts = [
        {
            'author':{'username': 'John'},
            'body': 'Beautiful day in Vietnam'
        },
        {
            'author':{'username': 'Sony'},
            'body': 'Beautiful day in Canada'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)