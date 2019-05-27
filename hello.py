from flask import Flask, render_template
# from flask import request
# from flask_script import Manager

app = Flask(__name__)
# manager = Manager(app)

@app.route('/')
def index():
    # return '<h1>Hello World!</h1>'
    # user_agent = request.headers.get('User_Agent')
    # return '<p>Your brower is {}!</p>'.format(user_agent)
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    # return '<h1>Hello, {}!</h1>'.format(name)
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
    # manager.run()
