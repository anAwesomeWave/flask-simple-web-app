from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/users/<name>')
def get_name(name):
    return render_template('username.html', username=name)


if __name__ == '__main__':
    app.run(debug=True)
