class Employee:
    def __init__(self, employee_id, name, department, basic_salary, bonus=0, overtime_hours=0):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.basic_salary = basic_salary
        self.bonus = bonus
        self.overtime_hours = overtime_hours

    def calculate_salary(self):
        overtime_pay = self.overtime_hours * 750
        total_salary = self.basic_salary + self.bonus + overtime_pay
        return total_salary
    
    def display_employee_details(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Basic Salary: INR {self.basic_salary}")
        print(f"Bonus: INR {self.bonus}")
        print(f"Overtime Hours: {self.overtime_hours}")
        print(f"Total Salary: INR {self.calculate_salary()}")

# Creating employee objects and calculating salary
emp1 = Employee(employee_id=101, name="Alice", department="IT", basic_salary=50000,
bonus=5000, overtime_hours=10)
emp2 = Employee(employee_id=102, name="Bob", department="HR", basic_salary=40000) # No bonus or overtime

# Displaying employee details
print("Employee 1 Details:")
emp1.display_employee_details()
print("\nEmployee 2 Details:")
emp2.display_employee_details()