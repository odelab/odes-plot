from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

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
    # because this function accepts POST, when 
    # user hit submit, the following if statement
    # will be run
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])
