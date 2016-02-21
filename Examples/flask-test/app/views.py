from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'J'}
    # array of json objects
    posts = [
        {
            'author': {'nickname': 'Fermi'},
            'body': 'Dimensional analysis is good!'
        },
        {
            'author': {'nickname': 'Bosch'},
            'body': 'I make ABS for Audi.'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts = posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', 
                           title='Sign In',
                           form=form)
