from flask import Flask, redirect


app = Flask(__name__)


@app.route("/")
def index():
    return redirect("/api/")


@app.route("/api/")
def api_home():
    return "API is running!"
