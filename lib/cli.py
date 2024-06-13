# lib/cli.py

from sqlalchemy.orm import sessionmaker
from models import Employee, Task, Project, engine
from helpers import (
    exit_program,
    helper_1
) 

Session = sessionmaker(bind=engine)

def main():
    session = Session()

    while True:
        menu()
        choice = input("> ")

        if choice == "0":
            helper_1()
        elif choice == "1":
            manage_employees(session)
        elif choice == "2":
            manage_projects(session)
        elif choice == "3":
            manage_tasks(session)
        elif choice == "4":
            exit_program()
        else:
            print("Invalid choice")


def menu():
    print("\t\t EMPLOYEE TASK MANAGER \t\t")
    print("Please select an option(0-4):")
    print("0. Help")
    print("1. Manage Employees")
    print("2. Manage Projects")
    print("3. Manage Tasks")
    print("4. Exit the program")

def manage_employees(session):
    while True:
        print("\nManage Employees:")
        print("1. Add Employee")
        print("2. View Employee")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Back to Main Menu")

        choice = input(">")

        if choice == "1":
            name = input("Enter Employee name: ")
            age = int(input("Enter Employee age: "))
            new_employee = Employee(name=name, age=age)
            session.add(new_employee)
            session.commit()
            print("Employee added successfully")

        elif choice == "2":
            employees = session.query(Employee).all()
            for employee in employees:
                print(f"ID: {employee.id}, Name: {employee.name}, Age: {employee.age}")
            
        elif choice == "3":
            emp_id = int(input("Enter employee ID to update: "))
            employee = session.query(Employee).get(emp_id)
            if employee:
                employee.name = input("Enter new name: ")
                employee.age = int(input("Enter new age: "))
                session.commit()
                print("Employee updated.")
            else:
                print("Employee not found.")

        elif choice == "4":
            emp_id = int(input("Enter employee ID to delete: "))
            employee = session.query(Employee).get(emp_id)
            if employee:
                session.delete(employee)
                session.commit()
                print("Employee deleted.")
            else:
                print("Employee not found.")

        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")


def manage_projects():
    pass

def manage_tasks():
    pass



if __name__ == "__main__":
    main()
