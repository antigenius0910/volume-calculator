import pytest
from flask import Flask, json
from volume_calculator.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_calculate_volume_cube(client):
    response = client.post('/calculate_volume', json={
        'shape': 'cube',
        'dimensions': {'side_length': 3}
    })
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['volume'] == 27

def test_calculate_volume_sphere(client):
    response = client.post('/calculate_volume', json={
        'shape': 'sphere',
        'dimensions': {'radius': 4}
    })
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['volume'] == pytest.approx(268.083, rel=1e-3)

def test_calculate_volume_cylinder(client):
    response = client.post('/calculate_volume', json={
        'shape': 'cylinder',
        'dimensions': {'radius': 3, 'height': 5}
    })
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['volume'] == pytest.approx(141.372, rel=1e-3)

def test_calculate_volume_cone(client):
    response = client.post('/calculate_volume', json={
        'shape': 'cone',
        'dimensions': {'radius': 3, 'height': 5}
    })
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['volume'] == pytest.approx(47.1239, rel=1e-3)

def test_calculate_volume_missing_dimension(client):
    response = client.post('/calculate_volume', json={
        'shape': 'cube',
        'dimensions': {}
    })
    data = json.loads(response.data)
    assert response.status_code == 400
    assert 'error' in data

def test_calculate_volume_invalid_shape(client):
    response = client.post('/calculate_volume', json={
        'shape': 'invalid_shape',
        'dimensions': {}
    })
    data = json.loads(response.data)
    assert response.status_code == 400
    assert 'error' in data
