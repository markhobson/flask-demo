from unittest.mock import Mock
from app.products import ProductRepository, index


class TestProductRepository:
    def test_get_all(self):
        product_repository = ProductRepository()
        
        products = product_repository.get_all()

        assert products == ["Apple", "Banana", "Carrot"]


def test_index(app):
    product_repository = Mock()
    product_repository.get_all = Mock(return_value=["x", "y", "z"])

    with app.app_context():
        response = index(product_repository)

    assert "<li>x</li>" in response \
        and "<li>y</li>" in response \
        and "<li>z</li>" in response
