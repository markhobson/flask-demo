import os
import pytest
from unittest.mock import Mock
from flask import Flask
from jinja2 import FileSystemLoader
from app.products import ProductView


@pytest.fixture()
def app():
    app = Flask("test")
    app.jinja_loader = FileSystemLoader(f"{os.getcwd()}/app/templates")
    return app


def test_index(app):
    product_repository = Mock()
    product_repository.get_all = Mock(return_value=["x", "y", "z"])
    view = ProductView(product_repository)

    with app.app_context():
        response = view.dispatch_request()

    assert "<li>x</li>" in response \
        and "<li>y</li>" in response \
        and "<li>z</li>" in response
