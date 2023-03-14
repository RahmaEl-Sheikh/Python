class Person:
    name=""
    age=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("constructor")
        print(self.name)
        print(self.age)
    def __del__(self):
        print("destructor")
r1=Person("Roma",25)
del r1