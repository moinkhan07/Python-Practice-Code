class Employee:

    def __init__(self,name,id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"Employee ID: {self.id} and Employee Name: {self.name}")

    

class Manager(Employee): #Inheritance
    def manager(self):
        print("I am manager!")

class HR(Manager): # Multi level Inheritance we can do here!
    def hr(self):
        print("I am a HR!")


e1 = HR("Moin",101)
e1.showDetails()
e1.manager()
e1.hr()