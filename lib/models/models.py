from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine
from sqlalchemy.orm import declarative_base, relationship

db_url = "sqlite:///company.db"

engine = create_engine(db_url)

Base =  declarative_base()


task_project_assoc = Table("task_project", Base.metadata, 
    Column("task_id", Integer, ForeignKey("tasks.id"), primary_key=True), 
    Column("project_id", Integer, ForeignKey("projects.id"), primary_key=True))


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True) 
    name = Column(String, nullable=False)
    department = Column(String, nullable=False)
    tasks = relationship("Task", back_populates="employee")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True) 
    description = Column(String, nullable=False)
    status = Column(String, nullable=False)
    employee_id = Column(Integer, ForeignKey("employees.id"))

    employee = relationship("Employee", back_populates="employee")
    projects = relationship("Project", secondary=task_project_assoc, back_populates="tasks")


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String,  nullable=False)
    description = Column(String,  nullable=False)

    tasks = relationship("Task", secondary=task_project_assoc, back_populates="projects")


Base.metadata.create_all(engine)
