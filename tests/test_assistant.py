from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_ask_valid():
    response = client.post(
        "/assistant/ask", json={"question": "¿Cómo solicito licencia?"}
    )

    assert response.status_code == 200
    assert response.json()["mode"] == "mock"
    assert response.json()["sources"] == []


def test_ask_missing_question():
    response = client.post("/assistant/ask", json={})

    assert response.status_code == 422


def test_ask_short_question():
    response = client.post("/assistant/ask", json={"question": "Hi"})

    assert response.status_code == 422


def test_ask_invalid_type():
    response = client.post("/assistant/ask", json={"question": 123})

    assert response.status_code == 422


def test_ask_spaces():
    response = client.post("/assistant/ask", json={"question": "    "})

    assert response.status_code == 422


def test_ask_invalid_json():
    response = client.post(
        "/assistant/ask",
        content='{"question": ',
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == 422
