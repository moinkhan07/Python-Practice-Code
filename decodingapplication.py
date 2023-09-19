import string
import random
N= 3
ranEnd = ''.join(random.choices(string.ascii_letters, k=N))
name = input("Enter Your Name: ")
message = input(f"{name.capitalize()}, Enter your message: ")
ranStart = ''.join(random.choices(string.ascii_letters, k=N))
if(len(message) <= 2):
    updatedMsg = ranStart + message[1] + message[0] + ranEnd
    print("Coded message is",updatedMsg)
else:
    messageUpd = message.replace(message[0],"")
    newMsg = messageUpd + message[0]
    encryptedStr = str(ranStart) + newMsg + str(ranStart)
    print("Coded message is",encryptedStr)

print("=============================================")
num = int(input("Enter 1 to decode the message or 0 to exit: "))
while(True):
    if(num == 1):
        print("Decoded Message is",message)
        break
    elif(num == 0):
        print("Wrong Input!")
        break
print("Thank You!")