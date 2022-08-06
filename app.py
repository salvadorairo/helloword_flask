from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'home'

@app.route('/r1')
def index():
    return 'Route 1'
    
@app.route('/r2')
def index():
    return 'Route 2'
    
@app.route('/r3')
def index():
    return 'Route 3'

