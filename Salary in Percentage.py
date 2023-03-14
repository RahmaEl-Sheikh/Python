class Employee:
    name=""
    age=0
    salary=0    
    def raise_salary(self,per,salary):
        self.salary = salary
        salar=(salary*(per/100))+salary
        sal =  "salary after raising by percentage of = %.2f is: %.2f" % (per,salar)
        print(sal) 
emp = Employee()
emp.raise_salary(10,5000)
