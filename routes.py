from app import app
from flask import render_template, request, redirect, session
import messages
import users
import visits
import trips
import vehicles
import passangers


@app.route("/")
def index():
    if not users.logged_in():
        return redirect("/login")
    visits.add_visit()
    counter = visits.get_counter()
    trip_list = trips.get_list()
    vehicle_list = vehicles.get_list(session.get("user_id"))
    return render_template(
        "index.html",
        counter=counter,
        count=len(trip_list),
        trips=trip_list,
        vehicles=vehicle_list)


@app.route("/chat")
def chat():
    if not users.logged_in():
        return redirect("/login")
    visits.add_visit()
    counter = visits.get_counter()
    message_list = messages.get_messages(0)
    return render_template("chat.html", counter=counter, count=len(message_list), messages=message_list)


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
        if password1 != password2:
            return render_template("error.html", message="Passwords are not equal")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Registeration failed")


@app.route("/send/<int:trip_id>", methods=["POST"])
def send(trip_id):
    if not users.logged_in():
        return redirect("/login")
    title = request.form["title"]
    content = request.form["content"]
    if len(title) > 100:
        return render_template("error.html", message="Title is too long")
    if len(content) > 5000:
        return render_template("error.html", message="Message is too long")
    if messages.send(title, content, trip_id):
        if trip_id == 0:
            return redirect("/chat")
        else:
            return redirect(f"/trips/{trip_id}")
    else:
        return render_template("error.html", message="Failed to send message")


@app.route("/users")
def profiles():
    if not users.logged_in():
        return redirect("/login")
    user_list = users.get_list()
    return render_template("users.html", users=user_list)


@app.route("/users/<int:id>", methods=["GET"])
def profile(id):
    if not users.logged_in():
        return redirect("/login")
    if request.method == "GET":
        user_info = users.get_user(id)
        vehicle_list = vehicles.get_list(id)
        return render_template("user.html", user=user_info, vehicles=vehicle_list)


@app.route("/users/<int:user_id>/add_vehicle", methods=["POST"])
def add_vehicle(user_id):
    if not users.logged_in():
        return redirect("/login")
    if request.method == "POST":
        reg_nro = request.form["reg_nro"]
        manufacturer = request.form["manufacturer"]
        model = request.form["model"]
        capacity = request.form["capacity"]
        if vehicles.add_vehicle(reg_nro, user_id, manufacturer, model, capacity):
            return redirect(f"/users/{user_id}")
        else:
            return redirect("/error")


@app.route("/users/<int:user_id>/del_vehicle/<int:vehicle_id>", methods=["GET"])
def del_vehicle(user_id, vehicle_id):
    if not users.logged_in():
        return redirect("/login")
    if vehicles.remove_vehicle(user_id, vehicle_id):
        return redirect(f"/users/{user_id}")
    else:
        return redirect("/error")


@app.route("/add_trip", methods=["POST"])
def add_trip():
    if not users.logged_in():
        return redirect("/login")
    departure = request.form["departure"]
    destination = request.form["destination"]
    vehicle = request.form["vehicle"]
    time = request.form["depart_time"]
    if trips.add_trip(departure, destination, vehicle, time):
        return redirect("/")
    else:
        return redirect("/error")


@app.route("/trips/<int:id>", methods=["GET"])
def trip(id):
    if not users.logged_in():
        return redirect("/login")
    trip_id = int(id)
    trip_info = trips.get_trip(id)
    vehicle_id = trip_info[2]
    vehicle_info = vehicles.get_by_id(vehicle_id)
    passanger_list = passangers.get_list(trip_id)
    message_list = messages.get_messages(trip_id)
    return render_template(
        "trip.html",
        trip=trip_info,
        vehicle=vehicle_info,
        messages=message_list,
        passangers=passanger_list)
