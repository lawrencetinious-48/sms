# k = ["rose", "rita", "moses", "joseph"]
# # print(type(k))
# print(k)

# from datetime import date

# class Student:
#     def __init__(self, age = None, name = None):
#         if age is None:
#             def get_age(self):
#                 while True:
#                     try:
#                         current_year = date.today().year
#                         birth_year = int(input("Enter your birth year(2003):  "))
            
#                     except ValueError:
#                         print(" Enter the correct birth year (2003)")
#                     else:
#                         break
            
#                 return current_year - birth_year
                
#         if name is None:
#             name = input("Enter your name: ").strip().title()

#         self.age = age
#         self.name = name

# teacher = Student()

# print(teacher.age, teacher.name)

# fruits = ["banana","apple","orange","mangoes"]
# k = [u.upper() for u in fruits]
# print(k)

# fruits = ["banana","apple","orange","mangoes"]
# fruits[1] = "tinious"
# print(fruits)

# fruits = ["banana","apple","orange","mangoes"]
# k = [fruits.sort(reverse = True)]
# for i in fruits:
#     if "a" in i:
#         k.append(i)
#         print(i)

# fruits = ["banana","apple","orange","mangoes"]
# k = [fruits.sort(key = str.lower)]
# for i in fruits:
#     if "a" in i:
#         k.append(i)
#         print(i)

# fruits = ["banana", "apple", "orange", "mangoes"]
# m = [fruits.sort(key = str.upper)] #fruits.sort(key = str.lower) #fruits.sort(revrse)
# for _ in fruits:
#     if "a" in _:
#         m.append(_) #type: ignore
#         print(_)

