# lib/models/models.py

from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine
from sqlalchemy.orm import declarative_base, relationship

db_url = "sqlite:///company.db"

engine = create_engine(db_url)

Base =  declarative_base()


task_project_assoc = Table(
    "task_project", Base.metadata, 
    Column("task_id", Integer, ForeignKey("tasks.id"), primary_key=True), 
    Column("project_id", Integer, ForeignKey("projects.id"), primary_key=True))


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True) 
    name = Column(String, nullable=False)
    department = Column(String, nullable=False)
    tasks = relationship("Task", back_populates="employee", cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Employee(id={self.id}, name={self.name}, department={self.department})>"                                                                                                                                       

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True) 
    description = Column(String, nullable=False)
    status = Column(String, nullable=False)
    employee_id = Column(Integer, ForeignKey("employees.id"))

    employee = relationship("Employee", back_populates="tasks")
    projects = relationship("Project", secondary=task_project_assoc, back_populates="tasks")

    def __repr__(self):
        return f"<Project(id={self.id}, name={self.name}, description={self.description})>"

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String,  nullable=False)
    description = Column(String,  nullable=False)

    tasks = relationship("Task", secondary=task_project_assoc, back_populates="projects")


Base.metadata.create_all(engine)
