import inject
from flask import Flask

app = Flask(__name__)

class ProductRepository:
    def get_all(self):
        return ["a", "b", "c"]

@app.route("/")
@inject.autoparams()
def index(product_repository: ProductRepository):
    products = product_repository.get_all()
    return f"<p>{products}</p>"

inject.configure()
