from flask import Flask, render_template

app = Flask(__name__)

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