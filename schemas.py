from pydantic import BaseModel


class EmployeeBase(BaseModel):
    employee_name: str
    department: str
    designation: str
    salary: float
    email: str


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeResponse(EmployeeBase):
    id: int

    class Config:
        from_attributes = True