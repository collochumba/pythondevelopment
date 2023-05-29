class account:# declaration of a class
    def __init__(self,cusid,name,accbalance = 0):#constructor to create instance
        self.cusid = cusid
        self.name = name
        self.accbalance = accbalance
    def balance(self):
        return self.accbalance
    def deposit(self, amount):
        self.accbalance = self.accbalance + amount
        return self.accbalance
    def withdraw(self,amount):
        if amount > self.accbalance:
            return "insufficient funds cannot withdraw"
        else:
            self.accbalance -= amount
            return self.accbalance
customer1 = account(101,"collins")
print("The intial balance:",customer1.balance())
print("brings the updated balance:",customer1.deposit(5000))
print("balance after withdraw:",customer1.withdraw(6000))
