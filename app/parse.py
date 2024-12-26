from dataclasses import dataclass
from urllib.parse import urljoin

import requests
from bs4 import Tag, BeautifulSoup

BASE_URL = "https://webscraper.io/"
HOME_URL = urljoin(BASE_URL, "test-sites/e-commerce/more/")


@dataclass
class Product:
    title: str
    description: str
    price: float
    rating: int
    num_of_reviews: int


def scrape_one_product(product: Tag) -> Product:
    return Product(
        title=product.select_one(".title")["title"],
        description=product.select_one(".description").text,
        price=float(product.select_one(".price").text.lstrip("$")),
        rating=int(product.select_one("[data-rating]")["data-rating"]),
        num_of_reviews=int(product.select_one(".review-count").text.split(" ")[0])
    )


def get_soup(url: str, session: requests.Session) -> BeautifulSoup:
    response = session.get(url)
    return BeautifulSoup(response.content, "html.parser")


def parse_one_page(url: str) -> [Product]:
    session = requests.Session()
    soup = get_soup(url, session)
    return [scrape_one_product(product) for product in soup.select(".product-wrapper")]


def get_all_products() -> None:
    print(parse_one_page(HOME_URL))


if __name__ == "__main__":
    get_all_products()
