import random as r


class Student:
    def __init__(self, name):
        self.name = name
        self.progress = r.randint(50, 80)
        self.happy = r.randint(50, 80)
        self.money = r.randint(100, 200)
        self.life = True

    def study(self):
        print(' Студент навчається')
        self.progress += r.randint(5, 10)
        self.happy -= r.randint(1, 5)

    def chill(self):
        print(' Студент відпочиває')
        self.happy += r.randint(5, 10)
        self.progress -= r.randint(3, 7)
        cost = r.randint(30, 100)
        if self.money >= cost:
            self.money -= cost
            print('Успішно знято', cost)
        else:
            print('Не вистачає коштів')

    def work(self):
        earn = r.randint(50, 100)
        self.money += earn
        print(' Студент працює')
        print('Сума на рахунку збільшена на', earn)

    def status(self):
        if self.progress < 20:
            print(' Відрахований від навчання')
            self.life = False
        elif self.progress < 50:
            print(' Намагається по навчанню, але потрібно краще')

    def info(self, day):
        print(f'\nДень {day}')
        print('Навчання:', self.progress,
              '| Щастя:', self.happy,
              '| Гроші:', self.money)

    def live_day(self, day):
        self.info(day)

        if self.money < 20:
            self.work()
        elif self.progress < 40:
            self.study()
        else:
            choice = r.randint(1, 3)
            if choice == 1:
                self.study()
            elif choice == 2:
                self.work()
            else:
                self.chill()

        self.status()



st = Student('Вася')

for day in range(1, 51):
    if not st.life:
        break
    st.live_day(day)



