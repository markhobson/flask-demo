from dataclasses import dataclass
from typing import Iterable

import inject
from flask import render_template
from flask.blueprints import Blueprint


@dataclass
class Product:
    id: int
    name: str


class ProductRepository:
    def __init__(self) -> None:
        self.products = [
            Product(1, "Apple"),
            Product(2, "Banana"),
            Product(3, "Carrot"),
        ]

    def get_all(self) -> Iterable[Product]:
        return self.products

    def get(self, product_id: int) -> Product:
        return next(filter(lambda product: product.id == product_id, self.products))


bp = Blueprint("products", __name__)


@bp.route("/")
@inject.autoparams()
def index(product_repository: ProductRepository) -> str:
    products = product_repository.get_all()
    return render_template("index.html", products=products)


@bp.route("/<int:product_id>")
@inject.autoparams()
def get(product_id: int, product_repository: ProductRepository) -> str:
    product = product_repository.get(product_id)
    return render_template("product.html", product=product)
