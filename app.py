from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome Omkar!"

@app.route("/about")
def about():
    return "About Page"

@app.route("/contact")
def contact():
    return "Contact Page"

@app.route("/services")
def services():
    return "Services Page"

@app.route("/logged in status")
def logged_in_status():
    return "Logged in status"

@app.route("/login")
def login():
    return "Login Page"


if __name__ == "__main__":
    app.run(debug=True)
