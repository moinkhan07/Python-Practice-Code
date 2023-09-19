import random
computer = [0,1,2]
uCount = 0
cCount = 0
while(True):
    ran = random.choice(computer)
    if(uCount == 5):
        print("==========================================")
        print(f"User Score {uCount}, So User Win's The Game!")
        break
    if(cCount == 5):
        print("==========================================")
        print(f"Computer Score {cCount}, So Computer Win's The Game!")
        break
    print("=====================================")
    print("| 0 is Snake | 1 is Water | 2 is Gun |")
    print("=====================================")
    print(f"Computer choice is {ran}")
    user = int(input("Enter your choice or enter -1 to exit: "))
    if(user == -1): break
    if(ran == 0 and user == 0):
        print("Draw!")
    elif(ran == 0 and user == 1):
        print("Computer Win!")
        cCount = cCount + 1
    elif(ran == 0 and user == 2):
        print("User Win!")
        uCount = uCount + 1
    elif(ran == 1 and user == 0):
        print("User Win!")
        uCount = uCount + 1
    elif(ran == 1 and user == 1):
        print("Draw!")
    elif(ran == 1 and user == 2):
        print("Computer Win!")
        cCount = cCount + 1
    elif(ran == 2 and user == 0):
        print("Computer Win!")
        cCount = cCount + 1
    elif(ran == 2 and user == 1):
        print("User Win!")
        uCount = uCount + 1
    elif(ran == 2 and user == 2):
        print("Draw!")
    else:
        print("Wrong Input!")
    print("=====================================")
    print(f"User Win: {uCount} | Commputer Win: {cCount}")

print("Thank You!")