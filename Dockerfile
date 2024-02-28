FROM python:3.10

WORKDIR /flask-app

COPY requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

CMD ["gunicorn", "-b", "0.0.0.0:8000", "my_app:app", "--log-level", "debug", "--timeout", "600"]