from typing import Generator

import inject
import pytest
from flask import Flask

from app import create_app


@pytest.fixture()
def container() -> Generator[None, None, None]:
    yield
    inject.clear()


@pytest.fixture(scope="session")
def app() -> Flask:
    return create_app()
