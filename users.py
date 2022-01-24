from flask import session
from db import db
from werkzeug.security import check_password_hash, generate_password_hash


def login(username, password):
    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()
    print(f"user: {user}")
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            return True
        else:
            return False


def logout():
    del session["user_id"]


def user_id():
    return session.get("user_id", 0)


def register(username, password):
    hash_value = generate_password_hash(password)
    print(f"hash_value: {hash_value}")
    try:
        sql = "INSERT INTO users (username,password) VALUES (:username,:password)"
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    except:
        print("ERROR: users.register() failed")
        return False
    return login(username, password)
