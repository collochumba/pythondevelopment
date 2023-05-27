fp = open("samplwritefile","w+")# w+ allows file to write and read
print("file pointer at first:",fp.tell())# current position of file pointer
fp.write("A sample of the written text IN (samplwritefile)")
print("postion of the file pointer after text written:",fp.tell())
#seek parameter takes 2 arguments(offset,positon)
fp.seek(0,0)#takes the file pointer to start  thats why contenst display
print("file pointer after seek function:",fp.tell())
content = fp.read()
print("TEXT IN THE FILE IS:",content)