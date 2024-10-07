from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/heartbeat')
def heartbeat():
    return "I am up!"

@app.route("/newgame")
def newgame():
    return "NEW GAME STARTED"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5004)