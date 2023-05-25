# a program to print hash keys for values of alphabet
# e.g 'a':97,'b':98....'z':122
d = {chr(x):x for x in range(97,123)}# using comprehesion
print("list of alphabets with hash keys:",d)
# to swap keys and values
d1 = {value:key for key,value in d.items()}# swaps keys and values
print("swaped values:", d1)