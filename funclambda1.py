# a program that returns numbers divisible by 2 using lambda func
#also known as anonymous function
l = [1,2,3,4,5,6,7,8,9]
even = list(filter(lambda num:num%2==0,l))#for even numbers
odd = list(filter(lambda num:num%2==1,l))#for odd number
print("The even no are:",even)#output even numbers from list
print("The odd no are:",odd)#output the odd numbers from list
