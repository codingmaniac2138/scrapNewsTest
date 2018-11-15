from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

@app.route("/")
def home_page():
    # landing page
    print("test landing page")
    return render_template("index.html",)