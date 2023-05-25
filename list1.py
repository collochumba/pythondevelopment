l = [100,300,400,500,600]
l2 = []
l3 = [x*x for x in l]
for i in l:
    l2.append(i*i)
print(l)
print("This is list with squared number of l:",l2)
print("comprehension of l:",l3)# functions as l2

