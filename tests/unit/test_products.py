from app.products import Product, ProductRepository


class TestProductRepository:
    def test_get_all(self):
        product_repository = ProductRepository()
        
        products = product_repository.get_all()

        assert products == [Product("Apple"), Product("Banana"), Product("Carrot")]
