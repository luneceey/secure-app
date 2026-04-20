import pytest
from app.main import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

def test_health(client):
	resp = client.get('/health')
	assert resp.status_code == 200
	assert resp.json == {"status": "healthy"}

def test_validate_age_valid(client):
	resp = client.post('/validate_age', json={'age": 25})
	assert resp.status_code == 200
	assert resp.json == {"valid": True, "message": "Age is valid"}

def test_validate_age_missing_field(client):
	resp = client.post('/validate_age', json={})
	assert resp.status_code == 400
	assert "Missing age field" in resp.json["error"]

def test_validate_age_negative(client):
	resp = client.post('/validate_age', json={"age": -5})
	assert resp.status_code == 400
	assert "Age must be an integer between 0 and 150" in resp.json["error"]

def test_validate_age_too_high(client):
	resp = client.post('/validate_age', json={"age": 200})
	assert resp.status_code == 400
	assert "Age must be an integer between 0 and 150" in resp.json["error"]

def test_validate_age_non_integer(client):
	resp = client.post('/validate_age', json={"age": "twenty"})
	assert resp.status_code == 400
	assert "Age must be an integer between 0 and 150" in resp.json["error"]