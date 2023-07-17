import inject
from products import ProductRepository


class FakeProductRepository:
    def get_all(self):
        return ["x", "y", "z"]


def test_index(client):
    inject.clear_and_configure(lambda binder: binder
        .bind(ProductRepository, FakeProductRepository())
    )

    response = client.get("/")

    assert b"<p>['x', 'y', 'z']</p>" in response.data
