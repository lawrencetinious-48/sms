# import datetime


from datetime import datetime

class student:
    def __init__(self, age=None, name=None):
        # Compute current year dynamically
        current_year = datetime.now().year #type: ignore

        # If age is not provided, ask for birth year and compute age
        if age is None:
            while True:
                birth = input("Enter your birth year (e.g. 1996): ").strip()
                try:
                    birth_year = int(birth)
                    age = current_year - birth_year
                    break
                except ValueError:
                    print("Please enter a valid numeric year.")

        # If name is not provided, ask for it
        if name is None:
            name = input("Enter your name: ").strip().title()

        self.age = age
        self.name = name

teacher = student()
print(teacher.age, teacher.name)


# x = ["banana", "matooke", "cassava", "water"]
# y = []

# for i in x:
#     if "c" in x:
#         y.append(i)
#         print(y)


# number= 2

# for k in range(12):
#     print(f"{number} * {k} = {number *  k}")
