class Person:
    def __init__(self):
        self.name = "Alex"
        self.db = self.Dob()

    def display(self):
        print("Name:", self.name)

#this is inner class
    class Dob:
        def __init__(self):
            self.dd =10
            self.mm = 5
            self.yy = 1987

        def display(self):
            print(f"Dob:{self.dd}/{self.mm}/{self.yy}")

#creating Person class object
p = Person()
p .display()

#create inner class object
x = p.db
x.display() 
