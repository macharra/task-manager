# lib/cli.py

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sqlalchemy.orm import sessionmaker
from lib.models.models import Employee, Task, Project, engine
from lib.helpers import (
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
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Back to Main Menu")

        choice = input("> ")

        if choice == "1":
            name = input("Enter Employee name: ")
            age = int(input("Enter Employee age: "))
            department = input("Enter Employee department: ")
            new_employee = Employee(name=name, age=age, department=department)
            session.add(new_employee)
            session.commit()
            print("Employee added successfully!")

        elif choice == "2":
            employees = session.query(Employee).all()
            for employee in employees:
                print(f"ID: {employee.id}, Name: {employee.name}, Age: {employee.age}, Department: {employee.department}")
            
        elif choice == "3":
            emp_id = int(input("Enter employee ID to update: "))
            employee = session.query(Employee).get(emp_id)
            if employee:
                employee.name = input("Enter new name: ")
                employee.age = int(input("Enter new age: "))
                employee.department = input("Enter new department: ")
                session.commit()
                print("Employee updated successfully!")
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


def manage_projects(session):
    while True:
        print ("\nManage Projects:")
        print("1. Add Project")
        print("1. View Projects")
        print("1. Update Project")
        print("1. Delete Project")
        print("5. Back to Main Menu")
        choice = input("> ")

        if choice == "1":
            name = input("Enter project name: ")
            description = input("Enter project description: ")
            new_project = Project(name=name, description=description)
            session.add(new_project)
            session.commit()
            print("Project added.")
        elif choice == "2":
            projects = session.query(Project).all()
            for project in projects:
                print(f"ID: {project.id}, Name: {project.name}, Description: {project.description}")
        elif choice == "3":
            proj_id = int(input("Enter project ID to update: "))
            project = session.query(Project).get(proj_id)
            if project:
                project.name = input("Enter new name: ")
                project.description = input("Enter new description: ")
                session.commit()
                print("Project updated.")
            else:
                print("Project not found.")
        elif choice == "4":
            proj_id = int(input("Enter project ID to delete: "))
            project = session.query(Project).get(proj_id)
            if project:
                session.delete(project)
                session.commit()
                print("Project deleted.")
            else:
                print("Project not found.")
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")


def manage_tasks(session):
    while True:
        print("\nManage Tasks:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Back to Main Menu")
        choice = input("> ")

        if choice == "1":
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            status = input("Enter task status: ")
            new_task = Task(name=name, description=description, status=status)
            session.add(new_task)
            session.commit()
            print("Task added.")

        elif choice == "2":
            tasks = session.query(Task).all()
            for task in tasks:
                print(f"ID: {task.id}, Name: {task.name}, Description: {task.description}, Status: {task.status}")

        elif choice == "3":
            task_id = int(input("Enter task ID to update: "))
            task = session.query(Task).get(task_id)
            if task:
                task.name = input("Enter new name: ")
                task.status = input("Enter new status: ")
                task.description = input("Enter new description: ")
                session.commit()
                print("Task updated.")
            else:
                print("Task not found.")

        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            task = session.query(Task).get(task_id)
            if task:
                session.delete(task)
                session.commit()
                print("Task deleted.")
            else:
                print("Task not found.")

        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")




if __name__ == "__main__":
    main()
