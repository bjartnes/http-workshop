import subprocess
import time
import requests
import pytest
from requests.adapters import HTTPAdapter
from tenacity import retry, stop_after_attempt
from urllib3 import Retry
from app import app
import os

def retry_session(retries, session=None, backoff_factor=3, backoff_max=3):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        backoff_max = backoff_max
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

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
    response = retry_session(3).get('http://localhost:5010/hang/0.01')
    assert response.status_code == 200
    assert "9, 81" in response.text

pytest.__retry_delay = 0.25
@retry(stop=stop_after_attempt(4))
def retry_get_with_delay():
    pytest.__retry_delay = pytest.__retry_delay - 0.05
    return get_with_delay(pytest.__retry_delay) 

def get_with_delay(delay):
    return retry_session(3).get('http://localhost:5010/hang/' + str(delay), timeout=0.11)

def test_longer_delays():
    with pytest.raises(requests.exceptions.ConnectionError):
        response = retry_session(3).get('http://localhost:5010/hang/0.2', timeout=0.1)

def test_retry_quits_with_connection_errors_with_trillion_retries():
    with pytest.raises(requests.exceptions.ConnectionError):
        response = retry_session(1000000000000).get('http://localhost:5010/hang/0.2', timeout=0.1)

def test_longer_delays_with_retry():
    response = retry_get_with_delay() 
    assert "9, 81" in response.text
