from flask import Flask

app = Flask(__name__)


#routes end with a slash which is a python wrapper
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/test')
def test():
    return "This is a test"
