import requests
from bs4 import BeautifulSoup


class QuotesParser:
    def __init__(self, url):
        self.url = url
        self.quotes = []

    def get_html(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        else:
            print(" Не вдалося завантажити сайт")
        return None

    def parse(self):
        html = self.get_html()
        if not html:
            return

        soup = BeautifulSoup(html, "html.parser")

        items = soup.find_all("div", class_="quote")

        for item in items:
            text = item.find("span", class_="text")
            author = item.find("small", class_="author")
            tags = item.find_all("a", class_="tag")
            author_link = item.find("a")

            self.quotes.append({
                "text": text.get_text(strip=True),
                "author": author.get_text(strip=True),
                "tags": ", ".join(tag.get_text() for tag in tags),
                "link": "https://quotes.toscrape.com" + author_link["href"]
            })

    def show_result(self):
        print("\nСПИСОК ЦИТАТ\n")

        for i, q in enumerate(self.quotes, start=1):
            print(f"{i}. Цитата: {q['text']}")
            print(f"   Автор: {q['author']}")
            print(f"   Теги: {q['tags']}")
            print(f"   Посилання на автора: {q['link']}")
            print("-" * 50)


url = "https://quotes.toscrape.com/"
parser = QuotesParser(url)
parser.parse()
parser.show_result()


