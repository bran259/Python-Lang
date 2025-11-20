class Department:
    # Has many employees
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.manager = None

    def add_employee(self, employee):
        # checking if employee is an isinstanceof class Employee
        if not isinstance(employee, Employee):
            print("Department must be an instance of Department class")
            raise TypeError("department must be an instance of Department")
         
        self.employees.append(employee)  
        # return self.employees
    
    def list_of_employees(self):
        return [f'{employee.name} {employee.position}'for employee in self.employees]


class Employee:
    # Belongs to a department
    def __init__(self, name, position, department):
        self.name = name
        self.position = position
        self._department = None  # internal attribute
        self.department = department  # call setter

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, department):
        if not isinstance(department, Department):
            raise TypeError("department must be an instance of Department")

        self._department = department
        department.employees.append(self)  # keep relationship consistent

engineering = Department("Engineering")
agriculture = Department("agriculture")

emp1 = Employee("Brian", "TM", engineering)
emp2 = Employee("Erasmus", "TM", engineering)
emp3 = Employee("Titus", "TM", engineering)
emp4 = Employee("Marion", "TM", engineering)
emp5 = Employee("Mercy", "TM", engineering)

# print(emp1.department.name)
# print([e.name for e in engineering.employees])

engineering.add_employee(emp1)
engineering.add_employee(emp2)
engineering.add_employee(emp3)
engineering.add_employee(emp4)
engineering.add_employee(emp5)

print(engineering.list_of_employees())
print(agriculture.list_of_employees())