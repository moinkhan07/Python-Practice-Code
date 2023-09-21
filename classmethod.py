class Employee:

    companyName = "Microsoft"
    
    def __init__(self,name):
        self.name = name

    def showInfo(self):
        print(f"The employee name is {self.name}, working in {self.companyName}")
    
    @classmethod #This will now act as a class method
    def changeCmpName(self,newCompany):
        self.companyName = newCompany
    
e1 = Employee("Moin Khan")
e1.showInfo()
e1.changeCmpName("Flipkart") #Here it is just changing the e1 state not the class variable data
e1.showInfo()
print(Employee.companyName)  #It will give us Microsoft  || But after adding @classmethod decorater in line 11 it will give the changed copany name whihc is flipkart in this case