from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Öffnet dein neues, grünes Profi-Design
    return render_template('index.html')

if __name__ == '__main__':
    # Wichtig: Port 5002, damit deine Spiele-Zentrale (5001) weiterlaufen kann!
    app.run(host='0.0.0.0', port=10000, debug=True)
