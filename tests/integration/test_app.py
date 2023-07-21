import inject
import pytest
from flask.testing import FlaskClient
from inject import Binder

from app.products import Product, ProductRepository
from tests.integration.fakes import FakeProductRepository
from tests.integration.pages import ProductPage, ProductsPage


@pytest.mark.usefixtures("container")
def test_list_products(client: FlaskClient) -> None:
    def config(binder: Binder) -> None:
        binder.bind(
            ProductRepository,
            FakeProductRepository([Product(1, "x"), Product(2, "y"), Product(3, "z")]),
        )

    inject.clear_and_configure(config)

    response = client.get("/")

    assert ProductsPage(response.text).products == ["x", "y", "z"]


@pytest.mark.usefixtures("container")
def test_get_product(client: FlaskClient) -> None:
    def config(binder: Binder) -> None:
        binder.bind(
            ProductRepository,
            FakeProductRepository([Product(1, "x"), Product(2, "y"), Product(3, "z")]),
        )

    inject.clear_and_configure(config)

    response = client.get("/2")

    assert ProductPage(response.text).header == "Product y"
