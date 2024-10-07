from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/heartbeat')
def heartbeat():
    return "I am up!"