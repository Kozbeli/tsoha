import users
from db import db


def get_list(user_id):
    sql = "SELECT * FROM  vehicles V WHERE V.user_id=:user_id;"
    result = db.session.execute(sql, {"user_id": user_id})
    vehicle_list = result.fetchall()
    if not vehicle_list:
        return []
    return vehicle_list

def get_vehicle(reg_nro):
    sql = "SELECT id FROM vehicles WHERE reg_nro=:reg_nro;"
    result = db.session.execute(sql, {"reg_nro": reg_nro})
    vehicle_id = result.fetchone()
    return vehicle_id

def add_vehicle(reg_nro, user_id, manufacturer, model, seats):
    if user_id == 0:
        return False
    sql = "INSERT INTO vehicles (reg_nro, user_id, manufacturer, model, capacity) "\
          "VALUES (:reg_nro, :user_id, :manufacturer, :model, :capacity);"
    db.session.execute(sql, {"reg_nro": reg_nro, "user_id": user_id, "manufacturer": manufacturer, "model": model, "capacity": seats})
    db.session.commit()
    return True

def remove_vehicle(user_id, vehicle_id):
    if user_id != users.user_id():
        return False
    sql = "DELETE FROM vehicles WHERE id=:vehicle_id"
    db.session.execute(sql, {"vehicle_id": vehicle_id})
    db.session.commit()
    return True