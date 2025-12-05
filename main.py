class Car:
    count = 0

    def __init__(self, brand, speed=0):
        self.brand = brand
        self.speed = speed
        Car.count += 1

    def accelerate(self, amount):
        self.speed += amount

    def brake(self, amount):
        self.speed += amount
        if self.speed < 0:
            self.speed = 0

    def show_speed(self):
        print(self.brand, "— швидкість:", self.speed)


# Створення об’єктів
C1 = Car("BMW")
C2 = Car("Audi", 20)
C3 = Car("Toyota", 10)

# Виклики методів
C1.accelerate(50)
C1.show_speed()

C2.brake(5)
C2.show_speed()

C3.accelerate(15)
C3.brake(30)
C3.show_speed()

print("Всього автомобілів:", Car.count)
