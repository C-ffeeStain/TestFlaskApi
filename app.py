from flask import Flask


app = Flask(__name__)


@app.route("/api/")
def api_home():
    return "API is running!"
