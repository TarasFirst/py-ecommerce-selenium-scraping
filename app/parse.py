from dataclasses import dataclass
from urllib.parse import urljoin

from bs4 import Tag

BASE_URL = "https://webscraper.io/"
HOME_URL = urljoin(BASE_URL, "test-sites/e-commerce/more/")


@dataclass
class Product:
    title: str
    description: str
    price: float
    rating: int
    num_of_reviews: int


def scrape_one_product(product: Tag):
    return Product(
        title=product.select_one(".title")["title"],
        description=product.select_one(".description").text,
        price=float(product.select_one(".price").text.lstrip("$")),
        rating=int(product.select_one("data-rating").text),
        num_of_reviews=int(product.select_one(".review-count").text.split(" ")[0])
    )



def get_all_products() -> None:
    pass


if __name__ == "__main__":
    get_all_products()
