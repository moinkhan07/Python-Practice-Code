def calculateGMean(a,b):
  mean = (a*b)/(a+b)
  print(mean)

calculateGMean(9,8)

def average(*numbers): # Single * means tuples and double ** means dict
    sum = 0
    for num in numbers:
        sum += num
    print("The average of numbers:",sum/len(numbers))    

average(10,20,30,40)

