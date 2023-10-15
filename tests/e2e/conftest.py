from typing import Generator

import inject
import pytest
from flask import Flask

from app import create_app


@pytest.fixture(name="app", scope="package")
def app_fixture() -> Generator[Flask, None, None]:
    yield create_app()
    inject.clear()
