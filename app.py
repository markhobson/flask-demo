from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    products = ["a", "b", "c"]
    return f"<p>{products}</p>"
