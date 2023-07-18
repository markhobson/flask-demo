from typing import Iterable
import pytest
import inject
from app.products import Product, ProductRepository


class FakeProductRepository:
    def get_all(self) -> Iterable[Product]:
        return [Product("x"), Product("y"), Product("z")]


@pytest.fixture()
def container():
    inject.clear_and_configure(lambda binder: binder
        .bind(ProductRepository, FakeProductRepository())
    )
    yield
    inject.clear()


def test_index(client, container):
    response = client.get("/")

    assert "<li>x</li>" in response.text \
        and "<li>y</li>" in response.text \
        and "<li>z</li>" in response.text
