class Student:
    # name = "",
    # age = "",
    # gender = ""

    def __init__(self):  #This is a default constructor!
        print("I am default Constructor!")

    def __init__(self,n,a,g):  #This is a parameterize constructor!
        self.name = n
        self.age = a
        self.gender = g


    info= lambda self:print(f"Name: {self.name} | Age: {self.age} | Gender: {self.gender}")

s1 = Student("Moin",8,"Male")
s1.info()
