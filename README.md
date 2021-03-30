# flask-lil-debut-api
this repo contains lil-debute api project.

## How to Run
Before we started, make sure you have installed Python in your system. Click [here](https://www.python.org/downloads/) to install Python. 
Step :
1. Install virtualenv and then create new virtual environment using virtualenv
   ```bash
   pip install virtualenv
   ```
   then 
   ```bash
   python -m venv env
   ```
2. Active virtual environment. To activate your brand new virtual environment you use the following command:
   
   Unix :
   ```bash
   $ source venv/bin/activate
   (venv) $ _
   ```
   Windows :
   ```bash
   $ venv\Scripts\activate
   (venv) $ _
   ```
3. After virtual environment activated, you need to install Flask dependency. To install flask dependency use the following command:
   ```bash
   (venv) $ pip install flask
   ```
4. If you want to confirm that your virtual environment now has Flask installed, you can start the Python interpreter and import Flask into it:
   ```bash
   >>> import flask
   >>> _
   ```
5. And then its done, you can run the app using this following command:
   ```bash
   python main.py
   ```
6. If you wanna simplify command in step 5, you must told virtual env what your apps name using :
   
   Unix :
   ```bash
   (venv) $ export FLASK_APP=main.py
   ```
   Windows :
   ```bash
   (venv) $ set FLASK_APP=main.py
   ```
7. After declaring environment variable, you can run this project using :
   ```bash
   (venv) $ flask run
   ```
   or if you wanna run in different port instead of `port=5000`:
   ```bash
   (venv) $ flask run --port=5050
   ```
8. Done.
   
