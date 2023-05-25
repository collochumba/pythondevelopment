#permutations using iter tools to show possible outcomes from a dice
import itertools
l = [1,2,3,4,5,6]
print(list(itertools.permutations(l,2)))#showcase any two possible outcomes
print("=======================================================================")
print(list(itertools.combinations(l,2)))#output any two possible combinations
