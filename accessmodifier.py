#There is no such access modifier in python like private protected we just use with some techniques.

class Employee:

    def __init__(self,name):
        self.__name = name  #__name is become private

    # def empDetails(self):
    #     print(f"Employee Name: {self.__name} | Employee Salary: {self.salary}") # But here we can create a function and access that private


e1 = Employee("Moin")
# print(e1.__name) # We cannot access __name
print(e1._Employee__name) # Here we can access private with the use ** NAME MANGLING **