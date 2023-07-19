from typing import Generator

import inject
import pytest
from flask import Flask
from flask.testing import FlaskClient

from app import create_app


@pytest.fixture()
def container() -> Generator[None, None, None]:
    yield
    inject.clear()


@pytest.fixture
def app() -> Flask:
    return create_app()


@pytest.fixture()
def client(app: Flask) -> FlaskClient:
    return app.test_client()
