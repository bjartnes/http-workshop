import pytest
import app

@pytest.fixture()
def test_app():
    testapp = app.app
    testapp.config.update({
        "TESTING": True,
    })

    yield testapp 

@pytest.fixture()
def client(test_app):
    return test_app.test_client()

def test_request_fails_when_reading(client):
    response = client.get("/fail")
    with pytest.raises(Exception):
        response.text

def test_request_ok_when_delay_short(client):
    response = client.get("/hang/0.01")
    response.text