class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def info(self):
        print("Ім'я:", self.__name)
        print("Вік:", self.__age)

    def is_adult(self):
        return self.__age > 1


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def info(self):
        super().info()
        print("Порода:", self.breed)


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def info(self):
        super().info()
        print("Колір:", self.color)


animals = [
    Dog("Бобік", 3, "Вівчарка"),
    Cat("Мурка", 1, "Сіра")
]

for a in animals:
    a.info()
    print("Доросла тварина:", a.is_adult())
    print()