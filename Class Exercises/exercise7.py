class Car:
    def __init__(self, make, model, mileage, price):
        self.make = make
        self.model = model
        self.mileage = mileage
        self.price = price
        self.is_running = False # Car is initially stopped


    def display_details(self):
        print(f"Car Details:\nMake: {self.make}\nModel: {self.model}\nMileage: {self.mileage}\
        miles\nPrice: ${self.price}")
        print(f"Status: {'Running' if self.is_running else 'Stopped'}\n")

    # Start the car
    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.make} {self.model} has started.\n")
        else:
            print(f"{self.make} {self.model} is already running.\n")

    # Stop the car
    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"{self.make} {self.model} has stopped.\n")
        else:
            print(f"{self.make} {self.model} is already stopped.\n")

    # Update the car's price
    def update_price(self, new_price):
        self.price = new_price
        print(f"The price of {self.make} {self.model} has been updated to ${self.price}.\n")

# Example of creating two car objects
car1 = Car("Toyota", "Camry", 25000, 22000)
car2 = Car("Honda", "Civic", 30000, 18000)

# Calling methods on car1
car1.display_details()
car1.start()
car1.update_price(21000)
car1.display_details()
car1.stop()

# Calling methods on car2
car2.display_details()
car2.start()
car2.stop()
car2.update_price(17000)
car2.display_details()