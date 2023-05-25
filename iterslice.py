import itertools
l = [10,20,30,40]
l2 = [100,200,300,400]
i = itertools.chain(l,l2)
print("two iterable objecst:",i)# show two iteratable objects
#use for loop to get the values
for value in itertools.islice(i,0,5):#sliced different
    print(value)