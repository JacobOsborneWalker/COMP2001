from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from config import Config  # Import the Config class

app = Flask(__name__)


app.config.from_object(Config)


db = SQLAlchemy(app)

class Trail(db.Model):
    __tablename__ = 'Trail'
    Trail_ID = db.Column(db.String(10), primary_key=True)
    Trail_Name = db.Column(db.String(64), nullable=False)
    Trail_Length = db.Column(db.Float, nullable=False)
    Trail_Elevation_Change = db.Column(db.Float, nullable=True)
    Trail_Expected_Time = db.Column(db.Time, nullable=True)
    Trail_Description = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return "Microservice is up and running!"

@app.route("/trails", methods=["GET"])
def get_trails():
    trails = Trail.query.all()
    return jsonify([
        {
            "Trail_ID": trail.Trail_ID,
            "Trail_Name": trail.Trail_Name,
            "Trail_Length": trail.Trail_Length,
            "Trail_Elevation_Change": trail.Trail_Elevation_Change,
            "Trail_Expected_Time": str(trail.Trail_Expected_Time) if trail.Trail_Expected_Time else None,
            "Trail_Description": trail.Trail_Description
        }
        for trail in trails
    ])

@app.route("/trail/<trail_id>", methods=["GET"])
def get_trail(trail_id):
    trail = Trail.query.get(trail_id)
    if trail:
        return jsonify({
            "Trail_ID": trail.Trail_ID,
            "Trail_Name": trail.Trail_Name,
            "Trail_Length": trail.Trail_Length,
            "Trail_Elevation_Change": trail.Trail_Elevation_Change,
            "Trail_Expected_Time": str(trail.Trail_Expected_Time) if trail.Trail_Expected_Time else None,
            "Trail_Description": trail.Trail_Description
        })
    return jsonify({"error": "Trail not found"}), 404

@app.route("/trail", methods=["POST"])
def create_trail():
    data = request.json
    try:
        new_trail = Trail(
            Trail_ID=data["Trail_ID"],
            Trail_Name=data["Trail_Name"],
            Trail_Length=data["Trail_Length"],
            Trail_Elevation_Change=data.get("Trail_Elevation_Change"),
            Trail_Expected_Time=data.get("Trail_Expected_Time"),
            Trail_Description=data.get("Trail_Description")
        )
        db.session.add(new_trail)
        db.session.commit()
        return jsonify({"message": "Trail created successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/trail/<trail_id>", methods=["PUT"])
def update_trail(trail_id):
    trail = Trail.query.get(trail_id)
    if trail:
        data = request.json
        trail.Trail_Name = data.get("Trail_Name", trail.Trail_Name)
        trail.Trail_Length = data.get("Trail_Length", trail.Trail_Length)
        trail.Trail_Elevation_Change = data.get("Trail_Elevation_Change", trail.Trail_Elevation_Change)
        trail.Trail_Expected_Time = data.get("Trail_Expected_Time", trail.Trail_Expected_Time)
        trail.Trail_Description = data.get("Trail_Description", trail.Trail_Description)
        db.session.commit()
        return jsonify({"message": "Trail updated successfully!"})
    return jsonify({"error": "Trail not found"}), 404

@app.route("/trail/<trail_id>", methods=["DELETE"])
def delete_trail(trail_id):
    trail = Trail.query.get(trail_id)
    if trail:
        db.session.delete(trail)
        db.session.commit()
        return jsonify({"message": "Trail deleted successfully!"})
    return jsonify({"error": "Trail not found"}), 404

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
