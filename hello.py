from flask import Flask
from flask import request


app = Flask(__name__)


@app.route('/')
def index():
    # return '<h1>Hello World!</h1>'
    user_agent = request.headers.get('User_Agent')
    return '<p>Your brower is {}!</p>'.format(user_agent)


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)


if __name__ == '__main__':
    app.run(debug=True)
