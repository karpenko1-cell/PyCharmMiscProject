class Product:
    def __init__(self, name, price, available=True):
        self.name = name
        self.price = price
        self.available = available


class Cart:
    def __init__(self):
        self.products = []

    def add(self, product):
        if product.available:
            self.products.append(product)
            print(f"Товар '{product.name}' додано в кошик")
        else:
            print(f"Товар '{product.name}' недоступний")

    def remove(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"Товар '{product.name}' видалено з кошика")

    def total_price(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    def info(self):
        if self.products == []:
            print("Кошик порожній")
        else:
            print("Товари в кошику:")
            for p in self.products:
                print(p.name, "-", p.price, "грн")
            print("Загальна сума:", self.total_price(), "грн")



p1 = Product("Телефон", 12000)
p2 = Product("Навушники", 1500)
p3 = Product("Ноутбук", 30000, False)

cart = Cart()
cart.add(p1)
cart.add(p2)
cart.add(p3)
cart.info()
