class BankAc:
    def __init__(self,owner):
        self.owerno = owner
        self.balance = 0

    def deposit(self,amount):
        self.balance += amount
        print('Сума на рахунку збільшено на',amount,'\nваш баланс',self.balance)
    def withdraw(self,amount):
       if self.balance >= amount:
         self.balance -= amount
         print('успешно знято', amount, '\nваш баланс', self.balance)
       else:
        print('Не вистачає коштив', '\nваш баланс', self.balance)

    def show_balance(self):
        print('Власник рахунку',self.owner,'поточний баланс',self.balance)

b1 = BankAc('сигма')
b1.deposit(1000)
b1.withdraw(1500)
b1.show_balance()
print()
b2 = BankAc('сигма')
b2.deposit(1000)
b2.deposit(1000)
b2.withdraw(2000)
b2.show_balance()
