from bs4 import BeautifulSoup


class ProductsPage:
    def __init__(self, html: str):
        self.soup = BeautifulSoup(html, "html.parser")
        self.products = [li.a.string for li in self.soup("li")]


class ProductPage:
    def __init__(self, html: str):
        self.soup = BeautifulSoup(html, "html.parser")
        self.header = self.soup.h1 and self.soup.h1.string
