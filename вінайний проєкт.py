import requests
from bs4 import BeautifulSoup as bs
import re


class CurrencyScraper:
    def __init__(self, url):
        self.url = url
        self.currencies = []

    def load_site(self):
        response = requests.get(
            self.url,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        if response.status_code == 200:
            return bs(response.text, "html.parser")
        else:
            print("Не вдалося завантажити сайт")
            return None

    def get_info(self, limit=5):
        soup = self.load_site()
        if not soup:
            return

        rows = soup.find("table").find_all("tr")[1:limit + 1]

        for row in rows:
            cols = row.find_all("td")

            buy_text = cols[1].get_text(strip=True)
            sell_text = cols[2].get_text(strip=True)

            # Беремо перше число з тексту (ігноруємо зміни)
            buy_match = re.search(r"\d+\.\d+", buy_text)
            sell_match = re.search(r"\d+\.\d+", sell_text)

            if buy_match and sell_match:
                buy = float(buy_match.group())
                sell = float(sell_match.group())
            else:
                continue

            self.currencies.append({
                "name": cols[0].get_text(strip=True),
                "buy": buy,
                "sell": sell
            })

    def show_info(self):
        print("\nОтримані курси валют:\n")
        for i, c in enumerate(self.currencies, 1):
            print(f"{i}. {c['name']}: Купівля {c['buy']:.2f} грн, Продаж {c['sell']:.2f} грн")




url = "https://minfin.com.ua/ua/currency/"
scraper = CurrencyScraper(url)
scraper.get_info(5)
scraper.show_info()


print("\nВиберіть дію:")
print("1 - Купити валюту")
print("2 - Продати валюту")

action = input("> ")

if action in ("1", "2"):
    choice = int(input("\nВиберіть валюту (номер):\n> "))
    if 1 <= choice <= len(scraper.currencies):
        amount = float(input("\nВведіть суму в гривнях:\n> "))

        currency = scraper.currencies[choice - 1]

        if action == "1":
            result = amount / currency["sell"]
            print(f"\nВи купуєте {currency['name']}. Отримаєте: {result:.2f} {currency['name']}")
        else:
            result = amount / currency["buy"]
            print(f"\nВи продаєте {currency['name']}. Отримаєте: {result:.2f} {currency['name']}")
    else:
        print("Невірний номер валюти")
else:
    print("Невірний вибір дії")









