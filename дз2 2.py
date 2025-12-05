class Employee:
    count = 0

    def __init__(self, name="NoName", position="Unknown", salary=0):
        self.name = name
        self.position = position
        self.salary = salary
        Employee.count += 1

    def get_salary_info(self):
        print("Заробітна плата", self.name + ":", self.salary)
E1 = Employee("Іван", "Менеджер", 15000)
E2 = Employee("Олена", "Бухгалтер", 18000)
E3 = Employee("Максим", "Програміст", 35000)

E1.get_salary_info()
E2.get_salary_info()
E3.get_salary_info()

print("Всього працівників:", Employee.count)