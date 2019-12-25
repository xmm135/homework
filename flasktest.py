from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello,World! 1'

@app.route('/test<name>')
def hello_world2(name):
    return 'Hello,World! 3' + name

if __name__ == '__main__':
    app.run()