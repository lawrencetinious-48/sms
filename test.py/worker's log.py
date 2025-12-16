import random
from datetime import datetime


def get_code():
    number = [234, 456, 729, 701]
    code = random.choice(number)
    print(code)


class Company:
    def __init__(self, name = None, time = None, department = None, sign_out = None):

        if name is None:
            self.user_name = input("Enter your name: ").strip().title()
            print(self.user_name)

        if time is None:
                self.time = datetime.now()
                print(f"You got in at: {self.time}:")
        
        if department is None:
            self.department = input("Enter your department: ").upper().strip()
            print(self.department)
        
        if sign_out is None:
            self.sign_out = datetime.now()
            print(f"You got out at: {self.sign_out}")

        self.username = name
        self.time = time
        self.department_in = department
        self.sign_out = sign_out

worker = Company()
print(worker.username, worker.time, worker.department, worker.sign_out)
get_code()