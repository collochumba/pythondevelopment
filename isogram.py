# a program to check if a word is an isogram or not
#a isogram is word with no repeating letters for example (come)
def get_isogram(word):
    word.lower()# to convert all the work to lowercase
    letters = set()#empty set to store the letters
    for letter in word:
        if letter in letters:
            return False
        else:
            letters.add(letter)#to add the unique letter to the set
    return True#when the all letters have been checked and its true the return that it is an isogram
# the code to run
word = input("Enter the word to check: ")
if get_isogram(word):
    print("true")
else:
    print("false")




        
