from typing import Generator

import inject
import pytest
from flask import Flask

from app import create_app


@pytest.fixture(name="container", scope="package")
def container_fixture() -> Generator[None, None, None]:
    yield
    inject.clear()


@pytest.fixture(name="app", scope="package")
def app_fixture() -> Flask:
    return create_app()
