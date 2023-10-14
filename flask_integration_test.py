import subprocess
import threading
import time
import requests
import pytest
from retry import retry
from app import app
import os
#@pytest.fixture(scope='module', autouse=True)
@pytest.fixture(scope='module', autouse=True)
def start_flask_app():
    flask_process= subprocess.Popen(["export FLASK_ENV=development && flask run --host=0.0.0.0 --port=5010"],
                                    stdout=subprocess.DEVNULL,
                                    shell=True,
                                    preexec_fn=os.setsid)
    time.sleep(1)
    yield
    flask_process.kill()

def test_short_delays():
    response = requests.get('http://localhost:5010/hang/0.01')
    assert response.status_code == 200
    assert "9, 81" in response.text

#@retry(ConnectionError, tries=3,delay=1, jitter=1)
@retry(Exception, tries=6)
def foo():
    return requests.get('http://localhost:5010/hang/0.3', timeout=0.2)

def test_longer_delays():
    with pytest.raises(requests.exceptions.ConnectionError):
        response = requests.get('http://localhost:5010/hang/0.3', timeout=0.2)

def test_longer_delays_with_retry():
    response = foo()
    assert "9, 81" in response.text
