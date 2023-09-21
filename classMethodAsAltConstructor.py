class Employee:
    
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @classmethod #Without this it will through us error
    def fromStr(self,string):
        return self(string.split("-")[0],string.split("-")[1])
    
e1 = Employee("Moin Khan",150000)
print(e1.name)
print(e1.salary)
#If we will get string as below:
string = "Moin Khan-150000"
#so we can use split method here:
e2 = Employee.fromStr(string) #But if we have larger amount of data we can't do split again and again so we make function for doing this.
print(e2.name)
print(e2.salary)