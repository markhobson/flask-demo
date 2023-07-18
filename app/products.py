import inject
from flask import render_template
from flask.blueprints import Blueprint


class ProductRepository:
    def get_all(self):
        return ["Apple", "Banana", "Carrot"]


bp = Blueprint("products", __name__)


@bp.route("/")
@inject.autoparams()
def index(product_repository: ProductRepository):
    products = product_repository.get_all()
    return render_template("index.html", products=products)
