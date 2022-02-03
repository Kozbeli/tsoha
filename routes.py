from app import app
from flask import render_template, request, redirect
import messages
import users
import visits


@app.route("/")
def index():
    visits.add_visit()
    counter = visits.get_counter()
    messageList = messages.get_list()
    print("counter is now", counter)
    return render_template("index.html", counter=counter, count=len(messageList), messages=messageList)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Invalid username or password")


@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        print(f"username: {username}")
        print(f"password1: {password1}")
        print(f"password2: {password2}")
        if password1 != password2:
            return render_template("error.html", message="Passwords are not equal")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Registeration failed")


@app.route("/new")
def new():
    return render_template("new.html")


@app.route("/send", methods=["POST"])
def send():
    title = request.form["title"]
    content = request.form["content"]
    if len(title) > 100:
        return render_template("error.html", message="Title is too long")
    if len(content) > 5000:
        return render_template("error.html", message="Message is too long")
    if messages.send(title, content):
        return redirect("/")
    else:
        return render_template("error.html", message="Failed to send message")


@app.route("/profile/<int:id>")
def profile(id):
    allow = False
    user = users.get_user(id)
    if users.is_admin():
        allow = True
        return render_template("profile.html", user=user)
    elif is_user() and user_id == id:
        allow = True
    elif is_user():
        sql = "SELECT 1 FROM friends WHERE user1=:user1 AND user2=:user2"
        result = db.session.execute(sql, {"user1":user_id(), "user2":id})
        if result.fetchone():
            allow = True
        if not allow:
            return render_template("error.html", error="Unauthorized access")