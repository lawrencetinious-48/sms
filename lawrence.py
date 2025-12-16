# carts = ['books', 'pens', 'pencils', 'colours']
# for cart in carts:
#     if cart == 'pencils':
#         # break
#         continue
#     print(cart)

# count = 5

# for i in range(12):
#     print(f'{count} * {i} = {count * i}')

from datetime import datetime, time

class Student:
    def __init__(self, age = None): # type: ignore
        self.age = age
        if age is None:
            def age():
                current_year = datetime.today()
                birth_year :int = int(input("Enter your birth year: "))
                self.age = "current_year - birth_year"
                print(self.age)
            
person = Student()
print(person.age)

