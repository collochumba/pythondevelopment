#this a program to demonstrate OOP
class account:# declaration of a class
    def __init__(self,cusid,name,accbalance = 0):#constructor to create instance
        self.cusid = cusid
        self.name = name
        self.accbalance = accbalance

customer1 = account(101,"collins")
print(customer1.cusid,customer1.name,customer1.accbalance)#accessing attributes
#of the object customer1