import inject
from flask import Flask
from app import products


def create_app():
    inject.configure()

    app = Flask(__name__)
    app.register_blueprint(products.bp)

    return app
