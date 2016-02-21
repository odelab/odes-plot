from flask import render_template, flash, redirect
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='d3 Notebook by ODE')
@app.route('/static/ace/<filename>')
def ace(filename):
    """ create endpoint for ace js
    """
    pass
