from fastapi.testclient import TestClient
from ragapp.main import app
client = TestClient(app)

def test_hit_and_miss():
    hit = client.post("/ask", json={"question": 'How long does database failover take on average?'}).json()
    assert hit["answered"] is True
    assert hit["citation"] == 'runbook.md'
    miss = client.post("/ask", json={"question": "orbital cafeteria soup"}).json()
    assert miss["answered"] is False

def test_empty():
    assert client.post("/ask", json={"question": " "}).status_code == 422

def test_source_filter():
    hit = client.post("/ask", json={"question": "failover seconds", "source": "runbook.md"}).json()
    assert hit["citation"] == "runbook.md"

