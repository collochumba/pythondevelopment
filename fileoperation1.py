fp = open("README.md","r") # this open readme file in the directory
content = fp.read()#this returns a string a shown below
#fp.readlines returns a list and line forms indexes for slicing
print(content)