# a program to square everying in a list using map
def sqr(num):
    return num**2
l = [10,20,30,40,50]
results=map(sqr,l)#shows no list but some info
results1 = list(map(sqr,l))#convert it to output list
print("certain infromation that iterable:",results)
print("the list of squared values:",results1)#outputs the list