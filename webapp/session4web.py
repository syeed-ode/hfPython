from flask import Flask, session

app = Flask(__name__)

app.secret_key = 'Eiz1XahxOhqu1ohs'

@app.route('/setuser/<user>')
def set_user(user: str) -> 'str':
    session['user'] = user
    return 'User value set to: ' + session['user']


@app.route('/getuser')
def get_user() -> 'str':
    return 'User value is currently set to: ' + session['user']


@app.route('/login')
def do_login() -> 'str':
    session['logged_in'] = True
    return 'You are now logged in.'


@app.route('/logout')
def do_logout() -> 'str':
    session.pop('logged_in')
    return 'You are now logged out.'


@app.route('/status')
def do_logout() -> 'str':
    if 'logged_in' in session:
        return 'You are still logged in!'
    return 'YOU ARE LOGGED OUT!'


@app.route('/')
def hello():
    return 'Hello from the simple webapp.'


@app.route('/page1')
def page1():
    return 'This is page 1.'


@app.route('/page2')
def page2():
    return 'This is page 2.'


@app.route('/page3')
def page3():
    return 'This is page 3.'


if __name__ == '__main__':
    app.run(debug=True)
