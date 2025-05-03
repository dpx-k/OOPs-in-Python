# Program to demonstrate handling multiple exceptions
try:
    user_input = input("Please enter a number to divide 10: ")
    num = int(user_input)

    # Attempting to divide 10 by the entered number
    result = 10 / num
    print(f"Result of division: 10 / {num} = {result}")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")