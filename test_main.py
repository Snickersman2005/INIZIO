from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Vyhledávání" in response.text


def test_get_css():
    response = client.get("/output.css")
    assert response.status_code == 200
    assert "text/css" in response.headers["content-type"]


def test_search_returns_correct_shape(monkeypatch):
    fake_response_data = {
        "organic": [
            {"title": "Example Title", "link": "https://example.com"}
        ]
    }

    class FakeResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return fake_response_data

    monkeypatch.setattr("main.requests.post", lambda *a, **k: FakeResponse())

    response = client.get("/search?q=python")
    assert response.status_code == 200

    data = response.json()
    assert data["query"] == "python"
    assert isinstance(data["results"], list)
    assert data["results"][0]["title"] == "Example Title"
    assert data["results"][0]["link"] == "https://example.com"


def test_search_handles_api_failure(monkeypatch):
    import requests

    def fake_post(*a, **k):
        raise requests.RequestException("boom")

    monkeypatch.setattr("main.requests.post", fake_post)

    response = client.get("/search?q=python")
    assert response.status_code == 200
    data = response.json()
    assert data["results"] == []
    assert data["error"] == "search_unavailable"