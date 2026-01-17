import requests
from bs4 import BeautifulSoup


url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

products = []

items = soup.find_all("article", class_="product_pod")[:10]

for item in items:
    title = item.h3.a["title"]
    price_text = item.find("p", class_="price_color").text
    price_text = item.find("p", class_="price_color").text

    price = float(
        "".join(c for c in price_text if c.isdigit() or c == ".")
    ) * 40

    products.append({
        "title": title,
        "price": int(price)
    })

print("\nТОП-10 товарів:\n")
for i, product in enumerate(products, 1):
    print(f"{i}. {product['title']} — {product['price']} грн")

cart = []
total = 0

while True:
    choice = int(input("\nЯкий товар ви хочете придбати? (введіть номер): "))
    qty = int(input("Скільки одиниць ви хочете купити?: "))

    product = products[choice - 1]
    subtotal = product["price"] * qty
    total += subtotal

    cart.append((product["title"], qty, subtotal))

    more = input("Хочете ще щось? (так/ні): ").lower()
    if more != "так":
        break

print("\nВаше замовлення:")
for item in cart:
    print(f"- {item[0]} x{item[1]} = {item[2]} грн")

print(f"\nЗагальна сума до сплати: {total} грн")





