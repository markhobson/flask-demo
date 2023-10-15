from bs4 import BeautifulSoup


class ProductsPage:
    def __init__(self, html: str):
        self._soup = BeautifulSoup(html, "html.parser")
        self.products = [li.a.string for li in self._soup("li")]


class ProductPage:
    def __init__(self, html: str):
        self._soup = BeautifulSoup(html, "html.parser")
        self.header = self._soup.h1 and self._soup.h1.string
