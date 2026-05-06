from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

import models
import schemas
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee Management System")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Employee Management System API is running"}


@app.post("/employees/", response_model=schemas.EmployeeResponse)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    existing_employee = db.query(models.Employee).filter(
        models.Employee.email == employee.email
    ).first()

    if existing_employee:
        raise HTTPException(status_code=400, detail="Employee email already exists")

    new_employee = models.Employee(
        employee_name=employee.employee_name,
        department=employee.department,
        designation=employee.designation,
        salary=employee.salary,
        email=employee.email
    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee


@app.get("/employees/")
def get_all_employees(db: Session = Depends(get_db)):
    employees = db.query(models.Employee).all()
    return employees


@app.get("/employees/{employee_id}")
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(models.Employee).filter(
        models.Employee.id == employee_id
    ).first()

    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee


@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, updated_employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    employee = db.query(models.Employee).filter(
        models.Employee.id == employee_id
    ).first()

    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    employee.employee_name = updated_employee.employee_name
    employee.department = updated_employee.department
    employee.designation = updated_employee.designation
    employee.salary = updated_employee.salary
    employee.email = updated_employee.email

    db.commit()
    db.refresh(employee)

    return employee


@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(models.Employee).filter(
        models.Employee.id == employee_id
    ).first()

    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(employee)
    db.commit()

    return {"message": "Employee deleted successfully"}


@app.get("/employees/department/{department_name}")
def get_employees_by_department(department_name: str, db: Session = Depends(get_db)):
    employees = db.query(models.Employee).filter(
        models.Employee.department == department_name
    ).all()

    return employees


@app.get("/reports/average-salary-by-department")
def average_salary_by_department(db: Session = Depends(get_db)):
    result = db.query(
        models.Employee.department,
        func.avg(models.Employee.salary).label("average_salary")
    ).group_by(models.Employee.department).all()

    return result


@app.get("/reports/departments-high-salary")
def departments_with_high_average_salary(min_salary: float, db: Session = Depends(get_db)):
    result = db.query(
        models.Employee.department,
        func.avg(models.Employee.salary).label("average_salary")
    ).group_by(models.Employee.department).having(
        func.avg(models.Employee.salary) >= min_salary
    ).all()

    return result
@app.get("/reports/average-salary/{department_name}")
def average_salary_for_department(department_name: str, db: Session = Depends(get_db)):
    result = db.query(
        models.Employee.department,
        func.avg(models.Employee.salary).label("average_salary")
    ).filter(
        models.Employee.department == department_name
    ).group_by(models.Employee.department).first()

    if result is None:
        raise HTTPException(status_code=404, detail="Department not found")

    return {
        "department": result.department,
        "average_salary": result.average_salary
    }