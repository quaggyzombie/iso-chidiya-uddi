from flask import Flask

app = Flask(__name__)

@app.route('/heartbeat')
def heartbeat():
    return "I am up!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5004)