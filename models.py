from sqlalchemy import Column, Integer, String, Float
from database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    employee_name = Column(String, index=True)
    department = Column(String)
    designation = Column(String)
    salary = Column(Float)
    email = Column(String, unique=True, index=True)