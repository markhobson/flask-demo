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

    assert b"<p>['x', 'y', 'z']</p>" in response.data
