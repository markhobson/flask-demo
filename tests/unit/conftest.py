import os
import pytest
from flask import Flask
from jinja2 import FileSystemLoader


@pytest.fixture()
def app():
    app = Flask("test")
    app.jinja_loader = FileSystemLoader(f"{os.getcwd()}/app/templates")
    return app
