from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'colin likes dicks in his butt'

if __name__ == '__main__':
    app.run()
