from flask import Flask

app = Flask(__name__)

@app.route('/')
def basic():
    return "Hi Everybody! \n Today we fly to New Jork"

@app.route('/test')
def test():
    return "This is just a test"

@app.route('/<name>')
def main_site(name):
    return "Welcome {name}! Welcome back!".formate(name = name)

if __name__ == '__main__':
    app.run()
