import threading
import time
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome 20190902 Class Guys"


@app.route('/my-route', methods=['GET','POST'])
def my_route():
    page = request.args.get('page', default = 1, type = int)
    filter = request.args.get('filter', default = '*', type = str)
    return (str(page)+filter)

@app.route('/login/<username>', methods=['GET'])
def login(username):
    return(username)


if __name__ == "__main__":
    app.run(host='localhost', port=5000,debug=True)