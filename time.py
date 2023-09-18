import time

hour = int(time.strftime("%H"))
min = int(time.strftime("%M"))
sec = int(time.strftime("%S"))
print(hour,":",min,":",sec)

if(hour<12):
    print("Good morning sir!")
elif(hour>12 and hour <= 16):
    print("Good afternoon sir!")
elif(hour > 16 and hour <= 19):
    print("Good evening sir!")
else:
    print("Good night sir!")