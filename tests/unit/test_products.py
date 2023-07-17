from unittest.mock import Mock
from app.products import ProductView


class TestProductView:
    def test_index(self, app):
        product_repository = Mock()
        product_repository.get_all = Mock(return_value=["x", "y", "z"])
        view = ProductView(product_repository)

        with app.app_context():
            response = view.dispatch_request()

        assert "<li>x</li>" in response \
            and "<li>y</li>" in response \
            and "<li>z</li>" in response
