def sum_even_numbers():
    N = int(input("Enter the length of integers: "))
    numbers = []
    for i in range(N):
        n = int(input("Enter an inter: "))#prompt the user to enter integers until satisfies the specified by the user
        numbers.append(n)#TO add the integer to empty list of numbers
    # do the list comprehenison to filter only the even numbers of the list
    even = [x for x in numbers if x % 2 == 0]
    #to sum all the even numbers
    sum_even = sum(even)
    #Then print out the sum of the even numbers
    print(sum_even)
sum_even_numbers()#calling the function

