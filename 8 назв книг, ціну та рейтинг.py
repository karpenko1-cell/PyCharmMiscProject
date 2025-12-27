import requests
from bs4 import BeautifulSoup as bs

class BookScraper:
    def __init__(self, url):
        self.url = url
        self.books = []

    def load_site(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return bs(response.text, "html.parser")
        else:
            print(" Не вдалося завантажити сайт")
            return None

    def get_info(self, limit=8):
        soup = self.load_site()
        if not soup:
            return

        items = soup.find_all("article", class_="product_pod")

        for item in items[:limit]:
            title = item.h3.a["title"]
            price = item.find("p", class_="price_color").get_text()
            rating = item.find("p", class_="star-rating")["class"][1]

            self.books.append({
                "title": title,
                "price": price,
                "rating": rating
            })

    def show_info(self):
        print("\033[34m\nСПИСОК КНИГ (8 шт.)\033[0m\n")
        for i, book in enumerate(self.books, start=1):
            print(f"{i}. Назва: {book['title']}")
            print(f"   Ціна: {book['price']}")
            print(f"   Рейтинг: {book['rating']}")
            print("-" * 40)


url = "http://books.toscrape.com/"
scraper = BookScraper(url)
scraper.get_info(8)
scraper.show_info()
