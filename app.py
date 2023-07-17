import inject
from flask import Flask
from products import ProductView


app = Flask(__name__)
app.add_url_rule("/", view_func=ProductView.as_view("index"))

inject.configure()
