class Person:
    name=''
    def __init__(self,name):
        self.name=name
        print("person")
        print(self.name)
class Employee(Person):
    salary=0.0
    def __init__(self,salary,name):
        self.salary=salary
        print("Employee")
        print(self.salary)
class Manger(Employee):
    dept=''
    def __init__(self,salary,dept,name):
        self.dept=dept
        print("Manger")
        Person.__init__(self,name)
        Employee.__init__(self,salary,name)
        print(self.dept)
        
m1=Manger("Roma",10000000000,"ro")