from flask import Flask

app = Flask(__name__)
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif','.txt']
app.config['UPLOAD_PATH'] = 'static/uploads/'
app.config['ROOT_PATH'] = 'D:\\developments\\Python\\flask-lil-debut-api\\'

from app import routes
