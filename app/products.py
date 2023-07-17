import inject
from flask.blueprints import Blueprint
from flask.views import View


class ProductRepository:
    def get_all(self):
        return ["a", "b", "c"]


class ProductView(View):
    @inject.autoparams()
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def dispatch_request(self):
        products = self.product_repository.get_all()
        return f"<p>{products}</p>"


bp = Blueprint("products", __name__)
bp.add_url_rule("/", view_func=ProductView.as_view("index"))
