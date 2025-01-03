CREATE TABLE CW2.trails (
    trail_id INT PRIMARY KEY,
    trail_name NVARCHAR(100),
    difficulty NVARCHAR(50),
    location NVARCHAR(100),
    length FLOAT,
    elevation_gain FLOAT
);

CREATE TABLE CW2.routes (
    route_id INT PRIMARY KEY,
    trail_id INT,
    route_type NVARCHAR(50),
    FOREIGN KEY (trail_id) REFERENCES trails(trail_id)
);

CREATE TABLE CW2.trail_features (
    feature_id INT PRIMARY KEY,
    trail_id INT,
    feature_name NVARCHAR(100),
    FOREIGN KEY (trail_id) REFERENCES trails(trail_id)
);
