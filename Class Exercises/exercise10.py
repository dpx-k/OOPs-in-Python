'''
Inheritance
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
    # Call the parent class constructor using super() to initialize name and age
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary
    
    # Override the show_details method from the parent class
    def show_details(self):
    # Call the parent class's show_details using super() to include name and age
        super().show_details()
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: {self.salary}")

# Create instances of Person and Employee
person1 = Person("John", 30)
employee1 = Employee("Alice", 25, 101, 50000)

# Display details of both person and employee
print("Person Details:")
person1.show_details()
print("\nEmployee Details:")
employee1.show_details()