from fastapi.testclient import TestClient
from BlogSite.asgi import fastapi as app
import sys

client = TestClient(app)


def test_read_main():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.text == "Hello World"

test_read_main()