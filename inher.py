#this code explains inheritance
class A:
    def method(self):
        print(1)
class B(A):# B is subcalss while A is superclass
    def method(self):
        print(2)
B().method()