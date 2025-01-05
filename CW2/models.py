from app import db


class Trail(db.Model):
    __tablename__ = 'Trail'
    Trail_ID = db.Column(db.String(10), primary_key=True)
    Trail_Name = db.Column(db.String(64), nullable=False)
    Trail_Length = db.Column(db.Float, nullable=False)
    Trail_Elevation_Change = db.Column(db.Float, default=None)
    Trail_Expected_Time = db.Column(db.Time, default=None)
    Trail_Description = db.Column(db.String(250), default=None)


class Opening(db.Model):
    __tablename__ = 'Openings'
    OpenID = db.Column(db.String(10), primary_key=True)
    Opening_Time = db.Column(db.Time, nullable=False)
    Closing_Time = db.Column(db.Time, nullable=False)
    Day_Open = db.Column(db.Date, nullable=False)
    Day_Close = db.Column(db.Date, nullable=False)


class TrailOpening(db.Model):
    __tablename__ = 'Trail_Openings'
    Trail_ID = db.Column(db.String(10), db.ForeignKey('Trail.Trail_ID'), primary_key=True)
    OpenID = db.Column(db.String(10), db.ForeignKey('Openings.OpenID'), primary_key=True)


class TrailRating(db.Model):
    __tablename__ = 'Trail_Ratings'
    Trail_Ratings_ID = db.Column(db.String(10), primary_key=True)
    Trail_ID = db.Column(db.String(10), db.ForeignKey('Trail.Trail_ID'), nullable=False)
    Trail_Rating = db.Column(db.Float, nullable=False)
    Trail_Difficulty = db.Column(db.String(10), nullable=False)


class TrailLog(db.Model):
    __tablename__ = 'Trail_Log'
    LogID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Trail_ID = db.Column(db.String(10), db.ForeignKey('Trail.Trail_ID'), nullable=False)
    Author = db.Column(db.String(64), nullable=False)
    Time_Added = db.Column(db.DateTime, nullable=False)
