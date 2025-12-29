class Employee:
    """
    Create an Employee class:
    employeeId, name, salary should be private
    Salary should not be set below minimum wage
    Provide a method to calculate annual salary

    """
    MIN_SALARY = 15000

    def __init__(self, emp_id, name, salary):
        self.__emp_id = emp_id
        self.__name = name
        self.set_salary(salary)

    def set_salary(self, salary):
        if salary >= self.MIN_SALARY:
            self.__salary = salary
        else:
            print("Salary below minimum wage")

    def annual_salary(self):
        return self.__salary * 12


emp = Employee(1, "Rahul", 20000)
print("Annual Salary:", emp.annual_salary())
