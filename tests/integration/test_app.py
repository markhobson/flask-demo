from typing import Generator, Iterable

import inject
import pytest
from flask.testing import FlaskClient
from inject import Binder

from app.products import Product, ProductRepository


class FakeProductRepository:
    products = [Product(1, "x"), Product(2, "y"), Product(3, "z")]

    def get_all(self) -> Iterable[Product]:
        return self.products

    def get(self, product_id: int) -> Product:
        return next(filter(lambda product: product.id == product_id, self.products))


@pytest.fixture()
def container() -> Generator[None, None, None]:
    yield
    inject.clear()


def test_list_products(client: FlaskClient, container: None) -> None:
    def config(binder: Binder) -> None:
        binder.bind(ProductRepository, FakeProductRepository())

    inject.clear_and_configure(config)

    response = client.get("/")

    assert (
        '<a href="/1">x</a>' in response.text
        and '<a href="/2">y</a>' in response.text
        and '<a href="/3">z</a>' in response.text
    )


def test_get_product(client: FlaskClient, container: None) -> None:
    def config(binder: Binder) -> None:
        binder.bind(ProductRepository, FakeProductRepository())

    inject.clear_and_configure(config)

    response = client.get("/2")

    assert "<h1>Product y</h1>" in response.text
