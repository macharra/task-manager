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

def manage_employees():
    pass

def manage_projects():
    pass

def manage_tasks():
    pass



if __name__ == "__main__":
    main()
