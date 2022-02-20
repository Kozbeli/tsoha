CREATE TABLE IF NOT EXISTS visitors(
    id SERIAL PRIMARY KEY,
    time TIMESTAMP
);

CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    email TEXT
);

CREATE TABLE IF NOT EXISTS vehicles(
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users ON DELETE CASCADE,
    reg_nro TEXT,
    manufacturer TEXT,
    model TEXT,
    capacity INTEGER
);

CREATE TABLE IF NOT EXISTS trips(
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    vehicle_id INTEGER REFERENCES vehicles ON DELETE CASCADE,
    departure TEXT,
    destination TEXT,
    seats_left INTEGER,
    depart_time TIMESTAMP,
    created_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS messages(
    id SERIAL PRIMARY KEY,
    title TEXT,
    content TEXT,
    user_id INTEGER REFERENCES users,
    trip_id INTEGER REFERENCES trips,
    sent_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS passangers(
    trip_id INTEGER REFERENCES trips ON DELETE CASCADE,
    user_id Integer REFERENCES users ON DELETE CASCADE
);