
from datetime import datetime
import pytz
from config import db

# trail model
class Trail(db.Model):
    __tablename__ = 'trail' 

    # info
    id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String(100), unique=True, nullable=False)  
    description = db.Column(db.String(255))  
    length = db.Column(db.Numeric(5, 2))  
    difficulty = db.Column(db.String(50))  
    location = db.Column(db.String(255))  
    # track when updated
    timestamp = db.Column(
        db.DateTime,
        default=lambda: datetime.now(pytz.timezone('Europe/London')),
        onupdate=lambda: datetime.now(pytz.timezone('Europe/London'))
    )  

# serialising data
from marshmallow import Schema, fields

class TrailSchema(Schema):
    id = fields.Int(dump_only=True) 
    name = fields.Str(required=True)
    description = fields.Str()
    length = fields.Decimal(as_string=True)
    difficulty = fields.Str()
    location = fields.Str()
    timestamp = fields.DateTime(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        fields = ("id", "name", "description", "length", "difficulty", "location", "timestamp")
