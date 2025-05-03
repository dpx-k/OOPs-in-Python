class Employee:
    company = "Tech Corp"

    def __init__(self, emp_id, name, salary):
        self.__emp_id = emp_id
        self.__name = name
        self.salary = salary
    
    # Getter method for emp_id
    def get_emp_id(self):
        return self.__emp_id
    
    # Setter method for emp_id
    def set_emp_id(self, emp_id):
        if isinstance(emp_id, int) and emp_id > 0:
            self.__emp_id = emp_id
        else:
            print("Invalid Employee ID. It should be a positive integer.")

    # Getter method for name
    def get_name(self):
        return self.__name
    
    # Setter method for name
    def set_name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self.__name = name
        else:
            print("Invalid name. It should be a non-empty string.")

    # Method to display employee details
    def display_employee(self):
        print(f"Employee Details:\nCompany: {Employee.company}\nEmployee ID:\
        {self.__emp_id}\nName: {self.__name}\nSalary: ${self.salary}")

# Example of creating and using the Employee class
emp1 = Employee(101, "Alice Johnson", 60000)
emp2 = Employee(102, "Bob Smith", 55000)

# Display details of both employees
emp1.display_employee()
print("\n")
emp2.display_employee()