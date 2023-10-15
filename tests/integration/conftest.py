from typing import Generator

import inject
import pytest
from flask import Flask
from flask.testing import FlaskClient

from app import create_app


@pytest.fixture(name="container")
def container_fixture() -> Generator[None, None, None]:
    yield
    inject.clear()


@pytest.fixture(name="app")
def app_fixture() -> Flask:
    return create_app()


@pytest.fixture(name="client")
def client_fixture(app: Flask) -> FlaskClient:
    return app.test_client()
