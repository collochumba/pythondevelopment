import itertools
l = [10,20,30,40,50]
count = 0 #initialize a counter to prevent infinite loop
for value in itertools.repeat(l):
    if count < 5:
        print(value)
    else:
        break
    count+=1
#values given are on list in five times