class BankAccount:
    def __init__(self, name, accno, initial_balance):
        # Private attributes (by convention)
        self.__name = name
        self.__accno = accno
        self.__balance = initial_balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive!")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive!")
        elif amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount}. New balance: {self.__balance}")

    # Method to check balance
    def check_balance(self):
        print(f"Current balance: {self.__balance}")

    # Method to display account details
    def display_account_details(self):
        print(f"Account Holder: {self.__name}")
        print(f"Account Number: {self.__accno}")
        print(f"Account Balance: {self.__balance}")

# Creating an instance of BankAccount
account = BankAccount("Alice Johnson", "987654321", 1000)

# Displaying account details
account.display_account_details()

# Depositing money
account.deposit(500)

# Withdrawing money
account.withdraw(200)

# Checking balance
account.check_balance()

# Trying to withdraw more than available balance
account.withdraw(1500)

# Checking balance again
account.check_balance()