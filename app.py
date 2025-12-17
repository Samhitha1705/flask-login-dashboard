from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret123"

# 🔹 Global login tracking (application-wide)
total_login_count = 0
unique_users = set()

@app.route("/")
def dashboard():
    return render_template(
        "dashboard.html",
        logged_in=session.get("logged_in"),
        username=session.get("username"),
        total_logins=total_login_count,
        user_count=len(unique_users),
        users=list(unique_users)
    )

@app.route("/login", methods=["GET", "POST"])
def login():
    global total_login_count, unique_users

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Accept ANY credentials (demo)
        if username and password:
            session["logged_in"] = True
            session["username"] = username

            # 📊 Track login stats
            total_login_count += 1
            unique_users.add(username)

            return redirect(url_for("dashboard"))

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("dashboard"))

if __name__ == "__main__":
    app.run(debug=True)
