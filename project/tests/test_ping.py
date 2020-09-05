# from app import main

# Given
def test_ping(test_app_with_db):

    # When
    response = test_app_with_db.get("/ping")

    # Then
    assert response.status_code == 200
    assert response.json() == {"environment": "dev", "ping": "pong", "testing": True}
