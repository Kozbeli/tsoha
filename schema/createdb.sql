INSERT INTO users (username, password, email)
VALUES ('tsubu',
        'pbkdf2:sha256:260000$PhvkK5Ec3d7CtEkR$e2f94bfe8c974af1b8169d1730782eafc0017e16dd41df48f665b39e8ce95db9',
        'asdf@asdf.com');

INSERT INTO users (username, password, email)
VALUES ('härski',
        'pbkdf2:sha256:260000$PhvkK5Ec3d7CtEkR$e2f94bfe8c974af1b8169d1730782eafc0017e16dd41df48f665b39e8ce95db9',
        'hjkl@hjkl.com');

INSERT INTO vehicles (reg_nro, user_id, manufacturer, model, capacity)
VALUES ('asd-123',
        1,
        'Toyota',
        'Corolla',
        5);

INSERT INTO vehicles (reg_nro, user_id, manufacturer, model, capacity)
VALUES ('xxx-123',
        2,
        'Fiat',
        'Punto',
        5);

INSERT INTO trips (vehicle_id, user_id, departure, destination, seats_left, depart_time, created_at)
VALUES (1,
        1,
        'Helsinki',
        'Tampere',
        4,
        '1111-11-11 07:00:00',
        NOW());

INSERT INTO trips (vehicle_id, user_id, departure, destination, seats_left, depart_time, created_at)
VALUES (1,
        1,
        'Tampere',
        'Helsinki',
        4,
        '1111-11-11 17:00:00',
        NOW());

INSERT INTO trips (vehicle_id, user_id, departure, destination, seats_left, depart_time, created_at)
VALUES (2,
        2,
        'Kerava',
        'Riihimäki',
        4,
        '2022-11-11 07:00:00',
        NOW());

INSERT INTO trips (vehicle_id, user_id, departure, destination, seats_left, depart_time, created_at)
VALUES (2,
        2,
        'Riihimäki',
        'Kerava',
        4,
        '2022-11-11 17:00:00',
        NOW());

INSERT INTO trips (id, user_id, vehicle_id, departure, destination, seats_left, depart_time, created_at)
VALUES (0,
        1,
        1,
        'Nowhere',
        'Nowhere',
        9999,
        '1111-11-11 00:00:00',
        NOW());


INSERT INTO passangers (trip_id, user_id)
VALUES (1, 1);
INSERT INTO passangers (trip_id, user_id)
VALUES (2, 1);