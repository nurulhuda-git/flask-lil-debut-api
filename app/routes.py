from app import app
from flask import request, abort, send_from_directory
from werkzeug.utils import secure_filename
import os
import pytesseract
import cv2
from skimage.filters import threshold_local
from PIL import Image
import numpy

@app.route('/')
@app.route('/index')
def hello_world():
   return 'Hello World'

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']

      filename = f.filename

      if filename != '':
         file_ext = os.path.splitext(filename)[1]

         if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)

         f.save(os.path.join(app.config['UPLOAD_PATH'], secure_filename(filename)))
         text = convert_to_bw(filename)
         print(text)
      return 'file uploaded successfully : ' + text, 201

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join(app.config['ROOT_PATH'], app.config['UPLOAD_PATH'])
    return send_from_directory(directory=uploads, filename=secure_filename(filename))


def bw_scanner(image):
   gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   T = threshold_local(gray, 21, offset = 5, method = "gaussian")
   return (gray > T).astype("uint8") * 255

def convert_to_bw(filename):
   src_filename = os.path.join(app.config['UPLOAD_PATH'], filename)
   dst_filename = os.path.join(app.config['UPLOAD_PATH'], 'bw_' + filename)

   img = cv2.imread(src_filename)

   result = bw_scanner(img)
   output = Image.fromarray(result)
   output.save(dst_filename)
 
   text = pytesseract.image_to_string(dst_filename)
   return text

