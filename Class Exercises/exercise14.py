class Person:
    def __init__(self):
        self.name = "Raja"

person = Person()

try:
    print(f"Person's age: {person.age}")
except AttributeError as e:
    print(f"Error: {e}")
    print("The attribute 'age' is not defined for this person.")