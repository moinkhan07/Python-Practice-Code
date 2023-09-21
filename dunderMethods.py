class Employee:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return(f"Employee name is {self.name} in str method")
    
    def __repr__(self):
        return(f"Employee name is {self.name} in repr method!")

    def __call__(self):
        print("Welcome To Learn Python!")


e1 = Employee("Moin Khan")
print(str(e1))
print(repr(e1))
e1()
