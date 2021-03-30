from app import app
import pytesseract
import cv2
from skimage.filters import threshold_local
from PIL import Image
import numpy
import os

def bw_scanner(image):
   gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   T = threshold_local(gray, 21, offset = 5, method = "gaussian")
   return (gray > T).astype("uint8") * 255

def convert_to_bw(filename, filter):
   src_filename = os.path.join(app.config['UPLOAD_PATH'], filename)
   dst_filename = os.path.join(app.config['UPLOAD_PATH'], 'bw_' + filename)

   if filter == 'black_and_white':
      img = cv2.imread(src_filename)

      result = bw_scanner(img)
      output = Image.fromarray(result)
      output.save(dst_filename)
 
      text = pytesseract.image_to_string(dst_filename)
   else:
      text = pytesseract.image_to_string(src_filename)
   return text