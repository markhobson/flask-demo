from unittest.mock import Mock
from products import ProductView

def test_index():
    product_repository = Mock()
    product_repository.get_all = Mock(return_value=["x", "y", "z"])
    view = ProductView(product_repository)

    response = view.dispatch_request()

    assert response == "<p>['x', 'y', 'z']</p>"
