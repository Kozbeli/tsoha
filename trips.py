import users
import vehicles
from db import db


def get_list():
    sql = "SELECT T.id, U.username, T.departure, T.destination, T.depart_time, T.created_at, " \
          "V.id, V.manufacturer, V.model, T.seats_left " \
          "FROM users U, trips T, Vehicles V " \
          "WHERE U.id=T.user_id AND V.id=T.vehicle_id AND T.id>0 ORDER BY T.created_at"
    result = db.session.execute(sql)
    return result.fetchall()


def send(title, content):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO messages (title, content, user_id, sent_at) VALUES (:title, :content, :user_id, NOW())"
    db.session.execute(sql, {"title": title, "content": content, "user_id": user_id})
    db.session.commit()
    return True


def add_trip(departure, destination, vehicle, depart_time):
    try:
        user_id = users.user_id()
        vehicle = vehicles.get_vehicle(vehicle)
        vehicle_id = vehicle[0]
        seats_left = vehicle[5] - 1
        sql = "INSERT INTO trips (user_id, vehicle_id, departure, destination, seats_left, depart_time, created_at) " \
              "VALUES (:user_id, :vehicle_id, :departure, :destination, :seats_left, :depart_time, NOW())"
        db.session.execute(sql, {
            "user_id": user_id,
            "vehicle_id": vehicle_id,
            "departure": departure,
            "destination": destination,
            "seats_left": seats_left,
            "depart_time": depart_time
        })
        db.session.commit()
        return True
    except:
        return False


def get_trip(trip_id):
    sql = "SELECT * FROM trips T WHERE T.id= :trip_id ;"
    result = db.session.execute(sql, {"trip_id": trip_id})
    return result.fetchone()
