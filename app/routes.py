from app import app
from flask import render_template, request, abort
from werkzeug.utils import secure_filename
import os

@app.route('/')
@app.route('/index')
def hello_world():
   return 'Hello World'

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']

      filename = f.filename

      if filename != '':
         file_ext = os.path.splitext(filename)[1]

         if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)

         f.save(os.path.join(app.config['UPLOAD_PATH'], filename))

         
      return 'file uploaded successfully'


