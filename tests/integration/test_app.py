from typing import Generator

import inject
import pytest
from flask.testing import FlaskClient
from inject import Binder

from app.products import Product, ProductRepository
from tests.support import FakeProductRepository


@pytest.fixture()
def container() -> Generator[None, None, None]:
    yield
    inject.clear()


def test_list_products(client: FlaskClient, container: None) -> None:
    def config(binder: Binder) -> None:
        binder.bind(
            ProductRepository,
            FakeProductRepository([Product(1, "x"), Product(2, "y"), Product(3, "z")]),
        )

    inject.clear_and_configure(config)

    response = client.get("/")

    assert (
        '<a href="/1">x</a>' in response.text
        and '<a href="/2">y</a>' in response.text
        and '<a href="/3">z</a>' in response.text
    )


def test_get_product(client: FlaskClient, container: None) -> None:
    def config(binder: Binder) -> None:
        binder.bind(
            ProductRepository,
            FakeProductRepository([Product(1, "x"), Product(2, "y"), Product(3, "z")]),
        )

    inject.clear_and_configure(config)

    response = client.get("/2")

    assert "<h1>Product y</h1>" in response.text
