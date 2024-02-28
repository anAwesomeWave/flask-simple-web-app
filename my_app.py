from flask import Flask
from flask import render_template
from prometheus_flask_exporter import PrometheusMetrics
from dotenv import load_dotenv


load_dotenv('.flask-prometh-env')

app = Flask(__name__, template_folder='templates')
metrics = PrometheusMetrics(app)


# app.config['SERVER_NAME'] = 'flask-app:8000'
@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/users/<name>')
def get_name(name):
    return render_template('username.html', username=name)


if __name__ == '__main__':
    app.run(debug=True)
