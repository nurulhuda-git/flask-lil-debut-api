from flask import Flask
import pytesseract

app = Flask(__name__)
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
# app.config['UPLOAD_PATH'] = 'static/uploads/'
app.config['UPLOAD_PATH'] = 'D:\\Temp\\'
# app.config['ROOT_PATH'] = 'D:\\developments\\Python\\flask-lil-debut-api\\'
app.config['ROOT_PATH'] = 'D:\\Temp\\'
pytesseract.pytesseract.tesseract_cmd = 'D:/Dependencies/OCR/tesseract.exe'

from app import routes
