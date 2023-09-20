class Math:
    def __init__(self,num):
        self.num = num

    def addToNum(self,n):
        self.num = self.num + n
    
    @staticmethod
    def sum(a,b):
        return a + b

a = Math(10)
print(a.num)
a.addToNum(20)
print(a.num)
print(Math.sum(12,3))