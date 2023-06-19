from app.main import app
from app.constants import WELCOME_MESSAGE
from fastapi.testclient import TestClient

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"app_description": WELCOME_MESSAGE }

def test_summarize():
    data = {'title': 'Title of text', 'text': 'This is the text i want to summarize', 'min_length': 1}
    response = client.post("/summarize", json=data)
    response_data = dict(response.json())

    assert response.status_code == 200
    assert list(response_data.keys()) == ['summary_text', 'title']
    assert len(response_data['summary_text']) >= data['min_length']