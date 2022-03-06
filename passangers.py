import trips
import users
from db import db


def get_list(id):
    sql = "SELECT U.username, T.departure, T.destination, U.id FROM users U, trips T, passangers P WHERE U.id=P.user_id AND T.id=P.trip_id AND T.id=:trip_id;"
    result = db.session.execute(sql, {"trip_id": id})
    return result.fetchall()


def passanger_in(trip_id):
    sql = "SELECT user_id FROM passangers WHERE trip_id=:trip_id"
    result = db.session.execute(sql, {"trip_id": trip_id})
    passangers = result.fetchall()
    for passanger in passangers:
        passanger_tuple = tuple(passanger)
        user_id = int(users.user_id())
        if passanger_tuple[0] == user_id:
            return True
    print(passangers)
    return False


def add_passanger(trip_id):
    user_id = users.user_id()
    if not user_id:
        return False
    if passanger_in(trip_id):
        return False
    if trips.decrement_capacity_of(trip_id):
        sql = "INSERT INTO passangers (trip_id, user_id) VALUES (:trip_id, :user_id)"
        db.session.execute(sql, {"trip_id": trip_id, "user_id": user_id})
        db.session.commit()
        return True
    return False


def remove_passanger(trip_id, user_id):
    if trips.increment_capacity_of(trip_id):
        sql = "DELETE FROM passangers WHERE trip_id=:trip_id AND user_id=:user_id;"
        db.session.execute(sql, {"trip_id": trip_id, "user_id": user_id})
        db.session.commit()
        return True
    return False