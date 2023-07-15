from flask import Flask

app = Flask(__name__)

class ProductRepository:
    def get_all(self):
        return ["a", "b", "c"]

@app.route("/")
def index():
    products = ProductRepository().get_all()
    return f"<p>{products}</p>"
