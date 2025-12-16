# class BankAccount:
#     def __init__(self, account_holder, balance = 0):
#         self.account_holder = account_holder
#         self.balance = balance
    
#     def deposit(self, amount):
#         self.balance += amount
#         return f"Deposited:{amount}, New balance is:{self.balance}"
    
#     def withdraw(self, amount):
#         if amount > self.balance:
#             return "Insufficient Fund!"
#         self.balance -= amount
#         return f"withdraw{amount}. New balance is:{self.balance} "
    
# account = BankAccount("tinious", 24500000)

# print(account.deposit(2000432), account.withdraw(10000000000000))

import datetime

class BankAccount:
    global name
    def __init__(self, account_holder = None, age = None, balance = 0):
        if account_holder is None:
            name = input("Enter your name: ").strip().title()
            print(name)
    
        if age is None:
            while True:
                birth_year = input("Enter your birth year(2005): ")
                try:
                   birth = int(birth_year)
                   current_year = datetime.date.today().year
                   age = current_year - birth

                   break
                except ValueError:
                    if age >= 18:
                        continue
                    else:
                        pass
        self.account_holder = name
        self.age = age
        self.balance = balance


    def deposit(self, amount):
        amount = int(input("Enter the amount you want to deposit: "))
        return self.balance + amount

    def withdraw(self, amount):
        amount = int(input("Enter the amount you want to withdraw: "))

        if amount > self.balance:
            return "Insufficient Fund! "
        else:
            return self.balance - amount

account = BankAccount()
print(account.deposit, account.withdraw)
    
    
        