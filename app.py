from flask import Flask
from markupsafe import escape

app = Flask(__name__)

# @app.route('/')

# def hello():
#     return '<h1>Welcome to Library in Dunn Loring!</h1>'

@app.route('/user/<name>')
def user_page(name):
    return f'User: {escape(name)}'