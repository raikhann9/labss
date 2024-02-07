class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        count=int(input())
        self.balance += count
        print("Accepted! Your current budget:", self.balance)

    def withdraw(self):
        count=int(input())
        if count < self.balance:
            self.balance -= count
            print("Accepted! Your current budget:", self.balance)
        else:
            print("Not enough to make a withdrawal!")

owner=input()
balance=int(input())
p1=Account(owner, balance)
p1.deposit()
p1.withdraw()