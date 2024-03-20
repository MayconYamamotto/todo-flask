import os
from flask import Flask, render_template
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os.path import join, dirname
from dotenv import load_dotenv
from .models import User

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)

db = SQLAlchemy()
DB_NAME = "database.db"

app.config['SECRET_KEY'] =  os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")

db.init_app(app)

with app.app_context():
    db.create_all()

# ROUTES
@app.route("/")
def signin():
    return render_template("signin.html", title="Sign in")

@app.route("/signup")
def signup():
    return render_template("signup.html", title="Sign up")

@app.route("/home")
def home():
    return render_template("home.html", title="Home")

if __name__ == "__main__":
    app.run(debug=True)