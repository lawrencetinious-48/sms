class Person:
    pass
personal = Person()
print(type(personal))

class Person:
    def greet(name):
        name = input("Enter your user_name: ").strip().title()
        print("Hello", name)

personal = Person()
personal.greet()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, This is {self.name} and i am {self.age} years old! ")

personal = Person("Tinious", 22)
personal.greet()

class calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

calc = calculator()
print(calc.add(1000, 5j))
print(calc.subtract(1000, 5j))

class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("woof woof")

class Owner:
    def __init__(self, name, address, number):
        self.name = name
        self.address = address
        self.number = number

owner1 = Owner("tinious", "mutongo hills", "256+ 709862572")
dog1 = Dog("bruce", "scottish", owner1)
dog1.bark()
print(dog1.name, dog1.breed, dog1.owner.name, dog1.owner.address, dog1.owner.number)

owner2 = Owner("lawrence", "namugongo", "256+ 709767542")
dog2 = Dog("freya", "greyhound", owner2)
dog2.bark()
print(dog2.name, dog2.breed, dog2.owner.name, dog2.owner.address, dog2.owner.number)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and i am {self.age} years old.")

personal1 = Person("tinious", 23)
personal1.greet()

personal2 = Person("lawrence", 33)
personal2.greet()

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.__email = email
        self.password = password

    def get_email(self):
        return self.__email

user1 = User("spiderman", "lawerancemulindwa48@gmail.com", "*****&$***")
user1.__email = "lawrencemulindwa48@gmail.com"
print(user1.__email)


def say_hi_to_user(self,user):
        print(f"sending massage to {user.username}: Hi {user.username}, its {self.username}")


user1 = User("spiderman", "lawerancemulindwa48@gmail.com", "*****&$***")
user2 = User("batman", "batman@gmail", "****@$***")
user1.say_hi_to_user(user2)
print(user1.email)
user1.email = "lawerancemulindwa48@gmail.com"

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

human = Person("Tinious", 22)
print(human.name, human.age)


# ? without the __init__ method we need to create the properties manually
class Person:
    pass

    def greet(self):
        print(f"Hello, my is {self.name}")

p1 = Person()
p1.name = "tinious"
p1.age = 22

print

class Person:
    def __init__(self, name = "lawrence", age = 22):
        self.name = name
        self.age = age

    def greet(abc):
        print(f"Hello my name is {abc.name} and am {abc.age} years old! ")

Human = Person("tinious", 23)
print(Human.name, Human.age)
Human.greet()

class Person:
    def __init__(self, name):
        self.user = name

    def greet(self):
        return f"Hello, ", {self.user}

    def welcome(self):
        message = self.greet()
        print (f"{message}, !Welcome to our bootcamp.")

p1 = Person("Tinious")
p1.welcome

from datetime import datetime

class User:
    def __init__(self,username, email, password):
        self.name = username
        self.__email = email
        self.password = password
    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        if "@" in new_email:
            print(f"Email accessed at {datetime.now()}")
            self.__email = new_email

user1 = User("Tinious", "lawrencemulindwa47@gmail.com", "*****@#**")
print(user1.name,user1.password)

user1.set_email("1123@422")
# user1.set_email("captainmotherfucker123@gmail.com")
print(user1.get_email())


# static attributes

class User:

    user_count = 0
    def __init__(self, name, email):
        self.username = name
        self.email = email
        User.user_count += 1

    @staticmethod
    def display_user(self):
        print(f"Username: {self.username}, Email:{self.email}")

user1 = User("lawrence","lawrence3548@")
user2 = User("mulindwa","mulindwa3548@")

print(User.user_count)
print(user1.user_count, user2.user_count)


encapsulation

class BadBankAccount:
    def __init__(self, balance):
        self.balance = balance


account = BadBankAccount(0.0)
account.balance = -1
print(account.balance)

class BankAccount:
    def __init__(self):
        self._balance = 0.0

    @property
    def balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive. ")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive. ")
        if amount >= self._balance:
            raise ValueError("Insufficient Fund!. ")
        self._balance -= amount

account = BankAccount()
print(account.balance)

account.deposit(100000)
print(account.balance)
account.withdraw(5000)
print(account.balance)

class Emailservice:

    def connect(self):
        print("connecting to email server")

    def authentication(self):
        print("Authenticating.......")

    def send_email(self):
         print("Sending email...")
        #  self._connect()
        #  self._authenticate()
        #  self.disconnecting()

    def disconnecting(self):
        print("Disconnecting from email server...")

email = Emailservice()
email.connect()
email.authentication()
email.send_email()
email.disconnecting()