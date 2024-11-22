from flask import Flask, render_template, request, redirect, url_for, flash, make_response

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Пример данных пользователей
users = {
    "admin": "admin",
    "user1": "mypassword"
}

def is_authorized():
    return request.cookies.get("username") is not None

@app.route("/")
def home():
    if is_authorized():
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in users and users[username] == password:
            response = make_response(redirect(url_for("dashboard")))
            response.set_cookie("username", username, max_age=60*60*24)
            return response
        else:
            flash("Неверное имя пользователя или пароль", "danger")

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if not is_authorized():
        return redirect(url_for("login"))
    
    username = request.cookies.get("username")
    return render_template("dashboard.html", username=username)

@app.route("/logout")
def logout():
    if is_authorized():
        response = make_response(redirect(url_for("home")))
        response.delete_cookie("username")
        return response
    else:
        redirect(url_for("home"))

@app.route('/reset')
def reset():
    pass

if __name__ == "__main__":
    app.run(debug=True)
