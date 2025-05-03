class Bank:
# Public attribute
    def __init__(self, name, accno, phno):
        self.name = name 
        self.accno = accno # Public attribute
        self.phno = phno 
        self._balance = 0 # Protected attribute 
        self.__pin = "1234" # Private attribute

# Method to deposit money (updates the protected attribute)
    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited: {amount}. New balance: {self._balance}")

# Method to get the pin (accessing the private attribute inside the class)
    def get_pin(self):
        return self.__pin
    
# Method to display information (demonstrating public and protected attributes)
    def display_info(self):
        print(f"Customer Name: {self.name}")
        print(f"Account Number: {self.accno}")
        print(f"Phone Number: {self.phno}")
        print(f"Balance: {self._balance}")

# Creating an instance of the Bank class
customer = Bank("John Doe", "123456789", "9876543210")

# Accessing public attributes
print(f"Public Attribute (Name): {customer.name}")
print(f"Public Attribute (Account Number): {customer.accno}")
print(f"Public Attribute (Phone Number): {customer.phno}")

# Accessing protected attribute (conventionally discouraged but possible)
print(f"Protected Attribute (Balance): {customer._balance}")

# Accessing private attribute (this will raise an error if accessed directly)
# print(f"Private Attribute (Pin): {customer.__pin}") # This would raise an AttributeError
# Accessing private attribute using a method
print(f"Private Attribute (Pin) through method: {customer.get_pin()}")

# Demonstrating deposit method and updated balance
customer.deposit(500)

# Displaying customer information using the public method
customer.display_info()