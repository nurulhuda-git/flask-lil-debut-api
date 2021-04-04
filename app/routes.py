from app import app
from flask import request, abort, send_from_directory
from werkzeug.utils import secure_filename
import os
from app.utils import ocr_utils as Utils
from app.models import response
from app.models.data import Data
from datetime import datetime

@app.route('/')
@app.route('/index')
def hello_world():
   return 'This is GRAMMAR Project API'

@app.route('/upload/<filter>', methods = ['GET', 'POST'])
def upload_file(filter):
   if request.method == 'POST':
      try:
         # Get current path
         root_url = request.url_root

         f = request.files['file']
         filename = f.filename
         ts = datetime.now().strftime("%Y-%m-%d-%H%M%S_")

         if filename != '':
            # Get file ext
            file_ext = os.path.splitext(filename)[1]

            # Check if file extension is correct
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
               return response.badRequest(None, 'File not supported')

            # Write into a file in UPLOAD_PATH path
            f.save(os.path.join(app.config['UPLOAD_PATH'], secure_filename(ts + filename)))
            # Convert to Black White
            text = Utils.convert_to_bw(filename,filter)
            # Cast to Data
            data = Data(root_url + 'uploads/' + ts + filename, text)
         return response.ok(data.toJSON(), 'Success')
      except Exception as e:
         print(e)
         return response.internalServerError(None, e.__str__)

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join(app.config['ROOT_PATH'], app.config['UPLOAD_PATH'])
    return send_from_directory(directory=uploads, filename=secure_filename(filename))

