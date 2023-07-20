import pytest
from playwright.sync_api import Page, expect

from tests.e2e.pages import ProductPage, ProductsPage


@pytest.mark.usefixtures("container", "live_server")
def test_list_products(page: Page) -> None:
    products_page = ProductsPage(page).open()

    expect(products_page.products).to_have_text(["Apple", "Banana", "Carrot"])


@pytest.mark.usefixtures("container", "live_server")
def test_get_product(page: Page) -> None:
    product_page = ProductPage(page).open(2)

    expect(product_page.header).to_have_text("Product Banana")
