import json
from datetime import date

DATA_FILE = "students.json"

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def get_age():
    while True:
        try:
            birth_year = int(input("Enter birth year (e.g. 2003): "))
            current_year = date.today().year
            return current_year - birth_year
        except ValueError:
            print("Invalid year. Try again.")

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(students):
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)
    print("✔ Data saved successfully.")

def add_student(students):
    name = input("Enter name: ").strip().title()
    age = get_age()
    students.append({"name": name, "age": age})
    print("✔ Student added.")

def view_students(students):
    if not students:
        print("No students found.")
        return
    for s in students:
        print(f"{s['name']} - {s['age']} years old")

def search_student(students):
    key = input("Enter name to search: ").strip().title()
    for s in students:
        if s["name"] == key:
            print(f"Found: {s['name']} - {s['age']} years old")
            return s
    print("Student not found.")
    return None

def update_student(students):
    student = search_student(students)
    if not student:
        return
    print("Enter new info (leave blank to keep old):")
    name = input("New name: ").strip().title()
    if name:
        student["name"] = name
    age_input = input("New birth year (or empty): ")
    if age_input:
        student["age"] = date.today().year - int(age_input)
    print("✔ Student updated.")

def delete_student(students):
    student = search_student(students)
    if not student:
        return
    students.remove(student)
    print("✔ Student deleted.")

def main():
    students = load_data()

    while True:
        print("\n==== Student Management ====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Save")
        print("7. Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            save_data(students)
        elif choice == "7":
            save_data(students)
            print("Exiting…")
            break
        else:
            print("Invalid option.")

main()
