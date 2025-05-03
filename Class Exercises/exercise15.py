class Math:
    def __init__(self, n1, n2):
    # Initializing the attributes n1 and n2
        self.n1 = n1
        self.n2 = n2

    # Method intended for addition, but due to the logical error, it performs subtraction
    def cal_add(self):
        return self.n1 - self.n2 # Logical error: should be addition but performs subtraction
    
    # Method intended for subtraction, but due to the logical error, it performs addition
    def cal_sub(self):
        return self.n1 + self.n2 # Logical error: should be subtraction but performs addition
    
# Creating an instance of Math with two numbers
math_obj = Math(10, 5)
# Demonstrating the logical errors
print(f"cal_add (should add but subtracts): {math_obj.cal_add()}") # This performs subtraction
print(f"cal_sub (should subtract but adds): {math_obj.cal_sub()}") # This performs addition