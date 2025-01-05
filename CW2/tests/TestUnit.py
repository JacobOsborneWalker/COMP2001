import pytest
from app import app, db
from models import Trail

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.session.remove()
            db.drop_all()

def test_create_trail(client):
    response = client.post('/trails', json={
        'Trail_ID': 'T001',
        'Trail_Name': 'TestTrail',
        'Trail_Length': 5.2,
        'Trail_Elevation_Change': 120.5,
        'Trail_Expected_Time': '01:30:00',
        'Trail_Description': 'test descripton'
    })
    assert response.status_code == 201
    assert response.get_json()['message'] == 'trial created successfully'

def test_create_trail_invalid_input(client):
    response = client.post('/trails', json={
        'Trail_ID': 'T002',
        'Trail_Name': '',
        'Trail_Length': -1.0
    })
    assert response.status_code == 400
    assert 'error' in response.get_json()

def test_get_all_trails(client):
    client.post('/trails', json={
        'Trail_ID': 'T001',
        'Trail_Name': 'TestTrail',
        'Trail_Length': 5.2
    })
    client.post('/trails', json={
        'Trail_ID': 'T002',
        'Trail_Name': 'The Imortal Bastion',
        'Trail_Length': 8.0
    })
    response = client.get('/trails')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2
