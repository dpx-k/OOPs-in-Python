class Car:
    wheels = 4

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"Car Brand: {self.brand}")
        print(f"Year: {self.year}")
        print(f"Wheels: {self.wheels}")

    # Class method (takes 'cls' as the first argument)
    @classmethod
    def change_wheels(cls, new_wheels):
        cls.wheels = new_wheels
        print(f"Wheels updated to {cls.wheels} for all cars")

    # Static method (doesn't take 'self' or 'cls' as the first argument)
    @staticmethod
    def is_eco_friendly(brand):
        eco_friendly_brands = ["Tesla", "Nissan", "Chevrolet"]
        if brand in eco_friendly_brands:
            return True
        return False
    
car1 = Car("Tesla", 2021)

Car.change_wheels(6)

car1.display_info()

print(car1.is_eco_friendly("Nissan"))
