CREATE TABLE IF NOt EXISTS visitors(
  id SERIAL PRIMARY KEY, 
  time TIMESTAMP
);

CREATE TABLE IF NOt EXISTS users(
  id SERIAL PRIMARY KEY,
  username TEXT UNIQUE,
  password TEXT,
  email TEXT,
  admin BOOLEAN
);

CREATE TABLE IF NOt EXISTS vehicles(
    id SERIAL PRIMARY KEY,
    reg_nro TEXT,
    manufacturer TEXT,
    model TEXT
);

CREATE TABLE IF NOt EXISTS vehicle_owners(
    user_id INTEGER REFERENCES users,
    vehicle_id INTEGER REFERENCES vehicles
);

CREATE TABLE IF NOt EXISTS messages(
  id SERIAL PRIMARY KEY,
  title TEXT,
  content TEXT,
  user_id INTEGER REFERENCES users,
  sent_at TIMESTAMP
);