class Employee:
    companyName = "Microsoft" #This is class varaible
    def __init__(self,name,salary):
        self.name = name #This is instance variables
        self.salary = salary #This is instance variables

    def getEmpDetails(self):
        print(f"The employee {self.name} get {self.salary} salary in {self.companyName}")

e1 = Employee("Moin",1200000)
e1.companyName = "Amazon" #We are changing the instance variable not the class variable
e1.getEmpDetails()
e2 = Employee("Faisal",1500000)
e2.getEmpDetails()