from app import app, greet

def test_greet_default():
    assert greet() == "Hello, world!"

def test_greet_custom_name():
    assert greet("Ameya") == "Hello, Ameya!"

def test_home_route():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello from EKS v2 - green candidate!" in response.data

def test_health_route():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}

def test_quote_route():
    client = app.test_client()
    response = client.get("/quote")
    assert response.status_code == 200
    assert "message" in response.get_json()
