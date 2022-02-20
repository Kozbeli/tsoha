from db import db


def get_list(id):
    sql = "SELECT U.username, T.departure, T.destination FROM users U, trips T, passangers P WHERE U.id=P.user_id AND T.id=P.trip_id AND T.id=:trip_id;"
    result = db.session.execute(sql, {"trip_id": id})
    return result. fetchall()
