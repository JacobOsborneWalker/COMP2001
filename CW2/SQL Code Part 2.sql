ALTER TABLE CW2.routes DROP CONSTRAINT FK_routes_trail_id;
ALTER TABLE CW2.trail_features DROP CONSTRAINT FK_trail_features_trail_id;

DROP TABLE IF EXISTS CW2.routes;
DROP TABLE IF EXISTS CW2.trail_features;
DROP TABLE IF EXISTS CW2.trails;


CREATE TABLE CW2.Trails (
    TrailID INT PRIMARY KEY,
    TrailName NVARCHAR(255) NOT NULL,
    Difficulty NVARCHAR(50),
    Location NVARCHAR(255),
    Length DECIMAL(10, 2),
    ElevationGain DECIMAL(10, 2),
    RouteID INT,
    RouteType NVARCHAR(50),
    TrailSummary NVARCHAR(MAX),
    TrailDescription NVARCHAR(MAX)
);


CREATE TABLE CW2.RouteTypes (
    RouteID INT PRIMARY KEY,
    RouteType NVARCHAR(50) NOT NULL
);


CREATE TABLE CW2.TrailFeatures (
    TrailFeatureID INT PRIMARY KEY,
    TrailID INT NOT NULL FOREIGN KEY REFERENCES CW2.Trails(TrailID),
    Feature NVARCHAR(255)
);

INSERT INTO CW2.Trails (TrailID, TrailName, Difficulty, Location, Length, ElevationGain, RouteID, RouteType, TrailSummary, TrailDescription)
VALUES 
(1, 'Trail number 1', 'Medium', 'Eastbourne', 5.5, 450, 101, 'Loop', 'Trail summary for number 1', 'Trail description for number 1.'),
(2, 'Trail Number 2', 'Hard', 'St Ives', 12.3, 1500, 102, 'Out and Back', 'Trail summary 2.', 'trail descripton.');

INSERT INTO CW2.TrailFeatures (TrailFeatureID, TrailID, Feature)
VALUES 
(1, 1, 'Waterfall'),
(2, 1, 'Beaches'),
(3, 2, 'Steap hills'),
(4, 2, 'Bycycle paths');

INSERT INTO CW2.RouteTypes (RouteID, RouteType)
VALUES 
(101, 'Loop'),
(102, 'Out and Back'),
(103, 'Point to Point');
