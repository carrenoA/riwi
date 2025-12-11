# import libraries that we'll use
import time
import sys

# DataBase ↓

students = [
    {
        "name": "Jeronimo",
        "age": 17,
        "phone": 3123326094,
        "subject": "Calculus"
    },
    {
        "name": "Ana",
        "age": 12,
        "phone": 3133326094,
        "subject": "Chemistry"
    },
    {
        "name": "Sofia",
        "age": 16,
        "phone": 3001247542,
        "subject": "History"
    },
    {
        "name": "Ronaldo",
        "age": 29,
        "phone": 3122249843,
        "subject": "Spanish"
    }
]

opcion = 0

# Functions ↓

# Create a student ↓


def create_student():
    # function to create a record
    def create_record():
        name = input("Enter the name: ")
        age = int(input("Enter the age: "))
        phonenumber = int(input("Enter the phone number: "))
        subject = input("Enter a subject: ")

        data = {
            "name": name,
            "age": age,
            "phone": phonenumber,
            "subject": subject,
        }
        return data
    # loop to add each record in the previous function
    while True:
        new = create_record()
        students.append(new)
        opt = input("\nDo you want to add a new student? (y/n): ").lower()
        if opt != "y":
            break

# Read a student ↓


def read_student(x):
    n_student = 0
    # 'i' traverse 'ts' array and print each value
    for i in x:
        n_student += 1
        print(f"Student {n_student}")
        print(f"Name: {i['name']}\nAge: {i['age']}")
        print(f"Phone Number: {i['phone']}\nSubject: {i['subject']}")
        print("-----------------------------------------\n")

# Update a student ↓


def update_student(x):

    dicc = input("Enter the student's name: ")
    p = input("Enter the attribute to change: ")
    c = input("Enter the new value: ")

    # 'x' = students[]
    for i in x:
        if i['name'] == dicc:
            i[p] = c
        print(i)

# Delete a student ↓


def delete_student():
    b = False
    phone = int(input("Enter the phone number of the student to delete: "))

    for student in students:  # VARIABLE GENERAL DE ALMACENAMIENTO ESTUDIANTES
        if student["phone"] == phone:
            students.remove(student)
            b = True

    if not b:
        print(f"Student with '{phone}' wasn't found")
    else:
        print("-------------Student deleted succesfully-------------")

# Calculate the average ↓


def average_age():
    avg = 0

    for i in students:
        avg = avg + i["age"]
    print(avg/len(students))

# MENU ↓


def show_menu():
    global option  # Set 'option' as a global variable

    time.sleep(1.5)
    print("-------MENU-------")
    time.sleep(1)

    print("1. Create a new student.")
    print("2. Show all students.")
    print("3. Update student's information.")
    print("4. Delete a student.")
    print("5. Average age")
    print("6. Exit\n")

    time.sleep(1)  # 1 second in the console to start

    while True:
        try:
            option = int(input("Choose an option: "))
            print("\n")
        except ValueError:
            print("This option is invalid, try again")
        else:
            break

    match option:
        case 1:
            create_student()
        case 2:
            read_student(students)
        case 3:
            update_student(students)
        case 4:
            delete_student()
        case 5:
            average_age()
        case 6:
            sys.exit("Exiting...")  # Stop program
        case _:
            print("This is not a valid option.")


print("Welcome to the student CRUD!")
time.sleep(1)
print("-------------------------------------------------")

# Show the menu until user choose the exit option
while True:
    show_menu()
