from unittest.mock import Mock
from app.products import Product, ProductRepository, index


class TestProductRepository:
    def test_get_all(self):
        product_repository = ProductRepository()
        
        products = product_repository.get_all()

        assert products == [Product("Apple"), Product("Banana"), Product("Carrot")]


def test_index(app):
    product_repository = Mock()
    product_repository.get_all = Mock(return_value=[Product("x"), Product("y"), Product("z")])

    with app.app_context():
        response = index(product_repository)

    assert "<li>x</li>" in response \
        and "<li>y</li>" in response \
        and "<li>z</li>" in response
