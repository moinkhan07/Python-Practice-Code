a = int(input("Enter number: "))

match a:
    case 0:
      print("It is O")
    case 1:
      print("It is 1")
    case 2:
      print("It is 2")
    case _ if(a == 10):
      print("It is I think 10!")
    case _:
        print("This is out the match!")