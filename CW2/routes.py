from flask import request, jsonify
from app import app, db
from models import Trail, TrailRating, TrailLog, Opening, TrailOpening

@app.route('/trails', methods=['POST'])
def create_trail():
    data = request.json
    try:
        new_trail = Trail(
            Trail_ID=data['Trail_ID'],
            Trail_Name=data['Trail_Name'],
            Trail_Length=data['Trail_Length'],
            Trail_Elevation_Change=data.get('Trail_Elevation_Change'),
            Trail_Expected_Time=data.get('Trail_Expected_Time'),
            Trail_Description=data.get('Trail_Description')
        )
        db.session.add(new_trail)
        db.session.commit()
        return jsonify({"message": "Trail created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/trails', methods=['GET'])
def get_trails():
    trails = Trail.query.all()
    return jsonify([
        {
            "Trail_ID": t.Trail_ID,
            "Trail_Name": t.Trail_Name,
            "Trail_Length": t.Trail_Length,
            "Trail_Elevation_Change": t.Trail_Elevation_Change,
            "Trail_Expected_Time": t.Trail_Expected_Time,
            "Trail_Description": t.Trail_Description
        } for t in trails
    ])

@app.route('/trails/<trail_id>', methods=['PUT'])
def update_trail(trail_id):
    data = request.json
    trail = Trail.query.filter_by(Trail_ID=trail_id).first()
    if not trail:
        return jsonify({"error": "Trail not found"}), 404

    trail.Trail_Name = data.get('Trail_Name', trail.Trail_Name)
    trail.Trail_Length = data.get('Trail_Length', trail.Trail_Length)
    trail.Trail_Elevation_Change = data.get('Trail_Elevation_Change', trail.Trail_Elevation_Change)
    trail.Trail_Expected_Time = data.get('Trail_Expected_Time', trail.Trail_Expected_Time)
    trail.Trail_Description = data.get('Trail_Description', trail.Trail_Description)

    db.session.commit()
    return jsonify({"message": "Trail updated successfully"})

@app.route('/trails/<trail_id>', methods=['DELETE'])
def delete_trail(trail_id):
    trail = Trail.query.filter_by(Trail_ID=trail_id).first()
    if not trail:
        return jsonify({"error": "Trail not found"}), 404

    db.session.delete(trail)
    db.session.commit()
    return jsonify({"message": "Trail deleted successfully"})
