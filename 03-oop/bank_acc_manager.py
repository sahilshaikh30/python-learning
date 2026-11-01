
# BankAccount class
# This class represents a bank account
class BankAccount:

    # Class variable: Same bank name for all accounts
    bank_name = "State Bank of India"

    # Constructor: Initializes account details when an object is created
    def __init__(self, acc_name, ini_balance):
        self.acc_name = acc_name
        self.ini_balance = ini_balance

    # Deposit method: Adds money to the account balance
    def deposit(self, amount):
        self.ini_balance = self.ini_balance + amount
        return self.ini_balance

    # Withdraw method: Deducts money if sufficient balance is available
    def withdraw(self, amount):
        if self.ini_balance >= amount:
            self.ini_balance = self.ini_balance - amount
        return self.ini_balance

    # Get balance method: Returns the current account balance
    def get_balance(self):
        return self.ini_balance

    # Get report method: Displays the account details and final balance
    def get_report(self):
        return f"""
    Bank: {self.bank_name}
    Account holder name: {self.acc_name}
    Final Balance: {self.get_balance()}
"""


# Create an object of the BankAccount class
data = BankAccount("Rahul", 5000)

# Deposit ₹2,000 into the account
data.deposit(2000)

# Withdraw ₹1,500 from the account
data.withdraw(1500)

# Display the final account report
print(data.get_report())
