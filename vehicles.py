import users
from db import db


def get_list(user_id):
    sql = "SELECT * FROM vehicle_owners O, vehicles V WHERE O.user_id=:user_id;"
    result = db.session.execute(sql, {"user_id": user_id})
    return result.fetchall()
