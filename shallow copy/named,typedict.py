from collections import namedtuple

Employee = namedtuple('Employee', ['name', 'age', 'department', 'salary'])

emp1 = Employee(name="John Doe", age=30, department="IT", salary=60000)

print(emp1.name)       
print(emp1.department) 


from typing import TypedDict


class Employee(TypedDict):
    name: str
    age: int
    department: str
    salary: int


emp2: Employee = {"name": "Jane Doe", "age": 28, "department": "HR", "salary": 50000}


print(emp2["name"])      
print(emp2["department"]) 

print(emp2["salary"])   


from enum import Enum

class EmployeeRole(Enum):
    ADMIN = "Admin"
    MANAGER = "Manager"
    EMPLOYEE = "Employee"


def get_employee_access(role: EmployeeRole):
    if role == EmployeeRole.ADMIN:
        return "Full Access"
    elif role == EmployeeRole.MANAGER:
        return "Limited Admin Access"
    elif role == EmployeeRole.EMPLOYEE:
        return "Basic Access"
    else:
        return "No Access"

role = EmployeeRole.MANAGER
print(role)  
print(role.value) 

print(get_employee_access(role))  