from app import app

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200

def test_quote():
    client = app.test_client()
    response = client.get("/quote")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, CI!"}
