import threading
import time
import requests
import pytest
from app import app

@pytest.fixture(scope='module', autouse=True)
def start_flask_app():
    server_thread = threading.Thread(target=app.run, kwargs={'host': 'localhost', 'port': 5010})
    server_thread.start()
    time.sleep(1)

def test_short_delays():
    response = requests.get('http://localhost:5010/hang/0.01')
    assert response.status_code == 200
    assert "9, 81" in response.text

def test_longer_delays():
    with pytest.raises(requests.exceptions.ConnectionError):
        response = requests.get('http://localhost:5010/hang/0.3', timeout=0.2)
