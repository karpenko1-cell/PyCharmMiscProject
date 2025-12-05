class Car:
    count = 0

    def __init__(self, make="Unknown", model="Unknown", year="0000"):
        self.make = make
        self.model = model
        self.year = year
        Car.count += 1

    def get_info(self):
        print(self.year, self.make, self.model)
C1 = Car("Toyota", "Corolla", "2010")
C2 = Car("BMW", "X5", "2018")
C3 = Car("Audi", "A6", "2020")

C1.get_info()
C2.get_info()
C3.get_info()

print("Всього автомобілів:", Car.count)