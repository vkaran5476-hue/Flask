from flask import Flask, render_template, request

app = Flask(__name__)

users = {
    "admin": "123",
    "karan": "321",
    "verma": "213"
}

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in users and users[username] == password:
            return render_template("welcome.html", name=username)
        else:
            return render_template("login.html", error="Invalid Username or Password ❌")

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)