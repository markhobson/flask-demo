from typing import Iterable

from app.products import Product


class FakeProductRepository:
    def __init__(self, products: Iterable[Product]):
        self._products = products

    def get_all(self) -> Iterable[Product]:
        return self._products

    def get(self, product_id: int) -> Product:
        return next(filter(lambda product: product.id == product_id, self._products))
