class Car: 
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self): 
        print(f"Car Brand: {self.brand}")
        print(f"Year: {self.year}")

my_car = Car("Sparrow Motorsport", 2025)
my_car.display_info()