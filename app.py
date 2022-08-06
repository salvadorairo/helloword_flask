from flask import Flask

app = Flask(__name__)

@app.route('/')
def rh():
    return 'home'

@app.route('/r1')
def r1():
    return 'Route 1'
    
@app.route('/r2')
def r2():
    return 'Route 2'
    
@app.route('/r3')
def r3():
    return 'Route 3'

