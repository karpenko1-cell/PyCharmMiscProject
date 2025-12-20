class Character:
    def __init__(self, name, health):
        self.__name = name
        self.__health = max(0, health)  # захист від негативного здоров'я

    def attack(self):
        print("Персонаж атакує")

    def take_damage(self, amount):
        if amount < 0:
            return
        self.__health -= amount
        if self.__health < 0:
            self.__health = 0

    def is_alive(self):
        return self.__health > 0

    def info(self):
        print(f"Ім'я: {self.__name}, Здоров'я: {self.__health}")


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 150)

    def attack(self):
        print("Воїн атакує мечем ⚔")


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, 100)

    def attack(self):
        print("Маг атакує магією ")


# Перевірка роботи
heroes = [
    Warrior("Артур"),
    Mage("Мерлін")
]

for hero in heroes:
    hero.info()
    hero.attack()
    hero.take_damage(40)
    hero.info()
    print("Живий:", hero.is_alive())
    print()