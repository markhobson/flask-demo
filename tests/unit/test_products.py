from app.products import Product, ProductRepository


class TestProductRepository:
    def test_get_all(self) -> None:
        product_repository = ProductRepository()
        
        products = product_repository.get_all()

        assert products == [Product(1, "Apple"), Product(2, "Banana"), Product(3, "Carrot")]

    def test_get(self) -> None:
        product_repository = ProductRepository()

        product = product_repository.get(2)

        assert product == Product(2, "Banana")
