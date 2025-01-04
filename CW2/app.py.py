from flask import Flask, request, jsonify, abort
from config import db
from models import Trail, TrailSchema

app = Flask(__name__)
app.config.from_object('config') 

trail_schema = TrailSchema()
trails_schema = TrailSchema(many=True)

#create n
@app.route('/api/trails', methods=['POST'])
def create_trail():
    trail_data = request.get_json()

    # check if exists
    existing_trail = Trail.query.filter(Trail.name == trail_data.get('name')).one_or_none()
    if existing_trail:
        abort(406, f"trail with name '{trail_data['name']}' already exists")

    # deserialise
    new_trail = trail_schema.load(trail_data, session=db.session)
    db.session.add(new_trail)
    db.session.commit()

    return trail_schema.dump(new_trail), 201


# get all trails
@app.route('/api/trails', methods=['GET'])
def get_all_trails():
    trails = Trail.query.all() 
    return trails_schema.dump(trails)


# retirve
@app.route('/api/trails/<string:name>', methods=['GET'])
def get_trail(name):
    trail = Trail.query.filter(Trail.name == name).one_or_none()
    if trail is None:
        abort(404, f"trail wit name '{name}' not found")
    
    return trail_schema.dump(trail)

#update
@app.route('/api/trails/<string:name>', methods=['PUT'])
def update_trail(name):
    trail = Trail.query.filter(Trail.name == name).one_or_none()
    if trail is None:
        abort(404, f"trail withh name '{name}' not found")

    trail_data = request.get_json()
    trail.name = trail_data.get('name', trail.name)
    trail.description = trail_data.get('description', trail.description)
    trail.length = trail_data.get('length', trail.length)
    trail.difficulty = trail_data.get('difficulty', trail.difficulty)
    trail.location = trail_data.get('location', trail.location)
    
    db.session.commit()

    return trail_schema.dump(trail)


#delete
@app.route('/api/trails/<string:name>', methods=['DELETE'])
def delete_trail(name):
    trail = Trail.query.filter(Trail.name == name).one_or_none()
    if trail is None:
        abort(404, "trail not fonud")

    db.session.delete(trail)
    db.session.commit()

    return '',

if __name__ == '__main__':
    app.run(debug=True)
