import os, sys
import utill
from flask import (
    Flask, 
    request, 
    redirect, 
    url_for, 
    render_template,
    flash,
    jsonify
)
from werkzeug import secure_filename

import hashlib

# get the absolute path for uploading files
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads')

ALLOWED_EXTENSIONS = set(['txt', 'csv', 'tsv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html',
                           title='d3 Notebook by ODE')

from flask import send_from_directory

# get the file name of the uploaded file
# return redirect(url_for('uploaded_file',
#                                    filename=filename))
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/upload_ajax', methods = ['POST'])
def upload_file_ajax():
    if request.method == 'POST':
        file = request.files['file']
        print file.filename        
        if file and allowed_file(file.filename):
            filename = utill.hashFileName(file.filename) 
            filename = secure_filename(filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #return render_template('index.html',
            #              title='d3 Notebook by ODE, UPLOADED!',
            #              upload_data_url = url_for('uploaded_file',
            #                                        filename=filename) )

            return jsonify(upload_data_url = url_for('uploaded_file',
                                                     filename = filename))
        else:
            return jsonify(error = 'Illegal extension. Supported types: ' + utill.listIterableContents(ALLOWED_EXTENSIONS))

@app.route('/static/ace/<filename>')
def ace(filename):
    """ create endpoint for ace js
    """
    pass


#from app import views
