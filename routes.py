from app import app
from flask import render_template, request, redirect
import messages, users, visits


@app.route("/")
def index():
    visits.add_visit()
    counter = visits.get_counter()
    messageList = messages.get_list()
    print("counter is now", counter)
    return render_template("index.html", counter=counter, count=len(messageList), messages=messageList)


@app.route("/send", methods=["POST"])
def send():
    content = request.form["content"]
    if messages.send(content):
        return redirect("/")
    else:
        return render_template("error.html", message="Failed to send message")


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
