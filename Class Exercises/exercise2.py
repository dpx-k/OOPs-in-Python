class Car: 
    wheels = 4 
    def __init__(self, brand, year): 
        self.brand = brand
        self.year = year 

    def display_info(self): 
        print(f"Car Brand: {self.brand}")
        print(f"Year: {self.year}")
        print(f"Wheels: {self.wheels}", "\n")
    
car1 = Car("Tata", 2013)
car2 = Car("Toyota", 2023)

car1.display_info()
car2.display_info()

Car.wheels = 6

car1.display_info()
car2.display_info()
