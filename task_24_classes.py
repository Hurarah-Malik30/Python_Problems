class EmployeeInfo:
    def __init__(self,emp_id,emp_name,emp_salary,emp_dept):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_dept = emp_dept
        
    def change_dept(self,new_dept):
        self.emp_dept = new_dept
        
    def display(self):
        print(f'Emp ID:{self.emp_id}    Emp Name:{self.emp_name}    Emp Dept:{self.emp_dept}    Emp Salary:{self.emp_salary}')
        
    def Compute_Salary(self,hours_worked):
        overtime = hours_worked - 50
        overtime_amount = (overtime * (self.emp_salary//50))
        print(self.emp_salary+overtime_amount)

e1 = EmployeeInfo("ADAMS", "E7876", 50000, "ACCOUNTING")
e2 = EmployeeInfo("JONES", "E7499", 45000, "RESEARCH")
e1.display()
e2.display()
e1.change_dept("SALES")
e1.display()
# e1.Compute_Salary(52)