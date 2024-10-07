from flask import Flask, render_template
import sqlite3
# DATABASE
# Sessions => Session ID, Status, Created_Timestamp
# Players => Unique ID (Discord ID), Player Name, Created_Timestamp
# Game Audit Log => TurnID, GameID, Dict with player UniqueID and status, Created_Timestamp
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