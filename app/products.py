from typing import Iterable
from dataclasses import dataclass
import inject
from flask import render_template
from flask.blueprints import Blueprint


@dataclass
class Product:
    name: str


class ProductRepository:
    def get_all(self) -> Iterable[Product]:
        return [Product("Apple"), Product("Banana"), Product("Carrot")]


bp = Blueprint("products", __name__)


@bp.route("/")
@inject.autoparams()
def index(product_repository: ProductRepository):
    products = product_repository.get_all()
    return render_template("index.html", products=products)
