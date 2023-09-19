#Map Function : 
cube = lambda x: x*x*x
l = [1,3,5,7,9,12,14,17,20]

newML = list(map(cube,l)) # WITHOUT list the output will like be <map object at 0x00000235C8F8AA10> 
print(newML)


#Filter Function :
test = lambda x: x > 10

newFl = list(filter(test,l))
print(newFl)


#Reduce Function : 
from functools import reduce

numbers = [11,12,13,14,15,16,17,18,19,20]

newFilL = reduce(lambda x,y:x+y,numbers)
print(newFilL)