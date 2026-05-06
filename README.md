# Employee Management System

A FastAPI and SQL-based backend project to manage employees, departments, designations, salaries, and employee records.

## Project Overview

Employee Management System is a backend application designed to manage employee information in an organization. Users can add, view, update, and delete employee records. The project also includes department-based filtering and salary reports using SQL concepts such as `GROUP BY` and `HAVING`.

This project demonstrates backend development concepts such as REST API creation, CRUD operations, database connectivity, request validation, SQL aggregation, and API testing using Swagger UI.

## Features

- Add new employee records
- View all employees
- View employee details by ID
- Update employee information
- Delete employee records
- Filter employees by department
- Calculate average salary by department
- Filter departments based on minimum average salary
- Store employee data using SQLite database
- Test APIs using Swagger UI

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn
- Git
- GitHub
- VS Code

## Requirements

Before running this project, make sure you have the following installed:

- Python 3.x
- pip
- Git
- VS Code or any code editor

## Project Structure

```text
employee-management-system/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
└── screenshots/
    └── swagger-ui.png
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home route to check API status |
| POST | `/employees/` | Add a new employee |
| GET | `/employees/` | Get all employees |
| GET | `/employees/{employee_id}` | Get employee by ID |
| PUT | `/employees/{employee_id}` | Update employee details |
| DELETE | `/employees/{employee_id}` | Delete employee |
| GET | `/employees/department/{department_name}` | Get employees by department |
| GET | `/reports/average-salary-by-department` | Get average salary by department |
| GET | `/reports/departments-high-salary` | Get departments with average salary above a given amount |
| GET | `/reports/average-salary/{department_name}` | Get average salary for a specific department |

## Screenshots

### Swagger API Documentation

![Swagger UI](screenshots/swagger-ui.png)

## How to Run This Project

### 1. Clone the Repository

```bash
git clone https://github.com/mdfaiyaz001/employee-management-system.git
```

### 2. Open the Project Folder

```bash
cd employee-management-system
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the FastAPI Server

```bash
uvicorn main:app --reload
```

If the above command does not work, use:

```bash
python -m uvicorn main:app --reload
```

### 5. Open the Application

```text
http://127.0.0.1:8000
```

### 6. Open API Documentation

```text
http://127.0.0.1:8000/docs
```

Swagger UI allows users to test all API endpoints for adding, viewing, updating, deleting, and analyzing employee records.

## Sample Request Body

Use this sample JSON while testing the POST API:

```json
{
  "employee_name": "Rahul Sharma",
  "department": "IT",
  "designation": "Python Developer",
  "salary": 45000,
  "email": "rahul@example.com"
}
```

## Sample Response

```json
{
  "employee_name": "Rahul Sharma",
  "department": "IT",
  "designation": "Python Developer",
  "salary": 45000,
  "email": "rahul@example.com",
  "id": 1
}
```

## What I Learned

- Built REST APIs using FastAPI
- Implemented CRUD operations
- Connected FastAPI with SQLite database
- Used SQLAlchemy ORM for database operations
- Used Pydantic for request and response validation
- Applied SQL aggregation using `GROUP BY` and `HAVING`
- Tested APIs using Swagger UI
- Managed project files using Git and GitHub

## Future Improvements

- Add user authentication
- Add separate department table
- Add employee search by name or email
- Add MySQL database support
- Add frontend dashboard
- Add deployment support

## Author

**MD Faiyaz**  
Python Backend Developer | AIML Student
