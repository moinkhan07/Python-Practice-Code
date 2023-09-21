ls = [1,2,3,4,5,6,7,8]
print(dir(ls)) #It will print all the method/operations that we can use in list or the above data

tup = (1,2,3,4,5,6,7,8,9)
print(dir(tup)) #It will print all the method/operations that we can use in Tuples or the above data

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

s1 = Student("Moin",19)
print(s1.__dict__) #It will give us the output as dict which means key:value pair :) {'name': 'Moin', 'age': 19}

# Help Method
print(help(Student))
