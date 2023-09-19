# Reading a file
# fl = open("test.txt","r")
# text = fl.read()
# print(text)
# fl.close()

#Writing a file
# fl = open("test.txt","w")
# fl.write("Computer")
# fl.close

# appending a file
# fl = open("test.txt","a")
# fl.write("Hello World!")
# fl.close()

# readline: reading a line by line from a file
# fl = open("test.txt","r")
# while True:
#     line = fl.readline()
#     if not line:
#         break
#     print(line)

# writeline: writing a line in a file
fl = open("test.txt","w")
line = ["hello\n","hello\n","hello\n"]
fl.writelines(line)
fl.close()
