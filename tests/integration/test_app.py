import inject
import pytest
from bs4 import BeautifulSoup
from flask.testing import FlaskClient
from inject import Binder

from app.products import Product, ProductRepository
from tests.support import FakeProductRepository


@pytest.mark.usefixtures("container")
def test_list_products(client: FlaskClient) -> None:
    def config(binder: Binder) -> None:
        binder.bind(
            ProductRepository,
            FakeProductRepository([Product(1, "x"), Product(2, "y"), Product(3, "z")]),
        )

    inject.clear_and_configure(config)

    response = client.get("/")

    assert [
        li.a.string for li in BeautifulSoup(response.text, "html.parser")("li")
    ] == ["x", "y", "z"]


@pytest.mark.usefixtures("container")
def test_get_product(client: FlaskClient) -> None:
    def config(binder: Binder) -> None:
        binder.bind(
            ProductRepository,
            FakeProductRepository([Product(1, "x"), Product(2, "y"), Product(3, "z")]),
        )

    inject.clear_and_configure(config)

    response = client.get("/2")

    soup = BeautifulSoup(response.text, "html.parser")
    assert soup.h1 and soup.h1.string == "Product y"
