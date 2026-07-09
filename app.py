from flask import Flask, render_template
from datetime import datetime
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        hostname=socket.gethostname(),
        current_time=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    )

@app.route("/health")
def health():
    return {
        "status": "UP"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
