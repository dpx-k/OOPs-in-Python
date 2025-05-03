from abc import ABC, abstractmethod
# Abstract class Vehicle
class Vehicle(ABC):
    @abstractmethod
    def number_of_wheels(self):
        pass

# Concrete class Car
class Car(Vehicle):
    def number_of_wheels(self):
        return 4 
    
# Concrete class Bike
class Bike(Vehicle):
    def number_of_wheels(self):
        return 2

# Instantiate Car and Bike
car = Car()
bike = Bike()

# Display number of wheels for each vehicle
print(f"A car has {car.number_of_wheels()} wheels.")
print(f"A bike has {bike.number_of_wheels()} wheels.")