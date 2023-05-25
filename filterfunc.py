# a program to check odd and even numbers using filter
def check_num(x):
    if  x%2 == 0:
        return x
l = [10,15,20,25,30,35]
results = list(filter(check_num,l))
print("the even numbers are:",results)