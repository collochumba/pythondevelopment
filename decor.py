def deco(funct):
    def new_func(val1,val2):
        if type(val1) == type(val2):
            return funct(val1,val2)#data types of concatinated data are same
        else:
            return funct(str(val1),str(val2))#different data types so u typecast
    return new_func
@deco
def concat(val1,val2):
    return val1 + val2
result = concat(10,17)
print (result)
result1 = concat(17, "Collins")
print(result1)
result = concat("python","-c-language")
print(result)