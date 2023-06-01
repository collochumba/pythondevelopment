class account:# declaration of a class
    count = 0#this is a class variable
    def __init__(self,cusid,name,accbalance = 0):#constructor to create instance
        self.cusid = cusid
        self.name = name
        self.accbalance = accbalance
        account.count +=1#intializing the increment of the objects
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
class savings(account):# shows inheritance,,, account is the parent class
    def __init__ (self,cusid,name,accbalance = 0):
        super().__init__(cusid,name,accbalance)#help difinition like in parent
        self.limit = 50000
    def withdraw(self, amount):
        if amount < self.limit:
            new_bal = super().withdraw(amount)
            self.limit -= amount
            return new_bal
        else:
            print("Daily limit reached")
cus1 = savings(107,"cobie")
cus2 = savings(117,"collisn")
print("this is amounted deposited by cus1:", cus1.deposit(70000))
print("this cus1 balance after withdraw:",cus1.withdraw(7000))
print ("this amount cus2 deposits:",cus2.deposit(1700000))
print("message when the is over withdraw:", cus2.withdraw(100000))

        

