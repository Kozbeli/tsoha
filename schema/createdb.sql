INSERT INTO users (username, password, email)
VALUES ('asdf',
        'pbkdf2:sha256:260000$PhvkK5Ec3d7CtEkR$e2f94bfe8c974af1b8169d1730782eafc0017e16dd41df48f665b39e8ce95db9',
        'asdf@asdf.com');

INSERT INTO users (username, password, email)
VALUES ('hjkl',
        'pbkdf2:sha256:260000$PhvkK5Ec3d7CtEkR$e2f94bfe8c974af1b8169d1730782eafc0017e16dd41df48f665b39e8ce95db9',
        'hjkl@hjkl.com');

INSERT INTO vehicles (reg_nro, user_id, manufacturer, model, capacity)
VALUES ('asd-123',
        1,
        'Toyota',
        'Corolla',
        5);

INSERT INTO trips (vehicle_id, user_id, departure, destination, depart_time)
VALUES (1,
        1,
        'Helsinki',
        'Tampere',
        '1111-11-11 07:00:00');

INSERT INTO trips (vehicle_id, user_id, departure, destination, depart_time)
VALUES (1,
        1,
        'Tampere',
        'Helsinki',
        '1111-11-11 17:00:00');