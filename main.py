import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/spiele-hub")
def spiele_hub():
    return render_template("spiele-hub.htmll")

if __name__ == "__main__":
    # Fest auf Port 10000 für Render gestellt
    app.run(debug=True, host="0.0.0.0", port=10000)
