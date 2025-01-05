import pytest
from app import app, db
from models import Trail, TrailLog

@pytest.fixture
def setup_app():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield
        db.session.remove()
        db.drop_all()

def test_trigger_logs_creation(setup_app):
    with app.app_context():
        trail = Trail(
            Trail_ID='T003',
            Trail_Name='Noxus Trail',
            Trail_Length=3.5
        )
        db.session.add(trail)
        db.session.commit()

        log = db.session.query(TrailLog).filter_by(Trail_ID='T003').first()
        assert log is not None
        assert log.Trail_ID == 'T003'

def test_trail_delete_cascade(setup_app):
    with app.app_context():
        trail = Trail(
            Trail_ID='T004',
            Trail_Name='Demacia Trail',
            Trail_Length=7.5
        )
        db.session.add(trail)
        db.session.commit()

        # Delete the trail
        db.session.delete(trail)
        db.session.commit()

        # Check if the log entry is also deleted
        log = db.session.query(TrailLog).filter_by(Trail_ID='T004').first()
        assert log is None
