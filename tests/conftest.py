import pytest
from app import app as CJKFlask

@pytest.fixture()
def app():
    yield CJKFlask

@pytest.fixture
def client(app):
    return app.test_client

