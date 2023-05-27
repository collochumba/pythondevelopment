
fp = open("samplwritefile","w+")# w+ allows file to write and read
print(fp.tell())# tells the current position of the file pointer
fp.write("A sample of the written text")
print(fp.tell())#current position is 28 
#that is why there is no output if one reads the file
content = fp.read()
print(content)#print empty because the file pointer is the end of line
# when you run the file there is no output in the first place