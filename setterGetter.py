class MyClass:
    def __init__(self,v):
        self.value = v
    
    def show(self):
        print(f"The value is {self.value}")
    
    @property
    def ten_Value(self):
        return self.value

    @ten_Value.setter
    def ten_Value(self,nv):
        self.value = nv

obj = MyClass(10)
obj.show()
print(f"Hello: {obj.ten_Value}")
# obj.ten_Value(100)
obj.ten_Value = 100
obj.show()
print("New Value:",obj.ten_Value)