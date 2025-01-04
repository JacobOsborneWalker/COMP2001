-- Create the CW2 schema if it doesn't exist
CREATE SCHEMA IF NOT EXISTS CW2;

-- Create Trail Table
CREATE TABLE CW2.Trail (
    Trail_ID VARCHAR(10) PRIMARY KEY,
    Trail_Name VARCHAR(64) NOT NULL,
    Trail_Length DECIMAL(3,1) NOT NULL CHECK (Trail_Length > 0),
    Trail_Elevation_Change DECIMAL(5,1) DEFAULT NULL CHECK (Trail_Elevation_Change BETWEEN -999.9 AND 999.9),
    Trail_Expected_Time TIME DEFAULT NULL,
    Trail_Description VARCHAR(250) DEFAULT NULL
);

-- Create Openings Table
CREATE TABLE CW2.Openings (
    OpenID VARCHAR(10) PRIMARY KEY,
    Opening_Time TIME NOT NULL,
    Closing_Time TIME NOT NULL,
    Day_Open DATE NOT NULL,
    Day_Close DATE NOT NULL,
    CHECK (Opening_Time < Closing_Time),
    CHECK (Day_Open <= Day_Close)
);

-- Create the Trail_Openings Link Table
CREATE TABLE CW2.Trail_Openings (
    Trail_ID VARCHAR(10) NOT NULL,
    OpenID VARCHAR(10) NOT NULL,
    PRIMARY KEY (Trail_ID, OpenID),
    FOREIGN KEY (Trail_ID) REFERENCES CW2.Trail(Trail_ID) ON DELETE CASCADE,
    FOREIGN KEY (OpenID) REFERENCES CW2.Openings(OpenID) ON DELETE CASCADE
);

-- Create the Ratings Table
CREATE TABLE CW2.Trail_Ratings (
    Trail_Ratings_ID VARCHAR(10) PRIMARY KEY,
    Trail_ID VARCHAR(10) NOT NULL,
    Trail_Rating DECIMAL(2,1) CHECK (Trail_Rating BETWEEN 0.0 AND 5.0),
    Trail_Difficulty VARCHAR(10) NOT NULL,
    CHECK (Trail_Difficulty IN ('very easy', 'easy', 'medium', 'hard', 'very hard')),
    FOREIGN KEY (Trail_ID) REFERENCES CW2.Trail(Trail_ID) ON DELETE CASCADE
);

-- Create the Trail Log Table
CREATE TABLE CW2.Trail_Log (
    LogID INT IDENTITY PRIMARY KEY,
    Trail_ID VARCHAR(10) NOT NULL,
    Author VARCHAR(64) NOT NULL,
    Time_Added DATETIME NOT NULL  
);

-- Trigger for logging trail creation
IF OBJECT_ID('CW2.Trail_Trigger', 'TR') IS NOT NULL
    DROP TRIGGER CW2.Trail_Trigger;

CREATE TRIGGER CW2.Trail_Trigger
ON CW2.Trail
AFTER INSERT
AS
BEGIN
    INSERT INTO CW2.Trail_Log (Trail_ID, Author, Time_Added)
    SELECT 
        i.Trail_ID,
        SYSTEM_USER,
        GETDATE()
    FROM
        inserted i;
END;

-- Create Procedures for CRUD operations

-- Create Procedure
IF OBJECT_ID('CW2.CreateTrail', 'P') IS NOT NULL
    DROP PROCEDURE CW2.CreateTrail;

CREATE PROCEDURE CW2.CreateTrail
    @Trail_ID VARCHAR(10),
    @Trail_Name VARCHAR(64),
    @Trail_Length DECIMAL(3,1),
    @Trail_Elevation_Change DECIMAL(5,1) = NULL,
    @Trail_Expected_Time TIME = NULL,
    @Trail_Description VARCHAR(250) = NULL
AS
BEGIN
    INSERT INTO CW2.Trail (Trail_ID, Trail_Name, Trail_Length, Trail_Elevation_Change, Trail_Expected_Time, Trail_Description)
    VALUES (@Trail_ID, @Trail_Name, @Trail_Length, @Trail_Elevation_Change, @Trail_Expected_Time, @Trail_Description);
END;

-- Retrieve Procedure
IF OBJECT_ID('CW2.RetreiveTrail', 'P') IS NOT NULL
    DROP PROCEDURE CW2.RetreiveTrail;

CREATE PROCEDURE CW2.RetreiveTrail
    @Trail_ID VARCHAR(10) = NULL
AS
BEGIN
    IF @Trail_ID IS NULL
    BEGIN
        SELECT * FROM CW2.Trail;
    END
    ELSE
    BEGIN
        SELECT * FROM CW2.Trail WHERE Trail_ID = @Trail_ID;
    END
END;

-- Update Procedure
IF OBJECT_ID('CW2.UpdateTrail', 'P') IS NOT NULL
    DROP PROCEDURE CW2.UpdateTrail;

CREATE PROCEDURE CW2.UpdateTrail
    @Trail_ID VARCHAR(10),
    @Trail_Name VARCHAR(64),
    @Trail_Length DECIMAL(3,1),
    @Trail_Elevation_Change DECIMAL(5,1) = NULL,
    @Trail_Expected_Time TIME = NULL,
    @Trail_Description VARCHAR(250) = NULL
AS
BEGIN
    UPDATE CW2.Trail
    SET
        Trail_Name = @Trail_Name,
        Trail_Length = @Trail_Length,
        Trail_Elevation_Change = @Trail_Elevation_Change,
        Trail_Expected_Time = @Trail_Expected_Time,
        Trail_Description = @Trail_Description
    WHERE Trail_ID = @Trail_ID;
END;

-- Delete Procedure
IF OBJECT_ID('CW2.DeleteTrail', 'P') IS NOT NULL
    DROP PROCEDURE CW2.DeleteTrail;

CREATE PROCEDURE CW2.DeleteTrail
    @Trail_ID VARCHAR(10)
AS
BEGIN
    DELETE FROM CW2.Trail
    WHERE Trail_ID = @Trail_ID;
END;
