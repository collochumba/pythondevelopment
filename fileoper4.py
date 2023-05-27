fp = open("samplefile.txt","r+")#open in read and write mode
contents = fp.read()
print(contents)
fp.write("\n\n this is line add by using write method in python")