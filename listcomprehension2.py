#program to print joined list of list using for loop&comprehension
l =[[1,2,3],[4,5,6],[7,8,9]]
l2 = []
for value in l:
    for value2 in value:
        l2.append(value2)
print("this is the joined list:",l2)
l3 = [val2 for val in l for val2 in val]#comprehesion
print("jioned list using comprehesion:",l3)