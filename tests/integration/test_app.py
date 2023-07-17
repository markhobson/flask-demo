import pytest
import inject
from app.products import ProductRepository


class FakeProductRepository:
    def get_all(self):
        return ["x", "y", "z"]


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
