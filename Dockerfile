FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
COPY main.py main.py
COPY static/. static/.
COPY app/. app/.

RUN apt-get update \
    && apt-get install tesseract-ocr -y
RUN apt-get install -y python3-opencv
RUN pip3 install -r requirements.txt
RUN export FLASK_APP=main.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]