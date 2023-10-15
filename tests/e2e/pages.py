from __future__ import annotations

from flask import url_for
from playwright.sync_api import Page


class ProductsPage:
    def __init__(self, page: Page):
        self._page = page
        self.products = page.get_by_role("listitem")

    def open(self) -> ProductsPage:
        self._page.goto(url_for("products.index", _external=True))
        return self


class ProductPage:
    def __init__(self, page: Page):
        self._page = page
        self.header = page.get_by_role("heading")

    def open(self, product_id: int) -> ProductPage:
        self._page.goto(url_for("products.get", product_id=product_id, _external=True))
        return self
