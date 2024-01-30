class InsecurityBank:
    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Input should be a nonnegative number")
        self.balance = initial_balance

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Input should be a positive number")
        if amount >= 5000:
            amount = amount * 1.3

        if amount > self.balance:
            raise ValueError(f"Insufficient balance:  {self.balance}")
        else:
            self.balance -= amount
        print(f"Successfully withdrawn {amount} from bank accout")

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Input should be a positive number")
        self.balance += amount
        print(f"Successfully deposited {amount} from bank accout")

    def check_balance(self):
        return self.balance
