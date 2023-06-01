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
customer1 = account(101,"collins")
customer2 = account(102,"Ebby")
customer3 = account(103,"Cobie-Elan")
print(customer1.name,customer2.name,customer3.name)
print("this are the no of customers: ",account.count)

