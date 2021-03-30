from app import app
from flask import request, abort, send_from_directory
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

         f.save(os.path.join(app.config['UPLOAD_PATH'], secure_filename(filename)))
      return 'file uploaded successfully', 201

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join(app.config['ROOT_PATH'], app.config['UPLOAD_PATH'])
    return send_from_directory(directory=uploads, filename=secure_filename(filename))

