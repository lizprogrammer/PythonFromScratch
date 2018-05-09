from flask import *

app = Flask(__name__)


@app.route('/names/<name>')
def index(name):
    return '<h1>Hi %s</h1>' % name


if __name__ == '__main__':
    app.run()
