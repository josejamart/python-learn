import pytest

from flaskr import flaskr


@pytest.fixture
def client():
    flaskr.app.config['TESTING'] = True

    with flaskr.app.test_client() as client:
        yield client


def test_hello_world(client):
    rv = client.get('/')
    assert b'Hello world!' in rv.data
