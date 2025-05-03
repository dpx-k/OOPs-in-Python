class Student:
    college_name = "ABC University"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.address = None  # Initialize address as None

    # Instance method to get details of the student
    def get_details(self):
        college_info = f", College: {Student.college_name}"
        address_info = f", Address: {self.address.get_address()}" if self.address else ""
        return f"Name: {self.name}, Age: {self.age}{college_info}{address_info}"

    # Class method to change the college name for all instances
    @classmethod
    def change_college(cls, new_college):
        cls.college_name = new_college

    # Static method to check if the student is an adult
    @staticmethod
    def is_adult(age):
        return age >= 18

    # Inner class for Address
    class Address:
        def __init__(self, city, state):
            self.city = city
            self.state = state

        # Method to return the address details
        def get_address(self):
            return f"City: {self.city}, State: {self.state}"

    # Another class to associate a student with a course
    class Course:
        def __init__(self, student):
        # Accepting a Student object during initialization
            self.student = student

        # Method to get student info in the course
        def get_student_info(self):
            return self.student.get_details()

# Creating student objects
student1 = Student("Alice", 20)
student2 = Student("Bob", 17)

# Creating address for student1 and associating it
student1.address = Student.Address("New York", "NY")

# Display student details
print(student1.get_details())
print(student2.get_details())

# Checking if the students are adults
print(f"Alice is an adult: {Student.is_adult(student1.age)}")
print(f"Bob is an adult: {Student.is_adult(student2.age)}")

# Changing the college for all students
Student.change_college("XYZ Institute")

# Display updated student details after college change
print("\nAfter changing college:")
print(student1.get_details())
print(student2.get_details())

# Creating Course object with student1
course = Student.Course(student1)
print(f"Student info in the course: {course.get_student_info()}")