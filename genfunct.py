#fibonnaci series of numbers
def fibo():
    first_num = 0
    second_num = 1
    yield second_num
    while(True):
        next_val = first_num + second_num
        yield next_val
        first_num,second_num = second_num, next_val
g = fibo()#  numbers where the previous sum of two prior nos  
#equal to the number preceeding
print(next(g))#1
print(next(g))#1
print(next(g))#2
print(next(g))#3
print(next(g))#5 forming fibonnaci series
for value in range(10):
    print(next(g))#outputs a list the first ten fibonnaci series 