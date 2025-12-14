# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self._age = age
#     def info(self):
#         return
#
#
#
#
# class StudentSchool(Student):
#     def __init__(self, name, age,school):
#         super().__init__(name, age)
#         self.school = school
#     def info(self):
#         print('у школі',self.school)
# class StudentUniversal(Student):
#     def __init__(self, name, age,nameUniversal):
#         super().__init__(name, age)
#         self.nameUniversal=nameUniversal
#     def info(self):
#         print('назва спеціальності',self.nameUniversal)
#
# # #class Human:
# #     def __init__(self):
# #         print(self._age)
#
# #st= Student('Світлана', 20)
# #st.info()
# # st1
# stud=[
# StudentUniversal('Сашко',20,'разробник'),
# StudentSchool('Глаша',11,101),
# Student('Гриша',4)
# ]
# for s in stud:
#     print(s.name,s._age,end=':')
#     s.info()

# class Dani:
#     def __init__(self,password):
#         self.__password = password
#
#     def chagePass(self,value):
#         return self.__password == value
#
# d1 = Dani('123')
# print(d1.chagePass('123456'))
# print(d1._Dani__password)

class Human:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def info(self):

        print("Ім'я",self.__name,"\nВік:",self.__age)
    def old(self):
        return self.__age>17

class School(Human):
    def __init__(self, name, age,clas,ball):
        super().__init__(name, age)
        self.clas = clas
        self.__ball = ball
    def grade(self):
        return sum(self.__ball) /len(self.__ball)
    def info(self):
        super().info()
        print('Середний бал учня:',self.grade())

class Worker(Human):
    def __init__(self, name, age, stavka,hour):
        super().__init__(name, age)
        self.__stavka = stavka
        self.hour = hour
    def salary(self):
        return self.__stavka * self.hour
    def info(self):
        super().info()
        print('Зарплатня',self.salary())

people=[
    School('Оля',15,9,[11,7,9,10]),
School('Петя',18,11,[11,5,9,10]),
Worker('Леана',32,175.50,50),
Worker('Андрій',22,190,85)
]
for p in people:
    p.info()
    print('Повнолітні:',p.old())
    print()