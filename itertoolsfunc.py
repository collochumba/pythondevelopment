import itertools
l1 = [10,20,30,40,50]
l2 = [100,200,300,400,500]
i = itertools.chain(l1,l2)#method for itertools
print(i)#show iterable object
#to show the value use for loop
for value in i:
    print(value)#outputs the values