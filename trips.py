import users
import vehicles
from db import db


def get_list():
    sql = "SELECT U.username, T.departure, T.destination, T.depart_time, T.created_at, " \
        "V.id, V.manufacturer, V.model, V.capacity "\
        "FROM users U, trips T, Vehicles V " \
        "WHERE U.id=T.user_id AND V.id=T.vehicle_id ORDER BY T.created_at"
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
        vehicle_id = vehicles.get_vehicle(vehicle)[0]
        sql = "INSERT INTO trips (user_id, vehicle_id, departure, destination, depart_time, created_at)"\
            "VALUES (:user_id, :vehicle_id, :departure, :destination, :depart_time, NOW())"
        db.session.execute(sql, {
            "user_id": user_id,
            "vehicle_id": vehicle_id,
            "departure": departure,
            "destination": destination,
            "depart_time": depart_time
        })
        db.session.commit()
        return True
    except:
        return False