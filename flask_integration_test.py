import subprocess
import time
import requests
import pytest
from retry import retry
from app import app
import os

@pytest.fixture(scope='module', autouse=True)
def start_flask_app():
    flask_process= subprocess.Popen(["export FLASK_ENV=development && flask run --host=0.0.0.0 --port=5010"],
                                    stdout=subprocess.DEVNULL,
                                    shell=True,
                                    preexec_fn=os.setsid)
    time.sleep(0.7)
    yield
    flask_process.kill()

def test_short_delays():
    response = requests.get('http://localhost:5010/hang/0.01')
    assert response.status_code == 200
    assert "9, 81" in response.text

pytest.__retry_delay = 0.25
@retry(tries=4)
def retry_my_function():
    pytest.__retry_delay = pytest.__retry_delay - 0.05
    return get_with_delay(pytest.__retry_delay) 

def get_with_delay(delay):
    return requests.get('http://localhost:5010/hang/' + str(delay), timeout=0.11)

def test_longer_delays():
    with pytest.raises(requests.exceptions.ConnectionError):
        response = requests.get('http://localhost:5010/hang/0.2', timeout=0.1)

def test_longer_delays_with_retry():
    response = retry_my_function() 
    assert "9, 81" in response.text
